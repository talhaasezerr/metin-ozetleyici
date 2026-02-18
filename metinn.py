"""
Metin Özetleme Modülü
"""
import os
from transformers import pipeline
import PyPDF2
import requests
from bs4 import BeautifulSoup
from typing import Optional

class TextSummarizer:
    def __init__(self):
        """Özetleme modelini başlat"""
        print("Model yükleniyor... (İlk çalıştırmada indirme yapılacak)")
        # Facebook'un BART modeli - Türkçe için alternatif: "facebook/mbart-large-50"
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        print("Model hazır!")
    
    def summarize(self, text: str, max_length: int = 150, min_length: int = 50) -> str:
        """
        Metni özetle
        
        Args:
            text: Özetlenecek metin
            max_length: Maksimum özet uzunluğu
            min_length: Minimum özet uzunluğu
        
        Returns:
            Özetlenmiş metin
        """
        if not text or len(text.strip()) < 100:
            return "Metin çok kısa, özetlenemiyor."
        
        try:
            # Metin çok uzunsa parçala
            max_chunk = 1024
            if len(text) > max_chunk:
                chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
                summaries = []
                for chunk in chunks[:3]:  # İlk 3 parça
                    result = self.summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
                    summaries.append(result[0]['summary_text'])
                return "\n\n".join(summaries)
            else:
                result = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
                return result[0]['summary_text']
        except Exception as e:
            return f"Hata oluştu: {str(e)}"
    
    def read_pdf(self, file_path: str) -> Optional[str]:
        """PDF dosyasından metin oku"""
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages[:10]:  # İlk 10 sayfa
                    text += page.extract_text()
                return text
        except Exception as e:
            return f"PDF okuma hatası: {str(e)}"
    
    def read_url(self, url: str) -> Optional[str]:
        """URL'den metin oku"""
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Script ve style taglerini kaldır
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Metni al
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text
        except Exception as e:
            return f"URL okuma hatası: {str(e)}"
    
    def read_text_file(self, file_path: str) -> Optional[str]:
        """TXT dosyasından metin oku"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Dosya okuma hatası: {str(e)}"
        
    