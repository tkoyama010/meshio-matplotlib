import meshio
import numpy as np
from numpy.testing import assert_array_equal

import meshioplt as mplt


def test_hexahedron():
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
    cells = [
        (
            "hexahedron",
            np.array([[0, 1, 3, 2, 4, 5, 7, 6], [7, 8, 10, 9, 11, 12, 14, 13]]),
        )
    ]
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
    assert expected[0][0] == actual[0][0]
    assert_array_equal(expected[0][1], actual[0][1])


def test_tetra():
    points = np.array(
        [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0],]
    )
    cells = [("tetra", np.array([[0, 1, 2, 3]]))]
    mesh = mplt.Mesh(points, cells)
    actual = mesh.faces
    expected = [
        ("triangle", np.array([[0, 1, 2], [1, 3, 2], [0, 2, 3], [0, 3, 1]])),
    ]
    assert expected[0][0] == actual[0][0]
    assert_array_equal(expected[0][1], actual[0][1])


def test_collection():
    assert False
