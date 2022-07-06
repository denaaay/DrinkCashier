import csv
import os
import datetime

fileData = 'data.csv'
keranjang = []
editFile = 1

def hapusLayar(): #fungsi ini digunakan untuk membuat menghapus layar agar output terlihat lebih rapi
    os.system('cls' if os.name == 'nt' else 'clear')

def kembaliKeMenu(): #fungsi ini digunakan untuk menggunakan ulang program tanpa harus run ulang
    global editFile

    editFile = 1
    print("")
    input("Tekan Enter Untuk Kembali Ke Menu")
    menu()

def login(): #fungsi ini digunakan untuk autentikasi pengguna
    salah = 1

    hapusLayar()
    print("=" * 32)
    print("""
   Selamat Datang di Kedai Awan
        Silahkan Login""", "\n")
    print("=" * 32)

    while salah <= 3:
        print("")
        username = str(input("Masukkan username : "))
        password = int(input("Masukkan password : "))

        salah += 1

        if username == 'admin':
            if password == 1234:
                menu()
            else:
                print("password salah")
        else:
            if password == 1234:
                print("username salah")
            else:
                print("username & password salah")

def menu(): #fungsi ini digunakan untuk menampilkan dan menginput data
    global keranjang
    keranjang = []
    hargaSementara = 0
    beli = 1
    hapusLayar()
    print("=" * 32)
    print("""
  Selamat Datang di Kedai Awan
      Silahkan Pilih Menu""", "\n")
    print("=" * 32)
    print("""
1. Kopi Hitam   Rp. 5000
2. Kopi Susu    Rp. 5000
3. Susu Hangat  Rp. 4000
4. Teh Panas    Rp. 3000
5. Es Teh       Rp. 3000
6. Es Jeruk     Rp. 3000
7. Susu Jahe    Rp. 5000""", "\n")

    while beli == 1:
        current = datetime.datetime.now()
        hari = current.day
        bulan = current.month
        tahun = current.year
        tanggal = f"{hari}-{bulan}-{tahun}"

        print("")
        pilihBarang = int(input("Masukkan Nomor Menu    : "))
        jumlahBarang = int(input("Masukkan Jumlah        : "))

        if pilihBarang == 1:
            namaBarang = "Kopi Hitam"
            hargaBarang = 5000
        elif pilihBarang == 2:
            namaBarang = "Kopi Susu"
            hargaBarang = 5000
        elif pilihBarang == 3:
            namaBarang = "Susu Hangat"
            hargaBarang = 4000
        elif pilihBarang == 4:
            namaBarang = "Teh Panas"
            hargaBarang = 3000
        elif pilihBarang == 5:
            namaBarang = "Es Teh"
            hargaBarang = 3000
        elif pilihBarang == 6:
            namaBarang = "Es Jeruk"
            hargaBarang = 3000
        elif pilihBarang == 7:
            namaBarang = "Susu Jahe"
            hargaBarang = 5000
        
        hargaSementara = hargaBarang * jumlahBarang
        dataCSV = {'Tanggal':tanggal, 'Nama Barang':namaBarang, 'Jumlah Barang':jumlahBarang, 'Harga Satuan':hargaBarang, 'Total Harga':hargaSementara}
        keranjang.append(dataCSV)
        print(keranjang)
        print("")

        while True:
            ulang = str(input("Ada Lagi? [y/t] : "))

            if ulang == 'y':
                break
            elif ulang == 't':
                beli += 2
                if editFile == 1:
                    tulisData()
                elif editFile == 2:
                    tambahData()               
                dataSementara()
                break
            else:
                continue

def tulisData(): #fungsi ini untuk menulis data, dengan menghapus data sebelumnya jika ada
    try:
        listData = ['Tanggal', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']

        with open(fileData, 'w', newline='') as fileTulis:
            tulis = csv.DictWriter(fileTulis, fieldnames=listData)
            tulis.writeheader()
            tulis.writerows(keranjang)
    except IOError as e:
        print(e)

def tambahData(): #fungsi ini diågunakan untuk menulis data, dengan menambahkan data ke data yang sudah ada
    try:
        listData = ['Tanggal', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']

        with open(fileData, 'a', newline='') as fileTambah:
            tulis = csv.DictWriter(fileTambah, fieldnames=listData)
            tulis.writerows(keranjang)
    except IOError as e:
        print(e)

def hapusData(): #fungsi ini digunakan untuk menghapus salah satu data yang diinginkan pengguna
    listData = ['Tanggal', 'Nama Barang', 'Jumlah Barang', 'Harga Satuan', 'Total Harga']
    print("")
    hapus = input("Masukkan Nama Menu : ")
    daftarHapus = []
    daftarBaru = []

    try:
        with open(fileData, 'r') as fileBaca:
            baca = csv.DictReader(fileBaca, delimiter=',')
            for isi in baca:
                if isi['Nama Barang'] == hapus:
                    daftarHapus.append(hapus)
                    continue
                else:
                    daftarBaru.append(isi)
    except IOError as e:
        print(e)

    if len(daftarHapus) == 0:
        print("Menu Belum Dipesan")
    else:
        try:
            with open(fileData, 'w', newline='') as fileTulis:
                tulis = csv.DictWriter(fileTulis, fieldnames=listData)
                tulis.writeheader()
                tulis.writerows(daftarBaru)
                print("")
                print("Menu Berhasil di Hapus")
        except IOError as e:
            print(e)
        dataSementara()


def editData(): #fungsi ini digunakan untuk memilih perintah untuk mengedit data
    global editFile

    print("")
    print("Ada Perubahan?")

    while True:
        edit = str(input("Tambah [t], Hapus [h], Selesai [s] : "))

        if edit == 't':
            editFile = 2
            menu()
        elif edit == 'h':
            hapusData()
        elif edit == 's':
            strukData()
        else:
            continue

def dataSementara(): #fungsi ini digunakan untuk menampilkan data sementara yang sudah diinput
    hapusLayar()

    try:
        with open(fileData, 'r') as fileBaca:
            baca = csv.DictReader(fileBaca, delimiter=',')
            
            print('-'*89)
            print(f"|\tTanggal \t Nama Barang \t Jumlah Barang \t Harga Satuan \t Total Harga \t|")
            print("-"*89) 
            for data in baca:
                print(f"|\t{data['Tanggal']} \t {data['Nama Barang']} \t {data['Jumlah Barang']} \t\t {data['Harga Satuan']} \t\t {data['Total Harga']} \t\t|")
    except IOError as e:
        print(e)

    editData()

def strukData(): #fungsi ini digunakan untuk menampilkan data akhir dan memproses pembayaran
    hapusLayar()
    
    listTotalHarga = []
    totalHarga = 0
    try:
        with open(fileData, 'r') as fileBaca:
            baca = csv.DictReader(fileBaca, delimiter=',')
            
            print('-'*89) 
            print(f"|\tTanggal \t Nama Barang \t Jumlah Barang \t Harga Satuan \t Total Harga \t|")
            print("-"*89) 
            for data in baca:
                print(f"|\t{data['Tanggal']} \t {data['Nama Barang']} \t {data['Jumlah Barang']} \t\t {data['Harga Satuan']} \t\t {data['Total Harga']} \t\t|")
                listTotalHarga.append(int(data['Total Harga']))
                totalHarga = sum(listTotalHarga)
    except IOError as e:
        print(e)

    print("")
    print(f"Total Pembayaran Anda Adalah : Rp. {totalHarga}")
    bayar = int(input("Masukkan Uang Anda           : Rp. "))
    kembalian = bayar - totalHarga
    print(f"Kembalian Anda Adalah        : Rp. {kembalian}")

    kembaliKeMenu()

if __name__ == "__main__":
    login()