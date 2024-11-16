# Inisialisasi list untuk menyimpan data
data_mahasiswa = []

while True:
    # Memasukkan data mahasiswa
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai Tugas (0-100): "))
    uts = float(input("Masukkan nilai UTS (0-100): "))
    uas = float(input("Masukkan nilai UAS (0-100): "))
    
    # Perhitungan nilai akhir
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
    
    # Menyimpan data dalam bentuk dictionary ke dalam list
    data_mahasiswa.append({
        "Nama": nama,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })
    
    # Menanyakan apakah ingin menambah data lagi
    lanjut = input("Tambah data lagi? (y/t): ").lower()
    if lanjut == 't':
        break

# Menampilkan semua data mahasiswa
print("\nDaftar Data Mahasiswa")
print("=" * 50)
print(f"{'Nama':<15} {'Tugas':<10} {'UTS':<10} {'UAS':<10} {'Nilai Akhir':<10}")
print("=" * 50)
for mahasiswa in data_mahasiswa:
    print(f"{mahasiswa['Nama']:<15} {mahasiswa['Tugas']:<10} {mahasiswa['UTS']:<10} {mahasiswa['UAS']:<10} {mahasiswa['Nilai Akhir']:<10.2f}")
print("=" * 50)
