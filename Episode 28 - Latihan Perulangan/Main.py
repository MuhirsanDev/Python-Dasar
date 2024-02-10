# Latihan Perulangan Membuat Segitiga

sisi = 10

## 1. Menggunakan FOR
print("======== FOR ========")

# dummy variabel
count = 1 
for i in range(sisi):
    print("*"*count)
    count += 1
    
    
## 2. Menggunakan WHILE 
print("======== WHILE ========")

count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi:
        break
    
    
## 3. Hanya Ganjil Saja
print("======== Ganjil ========")

count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        # akan diprint jika genap
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    
    else:
        # akan kembali keatas jika ganjil
        count += 1
        continue
    
    # akan break jika count melebihi sisi
    if count > sisi:
        break    
   
 
print("======== Bentuk Terbalik ========")

count = count - 2
spasi = 1

while True:
    if (count % 2):
        print(" "*spasi, "*"*count)
        spasi += 1
        count -= 1
    else:
        count -= 1
        continue

    if count == 0:
        break  

print("akhier dari while hehehehehe") 
 
 
 
# Bentuk ketupat
print("======== Bentuk Ketupat ========")

segitiga = int(input("Masukkan sisi segitiga yang anda inginkan = "))

if segitiga % 2:
    segitiga = segitiga
else :
    segitiga -= 1

angka = 1

while angka < segitiga:
    print ((angka*"*").center(segitiga))
    angka += 2

while angka > 0:
    print ((angka*"*").center(segitiga))
    angka -= 2
    
print("Tipis Tipis Abangkuhhhh")
    
    

