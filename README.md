# 📚 Kitap Yönetim Sistemi

![GitHub release (latest by date)](https://github.com/AkdenoriaInteractive/Kitap-Yonetim-Sistemi/releases/tag/v1.0.0)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Bu proje, **Python ve CustomTkinter** kullanılarak geliştirilmiş modern bir masaüstü uygulamasıdır.  
Kullanıcıların kitap eklemesini, düzenlemesini, silmesini ve listelemesini sağlayan şık ve kullanıcı dostu bir arayüz sunar.

---

## ⚡ Özellikler

- **Kitap Ekleme:** Kitap adı, yazar, yayın yılı, tür, sayfa sayısı, yayıncı, baskı, fiyat, stok ve eklenme tarihi ile kitap ekleme.  
- **Kitap Güncelleme:** Mevcut kitapları seçip bilgilerini kolayca güncelleme.  
- **Kitap Silme:** İstenmeyen kitapları listeden ve veritabanından silme.  
- **Vergi Oranı Ayarlama:** Fiyatlara uygulanacak vergi oranını istediğiniz gibi belirleme.  
- **Kategori Bazlı Renkler:** Kitap türüne göre listeleme renkleri, görsel olarak kolay ayırt etme.  
- **Arama ve Filtreleme:** Kitap adı, yazar, tür ve stok durumuna göre filtreleme.  
- **Modern Arayüz:** CustomTkinter ile koyu tema ve şık tasarım.  
- **Tam Ekran ve Responsive:** Pencere boyutuna göre otomatik olarak ayarlama.  
- **Veri Kaydetme:** Kitaplar `books.json` dosyasında saklanır, uygulama kapansa bile bilgiler korunur.

---

## 🖥 Teknolojiler

- Python 3.x  
- CustomTkinter (GUI)  
- Tkinter (arkaplan ve bazı kontroller)  
- JSON (veri saklama)

---
## 🎨 Kategori Renkleri
| Tür         | Renk    |
| ----------- | ------- |
| Roman       | #1E90FF |
| Tarih       | #32CD32 |
| Bilim       | #FFA500 |
| Fantastik   | #9370DB |
| Biyografi   | #FF69B4 |
| Psikoloji   | #00CED1 |
| Felsefe     | #FFD700 |
| Çocuk       | #FF4500 |
| Korku       | #8B0000 |
| Macera      | #228B22 |
| Klasik      | #8A2BE2 |
| Şiir        | #FF1493 |
| Bilim Kurgu | #00BFFF |
| Dram        | #FF6347 |
| Edebiyat    | #DAA520 |
| Sanat       | #FF8C00 |
| Gezi        | #20B2AA |
| Mizah       | #FF69B4 |
| Savaş       | #A52A2A |
| Din         | #9400D3 |
| Politika    | #2E8B57 |
| Ekonomi     | #FF7F50 |
| Sağlık      | #3CB371 |
| Teknoloji   | #4682B4 |
| Eğitim      | #D2691E |
| Diğer       | #A9A9A9 |


## 📁 Kurulum

1. Depoyu klonlayın:
```bash
git clone https://github.com/kullaniciAdi/kitap-yonetim-sistemi.git
python -m venv my_venv
my_venv\Scripts\activate  # Windows
source my_venv/bin/activate  # Mac/Linux
pip install customtkinter
python main.py
pyinstaller --onefile --windowed --icon=logo.ico main.py

--onefile: Tek bir exe oluşturur

--windowed: Konsol penceresi olmadan çalıştırır

--icon: Uygulama ikonu

Not: EXE çalıştırıldığında books.json otomatik olarak uygulama klasöründe oluşacaktır.
