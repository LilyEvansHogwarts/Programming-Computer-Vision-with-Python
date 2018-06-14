import os
from PIL import Image
import pickle
from pylab import *

def pca(X):
    mean_X = X.mean(axis=0)
    X = X - mean_X
    num_data, dim = X.shape
    
    if num_data<dim:
        M = dot(X,X.T)
        e,EV = linalg.eigh(M)
        tmp = dot(X.T,EV).T
        V = tmp[::-1]
        S = sqrt(maximum(1e-11,e[::-1]))
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        U,S,V = linalg.svd(X)
        V = V[:num_data]
    return V,S,mean_X


input_path = './a_thumbs/'

filelist = [os.path.join(input_path,f) for f in os.listdir(input_path)]
m,n = array(Image.open(filelist[0])).shape
X = array([array(Image.open(f)).flatten() for f in filelist])
print X.shape

V,S,immean = pca(X[:600])

with open('font_pca_models.pkl','wb') as f:
    pickle.dump(immean,f)
    pickle.dump(V,f)

with open('font_pca_models.pkl','rb') as f:
    immean = pickle.load(f)
    V = pickle.load(f)

subplot(2,4,1)
im = immean.reshape([m,n])
imshow(im)
gray()
title('mean')
axis('off')
for i in range(7):
    subplot(2,4,i+2)
    title('lambda '+str(i+1))
    axis('off')
    im = V[i].reshape([m,n])
    imshow(im)
show()

im = array(Image.open(filelist[0]))
imshow(im)
print 'Please click 3 points'
x = ginput(3)
savetxt('text.txt',x,'%i')
y = loadtxt('text.txt')
print 'you clicked:',y
show()
