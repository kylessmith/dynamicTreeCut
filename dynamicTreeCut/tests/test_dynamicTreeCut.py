from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist
import numpy as np


def test_cuttreeHybrid():
    from dynamicTreeCut import cutreeHybrid
    d = np.transpose(np.arange(1, 10001).reshape(100, 100))
    distances = pdist(d, "euclidean")
    link = linkage(distances, "average")
    test = cutreeHybrid(link, distances)

    true = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1]
    
    assert (test['labels'] == true).all()
    assert False
