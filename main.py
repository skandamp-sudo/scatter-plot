import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis', edgecolors='w', linewidth=0.5)

plt.title('Skanda M P', fontsize=16)
plt.xlabel('X-axis Label', fontsize=12)
plt.ylabel('Y-axis Label', fontsize=12)

cbar = plt.colorbar(scatter)
cbar.set_label('Color Scale', fontsize=12)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)


for i in range(len(x)):
    if sizes[i] > 700:
        plt.annotate(f'({x[i]:.2f}, {y[i]:.2f})', (x[i], y[i]), fontsize=8, ha='right')

plt.legend(['Data points'], loc='upper right')

plt.show()
