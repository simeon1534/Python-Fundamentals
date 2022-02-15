L = int(input())
W = int(input())
A = int(input())

zala_s = (L * 100) * (W * 100)
garderob = (A * 100) * (A * 100)
peika = zala_s / 10
svobodno_mqsto = zala_s - (garderob + peika)
tanciori = svobodno_mqsto / 7040
print(round(tanciori))
