# Sistem Manajemen Rental Mobil

## Deskripsi Program

Program **Sistem Manajemen Rental Mobil** adalah aplikasi berbasis Python yang memungkinkan pengguna untuk menyewa mobil, mengembalikan mobil yang disewa, dan bagi admin untuk mengelola inventaris mobil menggunakan operasi CRUD (Create, Read, Update, Delete). Sistem ini menyediakan antarmuka menu interaktif untuk pelanggan dan administrator.

## Deskripsi Data

Berikut adalah deskripsi data mobil (`Aset_Mobil`):

| No | Nama Kolom        | Tipe Data     | Deskripsi                                          |
|----|-------------------|---------------|----------------------------------------------------|
| 1  | `Plat`            | `str`         | Nomor plat mobil yang unik                         |
| 2  | `Model`           | `str`         | Model mobil                                        |
| 3  | `Tarif Harian`    | `int`         | Tarif sewa mobil per hari (dalam Rupiah)           |
| 4  | `Warna`           | `str`         | Warna mobil                                        |
| 5  | `Rating`          | `float`       | Rating mobil (skala 0.0 - 5.0)                     |
| 6  | `Ketersediaan`    | `bool`        | Status ketersediaan mobil (`True`/`False`)         |
| 7  | `fitur_unggulan`  | `list[str]`   | Daftar fitur unggulan dari mobil                   |

## Menu Utama

Program ini memiliki dua jenis pengguna dengan menu utama yang berbeda:

1. **Pelanggan**
2. **Admin**

### 1. Menu Pelanggan

Setelah login atau registrasi, pelanggan dapat mengakses menu berikut:

#### Sub Menu 1: Yuk Sewa Mobil

- **Sewa Mobil**
  - Pelanggan dapat melihat daftar mobil yang tersedia dan memilih mobil yang ingin disewa dengan memasukkan nomor plat.
  - Setelah memilih mobil, pelanggan memasukkan jumlah hari sewa.
  - Sistem akan menghitung total biaya sewa.
  - Pelanggan dapat mengonfirmasi penyewaan atau membatalkannya.
  - Jika dikonfirmasi, sistem akan memberikan struk penyewaan.

- **Cek Fitur dan Rating Mobil**
  - Pelanggan dapat melihat fitur unggulan dan rating dari setiap mobil yang tersedia.

#### Sub Menu 2: Balikin Mobil Yuk

- Pelanggan dapat mengembalikan mobil yang telah disewa.
- Sistem akan menampilkan daftar mobil yang sedang disewa oleh pelanggan.
- Pelanggan memilih mobil yang akan dikembalikan dengan memasukkan nomor plat.
- Setelah konfirmasi, sistem akan memperbarui status ketersediaan mobil dan memberikan struk pengembalian.

#### Sub Menu 3: Layanan Bantuan Pelanggan

- Pelanggan dapat menghubungi customer service dengan memasukkan nama dan pesan.
- Sistem akan mengonfirmasi bahwa pesan telah terkirim dan akan ditindaklanjuti oleh tim customer service.

### 2. Menu Admin

Admin dapat mengakses menu untuk mengelola data mobil:

#### Sub Menu 1: Tambah Mobil Baru (Create)

- Admin dapat menambahkan mobil baru ke dalam sistem.
- Data yang harus diinput antara lain:
  - `Plat`: harus unik dan tidak boleh kosong.
  - `Model`: tidak boleh kosong.
  - `Tarif Harian`: harus berupa angka positif dan tidak boleh kosong
  - `Warna`: tidak boleh kosong.
  - `Rating`: angka desimal antara 0.0 dan 5.0. dan tidak boleh kosong
  - `Fitur Unggulan`: daftar fitur yang harus diisi minimal satu fitur

#### Sub Menu 2: Lihat Daftar Mobil (Read)

- Admin dapat melihat daftar seluruh mobil.
- Opsi untuk menampilkan:
  - **Semua Mobil**: menampilkan semua mobil yang ada di sistem.
  - **Mobil Tersedia**: hanya menampilkan mobil yang tersedia untuk disewa.

#### Sub Menu 3: Update Informasi Mobil (Update)

- Admin dapat memperbarui informasi mobil yang ada.
- Admin memasukkan nomor plat mobil yang ingin diupdate.
- Data yang dapat diupdate:
  - `Model`
  - `Tarif Harian`
  - `Warna`
  - `Rating`
  - `Fitur Unggulan`

#### Sub Menu 4: Hapus Data Mobil (Delete)

- Admin dapat menghapus mobil dari sistem.
- Admin memasukkan nomor plat mobil yang ingin dihapus.
- Setelah konfirmasi, sistem akan menghapus mobil dari daftar.

#### Sub Menu 5: Keluar

- Admin keluar dari menu admin dan kembali ke menu utama.

## Autentikasi

Program ini memiliki fitur login dan registrasi:

- **Pelanggan**:
  - **Registrasi**: Pelanggan baru dapat mendaftar dengan username dan password.
  - **Login**: Pelanggan yang sudah terdaftar dapat login menggunakan username dan password.

- **Admin**:
  - **Login Admin**: Admin dapat login menggunakan password khusus (`admin123`).

## Alur Program

1. **Menu Awal**:
   - Pengguna memilih untuk login sebagai pelanggan atau admin.

2. **Login/Registrasi**:
   - **Pelanggan**: Dapat memilih untuk registrasi atau login.
   - **Admin**: Langsung memasukkan password admin.

3. **Akses Menu Sesuai Peran**:
   - **Pelanggan**: Mengakses menu pelanggan.
   - **Admin**: Mengakses menu admin.

4. **Melakukan Operasi Sesuai Menu**:
   - Menggunakan fitur-fitur yang tersedia sesuai dengan hak akses.

5. **Logout/Keluar**:
   - Pengguna dapat keluar dari sesi dan kembali ke menu awal.

## Catatan

- Program menggunakan modul berikut:
  - `datetime` untuk pengelolaan waktu penyewaan.
  - `tabulate` untuk menampilkan data dalam bentuk tabel.
  - `colorama` untuk memberikan warna pada teks di terminal.

- Semua input yang dimasukkan oleh pengguna divalidasi untuk memastikan data yang masuk sesuai dengan yang diharapkan.

- Program ini berjalan di terminal/command prompt dan interaktif melalui input pengguna.

## Cara Menjalankan Program

1. Pastikan Python 3.x telah terinstal di komputer Anda.
2. Install modul yang diperlukan
