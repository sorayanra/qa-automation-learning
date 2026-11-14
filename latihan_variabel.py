nama = "Soraya Nur Aulia" 
pekerjaan = "qaautomation"
pengalaman = 3
nilai = 99.9
status_belajar = True

print(nama)
print(pekerjaan)
print(pengalaman)
print(nilai)
print(status_belajar)

print(type(nama))
print(type(pekerjaan))
print(type(pengalaman))
print(type(nilai))
print(type(status_belajar))

nilai = 100

print(nilai==70)
print(nilai>120)
print(nilai<80)
print(nilai!=100)
print(nilai>=150)
print(nilai<=180)

password = "sorayaA0307!!?"
username = "SorayaaNra"

if password == "sorayaA0307!!?" or username == "SorayaaNra":
    print("Login berhasil")

elif password == "":
    print("Password belum diisi")

else: 
    print("Login gagal")

akun_aktif = False

if not akun_aktif:
    print("Akun tidak aktif")
else: 
    print("Akun aktif")

password = "soraya1234"

if len(password) >= 8:
    print("Password valid")

else : 
    print("password terlalu pendek")

username = "soraya"
password = "soraya123773!!"
akun_aktif = True

if akun_aktif : 
    if username == "soraya":
        if password == "soraya1237373":
            print("Login berhasil")

        else:
            print("password salah")
    else: 
        print("username salah")

else: 
    print("akun tidak aktif")

password = "123456"

if len(password) >= 8:
    print("password valid")

else :
    print("password terlalu pendek")

