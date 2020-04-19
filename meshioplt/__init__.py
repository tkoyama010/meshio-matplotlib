"""
[meshio](https://github.com/nschloe/meshio):heart: [matplotlib](https://github.com/matplotlib/matplotlib)

:exclamation: Inspired by [Custom 3D engine in Matplotlib](https://matplotlib.org/matplotblog/posts/custom-3d-engine/)
"""

class Mesh:
    def __init__(self, points, cells):
        self.points = points
        self.cells = cells
