from PIL import Image
from pylab import *
import os

def pca(X):
    num_data, dim = X.shape
    mean_X = X.mean(axis=0)
    X = X - mean_X
 
    if dim>num_data:
        M = dot(X,X.T)
        e,EV = linalg.eigh(M)
        tmp = dot(X.T, EV).T
        V = tmp[::-1]
        S = sqrt(e)[::-1]
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        U,S,V = linalg.svd(X)
        V = V[:num_data]

    return V,S,mean_X


input_path = './a_thumbs/'

infile = [os.path.join(input_path,f) for f in os.listdir(input_path)]
m,n = array(Image.open(infile[0])).shape
X = array([array(Image.open(f)).flatten() for f in infile])
print X.shape
V,S,mean_X = pca(X)

# mean
subplot(2,4,1)
gray()
title('mean')
axis('off')
im = mean_X.reshape([m,n])
imshow(im)

# lambda 
for i in range(7):
    subplot(2,4,i+2)
    im = V[i].reshape([m,n])
    imshow(im)
    axis('off')
    title('lambda '+str(i+1))
    
show()




