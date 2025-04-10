class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.jurusan}\nAlamat: {self.alamat}\n"

def buat_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    jurusan = input("Masukkan jurusan/prodi mahasiswa: ")
    alamat = input("Masukkan alamat mahasiswa: ")
    return Mahasiswa(nama, nim, jurusan, alamat)


mahasiswa_list = []


for i in range(3):
    print(f"\nData Mahasiswa ke-{i + 1}:")
    mahasiswa = buat_mahasiswa()
    mahasiswa_list.append(mahasiswa)


print("\nInformasi Mahasiswa:")
for mhs in mahasiswa_list:
    print(mhs.tampilkan_info())