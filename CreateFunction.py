import math

#=================================
#1 Konversi Suhu
#=================================

def convert_temp(value, unit):
    if unit == 'C':
        # Celcius ke Fahrenheit
        return (9/5 * value) + 32
    elif unit == 'F':
        # Fahrenheit ke Celcius
        return (value - 32) * 5/9

print("=== TASK 1 : KONVERSI SUHU ===")

nilai_suhu = float(input("masukkan nilai suhu: "))
satuan_suhu = input("masukkan satuan (C/F): ").upper()

hasil = convert_temp(nilai_suhu, satuan_suhu)

print("nilai suhu awal  :", nilai_suhu)
print("satuan suhu      :", satuan_suhu)
print("hasil konversi   :", hasil)

print("\n" + "="*40 + "\n")


#=====================================
# 2 Luas Lingkaran Menggunakan Lambda
#=====================================

luas_lingkaran = lambda r: math.pi * r**2
print("== TASK 2: LUAS LINGKARAN ===")
jari_jari = float(input("masukkan jari_jari lingkaran: "))
hasil_luas = luas_lingkaran(jari_jari)

print("Jari-jari lingkaran  :", jari_jari)
print("Luas lingkaran       :", hasil_luas)

print("\n" + "="*40 + "\n")