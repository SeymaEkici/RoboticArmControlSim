import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# PD kontrolör parametreleri
kp = 1.0  # Proportional gain
kd = 0.1  # Derivative gain

# Simülasyon parametreleri
time_step = 0.01  # Zaman adımı
sim_time = 5.0  # Toplam simülasyon süresi (saniye)
time = np.arange(0, sim_time, time_step)  # Zaman vektörü

# Başlangıç değerleri
theta = 0  # Başlangıç pozisyonu (açı, derece)
theta_target = 90  # Hedef pozisyonu (derece)
theta_dot = 0  # Başlangıç açısal hızı
tau = 0  # Başlangıç torku
inertia = 1.0  # Sistemin ataleti

# Robotic arm parametreleri
arm_length = 5  # Kol uzunluğu (birim)

# Kayıt için listeler
theta_list = []
error_list = []
time_list = []
path_x = []  # İz bırakmak için X pozisyonlarını tutan liste
path_y = []  # İz bırakmak için Y pozisyonlarını tutan liste

# İlk pozisyonu hesaplayıp kaydet
theta_list.append(theta)
path_x.append(arm_length * np.cos(np.radians(theta)))
path_y.append(arm_length * np.sin(np.radians(theta)))

# Simülasyon döngüsü
for t in time:
    error = theta_target - theta  # Hata hesaplama
    theta_ddot = tau / inertia  # Açısal ivme
    theta_dot += theta_ddot * time_step  # Açısal hız güncellemesi
    theta += theta_dot * time_step  # Pozisyon güncellemesi
    
    # PD kontrolör
    tau = kp * error - kd * theta_dot  # Tork hesaplama
    
    # Pozisyonu kaydet
    theta_list.append(theta)
    error_list.append(error)
    time_list.append(t)
    path_x.append(arm_length * np.cos(np.radians(theta)))
    path_y.append(arm_length * np.sin(np.radians(theta)))

# Animasyon oluşturma
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-arm_length - 1, arm_length + 1)
ax.set_ylim(-arm_length - 1, arm_length + 1)
ax.set_title("Robotic Arm Movement (PD Control)")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Grafik elemanları
line, = ax.plot([], [], 'o-', lw=4, color='blue')  # Robotic arm
path, = ax.plot([], [], lw=2, color='gray')  # İz
target_dot, = ax.plot([], [], 'ro', label='Target')  # Hedef noktası
start_dot, = ax.plot([path_x[0]], [path_y[0]], 'go', label="Start")  # Başlangıç noktası

def init():
    """Animasyon başlangıç ayarları."""
    line.set_data([], [])
    path.set_data([], [])
    target_dot.set_data([arm_length * np.cos(np.radians(theta_target))],
                        [arm_length * np.sin(np.radians(theta_target))])
    return line, path, target_dot, start_dot

def update(frame):
    line.set_data([0, path_x[frame]], [0, path_y[frame]])  # Robot kolunu güncelle
    path.set_data(path_x[:frame], path_y[:frame])  # İzi güncelle
    return line, path, target_dot, start_dot

# Animasyonu oluştur
ani = FuncAnimation(fig, update, frames=len(theta_list), init_func=init, blit=True, interval=10)

plt.legend()
plt.grid()
plt.show()

# Simülasyon sonrası hata grafiği
plt.figure()
plt.plot(time_list, error_list, label="Error")
plt.title("Error Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Error (degrees)")
plt.legend()
plt.grid()
plt.show()
