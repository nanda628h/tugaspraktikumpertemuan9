# tugas untuk menentukan nilai akhir

## Tugas
Buat program sederhana untuk menambahkan data kedalam sebuah
list dengan rincian sebagai berikut: Progam meminta memasukkan data sebanyak-banyaknya (gunakan
perulangan) Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban t (Tidak), maka program akan menampilkan daftar datanya.
Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)

# codingan tugas
``` python
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
```
## output tugas jika 1
``` python
Masukkan nama mahasiswa: ananda
Masukkan nilai Tugas (0-100): 30
Masukkan nilai UTS (0-100): 100
Masukkan nilai UAS (0-100): 37
Tambah data lagi? (y/t): t

Daftar Data Mahasiswa
==================================================
Nama            Tugas      UTS        UAS        Nilai Akhir
==================================================
ananda          30.0       100.0      37.0       56.95
==================================================
```
## output tugas jika 2 
```python
Masukkan nama mahasiswa: ananda
Masukkan nilai Tugas (0-100): 100
Masukkan nilai UTS (0-100): 23
Masukkan nilai UAS (0-100): 80
Tambah data lagi? (y/t): y
Masukkan nama mahasiswa: eka
Masukkan nilai Tugas (0-100): 90 
Masukkan nilai UTS (0-100): 90
Masukkan nilai UAS (0-100): 40
Tambah data lagi? (y/t): t

Daftar Data Mahasiswa
==================================================
Nama            Tugas      UTS        UAS        Nilai Akhir
==================================================
ananda          100.0      23.0       80.0       66.05
eka             90.0       90.0       40.0       72.50
==================================================
```
## penjelasan dari kode
Inisialisasi List:

data_mahasiswa adalah list kosong yang digunakan untuk menyimpan data mahasiswa dalam bentuk dictionary.
Input Data Mahasiswa:

Program meminta pengguna untuk memasukkan nama, nilai tugas, nilai UTS, dan nilai UAS.
Nilai-nilai tersebut kemudian dihitung untuk mendapatkan nilai akhir berdasarkan bobot yang diberikan:
Tugas: 30%
UTS: 35%
UAS: 35%
Menyimpan Data:

Setiap data mahasiswa dimasukkan sebagai dictionary dengan kunci "Nama", "Tugas", "UTS", "UAS", dan "Nilai Akhir".
Dictionary ini ditambahkan ke dalam list data_mahasiswa.
Perulangan:

Program menggunakan perulangan while True untuk memungkinkan pengguna menambahkan data sebanyak-banyaknya.
Setelah memasukkan data, program menanyakan apakah pengguna ingin melanjutkan (y/t).
Jika pengguna menjawab t, perulangan akan berhenti dengan break.
Menampilkan Data:

Program menampilkan daftar data mahasiswa dalam format tabel menggunakan perulangan for.
print dengan format string digunakan untuk merapikan tampilan tabel.
