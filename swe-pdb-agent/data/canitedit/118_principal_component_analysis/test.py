from solution import *
import math

def test_all():
    data = pd.DataFrame({
        'feature1': np.random.rand(100),
        'feature2': np.full(100, 1.0),
        'feature3': np.random.rand(100) * 0.01 + 1,
        'feature4': np.random.rand(100),
        'feature5': np.random.rand(100)
    })
    
    n_components = 2
    reducer = PCAFeatureReducer(data, n_components=n_components)
    principal_components = reducer.apply_pca()
    var_threshold = 0.01
    component_dot_products = np.dot(principal_components.T, principal_components)
    np.fill_diagonal(component_dot_products, 0)
    explained_variance_ratio = reducer.pca.explained_variance_ratio_
    
    assert principal_components.shape[1] == n_components
    assert not np.any(np.all(principal_components == 0, axis=0))
    assert np.all(np.var(principal_components, axis=0) > var_threshold)
    assert np.allclose(component_dot_products, 0, atol=1e-6)
    assert explained_variance_ratio.sum() >= 0.5