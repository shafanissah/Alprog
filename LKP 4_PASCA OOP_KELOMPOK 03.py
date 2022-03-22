passwordfix = 123456


while True :
    password = int(input("Masukkan PIN Anda :"))
    if password==passwordfix :
        
        print ("\n -----SELAMAT DATANG NASABAH-----")
        break
    else :
        print ("PIN anda salah, mohon masukkan PIN kembali")
 

#Parent Class
class user () :
    def __init__(self,nama,umur,gender) :
        self.nama = nama
        self.umur = umur
        self.gender = gender

    def tampilan_data(self):
        print ("")
        print ("========= BERIKUT DATA DIRI ANDA =========")
        print ("")
        return f" Nama Anda \t: {self.nama} \n Usia Anda \t: {self.umur} \n Gender Anda \t: {self.gender}"
    
    def tampilan_akhir(self):
        print ("")
        print ("========= JUMLAH SALDO REKENING =========")
        print ("")

Akbar = user ("Akbar","19","Laki - Laki")
print(Akbar.tampilan_data())


print ("")
print ("========= SELAMAT DATANG DI BANK 03 =========")
print ("")
 
 #Child Class
class Bank(user):
    def __init__(self,nama,umur,gender):
        super().__init__(nama,umur,gender)
        self.saldo = 0
  
    def deposit(self):
        amount = float(input("Masukkan jumlah yang ingin anda depositkan \t\t : "))
        self.saldo = self.saldo + amount
        print("Deposit berhasil dilakukan dan Saldo anda sekarang \t : %f" %self.saldo)

    def penarikan(self):
        while True:
          amount = float(input("Masukkan jumlah yang ingin anda tarik \t\t\t : "))
          if (self.saldo >= amount):
              self.saldo = self.saldo - amount
              print("Penarikan Berhasil")
              break
          else:
              print("\nMohon maaf, saldo tidak memadai")

    def tampilan_data(self):
        print ("")
        print ("================ Transaksi Berhasil ================")
        print ("")
        return f" Nama Anda \t\t\t: {self.nama} \n Usia Anda \t\t\t: {self.umur} \n Gender Anda \t\t\t: {self.gender} \n Jumlah Saldo Anda sekarang \t: {self.saldo}"

Akbar = Bank("Akbar","19","Laki - Laki")
Akbar.deposit()
Akbar.penarikan()
print(Akbar.tampilan_data())

print("\n --- TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI ---   ")