import re
import time

# Data lengkap
raw_data = [
    {"nama": "   Andi", "umur": "23 th", "kota": "jakrta"},
    {"nama": "Budi", "umur": " 30", "kota": "bandung "},
    {"nama": "citra", "umur": "tiga puluh", "kota": "JKT"},
    {"nama": "dwi", "umur": None, "kota": "surabaya"},
    {"nama": "Eka  ", "umur": "19", "kota": "bdg"},
    {"nama": "Fajar", "umur": "22tahun", "kota": "Jakarta"},
    {"nama": "gita", "umur": " - ", "kota": None},
    {"nama": "   hadi", "umur": "27", "kota": "sby"},
    {"nama": "Ika", "umur": "24 thn", "kota": "Jakrta"},
    {"nama": "joni", "umur": "31", "kota": "Bandun"},
    {"nama": "kiki", "umur": "17", "kota": ""},
    {"nama": "lina", "umur": "dua puluh", "kota": "J K T"},
    {"nama": "marco", "umur": "40+", "kota": " Surabaya"},
    {"nama": "nina", "umur": None, "kota": "jakartaa"},
    {"nama": "Omar", "umur": "18 th", "kota": "bdg "},
    {"nama": "putri", "umur": " 28", "kota": "SBY"},
    {"nama": None, "umur": "25", "kota": "Jakarta"},
    {"nama": "rini", "umur": "21 tahun", "kota": "banddung"},
    {"nama": "Sari", "umur": "0x1A", "kota": "Surabay"},
    {"nama": "toni", "umur": "35", "kota": "JKT"},
    {"nama": "umar", "umur": "36 th", "kota": "jakrta"},
    {"nama": "Vina", "umur": "23TH", "kota": None},
    {"nama": "Wawan", "umur": "-", "kota": "SBY"},
    {"nama": "xena", "umur": "29 thn", "kota": "bdung"},
    {"nama": "yani", "umur": "32", "kota": "Jakarta"},
    {"nama": "zaki", "umur": "empat puluh", "kota": "surabyaa"},
    {"nama": "aldi", "umur": "33th", "kota": "bdg"},
    {"nama": "bella", "umur": None, "kota": "bandung"},
    {"nama": "cindy", "umur": "25", "kota": "SBY "},
    {"nama": "dani", "umur": "??", "kota": "JKT"},
    {"nama": "elisa", "umur": "27tahun", "kota": "Jakarat"},
    {"nama": "farhan", "umur": "22", "kota": "sby"},
    {"nama": "galih", "umur": "31 th", "kota": "bdg"},
    {"nama": "hani", "umur": "17", "kota": "jakartA"},
    {"nama": "indra", "umur": "-", "kota": "BAndung"},
    {"nama": "joni", "umur": "21", "kota": "JKT "},
    {"nama": "kevin", "umur": "dua3", "kota": "sbY"},
    {"nama": "linda", "umur": "26", "kota": " surabaya"},
    {"nama": "maya", "umur": "  20 th", "kota": "jakrta"},
    {"nama": "nanda", "umur": "34 thn", "kota": "bdG"},
    {"nama": "oppa", "umur": None, "kota": "bandng"},
    {"nama": "peter", "umur": "25", "kota": "SBY"},
    {"nama": "Qori", "umur": "24 tahun", "kota": "jakarTa"},
    {"nama": "riko", "umur": "3O", "kota": "Bandunng"},
    {"nama": "Sinta", "umur": "20", "kota": "JKT"},
    {"nama": "Tono", "umur": "18", "kota": "BdG"},
    {"nama": "Uli", "umur": "19tahun", "kota": " SBY"},
    {"nama": "vera", "umur": "th30", "kota": "Jakartaa"},
    {"nama": "wiliam", "umur": "40", "kota": "surabay"},
]

# Fungsi Cleaning

def clean_nama(nama): 
    """Membersihkan nama: strip dan Title Case."""
    return nama.strip().title() if nama else None

def clean_umur(umur_str): 
    """Ekstraksi angka dari string umur, mengembalikan None jika tidak valid."""
    if not umur_str or str(umur_str).strip() in ['-', ' - ', '??', '']: 
        return None
    cleaned = str(umur_str).strip().lower()
    
    # Deteksi dan konversi heksadesimal
    hex_match = re.search(r'0x([0-9a-f]+)', cleaned)
    if hex_match: 
        return int(hex_match.group(1), 16)
        
    # Ekstraksi angka murni (mengabaikan teks angka seperti 'tiga puluh')
    angka_match = re.search(r'\d+', re.sub(r'[^\w\s]', '', cleaned))
    return int(angka_match.group(0)) if angka_match else None

def clean_kota(kota):
    """Membersihkan dan menstandarisasi nama kota."""
    if not kota: return None
    cleaned = str(kota).strip().lower()
    kota_map = {
        'jakarta':['jakrta','jkt','j k t','jakartaa','jakartA','jakarTa'],
        'bandung':['bdg','banddung','bandng','banding','bandun','bandunng'],
        'surabaya':['sby','surabay','surabyaa']
    }
    
    for standar, variasi in kota_map.items():
        if cleaned == standar or cleaned in variasi: return standar.title()
        
    return cleaned.title() # Mengembalikan nilai bersih jika tidak masuk peta

# Clean semua data
cleaned_data = []
for i, data in enumerate(raw_data):
    cleaned = {
        'id': i+1, 
        'nama': clean_nama(data['nama']), 
        'umur': clean_umur(data['umur']), 
        'kota': clean_kota(data['kota'])
    }
    cleaned_data.append(cleaned)

# 5 Algoritma Sorting
# Di program utama, kita akan sort berdasarkan indeks ke-2 (umur)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][2] > arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key[2] < arr[j][2]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx][2] > arr[j][2]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Menggunakan helper untuk Quick dan Merge Sort
def quick_sort_helper(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2][2]
    left = [x for x in arr if x[2] < pivot]
    middle = [x for x in arr if x[2] == pivot]
    right = [x for x in arr if x[2] > pivot]
    return quick_sort_helper(left) + middle + quick_sort_helper(right)

def merge_helper(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_helper(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort_helper(arr[:mid])
    right = merge_sort_helper(arr[mid:])
    return merge_helper(left, right)

# Dictionary algoritma
ALGORITMA = {
    1: ("Bubble Sort", bubble_sort),
    2: ("Insertion Sort", insertion_sort),
    3: ("Selection Sort", selection_sort),
    4: ("Quick Sort", quick_sort_helper),
    5: ("Merge Sort", merge_sort_helper)
}

# Fungsi Filter Data

def filter_data(pilihan):
    """Filter data berdasarkan pilihan, mengembalikan list of tuple (id, nama, umur) yang valid."""
    valid_data = [(d['id'], d['nama'], d['umur'], d['kota']) 
                for d in cleaned_data if d['umur'] is not None and d['nama'] is not None]
                
    if pilihan == 1: 
        data_set = valid_data
    elif pilihan == 2: 
        data_set = [d for d in valid_data if d[3] == 'Jakarta']
    elif pilihan == 3: 
        data_set = [d for d in valid_data if d[3] == 'Bandung']
    elif pilihan == 4: 
        data_set = [d for d in valid_data if d[3] == 'Surabaya']
    elif pilihan == 5: 
        data_set = [d for d in valid_data if d[2] < 20]
    elif pilihan == 6: 
        data_set = [d for d in valid_data if d[2] > 30]
    else:
        return []

    # Kita hanya membutuhkan (id, nama, umur) untuk sorting
    return [(d[0], d[1], d[2]) for d in data_set]

# Fungsi Menu

def tampilkan_menu_data():
    """Menampilkan menu data dengan hitungan dinamis."""
    print("\n" + "="*70)
    print("          PILIH DATA UNTUK DI-SORTING")
    print("="*70)
    print(f"1. SEMUA DATA VALID ({len(filter_data(1))})")
    print(f"2. DATA JAKARTA ({len(filter_data(2))})")
    print(f"3. DATA BANDUNG ({len(filter_data(3))})")
    print(f"4. DATA SURABAYA ({len(filter_data(4))})")
    print(f"5. DATA UMUR < 20 ({len(filter_data(5))})")
    print(f"6. DATA UMUR > 30 ({len(filter_data(6))})")
    print("0. KELUAR")
    print("="*70)

def tampilkan_menu_algoritma():
    """Menampilkan menu algoritma."""
    print("\n" + "="*50)
    print("          PILIH ALGORITMA SORTING")
    print("="*50)
    for key, (nama, _) in ALGORITMA.items():
        print(f"{key}. {nama}")
    print("0. KEMBALI KE MENU DATA")
    print("="*50)

# Program Utama

print("PROGRAM SORTING DATA SEDERHANA")

while True:
    tampilkan_menu_data()
    
    try:
        pilihan_data = int(input("Pilih data (0-6): "))
        if pilihan_data == 0: 
            print("Terima kasih!")
            break
            
        data_untuk_sort = filter_data(pilihan_data)
        if not data_untuk_sort:
            print("Data kosong untuk pilihan ini!")
            input("Tekan Enter untuk lanjut...")
            continue
            
        print(f"\nData dipilih: {len(data_untuk_sort)} record")
        print("Contoh 3 data pertama:", [f"{n}({u})" for _,n,u in data_untuk_sort[:3]])
        
        # LOOP PEMILIHAN ALGORITMA
        while True:
            tampilkan_menu_algoritma()
            pilihan_algo = int(input("Pilih algoritma (0-5): "))
            
            if pilihan_algo == 0: 
                break  # Kembali ke menu data
                
            if pilihan_algo not in ALGORITMA:
                print("Pilihan tidak valid!")
                input("Tekan Enter...")
                continue
                
            nama_algo, func_algo = ALGORITMA[pilihan_algo]
            
            # EKSEKUSI SORTING + WAKTU EKSEKUSI
            print(f"\nMenjalankan {nama_algo}...")
            print("-" * 60)
            
            # Membuat salinan data untuk memastikan data asli tidak berubah
            data_copy = data_untuk_sort.copy() 
            
            start_time = time.time()
            hasil_sort = func_algo(data_copy)
            end_time = time.time()
            waktu_eksekusi = (end_time - start_time) * 1000  # konversi ke ms
            
            print(f"Algoritma: {nama_algo}")
            print(f"Jumlah data: {len(hasil_sort)}")
            print(f"Waktu eksekusi: {waktu_eksekusi:.3f} ms")
            
            if hasil_sort:
                print(f"Termuda: {hasil_sort[0][1]} ({hasil_sort[0][2]} tahun)")
                print(f"Tertua: {hasil_sort[-1][1]} ({hasil_sort[-1][2]} tahun)")
            
            input("\nTekan Enter untuk pilih algoritma lain...")
            
    except ValueError:
        print("Masukkan angka yang valid!")
        input("Tekan Enter...")
    except KeyboardInterrupt:
        print("\nKeluar...")
        break
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
        input("Tekan Enter...")

print("\nProgram selesai!")
