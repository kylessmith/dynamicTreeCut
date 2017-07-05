Python translation of the hybrid dynamicTreeCut method created by Peter Langfelder and Bin Zhang.

dynamicTreeCut was originally published by in *Bioinformatics*:
	Langfelder P, Zhang B, Horvath S (2007) Defining clusters from a hierarchical cluster tree:
	the Dynamic Tree Cut package for R. Bioinformatics 2008 24(5):719-720

dynamicTreeCut R code is distributed under the GPL-3 License and
original sources should be cited.


dynamicTreeCut contains methods for detection of clusters in hierarchical clustering dendrograms.
*NOTE: though the clusters match the R output, the cluster names are shuffled*

Installing
==========

To install, it's best to create an environment after installing and downloading the
`Anaconda Python Distribution <https://www.continuum.io/downloads>`__

    conda env create --file environment.yml

PyPI install, presuming you have all its requirements (numpy and scipy) installed::

	pip install dynamicTreeCut

	
Importation
===========
::

	>>> from dynamicTreeCut import cutreeHybrid
	>>> from scipy.spatial.distance import pdist
	>>> import numpy as np
	>>> from scipy.cluster.hierarchy import linkage
	>>> d = np.transpose(np.arange(1,10001).reshape(100,100))
	>>> distances = pdist(d, "euclidean")
	>>> link = linkage(distances, "average")
	>>> clusters = cutreeHybrid(link, distances)
	..cutHeight not given, setting it to 495.1  ===>  99% of the (truncated) height range in dendro.
	..done.
	>>> clusters["labels"]
	[2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3
 	 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 1 1 1 1 1 1 1 1 1 1
 	 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
	
	
Compared to R::

	> library(dynamicTreeCut)
	> d = matrix(1:10000, 100)
	> distances <- dist(d, method="euclidean")
	> dendro <- hclust(distances, method="average")
	> clusters <- cutreeDynamic(dendro, distM=as.matrix(distances))
	  ..cutHeight not given, setting it to 495  ===>  99% of the (truncated) height range in dendro.
	  ..done.
	> clusters
	  [1] 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3
 	  [38] 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 1 1 1 1 1 1 1 1 1 1
 	  [75] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

Installation
============

If you dont already have numpy and scipy installed, it is best to download
`Anaconda`, a python distribution that has them included.  

    https://continuum.io/downloads

Dependencies can be installed by::

    pip install -r requirements.txt


License
=======

dynamicTreeCut is available under the GPL-3 License
