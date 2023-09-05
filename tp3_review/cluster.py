# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:20:07 2020

@author: pablonicolasr
"""

from sklearn.cluster import DBSCAN

def cluster_ip(X, min_samples, metric="cosine"):
    cluster = DBSCAN(
        eps=0.0111,
        min_samples=min_samples,
        metric=metric,
        algorithm="brute"
    )

    cluster.fit_predict(X)

    return cluster
