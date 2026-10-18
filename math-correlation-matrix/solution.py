
import numpy as np

from _load import load_solution

correlation = load_solution("math-expectation-variance-covariance").correlation


def correlation_matrix(x: np.ndarray) -> np.ndarray:
    """
    x is (num_samples, num_features). Returns a (num_features,
    num_features) matrix where entry [i, j] is the correlation
    (03-probability/03-covariance-correlation's `correlation`, already
    provided above) between feature column i and feature column j.

    The diagonal is always 1.0 (every feature correlates perfectly
    with itself), and the matrix is symmetric (corr(i, j) == corr(j, i)).
    """
    num_features= x.shape[1]
    corr_matrix = np.zeros((num_features, num_features))
    np.fill_diagonal(corr_matrix, 1.0)
    for i in range(num_features):
        for j in range(i+1, num_features):
            corr = np.corrcoef(x[:, i], x[:, j])[0, 1]
            corr_matrix[i, j] = corr
            corr_matrix[j, i] = corr
    return corr_matrix
    pass


def most_correlated_pair(corr_matrix: np.ndarray) -> tuple[int, int]:
    """
    Given a correlation matrix, returns the (row, col) index of the
    single most correlated pair of DIFFERENT features (excluding the
    diagonal, which is always a trivial 1.0), by absolute value (a
    strong NEGATIVE correlation counts too).
    """
    matrix = corr_matrix.copy()
    np.fill_diagonal(matrix, 0.0)

    i,j = np.unravel_index(np.argmax(np.abs(matrix)), matrix.shape)

    return (int(i), int(j))

    pass
