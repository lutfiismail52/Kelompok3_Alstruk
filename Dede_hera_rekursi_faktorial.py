# Program Faktorial dengan Rekursi

def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)

angka = int(input("Masukkan angka: "))

if angka <= 0:
    print("Angka harus lebih dari 0")
else:
    print("Hasil faktorial dari", angka, "adalah", faktorial(angka))