
def main():
    print("=== Program Pemesanan Makanan & Minuman ===")

    nama = input("Masukkan nama pemesan: ").strip()

    # menu makanan
    makanan = {
        1: ["Nasi Goreng", 15000],
        2: ["Mie Ayam", 10000],
        3: ["Bakso", 13000],
        4: ["Sate Ayam", 20000]
    }

    print("\n--- Menu Makanan ---")
    for i in makanan:
        print(f"{i}. {makanan[i][0]} - Rp{makanan[i][1]:,}".replace(",", "X").replace(".", ",").replace("X", "."))

    # --- INPUT MAKANAN (tanpa match/case) ---
    while True:
        try:
            pilih_makan = int(input("Pilih makanan (1-4): "))
            
            if pilih_makan not in makanan:
                print("Pilihan makanan tidak valid! Silakan coba lagi.")
                continue

            jml_makan = int(input("Jumlah makanan: "))
            
            if jml_makan <= 0:
                print("Jumlah makanan harus lebih dari 0! Silakan coba lagi.")
                continue

            break

        except ValueError:
            print("Input harus angka! Silakan coba lagi.")

    # menu minuman
    minuman = {
        1: ["Kopi Hitam", 5000],
        2: ["Kopi Susu", 7000],
        3: ["Es Teh Tawar", 4000],
        4: ["Es Teh Manis", 5000],
        5: ["Jus Buah", 8000]
    }

    print("\n--- Menu Minuman ---")
    for i in minuman:
        print(f"{i}. {minuman[i][0]} - Rp{minuman[i][1]:,}".replace(",", "X").replace(".", ",").replace("X", "."))

    # --- INPUT MINUMAN (tanpa match/case) ---
    while True:
        try:
            pilih_minum = int(input("Pilih minuman (1-5): "))
            
            if pilih_minum not in minuman:
                print("Pilihan minuman tidak valid! Silakan coba lagi.")
                continue

            jml_minum = int(input("Jumlah minuman: "))
            
            if jml_minum <= 0:
                print("Jumlah minuman harus lebih dari 0! Silakan coba lagi.")
                continue
            
            break
        
        except ValueError:
            print("Input harus angka! Silakan coba lagi.")

    # hitung total
    total_makan = makanan[pilih_makan][1] * jml_makan
    total_minum = minuman[pilih_minum][1] * jml_minum
    total = total_makan + total_minum

    # --- METODE PEMBAYARAN MENGGUNAKAN MATCH CASE ---
    print("\n--- Metode Pembayaran ---")
    print("1. Cash")
    print("2. Transfer Bank")
    print("3. GoPay")
    print("4. ShopeePay")
    print("5. Dana")

    pilih_bayar = input("Pilih metode (1-5): ")

    # Implementasi match case (switch case) untuk pemilihan metode
    match pilih_bayar:
        case "1":
            cara_bayar = "Cash"
        case "2":
            cara_bayar = "Transfer Bank"
        case "3":
            cara_bayar = "GoPay"
        case "4":
            cara_bayar = "ShopeePay"
        case "5":
            cara_bayar = "Dana"
        case _: # Case default (mirip 'else' atau 'default' pada switch)
            cara_bayar = "Tidak Diketahui / Pilihan Tidak Valid"

    # --- OUTPUT / STRUK ---
    def format_rupiah(angka):
        return f"Rp{angka:,}".replace(",", "X").replace(".", ",").replace("X", ".")

    print("\n========= STRUK PESANAN =========")
    print(f"Nama Pemesan     : {nama}")
    print(f"Makanan          : {makanan[pilih_makan][0]} x{jml_makan} = {format_rupiah(total_makan)}")
    print(f"Minuman          : {minuman[pilih_minum][0]} x{jml_minum} = {format_rupiah(total_minum)}")
    print("---------------------------------")
    print(f"Total Bayar      : {format_rupiah(total)}")
    print(f"Metode Pembayaran: {cara_bayar}")
    print("=================================")
    print("Terima kasih sudah memesan :)")

if __name__ == "__main__":
    main()