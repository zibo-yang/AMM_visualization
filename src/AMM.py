import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.animation as animation
import matplotlib

def exchange(m, n):
    
    #necessary data
    N = 40 # Meshsize
    fps = 10 # frame per sec
    frn = 50 # frame number of the animation
    
    #construct meshdata of two currencies (x,y) and get function to parameter z 
    x = np.arange(m,n,0.1)
    x, y = np.meshgrid(x, x)
    zarray = np.zeros((N, N, frn))
    x1 = np.linspace(m, n, 40)
    y1 = x1

    for i in range(frn):
        z2 = [np.multiply([x1[i]], y1) for i in range(40)]
        z = np.array(z2)
        zarray[:,:,i] = (30+i-z)/(x+y)
    
    #update the change of parameter z based on formula and time-varying constant
    def update_plot(frame_number, zarray, plot):
        plot[0].remove()
        if (frame_number%10==0):
            #ax.collections.pop()
            plot[1] = ax.contour(x,y, zarray[:,:,frame_number],[10],zorder=3,colors='red')
            plot[0] = ax.plot_surface(x, y, zarray[:,:,frame_number], cmap="coolwarm",
                     linewidth=0, antialiased=False, zorder=4)
        else:
            plot[0] = ax.plot_surface(x, y, zarray[:,:,frame_number], cmap="coolwarm",
                     linewidth=0, antialiased=False, zorder=4)

    #construct the animation
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    plot = [ax.plot_surface(x, y, zarray[:,:,0], cmap="coolwarm", linewidth=0, antialiased=False, shade=True,zorder=4), ax.contour(x,y, zarray[:,:,0],[10])]
    anim = animation.FuncAnimation(fig, update_plot, frn, fargs=(zarray, plot), interval=1000/fps)
    
    #set the 3d axis-space
    ax.set_zlim(0,20)
    ax.set_xlim(0,5)
    ax.set_ylim(0,5)
    ax.set_xlabel('X: currency x')
    ax.set_ylabel('Y: currency y')
    ax.set_zlabel('Z: parameter z')
    ax.set_title("currencies exchange situation of automated market maker \nwith formula: xy + z(x+y) = constant")
    
    #show
    plt.show()
    
    #save
    #f = r"/home/avalon/Desktop/AMM_visualiza/anim.gif"
    writervideo = animation.FFMpegWriter(fps=60)
    anim.save("./anim.gif", writer=writervideo)
    plt.close()
    

