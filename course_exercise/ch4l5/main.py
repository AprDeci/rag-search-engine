def add_vectors(vec1: list[float], vec2: list[float]) -> list[float]:
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same length")
    result = [vec1[i] + vec2[i] for i in range(len(vec1))]
    return result


def subtract_vectors(vec1: list[float], vec2: list[float]) -> list[float]:
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same length")
    result = [vec1[i] - vec2[i] for i in range(len(vec1))]
    return result
