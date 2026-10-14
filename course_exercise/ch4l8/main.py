from lib import dot, euclidean_norm


def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    if len(vec1) != len(vec2):
        raise ValueError("vectors must be the same length")
    dot_product = dot(vec1, vec2)
    magnitude_1 = euclidean_norm(vec1)
    magnitude_2 = euclidean_norm(vec2)
    if magnitude_1 == 0.0 or magnitude_2 == 0.0:
        return 0.0
    norm_product = magnitude_1 * magnitude_2
    return dot_product / norm_product
