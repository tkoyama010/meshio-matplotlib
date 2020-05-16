import numpy as np
from numpy.testing import assert_array_equal
import pytest

import meshioplt as mplt

# hexahedron

points1 = np.array(
    [
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 1.0],
        [0.0, 1.0, 1.0],
        [1.0, 1.0, 1.0],
        [2.0, 0.0, 0.0],
        [3.0, 0.0, 0.0],
        [2.0, 1.0, 0.0],
        [3.0, 1.0, 0.0],
        [2.0, 0.0, 1.0],
        [3.0, 0.0, 1.0],
        [2.0, 1.0, 1.0],
        [3.0, 1.0, 1.0],
    ]
)

cells1 = [
    ("hexahedron", np.array([[0, 1, 3, 2, 4, 5, 7, 6], [7, 8, 10, 9, 11, 12, 14, 13]]))
]

faces1 = [
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
                [7, 8, 10, 9],
                [12, 11, 13, 14],
                [11, 7, 9, 13],
                [8, 12, 14, 10],
                [11, 12, 8, 7],
                [9, 10, 14, 13],
            ]
        ),
    ),
]

# tetra

points2 = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

cells2 = [("tetra", np.array([[0, 1, 2, 3]]))]


faces2 = [
    ("triangle", np.array([[0, 1, 2], [1, 3, 2], [0, 2, 3], [0, 3, 1]])),
]


@pytest.mark.parametrize(
    "points, cells, faces", [(points1, cells1, faces1), (points2, cells2, faces2)]
)
def test_faces(points, cells, faces):
    mesh = mplt.Mesh(points, cells)
    actual = mesh.faces
    expected = faces
    assert expected[0][0] == actual[0][0]
    assert_array_equal(expected[0][1], actual[0][1])
