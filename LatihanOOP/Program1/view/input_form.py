class InputForm:
    @staticmethod
    def input_mahasiswa():
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        prodi = input("Masukkan Prodi: ")
        return nim, nama, prodi
