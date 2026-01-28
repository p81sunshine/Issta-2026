from solution import *
import math

def test_all():
    x_0_blob_0 = (0, 0)
    x_1_blob_0 = (0, 0.1)
    x_2_blob_0 = (0.1, 0)
    x_3_blob_0 = (0.2, -0.1)
    x_4_blob_0 = (0.1, 0.1)
    x_5_blob_0 = (0.2, 0)
    x_6_blob_0 = (0, 0.01)
    x_7_blob_0 = (0.01, 0)
    x_8_blob_0 = (0.1, 0.01)
    x_9_blob_1 = (2, 2)
    x_10_blob_1 = (2, 2.1)
    x_11_blob_1 = (2.1, 2)
    x_12_blob_1 = (2.2, 2.1)
    x_13_blob_1 = (2.1, 2.1)
    x_14_blob_1 = (2.2, 2)
    x_15_blob_1 = (2, 2.01)
    x_16_blob_1 = (2.01, 2)
    x_17_blob_1 = (2.1, 2.01)
    x_18_blob_2 = (0, 2)
    x_19_blob_2 = (0, 2.1)
    x_20_blob_2 = (0.1, 2)
    x_21_blob_2 = (0.2, 2.1)
    x_22_blob_2 = (0.1, 2.1)
    x_23_blob_2 = (0.2, 2)
    x_24_blob_2 = (0, 2.01)
    x_25_blob_2 = (0.01, 2)
    x_26_blob_2 = (0.1, 2.01)
    x_27_blob_3 = (2, 0)
    x_28_blob_3 = (2, 0.1)
    x_29_blob_3 = (2.1, 0)
    x_30_blob_3 = (2.2, 0.1)
    x_31_blob_3 = (2.1, 0.1)
    x_32_blob_3 = (2.2, 0)
    x_33_blob_3 = (2, 0.01)
    x_34_blob_3 = (2.01, 0)
    x_35_blob_3 = (2.1, 0.01)
    x_outlier_0 = (10, 10)
    x_outlier_1 = (-10, -10)
    x_outlier_2 = (10, -10)

    data = [x_0_blob_0, x_1_blob_0, x_2_blob_0, x_3_blob_0, x_4_blob_0, x_5_blob_0, x_6_blob_0, x_7_blob_0, x_8_blob_0,
            x_9_blob_1, x_10_blob_1, x_11_blob_1, x_12_blob_1, x_13_blob_1, x_14_blob_1, x_15_blob_1, x_16_blob_1, x_17_blob_1,
            x_18_blob_2, x_19_blob_2, x_20_blob_2, x_21_blob_2, x_22_blob_2, x_23_blob_2, x_24_blob_2, x_25_blob_2, x_26_blob_2,
            x_27_blob_3, x_28_blob_3, x_29_blob_3, x_30_blob_3, x_31_blob_3, x_32_blob_3, x_33_blob_3, x_34_blob_3, x_35_blob_3,
            x_outlier_0, x_outlier_1, x_outlier_2]
    X = np.array(data)
    gmm = GMM(n_components=4, n_iter=100)
    gmm.fit(X)

    labels = gmm.predict(X)

    assert len(set(labels)) == 4, f"Expected 4 clusters, got {len(set(labels))}."
    seen_labels = set()
    label_0 = set(labels[:9])
    assert len(label_0) == 1
    assert label_0.pop() not in seen_labels
    seen_labels.update(label_0)
    label_1 = set(labels[9:18])
    assert len(label_1) == 1
    assert label_1.pop() not in seen_labels
    seen_labels.update(label_1)
    label_2 = set(labels[18:27])
    assert len(label_2) == 1
    assert label_2.pop() not in seen_labels
    seen_labels.update(label_2)
    label_3 = set(labels[24:32])
    assert len(label_3) == 1
    assert label_3.pop() not in seen_labels
    seen_labels.update(label_3)