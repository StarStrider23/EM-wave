import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class FancyArrowPatch3D(FancyArrowPatch):
    """
    Modified version of the FancyArrowPatch class, FancyArrowPatch3D, that allows one
    to plot arrows in 3D. Similarly to the original class, to instantiate an arrow,
    a pair of triplets, (x1, y1, z1) and (x2, y2, z2), needs to be provided for the 
    arrow's tail and head respectively. Other than that, the modified class works 
    exactly the same as the original one. 
    """
    
    def __init__(self, xyz1, xyz2, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self.xyz1 = xyz1
        self.xyz2 = xyz2

    def do_3d_projection(self, renderer=None):
        (x1, y1, z1) = self.xyz1
        (x2, y2, z2) = self.xyz2
        x, y, z = proj3d.proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((x[0], y[0]), (x[1], y[1]))
        return np.min(z)