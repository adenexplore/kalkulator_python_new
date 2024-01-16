def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Input dari pengguna
num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

# Pilihan operasi
print("Pilih operasi:")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

choice = input("Masukkan pilihan (1/2/3/4): ")

# Hitung hasil
if choice == '1':
    result = tambah(num1, num2)
    operator = '+'
elif choice == '2':
    result = kurang(num1, num2)
    operator = '-'
elif choice == '3':
    result = kali(num1, num2)
    operator = '*'
elif choice == '4':
    result = bagi(num1, num2)
    operator = '/'
else:
    print("Pilihan tidak valid")
    exit()

# Tampilkan hasil
print(f"{num1} {operator} {num2} = {result}")
