"""meshio :heart: matplotlib

     * :exclamation: Inspired by Custom 3D engine in Matplotlib
"""


class Mesh:
    """Mesh object

     Mesh information of plot

    Attributes:
        points : points of mesh.
        cells : cells of mesh.

    """

    def __init__(self, points, cells):
        self._points = points
        self._cells = cells

    @property
    def points(self):
        """points

         points of mesh.
        """
        return self._points

    @property
    def cells(self):
        """cells

         cells of mesh.
        """
        return self._cells
