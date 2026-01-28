from solution import *
import math

def test_all():
    x_0_blob_0 = (0, 0)
    x_1_blob_0 = (0, 0.1)
    x_2_blob_0 = (0.1, 0)
    x_3_blob_0 = (0.2, -0.1)
    x_0_blob_1 = (2, 2)
    x_1_blob_1 = (2, 2.1)
    x_2_blob_1 = (2.1, 2)
    x_3_blob_1 = (2.2, 2.1)
    x_0_blob_2 = (0, 2)
    x_1_blob_2 = (0, 2.1)
    x_2_blob_2 = (0.1, 2)
    x_3_blob_2 = (0.2, 2.1)
    x_0_blob_3 = (2, 0) 
    x_1_blob_3 = (2, 0.1)
    x_2_blob_3 = (2.1, 0)
    x_3_blob_3 = (2.2, 0.1)
    x_outlier_0 = (10, 10)
    x_outlier_1 = (-10, -10)
    x_outlier_2 = (10, -10)
        
    clustering = DBSCAN(eps=0.5, min_samples=3)
    data = [x_0_blob_0, x_1_blob_0, x_2_blob_0, x_3_blob_0,
                                x_0_blob_1, x_1_blob_1, x_2_blob_1, x_3_blob_1,
                                x_0_blob_2, x_1_blob_2, x_2_blob_2, x_3_blob_2,
                                x_0_blob_3, x_1_blob_3, x_2_blob_3, x_3_blob_3,
                                x_outlier_0, x_outlier_1, x_outlier_2]
    X = np.array(data)
    clustering.fit(X)
    assert len(set(clustering.labels_)) - (1 if -1 in clustering.labels_ else 0) == 4, f"Expected 4 clusters, got {len(set(clustering.labels_)) - (1 if -1 in clustering.labels_ else 0)}."
    assert clustering.labels_[0] == 0
    assert clustering.labels_[1] == 0
    assert clustering.labels_[2] == 0
    assert clustering.labels_[3] == 0
    assert clustering.labels_[4] == 1
    assert clustering.labels_[5] == 1
    assert clustering.labels_[6] == 1
    assert clustering.labels_[7] == 1
    assert clustering.labels_[8] == 2
    assert clustering.labels_[9] == 2
    assert clustering.labels_[10] == 2
    assert clustering.labels_[11] == 2
    assert clustering.labels_[12] == 3
    assert clustering.labels_[13] == 3
    assert clustering.labels_[14] == 3
    assert clustering.labels_[15] == 3
    assert clustering.labels_[16] == -1
    assert clustering.labels_[17] == -1
    assert clustering.labels_[18] == -1