from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

def menu():
    print("\nMenu:")
    print("1. Tambah Mahasiswa")
    print("2. Hapus Mahasiswa")
    print("3. Ubah Mahasiswa")
    print("4. Cari Mahasiswa")
    print("5. Tampilkan Semua Mahasiswa")
    print("6. Keluar")

if __name__ == "__main__":
    data_mahasiswa = DataMahasiswa()

    while True:
        menu()
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            nim, nama, prodi = InputForm.input_mahasiswa()
            mhs = Mahasiswa(nim, nama, prodi)
            data_mahasiswa.tambah_data(mhs)
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
            data_mahasiswa.hapus_data(nim)
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
            nama_baru = input("Masukkan nama baru: ")
            prodi_baru = input("Masukkan prodi baru: ")
            data_mahasiswa.ubah_data(nim, nama_baru, prodi_baru)
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
            mahasiswa = data_mahasiswa.cari_data(nim)
            ViewMahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == "5":
            semua_mahasiswa = data_mahasiswa.tampilkan_data()
            ViewMahasiswa.tampilkan_mahasiswa(semua_mahasiswa)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
