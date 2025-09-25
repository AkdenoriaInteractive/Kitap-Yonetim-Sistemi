import json
import os
import customtkinter as ctk
from tkinter import PhotoImage, messagebox

# customtkinter ayarları
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

   
   
# dosyadan kitapları yükle
appdata_path = os.path.join(os.environ['APPDATA'], "KitapYonetim")
os.makedirs(appdata_path, exist_ok=True)
json_path = os.path.join(appdata_path, "books.json")


def load_books():
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books():
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

books = load_books()
selected_book_index = None

# Kategori renkleri
category_colors = {
    "Roman": "#1E90FF","Tarih": "#32CD32","Bilim": "#FFA500","Fantastik": "#9370DB",
    "Biyografi": "#FF69B4","Psikoloji": "#00CED1","Felsefe": "#FFD700","Çocuk": "#FF4500",
    "Korku": "#8B0000","Macera": "#228B22","Klasik": "#8A2BE2","Şiir": "#FF1493",
    "Bilim Kurgu": "#00BFFF","Dram": "#FF6347","Edebiyat": "#DAA520","Sanat": "#FF8C00",
    "Gezi": "#20B2AA","Mizah": "#FF69B4","Savaş": "#A52A2A","Din": "#9400D3",
    "Politika": "#2E8B57","Ekonomi": "#FF7F50","Sağlık": "#3CB371","Teknoloji": "#4682B4",
    "Eğitim": "#D2691E","Diğer": "#A9A9A9"
}

# Ana pencere
app = ctk.CTk()
app.title("Kitap Yönetim Sistemi")
app.geometry("1920x1080")
app.resizable(True, True)

title_font = ctk.CTkFont(size=20, weight="bold")
label_font = ctk.CTkFont(size=16)
book_font = ctk.CTkFont(size=16)

# Sol yer - Arama & Filtreleme
left_frame = ctk.CTkFrame(app, width=300, corner_radius=10)
left_frame.pack(side="left", fill="y", padx=15, pady=15)

ctk.CTkLabel(left_frame, text="Arama & Filtreleme", font=title_font).pack(pady=10)
search_name = ctk.CTkEntry(left_frame, placeholder_text="Kitap Adı")
search_name.pack(pady=5)
search_author = ctk.CTkEntry(left_frame, placeholder_text="Yazar")
search_author.pack(pady=5)
search_genre_var = ctk.StringVar(value="Hepsi")
ctk.CTkLabel(left_frame, text="Tür", font=label_font).pack(pady=(5,0))
search_genre_option = ctk.CTkOptionMenu(left_frame, values=["Hepsi"] + list(category_colors.keys()), variable=search_genre_var)
search_genre_option.pack(pady=5)
ctk.CTkLabel(left_frame, text="Stokta Olan", font=label_font).pack(pady=(5,0))
stock_var = ctk.StringVar(value="Hepsi")
stock_option = ctk.CTkOptionMenu(left_frame, values=["Hepsi", "Evet", "Hayır"], variable=stock_var)
stock_option.pack(pady=5)

def filter_books():
    filtered = []
    for b in books:
        if (search_name.get().lower() in b['Adı'].lower()) and \
           (search_author.get().lower() in b['Yazar'].lower()):
            if (search_genre_var.get() == "Hepsi") or (b['Tür'] == search_genre_var.get()):
                if stock_var.get() == "Hepsi" or stock_var.get() == b['Stok Durumu']:
                    filtered.append(b)
    update_book_list(filtered)

ctk.CTkButton(left_frame, text="Filtrele", command=filter_books).pack(pady=10)
ctk.CTkButton(left_frame, text="Tüm Kitaplar", command=lambda: update_book_list(books)).pack(pady=5)

# Orta yer - Kitap Listesi
middle_frame = ctk.CTkFrame(app, width=800, corner_radius=10)
middle_frame.pack(side="left", fill="both", expand=True, padx=15, pady=15)

ctk.CTkLabel(middle_frame, text="Kitap Listesi", font=title_font).pack(pady=5)

scroll_frame = ctk.CTkScrollableFrame(middle_frame, corner_radius=10)
scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

book_labels = []

def on_label_click(event, index):
    global selected_book_index
    selected_book_index = index
    b = books[index]
    for key in entries:
        if key == "Tür":
            entries[key].set(b.get(key, key))
        else:
            entries[key].delete(0, "end")
            entries[key].insert(0, b.get(key, ""))

def update_book_list(book_list):
    for lbl in book_labels:
        lbl.destroy()
    book_labels.clear()
    for idx, b in enumerate(book_list, 0):
        color = category_colors.get(b['Tür'], category_colors["Diğer"])
        info = f"{idx+1}. '{b['Adı']}' - {b['Yazar']} - {b['Tür']} - {b['Fiyat']} TL - Stok: {b['Stok']} ({b['Stok Durumu']})"
        lbl = ctk.CTkLabel(scroll_frame, text=info, text_color=color, font=book_font)
        lbl.pack(anchor="w", pady=2, padx=5)
        lbl.bind("<Button-1>", lambda e, i=idx: on_label_click(e, i))
        book_labels.append(lbl)

update_book_list(books)

# sağ yer - Kitap İşlemleri
right_frame = ctk.CTkFrame(app, width=600, corner_radius=10)
right_frame.pack(side="right", fill="y", padx=15, pady=15)

ctk.CTkLabel(right_frame, text="Kitap İşlemleri", font=title_font).pack(pady=10)

entries = {}
for field in ["Adı","Yazar","Yayın Yılı","Tür","Sayfa Sayısı","Yayıncı","Kaçıncı Baskı","Fiyat","Stok","Stokla Eklenme Tarihi"]:
    ctk.CTkLabel(right_frame, text=field, font=label_font).pack(pady=(2,0))
    if field == "Tür":
        entries[field] = ctk.CTkOptionMenu(right_frame, values=list(category_colors.keys()))
    else:
        entries[field] = ctk.CTkEntry(right_frame)
    entries[field].pack(pady=(0,5))

ctk.CTkLabel(right_frame, text="Vergi Oranı (%)", font=label_font).pack(pady=(10,0))
tax_entry = ctk.CTkEntry(right_frame)
tax_entry.pack(pady=(0,10))
tax_entry.insert(0,"20")

# fonksiyonlar
def add_book_gui():
    try:
        price = float(entries["Fiyat"].get())
        tax_rate = float(tax_entry.get())
        price_str = "{:.2f}".format(price * (1 + tax_rate/100))
    except ValueError:
        price_str = "0.00"
    stok = entries["Stok"].get()
    isAvailable = "Evet" if stok.isdigit() and int(stok)>0 else "Hayır"
    book = {key: entries[key].get() if key != "Tür" else entries["Tür"].get() for key in entries}
    book["Fiyat"] = price_str
    book["Stok Durumu"] = isAvailable
    books.append(book)
    save_books()
    update_book_list(books)
    messagebox.showinfo("Başarılı", f"'{book['Adı']}' başarıyla eklendi!")

def update_book_gui():
    global selected_book_index
    if selected_book_index is None:
        messagebox.showwarning("Uyarı","Güncellemek için bir kitap seçin!")
        return
    try:
        price = float(entries["Fiyat"].get())
        tax_rate = float(tax_entry.get())
        price_str = "{:.2f}".format(price * (1 + tax_rate/100))
    except ValueError:
        price_str = "0.00"
    stok = entries["Stok"].get()
    isAvailable = "Evet" if stok.isdigit() and int(stok)>0 else "Hayır"
    books[selected_book_index] = {key: entries[key].get() if key!="Tür" else entries["Tür"].get() for key in entries}
    books[selected_book_index]["Fiyat"] = price_str
    books[selected_book_index]["Stok Durumu"] = isAvailable
    save_books()
    update_book_list(books)
    messagebox.showinfo("Başarılı","Kitap bilgileri güncellendi!")

def delete_book_gui():
    global selected_book_index
    if selected_book_index is None:
        messagebox.showwarning("Uyarı","Silmek için bir kitap seçin!")
        return
    book_name = books[selected_book_index]["Adı"]
    del books[selected_book_index]
    selected_book_index = None
    save_books()
    update_book_list(books)
    messagebox.showinfo("Başarılı",f"'{book_name}' silindi!")

# Butonlar
ctk.CTkButton(right_frame, text="Kitap Ekle", command=add_book_gui).pack(pady=5)
ctk.CTkButton(right_frame, text="Güncelle", command=update_book_gui).pack(pady=5)
ctk.CTkButton(right_frame, text="Sil", command=delete_book_gui).pack(pady=5)

app.mainloop()
