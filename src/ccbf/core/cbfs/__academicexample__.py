import numpy as np
from .cbf import Cbf
from .symbolic_cbfs.nonlinear_1d_safety import (
    h1,
    dh1dx,
    d2h1dx2,
    h2,
    dh2dx,
    d2h2dx2,
)


def linear_class_k(k):
    def alpha(h):
        return k * h

    return alpha


# Define linear class k weights
k_default = 0.1

# Define cbf lists
cbfs_individual = [
    Cbf(h1, dh1dx, d2h1dx2, linear_class_k(k_default), h1),
    Cbf(h2, dh2dx, d2h2dx2, linear_class_k(k_default), h2),
]
cbfs_pairwise = []

cbf0 = np.zeros((len(cbfs_individual) + len(cbfs_pairwise),))
