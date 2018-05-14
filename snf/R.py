# -*- coding: utf-8 -*-

from snf import compute, plotting, metrics

affinityMatrix = compute.affinity_matrix
calNMI = metrics.normalized_mutual_info_score
concordanceNetworkMNI = metrics.nmi
displayClustersWithHeatmap = plotting.mod_heatmap
dist2 = compute.dist2
estimateNumberOfClustersGivenGraph = compute.get_n_clusters
rankFeaturesByNMI = metrics.rank_feature_by_nmi
SNF = compute.SNF
spectralClustering = compute.spectral_clustering
standardNormalization = compute.scipy.stats.zscore
