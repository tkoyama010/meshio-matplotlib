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
        faces = []
        for cell in self.cells:
            cell_type = cell[0]
            cell_datas = cell[1]
            face_type = "quad"
            face_datas = []
            for cell_data in cell_datas:
                face_datas.append(
                    [cell_data[0], cell_data[1], cell_data[2], cell_data[3]]
                )
                face_datas.append(
                    [cell_data[5], cell_data[4], cell_data[7], cell_data[6]]
                )
                face_datas.append(
                    [cell_data[4], cell_data[0], cell_data[3], cell_data[7]]
                )
                face_datas.append(
                    [cell_data[1], cell_data[5], cell_data[6], cell_data[2]]
                )
                face_datas.append(
                    [cell_data[4], cell_data[5], cell_data[1], cell_data[0]]
                )
                face_datas.append(
                    [cell_data[3], cell_data[2], cell_data[6], cell_data[7]]
                )
            faces.append((face_type, np.array(face_datas)))
        return faces
