import numpy as np 
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 
  
ON = 255
OFF = 0
  
def randomGrid(N): 
    return np.random.choice([ON, OFF] , N*N, p=[0.25, 0.75]).reshape(N, N) 
  
def update(frameNum, img, grid, N):

    newGrid = grid.copy() 
    for i in range(N): #for row
        total = 0
        for j in range(N): #for column
  
            #No edge cases
            if total == 0: #if first time through
                left_sum =    grid[(i-1)%N, (j-1)%N] + grid[i, (j-1)%N] +  grid[(i+1)%N, (j-1)%N] #j-1 column
                central_sum = grid[(i-1)%N, j]                          +  grid[(i+1)%N, j]      #j column
                right_sum =   grid[(i-1)%N, (j+1)%N] + grid[i, (j+1)%N] +  grid[(i+1)%N, (j+1)%N] #j+1 column
                total = int((left_sum + central_sum + right_sum)/255)
            else:
                left_sum =    central_sum + grid[i, (j-1)%N]
                central_sum = right_sum - grid[i, j]
                right_sum =   grid[(i-1)%N, (j+1)%N] + grid[i, (j+1)%N] +  grid[(i+1)%N, (j+1)%N]
                total = int((left_sum + central_sum + right_sum)/255)
  
            # apply Conway's rules 
            if grid[i, j]  == ON: 
                if (total < 2) or (total > 3): 
                    newGrid[i, j] = OFF 
            else: 
                if total == 3: 
                    newGrid[i, j] = ON 
  
    # update data 
    img.set_data(newGrid) 
    grid[:] = newGrid[:] 
    return img 
  
def main(): 
      
    N = 150   
    grid = randomGrid(N) 
  
    updateInterval = 16 #60FPS baby
    fig, ax = plt.subplots() 
    img = ax.imshow(grid, interpolation='nearest') 
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N ), interval=updateInterval) 
    plt.show() 
  

main() 
