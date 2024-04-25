import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.ndimage import gaussian_filter

###Fonction de bruitage poivre et sel###
def bruitage_poivresel(image,prob):
    output = np.zeros(image.shape, dtype=np.uint8)
    l=len(image)
    c=len(image[0])
    for i in range(l):
        for j in range(c):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > 1-prob:
                output[i][j] = 1
            else:
                output[i][j] = image[i][j]
    return output
########################################


#ImageOriginale=bruitage_poivresel(ImageOriginale,0.005)
#ImageOriginale=gaussian_filter(ImageOriginale,1)
