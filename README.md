# metin-ozetleyici
# Metin Özetleme Projesi

Bu proje, yapay zeka kullanarak metinleri otomatik olarak özetleyen bir Python uygulamasıdır.

## Özellikler

- ✅ PDF dosyalarından metin çıkarma ve özetleme
- ✅ Web sayfalarından metin çıkarma ve özetleme
- ✅ TXT dosyalarından metin okuma ve özetleme
- ✅ Facebook BART modeli ile gelişmiş özetleme
- ✅ Uzun metinler için otomatik parçalama

## Gereksinimler

Python 3.7 veya üzeri sürüm gereklidir.

## Kurulum

1. Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanılan Kütüphaneler

- **transformers**: Hugging Face'in transformer modelleri için
- **torch**: PyTorch - derin öğrenme framework'ü
- **PyPDF2**: PDF dosyalarını okumak için
- **requests**: HTTP istekleri yapmak için
- **beautifulsoup4**: Web sayfalarından metin çıkarmak için

## Kullanım

### Temel Kullanım

```python
from metinss import TextSummarizer

# Özetleyiciyi başlat
summarizer = TextSummarizer()

# Metin özetleme
text = "Özetlenecek uzun metniniz..."
summary = summarizer.summarize(text)
print(summary)
```

### PDF Dosyası Özetleme

```python
# PDF dosyasından metin oku
pdf_text = summarizer.read_pdf("dosya.pdf")
if pdf_text:
    summary = summarizer.summarize(pdf_text)
    print(summary)
```

### Web Sayfası Özetleme

```python
# URL'den metin oku
url_text = summarizer.read_url("https://example.com/article")
if url_text:
    summary = summarizer.summarize(url_text)
    print(summary)
```

### TXT Dosyası Özetleme

```python
# TXT dosyasından metin oku
txt_content = summarizer.read_text_file("dosya.txt")
if txt_content:
    summary = summarizer.summarize(txt_content)
    print(summary)
```

## Parametreler

`summarize()` metodu aşağıdaki parametreleri kabul eder:

- `text` (str): Özetlenecek metin
- `max_length` (int, varsayılan=150): Özetin maksimum kelime sayısı
- `min_length` (int, varsayılan=50): Özetin minimum kelime sayısı

## Örnek

```python
# Özel uzunlukta özet
summary = summarizer.summarize(
    text="Uzun metniniz...",
    max_length=200,
    min_length=100
)
```

## Notlar

- İlk çalıştırmada model otomatik olarak indirilecektir (~1.6 GB)
- PDF dosyalarından sadece ilk 10 sayfa işlenir
- Çok uzun metinler otomatik olarak parçalara ayrılır ve ilk 3 parça özetlenir
- En az 100 karakter uzunluğunda metin gereklidir

## Lisans

MIT

## Katkıda Bulunma

Pull request'ler kabul edilir. Büyük değişiklikler için lütfen önce bir issue açarak neyi değiştirmek istediğinizi tartışın.
