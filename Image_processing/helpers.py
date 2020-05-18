
import numpy as np 
import matplotlib.pyplot as plt


# fonction pour afficher une image et un titre
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
    
    
# Fct pour afficher une image et par dessus les Corners trouvés dns celle-ci 
def corners_show(image, coords, title=
"Corners detected"):
    plt.imshow(image, interpolation='nearest', cmap='gray')
    plt.title(title)
    plt.plot(coords[:, 1], coords[:, 0],'+r', markersize=15)
    plt.axis('off')
    plt.show()