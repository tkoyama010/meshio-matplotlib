"""meshio :heart: matplotlib

     * :exclamation: Inspired by Custom 3D engine in Matplotlib
"""
from typing import List, Tuple

import numpy as np


class Mesh:
    """Mesh object

     Mesh information of plot

    Attributes:
        points : points of mesh.
        cells : cells of mesh.
        faces : faces of mesh.

    """

    def __init__(self, points: np.ndarray, cells: List[Tuple[str, np.ndarray]]) -> None:
        self._points = points
        self._cells = cells

    @property
    def points(self) -> np.ndarray:
        """points

         points of mesh.
        """
        return self._points

    @property
    def cells(self) -> List[Tuple[str, np.ndarray]]:
        """cells

         cells of mesh.
        """
        return self._cells

    @property
    def faces(self) -> List[Tuple[str, np.ndarray]]:
        """faces

         faces of mesh.
        """
        faces = [
            (
                "quad",
                np.array(
                    [
                        [0, 1, 2, 3],
                        [5, 4, 7, 6],
                        [4, 0, 6, 2],
                        [1, 5, 3, 7],
                        [4, 5, 0, 1],
                        [2, 3, 6, 7],
                    ]
                ),
            )
        ]
        return faces
