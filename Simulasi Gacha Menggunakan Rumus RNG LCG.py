import matplotlib.pyplot as plt
import numpy as np

a = 17
m = 61
z0 = 3
n = 89

results = []

z = z0
for i in range(1, n+1):
 z_prev = z
 z = (a * z) % m
 u = z/m
 percentage = round(u * 100, 2)  # Kolom persentase
 rumus = f"(17 * {z_prev}) mod {m}"
 results.append([i, z_prev, rumus, z, round(u, 3), f"{percentage}%"])
results.append([90, "PASTI DAPAT", "PASTI DAPAT", "PASTI DAPAT", 1, "100%"])

print(f"{'1':<3} | {'zi-1(Bilangan Sebelumnya)':<28} | {'rumus zi = (17,zi-1) mod 61':<32} | {'z (Bilangan Acak)':<20} | {'ui = zi/61 (Bilangan Acak Seragam)':<35} | {'% (Persentase)':<10}")
print("_" * 150)

for row in results:
 print(f"{row[0]:<3} | {row[1]:<28} | {row[2]:<32} | {row[3]:<20} | {row[4]:<35} | {row[5]:<10}")

iterasi = [row[0] for row in results]  
value = [row[4] for row in results]  

plt.figure(figsize=(10, 6))
plt.plot(iterasi, value, marker='o', linestyle='-', color='b', label='Nilai Ui')
plt.axhline(y=1, color='r', linestyle='--', label='Ui = 1 (Guaranteed)')
plt.title("Grafik Bilangan Acak Seragam (Ui) dari LCG")
plt.xlabel("Wish/Gacha")
plt.ylabel("Nilai Ui")
plt.grid(True)
plt.legend()
plt.show()