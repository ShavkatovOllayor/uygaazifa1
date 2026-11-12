import matplotlib.pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
natijalar = [50, 55, 60, 58, 70, 80, 90]

plt.plot(kunlar, natijalar, color="purple", marker="o", linewidth=2)

plt.title("Haftalik natijalar")
plt.xlabel("Kunlar")
plt.ylabel("Natijalar")

plt.grid(True)

plt.savefig("natija.png")

plt.show()