from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 

def show_axes(pts : list[tuple[int,int,int]]):
    fig = plt.figure() 
    ax = Axes3D(fig)

    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    zs = [p[2] for p in pts]


    # creating the plot 
    plot_geeks = ax.scatter(xs, ys, zs, color='green') 

    # setting title and labels 
    ax.set_title("3D plot") 
    ax.set_xlabel('x-axis') 
    ax.set_ylabel('y-axis') 
    ax.set_zlabel('z-axis') 

    # displaying the plot 
    plt.show()
