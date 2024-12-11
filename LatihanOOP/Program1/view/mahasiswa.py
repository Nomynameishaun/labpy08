class ViewMahasiswa:
    @staticmethod
    def tampilkan_mahasiswa(data_mahasiswa):
        if not data_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            for m in data_mahasiswa:
                print(f"NIM: {m.nim}, Nama: {m.nama}, Prodi: {m.prodi}")

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print(f"Detail Mahasiswa:\nNIM: {mahasiswa.nim}\nNama: {mahasiswa.nama}\nProdi: {mahasiswa.prodi}")
        else:
            print("Mahasiswa tidak ditemukan.")
