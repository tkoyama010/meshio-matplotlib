"""meshio :heart: matplotlib

     * :exclamation: Inspired by Custom 3D engine in Matplotlib
"""
from typing import List, Tuple

import numpy as np

POINTS = np.ndarray
CELLS = List[Tuple(str, np.ndarray)]


class Mesh:
    """Mesh object

     Mesh information of plot

    Attributes:
        points : points of mesh.
        cells : cells of mesh.

    """

    def __init__(self, points: POINTS, cells: CELLS) -> None:
        self._points = points
        self._cells = cells

    @property
    def points(self) -> POINTS:
        """points

         points of mesh.
        """
        return self._points

    @property
    def cells(self) -> CELLS:
        """cells

         cells of mesh.
        """
        return self._cells
