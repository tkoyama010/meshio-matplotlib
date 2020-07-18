"""meshio :heart: matplotlib

     * :exclamation: Inspired by Custom 3D engine in Matplotlib
"""
from typing import List, Tuple

import numpy as np

import meshio

from matplotlib.patches import Polygon

import matplotlib.pyplot as plt


def hexahedrons_to_quads(cell_datas: np.ndarray) -> np.ndarray:
    """hexahedrons_to_quads

     convert hexahedron cells to quad faces.

    Args:
       cell_datas: point index of cells

    Returns:
       face_datas: point index of faces

    """
    face_datas = []
    for cell_data in cell_datas:
        face_datas.append([cell_data[0], cell_data[1], cell_data[2], cell_data[3]])
        face_datas.append([cell_data[5], cell_data[4], cell_data[7], cell_data[6]])
        face_datas.append([cell_data[4], cell_data[0], cell_data[3], cell_data[7]])
        face_datas.append([cell_data[1], cell_data[5], cell_data[6], cell_data[2]])
        face_datas.append([cell_data[4], cell_data[5], cell_data[1], cell_data[0]])
        face_datas.append([cell_data[3], cell_data[2], cell_data[6], cell_data[7]])
    return face_datas


def tetra_to_triangle(cell_datas: np.ndarray) -> np.ndarray:
    """tetra_to_triangle

     convert tetra cells to triangle.

    Args:
       cell_datas: point index of cells

    Returns:
       face_datas: point index of faces

    """
    face_datas = []
    for cell_data in cell_datas:
        face_datas.append([cell_data[0], cell_data[1], cell_data[2]])
        face_datas.append([cell_data[1], cell_data[3], cell_data[2]])
        face_datas.append([cell_data[0], cell_data[2], cell_data[3]])
        face_datas.append([cell_data[0], cell_data[3], cell_data[1]])
    return face_datas


def cell_to_face(cell: Tuple[str, np.ndarray]) -> Tuple[str, np.ndarray]:
    """cell_to_face

     convert cell to face.

    Args:
       cell: data structure of cell

    Returns:
       face: data structure of face
    """

    cell_type = cell[0]
    cell_datas = cell[1]
    if cell_type == "hexahedron":
        face_type = "quad"
        face_datas = hexahedrons_to_quads(cell_datas)
    elif cell_type == "tetra":
        face_type = "triangle"
        face_datas = tetra_to_triangle(cell_datas)
    else:
        face_type = "none"
        face_datas = np.array([])
    face = (face_type, np.array(face_datas))
    return face


def mesh_patches(file_name: str) -> List[Polygon]:
    """mesh_patches

     convert mesh to patches.

    Args:
       file_name: file name of mesh file

    Returns:
       patches: list of patch

    """
    patches = []
    mesh = meshio.read(file_name)
    points = mesh.points
    cells = mesh.cells
    for cell in cells:
        index = cell.data[0]
        polygon = plt.Polygon(
            (
                (points[index[0], 0], points[index[0], 1]),
                (points[index[1], 0], points[index[1], 1]),
                (points[index[2], 0], points[index[2], 1]),
                (points[index[3], 0], points[index[3], 1]),
            ),
            edgecolor="black",
            facecolor="gray",
        )
        patches.append(polygon)
    return patches


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
            face = cell_to_face(cell)
            faces.append(face)
        return faces
