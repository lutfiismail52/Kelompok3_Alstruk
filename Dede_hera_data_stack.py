# Program Stack (LIFO)
stack = []

while True:
    print("\nMenu Stack")
    print("1. Push")
    print("2. Pop")
    print("3. Tampilkan Stack")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        stack.append(data)
        print("Data berhasil ditambahkan")
    elif pilihan == "2":
        if len(stack) == 0:
            print("Stack kosong")
        else:
            print("Data keluar:", stack.pop())
    elif pilihan == "3":
        print("Isi stack:", stack)
    elif pilihan == "4":
        print("Program Stack selesai")
        break
    else:
        print("Pilihan tidak valid")