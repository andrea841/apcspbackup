import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import PIL

def make_mask(rows, columns, stripe_width):
    ''' insert a docstring here ''' 
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            #image[row][column] = [180, 100, 255, 255]
            if ((row-column)**2/stripe_width)**3 % 2 != 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                #image[row][column] = [255, 127, 127, 0] # pale red, alpha=0
                image[row][column] = [255, 127, 127, 0]
            else: 
                # Odd stripe
                #image[row][column] = [180, 150, 255, 255] # light purple 
                image[column][row] = [180, 150, 255, 255]
    return image
 
 
   
if __name__ == "__main__":
    image = make_mask(100,100,15)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask')     
    
    
''' 

def make_mask(rows, columns, stripe_width):
    An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns

    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row+column)/stripe_width % 2 != 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [255, 127, 127, 0] # pale red, alpha=0
            
            else:
                # Odd stripe
                image[row][column] = [180, 100, 255, 255] # magenta, alpha=255
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,10)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask')     

''' 