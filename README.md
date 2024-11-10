# Latihan1

## Deskripsi Program
Program sederhana untuk menghasilkan bilangan random (acak) dengan range 0 sampai 0.5 sebanyak N kali, dimana N adalah input dari user.

## Alur Algoritma
1. Program melakukan import library `random` untuk menggunakan fungsi bilangan acak

2. Program meminta user memasukkan nilai N sebagai jumlah bilangan yang akan digenerate
  - Input berupa bilangan bulat positif
  - Disimpan dalam variabel `n`

3. Program melakukan perulangan/loop sebanyak N kali:
  - Menggunakan fungsi `range(1, n+1)` agar loop mulai dari 1 sampai N
  - Di setiap loop:
    - Generate bilangan random antara 0-0.5 menggunakan `random.uniform()`
    - Tampilkan nomor data dan bilangan random yang dihasilkan

## Fungsi yang Digunakan
- `random.uniform(a,b)`: Menghasilkan bilangan random float antara a dan b
- `range(start,end)`: Membuat sequence bilangan dari start sampai end-1  
- `input()`: Menerima input dari user
- `int()`: Mengkonversi string menjadi integer
- `print()`: Menampilkan output ke layar

## Contoh Output
![Output latihan1](output/output_latihan1.png)


# Latihan2 

## Deskripsi Program
Program untuk menghitung laba bulanan berdasarkan persentase yang telah ditentukan dari modal awal. Program akan menampilkan laba per bulan dan total laba keseluruhan.

## Alur Algoritma
1. Inisialisasi data awal:
  - Modal awal ditetapkan sebesar 100.000.000
  - Array/List `laba_per_bulan` berisi persentase laba tiap bulan [0, 0, 1, 1, 5, 5, 5, 3]
  - Variabel `total_laba` diinisialisasi dengan nilai 0

2. Melakukan perulangan/loop menggunakan for loop untuk setiap bulan:
  - Menggunakan `enumerate()` agar mendapatkan indeks(i) dan nilai(laba)
  - Parameter `start=1` membuat indeks dimulai dari 1
  - Di setiap perulangan/loop:
    - Hitung laba bulan = (persentase / 100) × modal
    - Tambahkan laba bulan ke total laba

3. Menampilkan hasil:
  - Untuk bulan 1-2: tampilkan dalam bilangan bulat
  - Untuk bulan 3-8: tampilkan dengan 1 angka desimal
  - Di akhir tampilkan total laba

## Fungsi yang Digunakan
- `enumerate()`: Menghasilkan pasangan indeks dan nilai dari sequence
- `print()`: Menampilkan output ke layar
- Format string (f-string): Memformat output dengan spesifikasi tertentu
- `int()`: Mengkonversi ke bilangan bulat
- `.1f`: Format untuk menampilkan 1 angka di belakang koma

## Contoh Output
![Output latihan2](output/output_latihan2.png)
