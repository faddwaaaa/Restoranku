
# RESTORANKU

print("======================================")
print("             RESTORANKU")
print("======================================")

# Memasukkan identitas pelanggan
pelanggan = input("Masukkan nama pelanggan : ")
no_meja = input("Masukkan nomor meja      : ")

# Menampilkan daftar menu
print("\n============== DAFTAR MENU ==============")
print("Kode  Nama Menu             Harga")
print("-----------------------------------------")
print("NG    Nasi Goreng           Rp 25.000")
print("MA    Mie Ayam              Rp 20.000")
print("AB    Ayam Bakar            Rp 30.000")
print("ES    Es Teh                Rp 5.000")
print("JM    Jus Mangga            Rp 10.000")
print("=========================================")

# Menyiapkan list untuk menyimpan pesanan
nama_menu = []
harga_menu = []
jumlah_pesan = []
total_harga = []

# Memasukkan jumlah jenis menu
banyak_jenis = int(input("\nBerapa jenis menu yang ingin dipesan? "))

# Mengulang proses pemesanan
for i in range(banyak_jenis):
    print("\nPesanan ke-", i + 1)

    kode = input("Masukkan kode menu (NG/MA/AB/ES/JM): ")
    kode = kode.upper()

    if kode == "NG":
        nama = "Nasi Goreng"
        harga = 25000
    elif kode == "MA":
        nama = "Mie Ayam"
        harga = 20000
    elif kode == "AB":
        nama = "Ayam Bakar"
        harga = 30000
    elif kode == "ES":
        nama = "Es Teh"
        harga = 5000
    elif kode == "JM":
        nama = "Jus Mangga"
        harga = 10000
    else:
        nama = "Tidak Ada"
        harga = 0
        print("Kode menu tidak tersedia. Silakan masukkan lagi.")

    jumlah = int(input("Masukkan jumlah porsi: "))
    total = harga * jumlah

    # Menyimpan data pesanan ke dalam list
    nama_menu.append(nama)
    harga_menu.append(harga)
    jumlah_pesan.append(jumlah)
    total_harga.append(total)

# Menampilkan rincian pesanan
print("\n")
print("=============== STRUK PEMESANAN ===============")
print("Nama Pelanggan : ", pelanggan)
print("Nomor Meja     : ", no_meja)
print("------------------------------------------------")
print(f"{'No':<4}{'Nama Menu':<15}{'Harga':<11}{'Jumlah':<8}{'Total'}")
print("------------------------------------------------")

for i in range(banyak_jenis):
    print(f"{i+1:<4}{nama_menu[i]:<15}{'Rp '+str(harga_menu[i]):<11}{jumlah_pesan[i]:<8}{'Rp '+str(total_harga[i])}")

print("------------------------------------------------")

# Menghitung total seluruh pesanan
subtotal = sum(total_harga)

# Diskon 10% jika jumlah seluruh porsi minimal 3
total_porsi = sum(jumlah_pesan)

if total_porsi >= 3:
    diskon = int(subtotal * 10 / 100)
else:
    diskon = 0

# Menghitung pajak dan total pembayaran
setelah_diskon = subtotal - diskon
pajak = int(setelah_diskon * 10 / 100)

total_sementara = setelah_diskon + pajak

# Membulatkan total pembayaran ke Rp500 terdekat
total_bayar = round(total_sementara / 500) * 500

# Menyesuaikan pajak dengan total pembayaran
pajak = total_bayar - setelah_diskon

print("Subtotal       : Rp", subtotal)
print("Total Porsi    : ", total_porsi)
print("Diskon         : Rp", diskon)
print("Pajak 10%      : Rp", pajak)
print("Total Bayar    : Rp", total_bayar)
print("================================================")

# Memasukkan uang pembayaran
uang_bayar = int(input("Masukkan uang pembayaran: Rp "))

if uang_bayar >= total_bayar:
    uang_kembali = uang_bayar - total_bayar
else:
    uang_kembali = 0
    print("Uang pembayaran kurang!")

# Menampilkan bagian akhir struk
print("\n============== PEMBAYARAN ==============")
print("Uang Bayar     : Rp", uang_bayar)
print("Uang Kembali   : Rp", uang_kembali)
print("----------------------------------------")
print("Terima kasih sudah berkunjung!")
print("          SELAMAT MENIKMATI")
print("========================================")
