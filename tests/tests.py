import matplotlib.pyplot as plt
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
    mesh = mplt.mesh(points, cells)
    return True
