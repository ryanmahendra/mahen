# ======================================================================
# BAGIAN 4: KASIR
# ======================================================================
def kasir():
    keranjang = []   # isi: {"id":..., "nama":..., "harga":..., "jumlah":...}

    # --- Langkah 1: pilih obat sampai selesai ---
    while True:
        tampilkan_stok()
        id_obat = minta_angka("\nMasukkan ID obat (0 = selesai belanja): ")
        if id_obat == 0:
            break

        obat = cari_obat(id_obat)
        if obat is None:
            print("   ID tidak ditemukan.")
            continue

        # Hitung stok yang masih bisa dijual (stok gudang dikurangi yang sudah di keranjang)
        sudah_dipilih = sum(k["jumlah"] for k in keranjang if k["id"] == id_obat)
        tersedia = obat["stok"] - sudah_dipilih
        if tersedia <= 0:
            print("   Stok habis.")
            continue

        jumlah = minta_angka(f"Jumlah {obat['nama']} (tersedia {tersedia}): ", minimal=1)
        if jumlah > tersedia:
            print("   Jumlah melebihi stok.")
            continue

        keranjang.append({"id": obat["id"], "nama": obat["nama"],
                          "harga": obat["harga"], "jumlah": jumlah})
        print(f"   {obat['nama']} x{jumlah} masuk keranjang.")

    if not keranjang:
        print("Keranjang kosong, transaksi dibatalkan.")
        return

    # --- Langkah 2: hitung total ---
    total = sum(k["harga"] * k["jumlah"] for k in keranjang)
    print("\nRINGKASAN BELANJA")
    for k in keranjang:
        print(f"  {k['nama']:<24}{k['jumlah']:>3} x {rupiah(k['harga']):>9}")
    print(f"  TOTAL: {rupiah(total)}")

    # --- Langkah 3: pembayaran ---
    while True:
        bayar = minta_angka("Uang diterima (0 = batal): ")
        if bayar == 0:
            print("Transaksi dibatalkan.")
            return
        if bayar >= total:
            break
        print(f"   Uang kurang {rupiah(total - bayar)}.")

    # --- Langkah 4: kurangi stok & simpan transaksi ---
    for k in keranjang:
        cari_obat(k["id"])["stok"] -= k["jumlah"]

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M")
    data["transaksi"].append({"waktu": waktu, "total": total, "bayar": bayar,
                              "barang": keranjang})
    simpan_data()

    # --- Langkah 5: cetak struk di layar ---
    print("\n" + "=" * 40)
    print(f" STRUK  {waktu}")
    print("=" * 40)
    for k in keranjang:
        print(f" {k['nama']:<22}{k['jumlah']:>3} x {rupiah(k['harga']):>9}")
    print("-" * 40)
    print(f" Total     : {rupiah(total)}")
    print(f" Bayar     : {rupiah(bayar)}")
    print(f" Kembalian : {rupiah(bayar - total)}")
    print("=" * 40)