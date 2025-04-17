
class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.cek_sks_valid(sks):
            raise ValueError(f"SKS tidak valid untuk mata kuliah {nama}")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def cek_sks_valid(sks):
        return sks in [2, 3]  

    def __str__(self):
        return f"{self.kode} - {self.nama} ({self.sks} SKS)"


class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.cek_nim_valid(nim):
            raise ValueError(f"NIM tidak valid: {nim}")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.mata_kuliah = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_mata_kuliah(self, mk):
        self.mata_kuliah.append(mk)

    def tampilkan_info(self):
        print(f"\nNama   : {self.nama}")
        print(f"NIM    : {self.nim}")
        print(f"Prodi  : {self.prodi}")
        print("Mata Kuliah:")
        for mk in self.mata_kuliah:
            print(f" - {mk}")

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def cek_nim_valid(nim):
        return isinstance(nim, str) and nim.startswith("23") and len(nim) == 10



class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.cek_nama_kampus_valid(nama):
            raise ValueError("Nama kampus tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat
        Kampus.jumlah_mahasiswa = Mahasiswa.jumlah_mahasiswa

    @classmethod
    def tampilkan_info_kampus(cls, nama_kampus):
        print(f"\nNama Kampus     : {nama_kampus}")
        print(f"Total Mahasiswa : {cls.jumlah_mahasiswa}")

    @staticmethod
    def cek_nama_kampus_valid(nama):
        return not any(char.isdigit() for char in nama)



while True:
    try:
        nama_kampus = input("Masukkan nama kampus: ")
        alamat_kampus = input("Masukkan alamat kampus: ")
        kampus = Kampus(nama_kampus, alamat_kampus)
        break
    except ValueError as e:
        print(e)


print("\nMasukkan 8 mata kuliah:")
daftar_matkul = []
for i in range(8):
    while True:
        try:
            print(f"\nMata kuliah ke-{i+1}")
            kode = input("  Kode       : ")
            nama = input("  Nama       : ")
            sks = int(input("  Jumlah SKS : "))
            mk = MataKuliah(kode, nama, sks)
            daftar_matkul.append(mk)
            break
        except ValueError as e:
            print(f"  Error: {e}")


print("\nMasukkan data 6 mahasiswa:")
daftar_mahasiswa = []
for i in range(6):
    while True:
        try:
            print(f"\nMahasiswa ke-{i+1}")
            nama = input("  Nama  : ")
            nim = input("  NIM   : ")
            prodi = input("  Prodi : ")
            mhs = Mahasiswa(nama, nim, prodi)

            print("  Pilih minimal 4 mata kuliah (masukkan index dipisah koma, contoh: 0,1,2,3)")
            for idx, mk in enumerate(daftar_matkul):
                print(f"    [{idx}] {mk}")
            index_matkul = input("  Pilih matkul: ").split(',')

            if len(index_matkul) < 4:
                raise Exception("  Minimal harus memilih 4 mata kuliah.")

            for idx in index_matkul:
                mhs.tambah_mata_kuliah(daftar_matkul[int(idx.strip())])

            daftar_mahasiswa.append(mhs)
            break
        except Exception as e:
            print(f"  Error: {e}")


print("\n===== INFO MAHASISWA =====")
for m in daftar_mahasiswa:
    m.tampilkan_info()

print("\n===== INFO KAMPUS =====")
Kampus.tampilkan_info_kampus(kampus.nama)
print("Nama kampus valid?", "Ya" if Kampus.cek_nama_kampus_valid(kampus.nama) else "Tidak")



