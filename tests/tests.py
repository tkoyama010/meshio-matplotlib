import meshio
import numpy as np

import meshioplt as mplt


def test():
    points = np.array(
        [
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [1.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0],
        ]
    )
    cells = [("hexahedron", np.array([[0, 1, 3, 2, 4, 5, 7, 6]]))]
    mesh = mplt.Mesh(points, cells)
    actual = mesh.faces
    expected = [
        meshio.CellBlock("quad", np.array([0, 1, 2, 3])),
        meshio.CellBlock("quad", np.array([5, 4, 7, 6])),
        meshio.CellBlock("quad", np.array([4, 0, 6, 2])),
        meshio.CellBlock("quad", np.array([1, 5, 3, 7])),
        meshio.CellBlock("quad", np.array([4, 5, 0, 1])),
        meshio.CellBlock("quad", np.array([2, 3, 6, 7])),
    ]
    assert expected == actual
