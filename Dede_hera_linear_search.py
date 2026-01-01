# Program Linear Search
# Mencari data dalam list

data = []
jumlah = int(input("Masukkan jumlah data: "))

for i in range(jumlah):
    nilai = int(input(f"Masukkan data ke-{i+1}: "))
    data.append(nilai)

print("Data yang dimasukkan:", data)

cari = int(input("Masukkan data yang ingin dicari: "))

ditemukan = False
for i in range(len(data)):
    if data[i] == cari:
        print(f"Data {cari} ditemukan pada indeks ke-{i}")
        ditemukan = True
        break

if not ditemukan:
    print("Data tidak ditemukan")