# Cosine Similarity

Dot product has a problem: it's affected by vector magnitude. Vectors have both direction _and_ magnitude (size). Direction is the important part for semantic similarity, but length can affect vector operations. For example, these two vectors have identical direction but different magnitudes:

![vector magnitudes](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/Yl4A6s7-760x605.png)

In semantic search, we usually _don't care_ about vector magnitude, just direction. Magnitude can represent "confidence" or "strength." For example, say we search for "positive Paddington reviews." We probably want both of these in the results set:

- "Paddington is good" (lower magnitude)
- "Paddington is SO AMAZING" (higher magnitude)

**[Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) solves this** by measuring the _angle_ between vectors, ignoring their length. For example, the dot product of these two vectors:

- `[0.6, 0.8]` (magnitude = `1.0`)
- `[3.0, 4.0]` (magnitude = `5.0`)

is `5.0`.

The vectors point in exactly the **same direction** (same type of movie), but the dot product is heavily influenced by magnitude. _For our purposes, we want to ignore magnitude and focus on direction._

**Cosine similarity measures the cosine of the angle** between two vectors, meaning it only cares about their direction. This value conventionally ranges from `-1.0` to `1.0`:

- **`1.0`:** Vectors point in exactly the same direction (perfectly similar)
- **`0.0`:** Vectors are perpendicular (no similarity)
- **`-1.0`:** Vectors point in opposite directions (perfectly dissimilar)

![cosine similarity](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/o4lJdJO-1020x742.png)

The formula is as follows:

```py
cosine_similarity = dot_product(A, B) / (magnitude(A) * magnitude(B))
```

And it works in two steps:

1. **Calculate similarity:** The dot product measures how much vectors align.
2. **Remove length bias:** Dividing by magnitudes removes the effect of vector size.

## Assignment

**Complete the `cosine_similarity` function.**

1. [ ] If the input vectors are not the same length, raise a `ValueError`.
2. [ ] Calculate the dot product of the vectors using the `dot` function provided for you.
3. [ ] Calculate the magnitude of each vector by using the provided `euclidean_norm` function.
   > [!tip]
   > If you're curious, `euclidean_norm` just adds the _squares_ of all the numbers in a vector, then takes the _square root_ of that sum. This should be reminiscent of the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem).
4. [ ] If either magnitude is `0`, return `0.0`; this guards against dividing by zero later.
5. [ ] Return the `dot_product` divided by the _product_ (multiplication) of the two magnitudes.
