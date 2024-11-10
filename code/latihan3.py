saldo = 1000000

while True:
    print(f"Saldo saat ini {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    pilihan = input("Pilih menu (1/2): ")
    if pilihan == '1':
        nom_tarik = int(input("Masukkan Jumlah penarikan: "))
        if saldo > nom_tarik:
            saldo -= nom_tarik
        else:
            print("Saldo Anda Tidak Cukup")
    else:
        print("Terimakasih telah menggunakan ATM")
        break


