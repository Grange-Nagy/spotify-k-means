from matplotlib import pyplot as plt
import numpy as np

def findOutlier(colors):

    #this feels like a gradient decent problem?
    npColors = np.array(colors)
    mean = npColors.mean(axis=0)
    print(mean)

    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter3D(*zip(*colors))

    ax.set_xlabel('Lightness')
    ax.set_ylabel('Red-Green')
    ax.set_zlabel('Blue-Yellow')

    plt.show()

    #want 2 groupings, one with most of the points, then the rest
    #try to group the main group with an elipsoid?
    #do I care about the lightness dimension?

    




findOutlier([[106, 130,  97],
             [199, 128, 123],
             [ 90, 140, 142],
             [ 27, 129, 126],
             [153, 126, 105],
             [ 81, 133,  93],
             [168, 134, 159],
             [223, 128, 122],
             [129, 127,  99],
             [ 56, 140, 141],
             [121, 145, 149],
             [ 60, 125, 123],
             [177, 128, 121],
             [153, 129, 128],
             [121, 128, 127]])