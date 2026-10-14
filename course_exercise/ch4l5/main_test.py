import pytest
from main import add_vectors, subtract_vectors

run_cases = [
    pytest.param([1, 2, 3], [4, 5, 6], "add", [5, 7, 9]),
    pytest.param([4, 5, 6], [1, 2, 3], "subtract", [3, 3, 3]),
    pytest.param([1, -2, 3], [-4, 5, -6], "add", [-3, 3, -3]),
    pytest.param([1, -2, 3], [-4, 5, -6], "subtract", [5, -7, 9]),
]

submit_cases = [
    pytest.param(
        [0.5, 0.25],
        [0.25, 0.75],
        "add",
        [0.75, 1.0],
        marks=pytest.mark.submit,
    ),
    pytest.param([1], [1, 2], "subtract", "exception", marks=pytest.mark.submit),
    pytest.param([], [], "subtract", [], marks=pytest.mark.submit),
    pytest.param(
        [1, 0, -1, 2, -2],
        [2, -2, 1, -1, 0],
        "add",
        [3, -2, 0, 1, -2],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [1, 0, -1, 2, -2],
        [2, -2, 1, -1, 0],
        "subtract",
        [-1, 2, -2, 3, -2],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("vec1", "vec2", "op", "expected"), run_cases + submit_cases)
def test_vector_operation(vec1, vec2, op, expected):
    print("\n---------------------------------")
    print(f"Vector 1:  {vec1}")
    print(f"Vector 2:  {vec2}")
    print(f"Operation: {op}")
    print(f"\nExpected result: {expected}")

    try:
        result = (
            add_vectors(vec1, vec2) if op == "add" else subtract_vectors(vec1, vec2)
        )
    except ValueError:
        result = "exception"

    print(f"Actual result:   {result}")
    assert result == expected
