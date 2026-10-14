def dot(vec1: list[float], vec2: list[float]) -> float:
    if len(vec1) != len(vec2):
        raise ValueError("vectors must be the same length")
    total = 0.0
    for i in range(len(vec1)):
        total += vec1[i] * vec2[i]
    return total


def euclidean_norm(vec: list[float]) -> float:
    total = 0.0
    for x in vec:
        total += x**2

    return total**0.5
