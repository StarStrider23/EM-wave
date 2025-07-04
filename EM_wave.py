import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from matplotlib import animation
from FancyArrowPatch3D import FancyArrowPatch3D as arrow

fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(111, projection='3d')

t = np.linspace(0,50,250)
y = np.zeros_like(t)

# E-field's (and implicitely B-field's) amplitude

E = 1
 
values = []
for frame, step in enumerate(t):
    z = E * np.sin(t - step)
    values.append([np.linspace(0, len(t), 2*len(t)+1)[:frame+1], y[:frame+1], z[:frame+1]])

# Creating a coordinate system

x_axis = arrow((-0.1, 0, 0), (7, 0, 0), mutation_scale=20, arrowstyle='-|>', linestyle='solid', label='_nolegend_', color='k')
y_axis = arrow((0, 0.6, 0), (0, -1.1, 0), mutation_scale=20, arrowstyle='-|>', linestyle='solid', label='_nolegend_', color='k')
z_axis = arrow((0, 0, -0.6), (0, 0, 1.1), mutation_scale=20, arrowstyle='-|>', linestyle='solid', label='_nolegend_', color='k') 

def animate(i):
    ax.cla()

    ax.set(xlim=(0,15), ylim=(-1,1), zlim=(-1,1))

    plt.axis('off')

    # Creating a light ray that propagates along the x-axis and arrows for the electric and magnetic fields 
    # using the modified FancyArrowPatch (FancyArrowPatch3D)

    for j in range(1, i):
        if j <= 30:
            ax.plot(values[j][0], values[j][1], values[j][1], color='y', lw=2)
            arr1 = arrow((values[i][0][j], 0, 0), (values[i][0][j], 0, values[i][2][j]), mutation_scale=5, arrowstyle='simple', linestyle='solid', color='b', label='_nolegend_')
            arr2 = arrow((values[i][0][j], 0, 0), (values[i][0][j], values[i][2][j], 0), mutation_scale=5, arrowstyle='simple', linestyle='solid', color='r', label='_nolegend_')
            ax.add_patch(arr1)
            ax.add_patch(arr2)
        
    arrow1 = arrow((0, 0, 0), (0, 0, values[i][2][0]), mutation_scale=20, arrowstyle='simple', linestyle='solid', color='darkblue', label='_nolegend_')
    ax.add_patch(arrow1)

    txt1 = ax.text(0+0.25, 0, 0, 'E', color='darkblue', fontweight='bold')
    txt1.set_text('E')
    txt1.set_z(values[i][2][0]+0.15 if values[i][2][0]>=0 else values[i][2][0]-0.15)

    arrow2 = arrow((0, 0, 0), (0, values[i][2][0], 0), mutation_scale=20, arrowstyle='simple', linestyle='solid', color='darkred', label='_nolegend_')
    ax.add_patch(arrow2)

    txt2 = ax.text(0, 0+0.25, 0, 'B', color='darkred', fontweight='bold')
    txt2.set_text('B')
    txt2.set_y(values[i][2][0]+0.15 if values[i][2][0]>=0 else values[i][2][0]-0.15)

    ax.add_patch(x_axis)
    ax.text(7+0.25, 0, 0, 'X', fontweight='bold')

    ax.add_patch(y_axis)
    ax.text(0, -1.1-0.1, 0, 'Y', fontweight='bold')

    ax.add_patch(z_axis)
    ax.text(0, 0, 1.1+0.1, 'Z',fontweight='bold')

    plt.title('EM wave propagation', fontweight='bold', fontsize=16)

    # Legend for the plot, which is commented out since the animation gets a lot
    # more slower if the legend is on. Still, feel free to enable it.

    # label1 = mp.Patch(color='y', label='EM wave propagation')
    # label2 = mp.Patch(color='b', label='E-field')
    # label3 = mp.Patch(color='r', label='B-field')
    # plt.legend(handles=[label1, label2, label3])

    return []

animate = animation.FuncAnimation(fig, animate, frames=len(t), interval=100, repeat=True)

plt.show()
