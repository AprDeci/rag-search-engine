# Vector Operations

Vectors are lists of numbers that represent points in space. The interesting part is that _semantically similar words have vectors that are close together_. That means we need vector math to measure _how close_ two vectors are.

![vector explainer](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Vectors-1920x1080.mp4)

## Vector Addition

Vector addition is useful for **combining concepts**. For example: "I want a result that's like this _and_ like that."

With vector addition, we just add the corresponding elements of two vectors together.

```text
[0.5, -0.2,  0.8]
+
[0.1,  0.9, -0.3]
=
[0.6,  0.7,  0.5]
```

"The Great Bear" embeds to `[0.5, -0.2, 0.8]` (Animation, Adventure, Family). "Back Country" embeds to `[0.1, 0.9, -0.3]` (Horror, Thriller, Survival). Add them together and we get `[0.6, 0.7, 0.5]`, a _mix_ of those genres: Family, Adventure, and Horror.

## Vector Subtraction

Vector subtraction is useful for **removing concepts**. For example: "I want a result that's like this but _not_ that."

```text
[0.5, -0.2,  0.8]
-
[0.1,  0.9, -0.3]
=
[0.4, -1.1,  1.1]
```

"The Great Bear" embeds to `[0.5, -0.2, 0.8]` (Animation, Adventure, Family). If we subtract "The Revenant," which embeds to `[0.1, 0.9, -0.3]` (Horror, Thriller, Survival), we get `[0.4, -1.1, 1.1]`, representing Family Adventure but _not_ Horror or Survival.

## Assignment

**Implement the `add_vectors` and `subtract_vectors` functions.**

1. [ ] `add_vectors(vec1, vec2)` takes two vectors (lists of floats) and returns their _sum_ as a new vector.
   1. [ ] If the input vectors do _not_ have the same length, raise a `ValueError` with a helpful message.
   2. [ ] Iterate over the indices of both input vectors, and add the corresponding elements together.
   3. [ ] Return the resulting list of sums.
2. [ ] `subtract_vectors(vec1, vec2)` takes two vectors (lists of floats) and returns their _difference_ as a new vector.
   1. [ ] If the input vectors do _not_ have the same length, raise a `ValueError` with a helpful message.
   2. [ ] Iterate over the indices of both input vectors, and subtract the second vector's element from the first.
   3. [ ] Return the resulting list of differences.
