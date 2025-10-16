import re

data_produk = []

def validasi_nama(nama):
    if not re.match(r'^[A-Za-z0-9 ]+$', nama):
        raise ValueError("Nama produk hanya boleh berisi huruf, angka, dan spasi!")
    return nama

def validasi_kode(kode):
    if not re.match(r'^[A-Z]{3,5}[0-9]{3,5}$', kode):
        raise ValueError("Kode produk harus terdiri dari 3-5 huruf kapital diikuti 3-5 angka!")
    return kode

def validasi_email(email):
    if not re.match(r'^[\a-z0-9\.-]+@[\a-z\.-]+\.[a-z]+$', email):
        raise ValueError("Format email tidak valid!")
    return email

def harga_satuan(harga):
    try:
        harga = float(harga)
        if harga <= 0:
            raise ValueError("Harga tidak boleh negatif.")
        return harga
    except ValueError:
        raise ValueError("Harga harus berupa angka")

def stok_barang(stok):
    try:
        nilai = int(stok)
        if nilai < 0:
            raise ValueError("stok tidak boleh negatif!")
        return nilai
    except ValueError:
        raise ValueError("stok harus berupa angka")


def hitung_penjualan(harga, stok):
    return harga * stok

def tentukan_kategori(harga):
    if harga >= 5000000:
        return "Mahal"
    elif harga > 1000000:
        return "Sedang"
    else:
        return "Murah"

def analisis_data():
    try:
        if not data_produk:
            raise ValueError("Tidak ada data produk untuk dianalisis!")

        print("\n=== HASIL ANALISIS DATA ===")
        total_penjualan = 0
        total_harga = 0
        kategori_count = {"Mahal": 0, "Sedang": 0, "Murah": 0}

        for p in data_produk:
            total_penjualan += p['Penjualan']
            total_harga += p['Harga']
            kategori_count[p['Kategori']] += 1
            print(f"{p['Nama']} ({p['Kode']}) - Harga: Rp{p['Harga']:,} - Stok: {p['Stok']} - Penjualan: Rp{p['Penjualan']:,} - Kategori: {p['Kategori']}")

        rata_harga = total_harga / len(data_produk)
        produk_termahal = max(data_produk, key=lambda x: x['Harga'])
        produk_termurah = min(data_produk, key=lambda x: x['Harga'])

        print(f"\nTotal Penjualan Keseluruhan: Rp{total_penjualan:,}")
        print(f"Rata-rata Harga Produk: Rp{rata_harga:,.0f}")
        print(f"Produk Termahal: {produk_termahal['Nama']} (Rp{produk_termahal['Harga']:,})")
        print(f"Produk Termurah: {produk_termurah['Nama']} (Rp{produk_termurah['Harga']:,})\n")

        print(f"Jumlah Produk Kategori Mahal: {kategori_count['Mahal']}")
        print(f"Jumlah Produk Kategori Sedang: {kategori_count['Sedang']}")
        print(f"Jumlah Produk Kategori Murah: {kategori_count['Murah']}")

        print("\n=== DAFTAR PRODUK (REKURSIF) ===")
        tampilkan_rekursif(data_produk, 0)
        print("\nData berhasil dianalisis!")
        
    except ValueError as e:
        print(f"\nError: {e}")

def tampilkan_rekursif(list_produk, index):
    if index < len(list_produk):
        print(list_produk[index]['Nama'])
        tampilkan_rekursif(list_produk, index + 1)

def input_data():
    while True:
        nama = input("\nNama Produk (ketik 'selesai' untuk kembali ke menu): ")
        if nama.lower() =='selesai':
            break
        try:
            nama = validasi_nama(nama)
            kode = validasi_kode(input("Kode Produk: "))
            email = validasi_email(input("Email Supplier: "))
            harga = harga_satuan(input("Harga Produk: "))
            stok = stok_barang(input("Stok Barang: "))

            penjualan = hitung_penjualan(harga, stok)
            kategori = tentukan_kategori(harga)

            produk = {
                "Nama": nama,
                "Kode": kode,
                "Email": email,
                "Harga": harga,
                "Stok": stok,
                "Penjualan": penjualan,
                "Kategori": kategori
            }
            data_produk.append(produk)
            print("Data produk berhasil disimpan!")
        except ValueError as e:
            print(f" Error: {e}")
def main():
    while True:
        print("\n=== SISTEM ANALISIS DATA PRODUK E-COMMERCE ===")
        print("=== MENU UTAMA ===")
        print("1. Input Data Produk")
        print("2. Lihat Hasil Analisis")
        print("3. Keluar Program")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            input_data()
        elif pilihan == '2':
            analisis_data()
        elif pilihan == '3':
            print("\nTerima kasih telah menggunakan program ini! ")
            break
        else:
            print("=Pilihan tidak valid, coba lagi!")

if __name__ == "_main_": main()

main()