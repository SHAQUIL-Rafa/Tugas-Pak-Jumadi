# Tema: Perhitungan Biaya Belanja

# Penjumlahan
print("Menghitung total belanja:")
apel_harga = 5000  # harga per apel
jeruk_harga = 7000  # harga per jeruk
apel_jumlah = 3
jeruk_jumlah = 4
total_belanja = (apel_harga * apel_jumlah) + (jeruk_harga * jeruk_jumlah)
print("Total belanja untuk apel dan jeruk adalah: ", total_belanja)

# Pengurangan
uang = 50000
belanja = total_belanja
sisa_uang = uang - belanja
print("Sisa uang Anda setelah belanja adalah: ", sisa_uang)

# Perkalian
harga_per_item = 15000
jumlah_item = 5
total_harga = harga_per_item * jumlah_item
print("Total harga untuk ", jumlah_item, " item adalah: ", total_harga)

# Pembagian
total_kue = 20
jumlah_anak = 5
kue_per_anak = total_kue / jumlah_anak
print("Setiap anak akan mendapatkan kue sebanyak: ", kue_per_anak)

# Sisa Bagi / Modulus
uang_terpakai = 37
uang_sisa = 10
sisa_bagi = uang_terpakai % uang_sisa
print("Sisa uang setelah dibagi: ", sisa_bagi)

# Pangkat
diskon = 0.1  # 10% diskon
harga_asli = 20000
harga_setelah_diskon = harga_asli * (1 - diskon)
print("Harga setelah diskon adalah: ", harga_setelah_diskon)

# Pembagian Bulat
print("Pembagian bulat dari 10 dibagi 3 adalah: ", 10 // 3)


# Tema: Perbandingan Suhu

# Sama dengan (==)
print('Operator sama dengan')
suhu_hari_ini = 30  # suhu dalam derajat Celsius
suhu_hari_kemarin = 30
print('Suhu hari ini == Suhu hari kemarin bernilai', suhu_hari_ini == suhu_hari_kemarin)
print('Suhu hari ini == 25 bernilai', suhu_hari_ini == 25)
print()

# Tidak sama dengan (!=)
print('Operator tidak sama dengan')
print('Suhu hari ini != Suhu hari kemarin bernilai', suhu_hari_ini != suhu_hari_kemarin)
print('Suhu hari ini != 35 bernilai', suhu_hari_ini != 35)
print()

# Lebih besar dari (>)
print('Operator lebih besar dari')
print('Suhu hari ini > 25 bernilai', suhu_hari_ini > 25)
print('Suhu hari ini > 35 bernilai', suhu_hari_ini > 35)
print()

# Lebih kecil dari (<)
print('Operator lebih kecil dari')
print('Suhu hari ini < 35 bernilai', suhu_hari_ini < 35)
print('Suhu hari ini < 20 bernilai', suhu_hari_ini < 20)
print()

# Lebih besar dari atau sama dengan (>=)
print('Operator lebih besar dari atau sama dengan')
print('Suhu hari ini >= 30 bernilai', suhu_hari_ini >= 30)
print('Suhu hari ini >= 35 bernilai', suhu_hari_ini >= 35)
print()

# Lebih kecil dari atau sama dengan (<=)
print('Operator lebih kecil dari atau sama dengan')
print('Suhu hari ini <= 30 bernilai', suhu_hari_ini <= 30)
print('Suhu hari ini <= 25 bernilai', suhu_hari_ini <= 25)
print()






# Tema: Pengelolaan Saldo Rekening

# Sama dengan (=)
print('Operator sama dengan')
saldo = 1000  # saldo awal
print('Saldo awal:', saldo)
setoran = 500
print('Setoran:', setoran)
saldo = setoran  # mengubah saldo menjadi setoran
print('Saldo setelah setoran:', saldo)

# Tambah sama dengan (+=)
print('Operator tambah sama dengan')
saldo = 1000
print('Saldo:', saldo)
saldo += 200  # menambah saldo
print('Saldo setelah penambahan:', saldo)
print()

# Kurang sama dengan (-=)
print('Operator kurang sama dengan')
saldo = 1200
print('Saldo:', saldo)
tarik_tunai = 300
saldo -= tarik_tunai  # mengurangi saldo
print('Saldo setelah tarik tunai:', saldo)
print()

# Kali sama dengan (*=)
print('Operator kali sama dengan')
saldo = 1000
print('Saldo:', saldo)
saldo *= 1.05  # menambahkan bunga 5%
print('Saldo setelah bunga:', saldo)
print()

# Bagi sama dengan (/=)
print('Operator bagi sama dengan')
saldo = 1000
print('Saldo:', saldo)
saldo /= 2  # membagi saldo
print('Saldo setelah dibagi dua:', saldo)
print()

# Sisa bagi sama dengan (%=)
print('Operator sisa bagi sama dengan')
saldo = 7
print('Saldo:', saldo)
saldo %= 3  # sisa bagi
print('Sisa saldo setelah dibagi 3:', saldo)
print()

# Pangkat sama dengan (**=)
print('Operator pangkat sama dengan')
saldo = 10
print('Saldo:', saldo)
saldo **= 2  # saldo dipangkatkan
print('Saldo setelah dipangkatkan:', saldo)
print()

# Pembagian bulat sama dengan (//=)
print('Operator pembagian bulat sama dengan')
saldo = 10
print('Saldo:', saldo)
saldo //= 3  # pembagian bulat
print('Saldo setelah pembagian bulat:', saldo)
print()




# Tema: Evaluasi Kelayakan Pendaftaran

# and
print('Evaluasi kelayakan pendaftaran:')
umur = 18
nilai = 75
print('Umur >= 18 dan Nilai >= 70 bernilai', umur >= 18 and nilai >= 70)
print('Umur >= 18 dan Nilai >= 80 bernilai', umur >= 18 and nilai >= 80)
print('Umur < 18 dan Nilai >= 70 bernilai', umur < 18 and nilai >= 70)
print('Umur < 18 dan Nilai < 70 bernilai', umur < 18 and nilai < 70)
print()

# or
print('Evaluasi alternatif kelayakan pendaftaran:')
print('Umur >= 18 atau Nilai >= 70 bernilai', umur >= 18 or nilai >= 70)
print('Umur >= 18 atau Nilai >= 80 bernilai', umur >= 18 or nilai >= 80)
print('Umur < 18 atau Nilai >= 70 bernilai', umur < 18 or nilai >= 70)
print('Umur < 18 atau Nilai < 70 bernilai', umur < 18 or nilai < 70)
print()

# not
print('Evaluasi negasi kelayakan pendaftaran:')
print('Bukan (Umur >= 18) bernilai', not (umur >= 18))
print('Bukan (Nilai >= 70) bernilai', not (nilai >= 70))



#Operator Bitwise

#&
a = 13 #dalam biner bernilai 0000 1101
b = 37 #dalam biner bernilai 0010 0101
c = a & b #akan bernilai     0000 0101
print(c)
print()

#|
a = 13 #dalam biner bernilai 0000 1101
b = 37 #dalam biner bernilai 0010 0101
c = a | b #akan bernilai     0010 1101
print(c)




#Operator Keanggotaan

#in
sebuah_list = [1,2,3,4,5]
print('sebua_list =', sebuah_list)
print('5 in sebuah_list bernilai', 5 in sebuah_list)
print('10 in sebuah_list bernilai', 10 in sebuah_list)
print()

#not in
sebuah_list = [1,2,3,4,5]
print('sebua_list =', sebuah_list)
print('5 not in sebuah_list bernilai', 5 not in sebuah_list)
print('10 not in sebuah_list bernilai', 10 not in sebuah_list)




#Operator Identitas

#is
a, b, c = 10, 10, 5
print('a =', a)
print('b =', b)
print('c =', c)
print('a is b bernilai', a is b)
print('a is c bernilai', a is c)
print()

#is not
a, b, c = 10, 10, 5
print('a =', a)
print('b =', b)
print('c =', c)
print('a is not b bernilai', a is not b)
print('a is not c bernilai', a is not c)