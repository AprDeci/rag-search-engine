from math import isclose

import pytest
from main import dot

run_cases = [
    pytest.param([1, 2, 3], [1, 2, 3], 14.0),  # identical vectors
    pytest.param([1, 0, 0], [0, 1, 0], 0.0),  # orthogonal
    pytest.param([1, -2, 3], [-1, 2, -3], -14.0),  # opposite direction
    pytest.param([1, 2], [10, 20], 50.0),  # k * b scales the dot
    pytest.param([1, -1, 0], [1, 1, 0], 0.0),  # Mixed signs / cancels to zero
    pytest.param([0.5, 0.25], [0.2, 0.4], 0.2),  # Fractions / decimals
    pytest.param([1e9, 2e9], [3e9, -4e9], -5e18),  # Large magnitudes
    pytest.param([1, 2, 3], [1, 2], "exception"),  # Error: length mismatch
]

submit_cases = [
    # Very small magnitudes
    pytest.param([1e-9, 2e-9], [3e-9, 4e-9], 1.1e-17, marks=pytest.mark.submit),
    # Empty vectors (valid, length match)
    pytest.param([], [], 0.0, marks=pytest.mark.submit),
    # Single-element vectors
    pytest.param([-7.0], [5.0], -35.0, marks=pytest.mark.submit),
    # Typical mixed integers
    pytest.param([2, 3, 4], [5, 6, 7], 56.0, marks=pytest.mark.submit),
    # All zeros
    pytest.param(
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
        0.0,
        marks=pytest.mark.submit,
    ),
    # Longer vector
    pytest.param(
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        35.0,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("vec1", "vec2", "expected"), run_cases + submit_cases)
def test_dot_product(vec1, vec2, expected):
    print("\n---------------------------------")
    print(f"Vector 1: {vec1}")
    print(f"Vector 2: {vec2}")
    print(
        f"\nExpected result: {expected:.2f}"
        if isinstance(expected, float)
        else f"\nExpected result: {expected}"
    )

    try:
        result = dot(vec1, vec2)
    except ValueError:
        result = "exception"

    print(
        f"Actual result:   {result:.2f}"
        if isinstance(result, (int, float))
        else f"Actual result:   {result}"
    )
    if isinstance(expected, float):
        assert isinstance(result, (int, float))
        assert isclose(result, expected)
    else:
        assert result == expected
