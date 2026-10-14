# Dot Product Similarity

Let's learn our first method for measuring similarity between embeddings: the [dot product](https://en.wikipedia.org/wiki/Dot_product).

The dot product measures how much two vectors point in the same direction. It's calculated by multiplying corresponding elements and summing the results. Say we want the dot product of these two vectors:

- `[.8, .5, .5]`
- `[.5, .4, .6]`

First we multiply each pair of corresponding elements:

- `.8 × .5 = 0.4`
- `.5 × .4 = 0.2`
- `.5 × .6 = 0.3`

Then we sum those products:

- `0.4 + 0.2 + 0.3 = 0.9`

The final result is `0.9`. The more similar the vectors are, the _higher_ the dot product will be. If they point in opposite directions, the dot product will be negative.

## Assignment

Later we'll use [NumPy](https://numpy.org/) to handle vector math for us. But I want you to do it by hand at least once... _for the learnings_!

**Implement the `dot` function.** It takes two vectors (lists of floats) as input and returns their dot product (a single float).

1. [ ] If `vec1` and `vec2` are not the same length, raise a `ValueError` with a helpful message.
2. [ ] Iterate over the indices of the vectors, multiplying each pair of corresponding elements and adding the result to a running total.
3. [ ] Return the total.
