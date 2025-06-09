import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
A = 1  # Amplitud
f = 2  # Frecuencia en Hz
phi = np.pi / 4  # Fase en radianes
Ts = 0.01  # Período de muestreo

# Tiempo continuo
t = np.linspace(0, 1, 1000)  # Vector de tiempo continuo
x_t = A * np.sin(2 * np.pi * f * t + phi)  # Señal continua

# Tiempo discreto
n = np.arange(0, 1, Ts)  # Vector de tiempo discreto
x_n = A * np.sin(2 * np.pi * f * n + phi)  # Señal discreta

# Graficar
plt.figure(figsize=(10, 5))

# Señal en tiempo continuo
plt.subplot(2, 1, 1)
plt.plot(t, x_t, label="Señal continua")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal en tiempo continuo")
plt.legend()
plt.grid()

# Señal en tiempo discreto
plt.subplot(2, 1, 2)
plt.stem(n, x_n, basefmt=" ", label="Señal discreta")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal en tiempo discreto")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

