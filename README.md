# labpy08
## Program Manajemen Data Mahasiswa (OOP)
Ini adalah program Python yang menggunakan konsep Object-Oriented Programming (OOP) untuk mengelola data mahasiswa. Program ini memungkinkan pengguna untuk menambah, menghapus, mengubah, mencari, dan menampilkan data mahasiswa. Data mahasiswa disimpan dalam struktur berbasis kelas dan dipisahkan menjadi beberapa modul dengan menggunakan konsep package dan module.
```ruby
Program1/
├── data/
│   ├── __init__.py
│   └── mahasiswa.py
├── view/
│   ├── __init__.py
│   ├── input_form.py
│   └── mahasiswa.py
├── main.py
```

Penjelasan File
1. data/mahasiswa.py
File ini berisi kelas untuk menyimpan dan memanipulasi data mahasiswa. Ada dua kelas di dalamnya:

Mahasiswa: Kelas ini menyimpan informasi mahasiswa seperti NIM, nama, dan program studi.
DataMahasiswa: Kelas ini berfungsi untuk mengelola data mahasiswa secara kolektif. Kelas ini menyediakan metode untuk menambah, menghapus, mengubah, mencari, dan menampilkan data mahasiswa.
2. view/input_form.py
File ini berisi kelas InputForm yang digunakan untuk mengambil input dari pengguna saat menambahkan data mahasiswa. Metode yang ada di dalamnya adalah input_mahasiswa(), yang meminta pengguna untuk memasukkan NIM, nama, dan program studi mahasiswa.

3. view/mahasiswa.py
File ini berisi kelas ViewMahasiswa yang bertanggung jawab untuk menampilkan data mahasiswa. Ada dua metode utama:

tampilkan_mahasiswa(): Menampilkan daftar semua mahasiswa.
tampilkan_detail(): Menampilkan detail informasi seorang mahasiswa berdasarkan NIM.
4. main.py
File utama yang menjalankan program. Di sini, menu utama ditampilkan kepada pengguna, dan pengguna dapat memilih berbagai opsi untuk mengelola data mahasiswa. Program ini berinteraksi dengan kelas-kelas yang ada di modul data dan view untuk memproses data mahasiswa sesuai dengan pilihan pengguna.

Fitur Program
Tambah Mahasiswa: Pengguna dapat menambahkan data mahasiswa baru (NIM, nama, program studi).
Hapus Mahasiswa: Pengguna dapat menghapus data mahasiswa berdasarkan NIM.
Ubah Mahasiswa: Pengguna dapat mengubah nama dan program studi mahasiswa berdasarkan NIM.
Cari Mahasiswa: Pengguna dapat mencari mahasiswa berdasarkan NIM dan melihat detailnya.
Tampilkan Semua Mahasiswa: Pengguna dapat menampilkan daftar seluruh mahasiswa yang terdaftar.
Cara Menggunakan
Menjalankan Program:

Pastikan Anda telah menginstal Python di komputer Anda.
Buka terminal/command prompt, lalu navigasikan ke folder proyek ini.
Jalankan perintah berikut untuk memulai program:
```ruby
python main.py
```
Menu Program: Setelah menjalankan program, Anda akan diberikan pilihan menu untuk memilih aksi yang ingin dilakukan. Pilih angka yang sesuai dengan opsi yang diinginkan.

Contoh Input:

Untuk menambah mahasiswa, program akan meminta Anda untuk memasukkan NIM, nama, dan program studi.
Untuk mencari mahasiswa, masukkan NIM mahasiswa yang ingin dicari.
Keluar dari Program: Pilih opsi "6" untuk keluar dari program.

