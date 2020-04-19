import meshio
import numpy as np
from numpy.testing import assert_array_equal

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
        (
            "quad",
            np.array(
                [
                    [0, 1, 3, 2],
                    [5, 4, 6, 7],
                    [4, 0, 2, 6],
                    [1, 5, 7, 3],
                    [4, 5, 1, 0],
                    [2, 3, 7, 6],
                ]
            ),
        )
    ]
    assert expected[0][0] == actual[0][0]
    assert_array_equal(expected[0][1], actual[0][1])
