"""meshio :heart: matplotlib

     * :exclamation: Inspired by Custom 3D engine in Matplotlib
"""
import numpy as np
from typing import List, Tuple

class Mesh:
    """Mesh object

     Mesh information of plot

    Attributes:
        points : points of mesh.
        cells : cells of mesh.

    """

    def __init__(self, points: np.ndarray, cells: List[Tuple(str, np.ndarray)]) -> None:
        self._points = points
        self._cells = cells

    @property
    def points(self) -> np.ndarray:
        """points

         points of mesh.
        """
        return self._points

    @property
    def cells(self) -> List[Tuple(str, np.ndarray)]:
        """cells

         cells of mesh.
        """
        return self._cells
