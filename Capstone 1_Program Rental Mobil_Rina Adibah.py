from datetime import datetime, timedelta
from textwrap import fill
from tabulate import tabulate
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# =======================================================================================================================================#
#                                                              DATA MOBIL
# =======================================================================================================================================#

# Daftar Aset Mobil
Aset_Mobil = [
    {'Plat': 'A001', 'Model': 'Camry', 'Tarif Harian': 1200000, 'Warna': 'Silver', 'Rating': 4.9, 'Ketersediaan': True, 'fitur_unggulan': [
        'Nyaman dan irit bahan bakar',
        'Interior mewah',
        'Performa mesin yang halus',
        'Ruang kabin luas',
        'Sistem keamanan canggih'
    ]},
    {'Plat': 'B002', 'Model': 'Fortuner', 'Tarif Harian': 850000, 'Warna': 'Hitam', 'Rating': 4.7, 'Ketersediaan': True,'fitur_unggulan': [
        'Tangguh di segala medan',
        'Kabin luas dan nyaman',
        'Desain eksterior gagah',
        'Performa off-road yang baik',
        'Fitur keselamatan lengkap'
    ]},
    {'Plat': 'C003', 'Model': 'Civic', 'Tarif Harian': 750000, 'Warna': 'Biru', 'Rating': 4.6, 'Ketersediaan': True,'fitur_unggulan': [
        'Desain sporty dan modern',
        'Efisiensi bahan bakar tinggi',
        'Handling yang baik',
        'Interior ergonomis',
        'Sistem infotainment canggih'
    ]},
    {'Plat': 'D004', 'Model': 'Pajero', 'Tarif Harian': 950000, 'Warna': 'Grey', 'Rating': 4.8, 'Ketersediaan': True,'fitur_unggulan': [
        'Kemampuan off-road luar biasa',
        'Interior mewah dan nyaman',
        'Mesin bertenaga',
        'Sistem suspensi yang nyaman',
        'Fitur keselamatan lengkap'
    ]},
    {'Plat': 'E005', 'Model': 'Terios', 'Tarif Harian': 1300000, 'Warna': 'Merah', 'Rating': 4.5, 'Ketersediaan': True,'fitur_unggulan': [
        'Harga terjangkau',
        'Ruang kabin luas',
        'Desain modern',
        'Konsumsi bahan bakar efisien',
        'Fitur keselamatan standar'
    ]},
    {'Plat': 'F006', 'Model': 'Ertiga', 'Tarif Harian': 250000, 'Warna': 'Putih', 'Rating': 4.4, 'Ketersediaan': True,'fitur_unggulan': [
        'Ekonomis dan irit bahan bakar',
        'Ruang kabin yang cukup luas',
        'Desain simpel dan elegan',
        'Perawatan mudah',
        'Fitur hiburan standar'
    ]},
    {'Plat': 'G007', 'Model': 'Alphard', 'Tarif Harian': 1500000, 'Warna': 'Hitam', 'Rating': 4.8, 'Ketersediaan': True,'fitur_unggulan': [
        'Kemewahan dan kenyamanan maksimal',
        'Ruang kabin sangat luas',
        'Fitur hiburan lengkap',
        'Performa mesin yang kuat',
        'Sistem keamanan mutakhir'
    ]},
    {'Plat': 'H008', 'Model': 'Jazz', 'Tarif Harian': 600000, 'Warna': 'Kuning', 'Rating': 4.5, 'Ketersediaan': True,'fitur_unggulan': [
        'Desain compact dan stylish',
        'Handling lincah di perkotaan',
        'Konsumsi bahan bakar irit',
        'Kabin fleksibel dan luas untuk kelasnya',
        'Sistem audio berkualitas tinggi'
    ]},
    {'Plat': 'I009', 'Model': 'CR-V', 'Tarif Harian': 1100000, 'Warna': 'Putih', 'Rating': 4.7, 'Ketersediaan': True,'fitur_unggulan': [
        'Performa tangguh untuk perjalanan jauh',
        'Kenyamanan suspensi yang baik',
        'Kabin luas dan mewah',
        'Fitur keselamatan modern',
        'Mesin bertenaga dengan efisiensi baik'
    ]},
    {'Plat': 'J010', 'Model': 'Xenia', 'Tarif Harian': 400000, 'Warna': 'Merah', 'Rating': 4.3, 'Ketersediaan': True,'fitur_unggulan': [
        'Harga ekonomis',
        'Kabin lega untuk keluarga',
        'Konsumsi bahan bakar irit',
        'Desain eksterior modern',
        'Fitur keselamatan dasar'
    ]}
]

List_Mobil_Tersewa = []

# ====================================================================================================================================== #
#                                                       FUNGSI SIGN UP / LOGIN
# ====================================================================================================================================== #

users = {}
#=========== Fungsi SIGN UP ===========#
def func_sign_up():
    print(Fore.YELLOW + "\n--- Pendaftaran Pengguna Baru ---")

    # validasi username
    while True:
        username = input('Masukkan username: ').strip()
        if not username:
            print(Fore.RED + '⚠️  Username tidak boleh kosong, silakan coba lagi.')
            continue
        if username in users:
            print(Fore.RED + '⚠️  Username sudah terdaftar, coba username lain.')
            continue
        break

    # Validasi password
    while True:
        password = input('Masukkan password: ').strip()
        if not password:
            print(Fore.RED + '⚠️  Password tidak boleh kosong, silakan coba lagi.')
            continue
        break
    
    users[username] = password
    print(Fore.GREEN + '\nRegistrasi berhasil 🎉')
    input(Fore.CYAN + 'Silakan tekan Enter untuk melanjutkan ke menu login...')
    return func_login_pelanggan()

#=========== Fungsi LOG IN PELANGGAN ===========#
def func_login_pelanggan():
    print(Fore.YELLOW + "\n--- Login Pengguna ---")

    while True:
        username = input('Masukkan username: ')
        password = input('Masukkan password: ')
    
        if username in users and users[username] == password:
            print(Fore.GREEN + 'Login berhasil, Halo 👋')
            return func_menu_pelanggan() 
        else:
            print(Fore.RED + '⚠️  Login gagal! Username atau password salah.')
            
            # Opsi mencoba login lagi atau keluar
            retry = input(Fore.YELLOW + 'Coba lagi?' + '(ya/tidak): ' + Style.RESET_ALL).lower()
            if retry != 'ya':
                print(Fore.CYAN + 'Kembali ke menu utama...')
                return func_menu_awal()
        
#=========== Fungsi Login Admin ===========# 
def func_login_admin():
    print(Fore.YELLOW + "\n--- Login Admin ---")

    while True:
        password = input('Masukkan Password Admin: ')
        if not password:
            print(Fore.RED + '⚠️  Password tidak boleh kosong. Silakan coba lagi.')
        else: 
            if password == 'admin123':
                print(Fore.GREEN + 'Login Admin berhasil. Halo admin! 👋')
                return func_menu_admin()
            else:
                print(Fore.RED + '⚠️  Password salah. Akses ditolak!')
                continue

# ====================================================================================================================================== #
#                                                               FUNGSI PELANGGAN
# ====================================================================================================================================== #
# Menu Pelanggan: Yuk Sewa Mobil 
def func_yuk_sewa():
    while True:
        print(Fore.YELLOW + '''
=====================================''' + Fore.WHITE + '''
>>>>>>>>>> MENU PENYEWAAN <<<<<<<<<<<''' + Fore.YELLOW + '''
=====================================''')
        pilihan_menu_sewa =input(Fore.CYAN + '''  
           1. Sewa Mobil
   2. Cek fitur dan rating mobil''' + Fore.WHITE + '''

    9. Kembali ke Menu Pelanggan 
      0. Kembali ke Menu Utama''' + Fore.YELLOW + '''
        
=====================================''' + Fore.WHITE + '''
Masukkan pilihanmu: ''')
        if pilihan_menu_sewa == '': 
            print(Fore.RED + '⚠️  Input tidak boleh kosong, coba lagi!')
        elif pilihan_menu_sewa == '1':
            func_sewa_mobil()
            break
        elif pilihan_menu_sewa == '2':
            func_cek_fitur_rating()
            break
        elif pilihan_menu_sewa == '9':
            func_menu_pelanggan()
            break
        elif pilihan_menu_sewa == '0':
            func_menu_awal()
            break
        else:
            print(Fore.RED + '⚠️  Pilihan nggak ada nih, cek lagi yuk!')
            continue

# Fungsi Cek fitur dan Rating Mobil (Katalog)
def func_cek_fitur_rating():
    print(Fore.YELLOW + '''
================================''' + Fore.WHITE + '''
>>> REVIEW DAN RATING MOBIL <<< ''' + Fore.YELLOW + '''
================================''')
    for mobil in Aset_Mobil:
        print(Fore.WHITE + f"🚗  Model: {mobil['Model']}\n⭐  Rating: {mobil['Rating']}\n🔍  Fitur Unggulan:")
        for fitur in mobil['fitur_unggulan']:
            print(Fore.MAGENTA + f"     - {fitur}")
        print(Fore.WHITE + "\n" + "="*40 + "\n")
    
    input(Fore.CYAN + "\nTekan Enter untuk kembali ke menu penyewaan...")
    func_yuk_sewa()

# Fungsi Sewa Mobil
def func_sewa_mobil():
    print(Fore.WHITE + '''
------------------- PILIH MOBILMU---------------------''' + Fore.YELLOW + '''
======================================================''' + Fore.WHITE + '''
          >>>>>> DAFTAR SELURUH MOBIL <<<<<<''' + Fore.YELLOW + '''
======================================================''' + Fore.WHITE + '''
| Plat   | Model    | Tarif Harian | Warna  | Rating |''' + Fore.YELLOW + '''
------------------------------------------------------''')
    for mobil in Aset_Mobil:
        if mobil['Ketersediaan']:
            print(f"| {mobil['Plat']:<6} | {mobil['Model']:<8} | Rp {mobil['Tarif Harian']:<9} | {mobil['Warna']:<6} | {mobil['Rating']:<6} |")
    
    print(Fore.YELLOW + "\n" + "="*55 + "\n")

    # inputan ulang ketika plat mobil tidak ditemukan
    while True: 
        plat_mobil = input('Masukkan Plat Mobil yang ingin disewa: ').upper()
        mobil_ditemukan = next((mobil for mobil in Aset_Mobil if mobil['Plat'].upper() == plat_mobil and mobil['Ketersediaan']), None)
            
        if mobil_ditemukan: # Jika mobil ditemukan, lanjutkan proses penyewaan
            while True:
                try:
                    # input dan memvalidasi input pengguna
                    hari = int(input('Masukkan jumlah hari sewa: '))
                    if hari <= 0:
                        print(Fore.RED + '⚠️  Jumlah hari harus lebih dari 0.')
                        continue # kembali ke input hari jika invalid
                    break
                except ValueError:
                    # Error handling for invalid numeric input
                    print(Fore.RED + '⚠️  Input tidak valid. Jumlah hari harus berupa angka.')
                    continue # kembali ke input hari jika invalid
            
            # Ambil waktu peminjaman saat ini
            waktu_peminjaman = datetime.now()  # Waktu peminjaman sekarang
            waktu_pengembalian = waktu_peminjaman + timedelta(days=hari)  # Waktu pengembalian dihitung berdasarkan hari sewa

            # Menghitung total biaya
            total_biaya = mobil_ditemukan['Tarif Harian'] * hari
            print(Fore.GREEN + f'💰 Total biaya sewa: Rp {total_biaya}')

            # Konfirmasi pengguna untuk melakukan rental
            while True:
                konfirmasi = input(Fore.YELLOW + '❔  Konfirmasi penyewaan' + Fore.WHITE +  '(ya/tidak)? ').lower()
                if konfirmasi == 'ya':
                    mobil_ditemukan['Ketersediaan'] = False
                    mobil_sewa = mobil_ditemukan.copy()
                    mobil_sewa['Durasi'] = hari
                    mobil_sewa['Waktu Peminjaman'] = waktu_peminjaman
                    mobil_sewa['Waktu Pengembalian'] = waktu_pengembalian
                    mobil_sewa['Total Biaya'] = total_biaya # Menyimpan total biaya
                    List_Mobil_Tersewa.append(mobil_sewa)

                    # Tampilkan Receipt Penyewaan
                    print(Fore.GREEN + f'\n✔️  Mobil dengan plat {plat_mobil} berhasil disewa!')
                    print(Fore.GREEN + '\n============' + Fore.YELLOW + 'RECEIPT PENYEWAAN' + Fore.GREEN + '============')
                    print(f"Model        : {mobil_sewa['Model']}")
                    print(f"Plat Mobil   : {mobil_sewa['Plat']}")
                    print(f"Warna        : {mobil_sewa['Warna']}")
                    print(f"Tarif Harian : Rp {mobil_sewa['Tarif Harian']}")
                    print(f"Jumlah Hari  : {hari} hari")
                    print(f"Total Biaya  : Rp {total_biaya}")
                    print(f"Waktu Peminjaman: {mobil_sewa['Waktu Peminjaman'].strftime('%Y-%m-%d %H:%M:%S')}")
                    print(f"Waktu Pengembalian: {mobil_sewa['Waktu Pengembalian'].strftime('%Y-%m-%d %H:%M:%S')}")
                    print(Fore.GREEN + "===========================================\n")
                
                    # Arahkan pengguna kembali ke menu pelanggan
                    input(Fore.CYAN + "Tekan Enter untuk kembali ke menu pelanggan...")
                    return func_menu_pelanggan()

                elif konfirmasi == 'tidak':
                    # Jika rental is canceled
                    print(Fore.RED + "\n=====" + Fore.WHITE + 'PENYEWAAN DIBATALKAN' + Fore.RED + "=====\n")
                    print(f"Model        : {mobil_ditemukan['Model']}")
                    print(f"Plat Mobil   : {mobil_ditemukan['Plat']}")
                    print(f"Warna        : {mobil_ditemukan['Warna']}")
                    print(f"Tarif Harian : Rp {mobil_ditemukan['Tarif Harian']}")
                    print(f"Total Biaya  : Rp {total_biaya}")
                    print(Fore.RED + "\nPenyewaan Anda telah dibatalkan.")
                    print(Fore.RED + "===============================")

                    input(Fore.CYAN + "Tekan Enter untuk kembali ke menu pelanggan...")
                    return func_menu_pelanggan()
            
                else:
                    print(Fore.RED + '⚠️  Input tidak valid. Coba lagi!')
                    continue

        else:
            print(Fore.RED + '⚠️  Plat mobil tidak ditemukan atau tidak tersedia.')
            continue # Kembali ke input plat mobil

# Balikin Mobil Yuk
def func_balikin_mobil():
    # Cek apakah ada mobil yang disewa
    if not List_Mobil_Tersewa:
        print(Fore.YELLOW + '''
===========================================''' + Fore.RED + '''
       >>>>> PENGEMBALIAN MOBIL <<<<<''' + Fore.YELLOW + '''
===========================================''' + Fore.WHITE + '''

      Anda saat ini *TIDAK* memiliki
        mobil yang sedang disewa.

   Mohon cek kembali jika ada kesalahan,
     atau sewa mobil sekarang di menu 
             penyewaan mobil!''' + Fore.YELLOW + '''

===========================================''')
        input(Fore.CYAN + 'Tekan enter untuk kembali ke menu pelanggan...')
        return func_menu_pelanggan()
    
    table_data = []
    no = 1
    for mobil in List_Mobil_Tersewa:
        waktu_peminjaman = mobil['Waktu Peminjaman'].strftime('%Y-%m-%d %H:%M:%S')
        waktu_pengembalian = mobil['Waktu Pengembalian'].strftime('%Y-%m-%d %H:%M:%S')
        table_data.append([
            no, mobil['Plat'], mobil['Model'], mobil['Warna'], 
            f"Rp {mobil['Tarif Harian']}", f"{mobil['Durasi']} hari", 
            waktu_peminjaman, waktu_pengembalian, f"Rp {mobil['Total Biaya']}"
        ])
        no += 1

    # Display the table using tabulate
    headers = ["No", "Plat", "Model", "Warna", "Tarif Harian", "Durasi Sewa", "Waktu Peminjaman", "Waktu Pengembalian", "Total Biaya"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    while True:
        # Input plat mobil yang ingin dikembalikan
        plat_mobil = input(Fore.YELLOW + '\nMasukkan Plat Mobil yang ingin dikembalikan: ').upper()

        # Cari mobil yang ingin dikembalikan di list mobil yang disewa
        mobil_ditemukan = next((mobil for mobil in List_Mobil_Tersewa if mobil['Plat'].upper() == plat_mobil), None)

        if mobil_ditemukan:
            print(Fore.YELLOW + '''
--------------------------------------------''' + Fore.WHITE + '''
    DETAIL MOBIL YANG AKAN DIKEMBALIKAN''' + Fore.WHITE + '''
--------------------------------------------''')
            print(Fore.GREEN + f"Model        : {mobil_ditemukan['Model']}")
            print(f"Plat Mobil   : {mobil_ditemukan['Plat']}")
            print(f"Warna        : {mobil_ditemukan['Warna']}")
            print(f"Tarif Harian : Rp {mobil_ditemukan['Tarif Harian']}")
            print(f"Durasi Sewa  : {mobil_ditemukan['Durasi']} hari")
            print(f"Waktu Peminjaman: {mobil_ditemukan['Waktu Peminjaman'].strftime('%Y-%m-%d %H:%M:%S')}")  # Tampilkan waktu peminjaman
            print(f"Waktu Pengembalian: {mobil_ditemukan['Waktu Pengembalian'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(Fore.YELLOW + '\n--------------------------------------------\n')
        
            konfirmasi = input(Fore.YELLOW + f"❔  Apakah Anda yakin ingin mengembalikan mobil {mobil_ditemukan["Model"]}?" + Fore.WHITE + '(ya/tidak): ').lower()
        
            # Jika pengembalian dikonfirmasi
            if konfirmasi == 'ya':
                # Update ketersediaan mobil di Aset_Mobil
                for mobil in Aset_Mobil:
                    if mobil['Plat'] == mobil_ditemukan['Plat']:
                        mobil['Ketersediaan'] = True
                        break
            
                # Hapus mobi dari list yang disewa
                List_Mobil_Tersewa.remove(mobil_ditemukan)
                print(Fore.GREEN + f'✔️  Mobil dengan plat {plat_mobil} berhasil dikembalikan!')

                # Tampilkan Receipt Pengembalian
                print(Fore.GREEN + '''
==========================================''' + Fore.WHITE + '''
        🧾 RECEIPT PENGEMBALIAN 🧾''' + Fore.GREEN + '''
==========================================''')
                print(f"Model        : {mobil_ditemukan['Model']}")
                print(f"Plat Mobil   : {mobil_ditemukan['Plat']}")
                print(f"Warna        : {mobil_ditemukan['Warna']}")
                print(f"Tarif Harian : Rp {mobil_ditemukan['Tarif Harian']}")
                print(f"Durasi Sewa  : {mobil_ditemukan['Durasi']} hari")
                print(f"Waktu Peminjaman : {mobil_ditemukan['Waktu Peminjaman'].strftime('%Y-%m-%d %H:%M:%S')}") 
                print(f"Waktu Pengembalian: {mobil_ditemukan['Waktu Pengembalian'].strftime('%Y-%m-%d %H:%M:%S')}")
                print(Fore.GREEN + '''
--------------------------------------------''' + Fore.WHITE + '''
Terima kasih telah menggunakan layanan kami.
                   😊😊😊''' + Fore.GREEN + '''
--------------------------------------------''')

                input(Fore.CYAN + "Tekan Enter untuk kembali ke menu pelanggan...")
                return func_menu_pelanggan()
            else:
                print(Fore.RED + '\n⚠️  Pengembalian dibatalkan.')
                input(Fore.CYAN + '\nTekan enter untuk kembali ke menu pelanggan...')
                return func_menu_pelanggan()
    
        # Jika plat mobil tidak ditemukan
        else:
            print(Fore.RED + '⚠️  Plat mobil tidak ditemukan dalam daftar mobil yang Anda sewa.')
            continue

# Fungsi Menghubungi CS
def func_hubungi_cs():
    print(Fore.CYAN + '''
=====================================''' + Fore.WHITE + '''
   >>> HUBUNGI CUSTOMER SERVICE <<<''' + Fore.CYAN + '''
=====================================''')
    nama = input('👤  Masukkan nama Anda: ').capitalize()
    pesan = input('📨  Silakan tulis pesan atau pertanyaan Anda: ')
    print(Fore.WHITE + '''
-------------------------------------''' + Fore.GREEN + '''
>>>> Pesan Anda telah terkirim! <<<<''' + Fore.WHITE + '''
-------------------------------------''')
    print(f"Terima kasih {nama} 😊 kami akan segera menghubungi Anda kembali melalui kontak yang terdaftar 🙏")
    input(Fore.CYAN + "Tekan Enter untuk kembali ke menu layanan bantuan...")
    func_menu_pelanggan()

# ====================================================================================================================================== #
#                                                           MENU UTAMA PELANGGAN
# ====================================================================================================================================== #
def func_menu_pelanggan():
    pilihan = (input(Fore.CYAN + '''
=====================================''' + Fore.WHITE +'''
>>>>>>>>>> MENU PELANGGAN <<<<<<<<<<<''' + Fore.CYAN + '''
=====================================''' + Fore.YELLOW + '''
                                   
        1. Yuk Sewa Mobil
       2. Balikin Mobil Yuk
    3. Layanan Bantuan Pelanggan''' + Fore.WHITE + '''

       0. Balik ke Menu Utama''' + Fore.CYAN + '''
                  
=====================================''' + Fore.YELLOW + '\nSilahkan pilih: ' + Style.RESET_ALL))
    
    if pilihan == '1':
        func_yuk_sewa()
    elif pilihan == '2':
        func_balikin_mobil()
    elif pilihan == '3':
        func_hubungi_cs()
    elif pilihan == '0':
        func_menu_awal()
    else:
        print(Fore.RED + '⚠️  Pilihan nggak ada nih. Cek lagi yuk!')                                                                                     
        func_menu_pelanggan()

# ====================================================================================================================================== #
#                                                          FUNGSI ADMIN - CRUD
# ====================================================================================================================================== #
# Fungsi untuk menampikan menu admin
def func_menu_admin():
    while True:
        print(Fore.CYAN + '''
=========================================''' + Fore.WHITE + '''
  >>>>>>>>>>>>> MENU ADMIN <<<<<<<<<<<<<''' + Fore.CYAN + '''
=========================================''' + Fore.YELLOW + '''
    1. Tambah Mobil Baru (Create)
    2. Lihat Daftar Mobil (Read)
    3. Update Informasi Mobil (Update)
    4. Hapus Data Mobil (Delete)''' + Fore.WHITE +'''
    5. Keluar''' + Fore.CYAN + '''
=========================================''')                    
        pilihan = input(Fore.WHITE + 'Masukkan pilihan: ')

        if pilihan == '1':
            create_mobil()
        elif pilihan == '2':
            read_mobil()
        elif pilihan == '3':
            update_mobil()
        elif pilihan == '4':
            delete_mobil()
        elif pilihan == '5':
            print('🏃‍♂️ Keluar dari sistem admin.')
            break
        else:
            print(Fore.RED + '⚠️  Pilihan tidak valid, coba lagi.')

# Fitur 1: Create - Tambah Mobil Baru
def create_mobil():
    print(Fore.YELLOW + '\n== Tambah Mobil Baru ==')

    # Pengecekan validitas input plat mobil (tidak boleh kosong dan harus unik)
    while True:
        plat = input('Masukkan Plat Mobil (unik): ').upper().strip()
        if not plat:
            print(Fore.RED + "⚠️  Plat mobil tidak boleh kosong.")
            continue
        elif any(mobil['Plat'] == plat for mobil in Aset_Mobil):
            print(Fore.RED + f"⚠️  Plat mobil {plat} sudah ada dalam database, gunakan plat lain.")
            continue
        break

    # Input Model Mobil (tidak boleh kosong)
    while True:
        model = input('Masukkan Model Mobil: ').capitalize().strip()
        if not model:
            print(Fore.RED + "⚠️  Model mobil tidak boleh kosong.")
            continue
        break

    # Input Tarif Harian dengan validasi angka (integer)
    while True:
        tarif_harian = input('Masukkan Tarif Harian Mobil (dalam angka): ').strip()
        if not tarif_harian.isdigit():  # Cek apakah input adalah angka positif
            print(Fore.RED + "⚠️  Tarif harian harus berupa angka positif.")
            continue
        tarif_harian = int(tarif_harian)
        break

    # Input Warna Mobil (tidak boleh kosong)
    while True:
        warna = input('Masukkan Warna Mobil: ').capitalize().strip()
        if not warna:
            print(Fore.RED + "⚠️  Warna mobil tidak boleh kosong.")
            continue
        break

    # Input Rating dengan validasi angka (float antara 0.0 - 5.0)
    while True:
        rating = input('Masukkan Rating Mobil (antara 0.0 dan 5.0): ').strip()
        try:
            rating = float(rating)
            if rating < 0.0 or rating > 5.0:
                print(Fore.RED + "⚠️  Rating harus antara 0.0 dan 5.0.")
                continue
        except ValueError:
            print(Fore.RED + "⚠️  Rating harus berupa angka desimal antara 0.0 dan 5.0.")
            continue
        break

    # Input Fitur Unggulan Mobil (opsional, bisa lebih dari satu)
    fitur_unggulan = []
    while True:
        fitur = input("Masukkan Fitur Unggulan (ketik 'selesai' jika tidak ada lagi): ").strip()
        if fitur.lower() == 'selesai':
            break
        elif not fitur:
            print(Fore.RED + "⚠️  Fitur tidak boleh kosong. Masukkan fitur atau ketik 'selesai'.")
        else:
            fitur_unggulan.append(fitur)

    # Menambahkan data mobil ke dalam Aset_Mobil
    Aset_Mobil.append({
        'Plat': plat,
        'Model': model,
        'Tarif Harian': tarif_harian,
        'Warna' : warna, 
        'Rating': rating,
        'Ketersediaan': True, # Secara default mobil baru tersedia untuk disewa
        'fitur_unggulan': fitur_unggulan
    })

    print(Fore.GREEN + f'✔️  Mobil {model} dengan plat {plat} berhasil ditambahkan.\n')

# Fitur 2: Read - Tampilan Seluruhan Data Mobil
def read_mobil():
    print(Fore.YELLOW + '\n=== Daftar Seluruh Mobil ===')
    
    if not Aset_Mobil:
        # Jika tidak ada mobil dalam data
        print(Fore.RED + '⚠️  Tidak ada data mobil yang tersedia.')
    else:
        while True:
            # Opsi untuk memilih apakah akan menampilkan semua mobil atau hanya yang tersedia
            pilihan = input(Fore.YELLOW + "\nIngin melihat semua mobil atau hanya yang tersedia?" + Fore.WHITE + "(ketik 'semua' atau 'tersedia'): ").lower().strip()
            if pilihan not in ['semua', 'tersedia']:
                # Jika input tidak valid, berikan kesempatan untuk mengulang
                print(Fore.RED + "⚠️  Input tidak valid. Silakan ketik 'semua' atau 'tersedia'.")
                continue  # Kembali ke input

            # Filter mobil berdasarkan pilihan pengguna
            if pilihan == 'tersedia':
                mobil_list = [mobil for mobil in Aset_Mobil if mobil['Ketersediaan']]  # Filter yang tersedia
            else:
                mobil_list = Aset_Mobil  # Semua mobil

            if not mobil_list:
                # Jika tidak ada mobil yang cocok dengan filter
                print(Fore.RED + f"⚠️  Tidak ada mobil yang {pilihan}.")
                break  # Keluar dari loop jika tidak ada mobil yang sesuai

            headers = ["Plat", "Model", "Tarif Harian", "Warna", "Rating", "Ketersediaan", "Fitur Unggulan"]
            table_data = []

            # Looping melalui mobil untuk menyiapkan data
            for mobil in mobil_list:
                fitur_unggulan = fill(', '.join(mobil['fitur_unggulan']), width=40)  # Bungkus teks menjadi 40 karakter per baris
                ketersediaan_str = 'Tersedia' if mobil['Ketersediaan'] else 'Tidak Tersedia'
                
                # Masukkan data ke dalam tabel
                table_data.append([mobil['Plat'], mobil['Model'], f"Rp {mobil['Tarif Harian']}", mobil['Warna'], mobil['Rating'], ketersediaan_str, fitur_unggulan])

            # Tampilkan tabel dengan tabulate
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

            break  # Keluar setelah menampilkan data

    # Kembali ke menu admin setelah selesai
    input(Fore.CYAN + "\nTekan Enter untuk kembali ke menu admin...")

# Fitur 3: Update - Perbarui Data Mobil
def update_mobil():
    print(Fore.YELLOW + "     \n=== Update Informasi Mobil ===")
    plat = input("Masukkan Plat Mobil yang ingin diupdate: ").upper()
    
    # Cari mobil berdasarkan plat
    mobil_ditemukan = next((mobil for mobil in Aset_Mobil if mobil['Plat'] == plat), None)
    
    if mobil_ditemukan:
        # Tampilkan data mobil sebelum update
        print(Fore.GREEN + "\nData mobil ditemukan:\n")
        print(f"Plat Mobil     : {mobil_ditemukan['Plat']}")
        print(f"Model Mobil    : {mobil_ditemukan['Model']}")
        print(f"Tarif Harian   : Rp {mobil_ditemukan['Tarif Harian']}")
        print(f"Warna Mobil    : {mobil_ditemukan['Warna']}")
        print(f"Rating Mobil   : {mobil_ditemukan['Rating']}")
        print(f"Ketersediaan   : {'Tersedia' if mobil_ditemukan['Ketersediaan'] else 'Tidak Tersedia'}")
        print(Fore.YELLOW + "Fitur Unggulan :")

        # Cek apakah fitur unggulan ada dan bukan none atau kosong
        if mobil_ditemukan['fitur_unggulan']:
            for fitur in mobil_ditemukan['fitur_unggulan']:
                print(Fore.CYAN + f"  - {fitur}")
        else:
            print(Fore.RED + "  - Tidak ada fitur unggulan yang diinput.")

        # Update informasi mobil dengan validasi
        # 1. Update Model
        model_baru = input(f"\nMasukkan model baru [{mobil_ditemukan['Model']}]: ").capitalize()
        if model_baru:
            mobil_ditemukan['Model'] = model_baru

        # 2. Update Tarif Harian dengan validasi integer
        while True:
            tarif_baru = input(f"Masukkan tarif harian baru [{mobil_ditemukan['Tarif Harian']}] (biarkan kosong jika tidak ingin mengubah): ")
            if tarif_baru:
                try:
                    tarif_baru = int(tarif_baru)
                    mobil_ditemukan['Tarif Harian'] = tarif_baru
                except ValueError:
                    print(Fore.RED + "⚠️  Tarif harian harus berupa angka. Silakan coba lagi.")
                    continue
            break

        # 3. Update Warna
        warna_baru = input(f"Masukkan warna baru [{mobil_ditemukan['Warna']}]: ").capitalize()
        if warna_baru:
            mobil_ditemukan['Warna'] = warna_baru

        # 4. Update Rating dengan validasi float
        while True:
            try:
                rating_baru = input(f"Masukkan rating baru [{mobil_ditemukan['Rating']}]: ")
                if rating_baru:  # Jika ada input baru, update
                    rating_baru = float(rating_baru)
                    if 0 <= rating_baru <= 5:  # Rating harus di antara 0 dan 5
                        mobil_ditemukan['Rating'] = rating_baru
                    else:
                        print(Fore.RED + "⚠️  Rating harus di antara 0 dan 5.")
                        continue
                break  # Keluar dari loop jika berhasil
            except ValueError:
                print(Fore.RED + "⚠️  Rating harus berupa angka desimal antara 0 dan 5. Silakan coba lagi.")

        # 5. Update Fitur Unggulan
        fitur_unggulan_baru = input(f"Masukkan fitur unggulan baru (pisahkan dengan koma) atau kosongkan untuk tidak mengubah: ")
        if fitur_unggulan_baru:
            mobil_ditemukan['fitur_unggulan'] = [fitur.strip() for fitur in fitur_unggulan_baru.split(',')]

        # Tampilkan hasil setelah update
        print(Fore.GREEN + "\n✔️  Data mobil setelah diupdate:\n")
        print(f"Plat Mobil     : {mobil_ditemukan['Plat']}")
        print(f"Model Mobil    : {mobil_ditemukan['Model']}")
        print(f"Tarif Harian   : Rp {mobil_ditemukan['Tarif Harian']}")
        print(f"Warna Mobil    : {mobil_ditemukan['Warna']}")
        print(f"Rating Mobil   : {mobil_ditemukan['Rating']}")
        print(f"Ketersediaan   : {'Tersedia' if mobil_ditemukan['Ketersediaan'] else 'Tidak Tersedia'}")
        print(Fore.YELLOW + "Fitur Unggulan :")
        for fitur in mobil_ditemukan['fitur_unggulan']:
            print(Fore.CYAN + f"  - {fitur}")

    else:
        print(Fore.RED + f"⚠️  Mobil dengan plat {plat} tidak ditemukan.\n")

# Fitur 4: Delete - Hapus Data Mobil
def delete_mobil():
    print(Fore.YELLOW + "\n=== Hapus Data Mobil ===")
    
    while True:
        # Meminta pengguna memasukkan plat mobil
        plat = input("Masukkan Plat Mobil yang ingin dihapus: ").upper().strip()
        
        # Validasi input agar tidak kosong
        if not plat:
            print(Fore.RED + "⚠️  Plat mobil tidak boleh kosong. Silakan coba lagi.")
            continue
        
        # Cari mobil berdasarkan plat
        mobil_ditemukan = next((mobil for mobil in Aset_Mobil if mobil['Plat'] == plat), None)
        
        if mobil_ditemukan:
            # Menampilkan informasi mobil yang akan dihapus
            print(Fore.GREEN + f"\n✔️  Mobil ditemukan: {mobil_ditemukan['Model']} (Plat: {mobil_ditemukan['Plat']}, Warna: {mobil_ditemukan['Warna']})")
            
            # Meminta konfirmasi dari pengguna sebelum menghapus
            konfirmasi = input(Fore.YELLOW + "❔  Anda yakin ingin menghapus mobil ini?" + Fore.WHITE + "(ya/tidak): ").lower().strip()
            
            if konfirmasi == 'ya':
                Aset_Mobil.remove(mobil_ditemukan)
                print(Fore.GREEN + f"\n🗑️  Data mobil dengan plat {plat} berhasil dihapus.\n")
                return  # Keluar dari fungsi setelah penghapusan berhasil
            else:
                print(Fore.RED + "❌ Penghapusan dibatalkan.")
                return  # Keluar dari fungsi jika penghapusan dibatalkan
            
        else:
            # Jika plat mobil tidak ditemukan dalam daftar
            print(Fore.RED + f"🔍  Mobil dengan plat {plat} tidak ditemukan.\n")
            coba_lagi = input(Fore.YELLOW + "❔  Apakah Anda ingin mencoba lagi?" + "(ya/tidak): ").lower().strip()
            
            if coba_lagi != 'ya':
                print(Fore.CYAN + "Kembali ke menu admin.")
                return  # Keluar dari fungsi jika pengguna memilih untuk tidak mencoba lagi

# ===================================================================================================================================== #
#                                                         MENU START PROGRAM
# ===================================================================================================================================== #
def func_menu_awal():
    while True:
        pilihan_diri = input(Fore.YELLOW + '''    
      === SELAMAT DATANG ===''' + Fore.CYAN + '''
>>> Sewa Mobilmu Sekarang Juga <<<'''+ Fore.MAGENTA + '''
----------------------------------''' +                             
        Fore.YELLOW + ''' 
>>> KAMU MAU LOGIN SEBAGAI APA <<<''' + Fore.WHITE + '''

        1. Pelanggan 🚗  
          2. Admin 🛠️''' + Fore.MAGENTA + '''

----------------------------------''' + Fore.WHITE +'''
pilih menu: ''' + Style.RESET_ALL)
    
        if pilihan_diri == '1':
            while True:
            # Pilihan untk pelanggan: Sign Up atau Login
                print('''                                            
1. 📝 SIGN UP
2. 🔑 LOGIN ''') 
                pilihan = input(Fore.MAGENTA + '''pilih menu: ''' + Style.RESET_ALL)
                    
                if pilihan == '1':
                    func_sign_up()
                    break
                elif pilihan == '2':
                    func_login_pelanggan()
                    break
                else:
                    print(Fore.RED + '⚠️  Pilihan nggak ada nih. Cek lagi yuk!')
                    
        elif pilihan_diri == '2':
            func_login_admin()

        else:
            print(Fore.RED + '⚠️  Pilihan nggak ada nih. Cek lagi yuk!')                               
func_menu_awal()














