# Program Queue (FIFO)
queue = []

while True:
    print("\nMenu Queue")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Tampilkan Queue")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        queue.append(data)
        print("Data berhasil ditambahkan")
    elif pilihan == "2":
        if len(queue) == 0:
            print("Queue kosong")
        else:
            print("Data keluar:", queue.pop(0))
    elif pilihan == "3":
        print("Isi queue:", queue)
    elif pilihan == "4":
        print("Program Queue selesai")
        break
    else:
        print("Pilihan tidak valid")