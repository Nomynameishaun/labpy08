class Mahasiswa:
    def __init__(self, nim, nama, prodi):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi

class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_data(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_data(self, nim, nama_baru, prodi_baru):
        for m in self.data:
            if m.nim == nim:
                m.nama = nama_baru
                m.prodi = prodi_baru

    def cari_data(self, nim):
        for m in self.data:
            if m.nim == nim:
                return m
        return None

    def tampilkan_data(self):
        return self.data
