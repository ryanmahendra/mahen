# =======================================================
# BAGIAN 1: MENYIMPAN DAN MEMBACA DATA
# =======================================================
def simpan_data():
    """Tulis isi variabel data ke file JSON. Dipanggil setiap ada perubahan."""
    with open(FILE_DATA,"w", encoding="utf-8") as file:
       json.dump(data,file, indent=2, ensure_ascii=False)


def muat_data():
    """Dipanggil sekali saat program mulai.
    Jika file sudah ada -> bacanya. Jika belum -> buat 3 obat contoh."""
    global data
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, encoding="utf-8") as file:
            data = json.load(file)
    else:
        data["obat"] = [
            {"kode": "01", "nama": "Paracetamol 500mg", "harga": 5000,
             "stok": 50, "kadaluwarsa": "30-06-2028"},
            {"kode": "02", "nama": "Vitamin C", "harga": 22000,
             "stok": 8, "kadaluwarsa": "31-03-2027"},
            {"kode": "03", "nama": "Antasida", "harga": 4000,
             "stok": 30, "kadaluwarsa": "15-01-2027"}
        ]
        simpan_data()
        