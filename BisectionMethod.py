import math

def pangkat(bil, jumlah, nilai):
  bilangan = jumlah 
  pangkat = 0
  total = 0
  while bilangan >= 0:
    a = bil[bilangan]*math.pow(nilai,pangkat)
    total += a
    pangkat += 1
    bilangan -= 1
  return total

def bisection(a, b, bil,jumlah,e, N):
  x_a = a
  x_b = b
  
  fx_a = pangkat(bil, jumlah, x_a)
  fx_b = pangkat(bil, jumlah, x_b) 
  if fx_a*fx_b > 0:
    print("Masukkan angka lain")
    return None

  for n in range (1,N):
    x_t = (x_a + x_b)/2
    fx_a = pangkat(bil, jumlah, x_a)
    fx_b = pangkat(bil, jumlah, x_b)
    fx_t = pangkat(bil, jumlah, x_t)
    print("Iterasi ke ",n)
    print("x_a = ",x_a)
    print("x_b = ",x_b)
    print("x_t = ", x_t)
    print("f(x_a) = ", fx_a)
    print("f(x_b) = ", fx_b)
    print("f(x_t) = ", fx_t)
    if ((fx_t*fx_a) >= 0):
      print("(fx_t).(fx_a) = +")
    else:
      print("(fx_t).(fx_a) = -")
    print()
    if abs(fx_t) <= e:
      return (x_t)
    else:
      if fx_a*fx_t < 0:
        x_b = x_t
      elif fx_b*fx_t < 0:
        x_a = x_t
  return (x_t)

banyakBilangan = int(input("Masukkan Pangkat Tertinggi = "))
bil = []
jumlah = banyakBilangan
while banyakBilangan >= 0:
  angka = int(input(f"Masukkan koefisien dengan pangkat ke - {banyakBilangan} = "))
  bil.append(angka)
  banyakBilangan -= 1

a = int(input("Masukkan x_a = "))
b = int(input("Masukkan x_b = ")) 
e = float(input("Masukkan Nilai Toleransi = "))
N = int(input('Masukkan iterasi maksimal : '))
x_root = bisection(a,b,bil,jumlah,e,N)
print("Akar = ", x_root)