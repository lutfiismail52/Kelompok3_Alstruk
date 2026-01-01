# Program Bubble Sort
# Mengurutkan data dari kecil ke besar

data = []
jumlah = int(input("Masukkan jumlah data: "))

for i in range(jumlah):
    nilai = int(input(f"Masukkan data ke-{i+1}: "))
    data.append(nilai)

print("Data sebelum diurutkan:", data)

for i in range(len(data)):
    for j in range(0, len(data)-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print("Data setelah diurutkan:", data)
