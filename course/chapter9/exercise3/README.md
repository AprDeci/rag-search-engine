# Precision Metrics

Okay, so your search system can return 100 movies about "bears," but how many are **actually relevant**?

That's what _precision_ measures. It's a simple formula:

```py
precision = relevant_retrieved / total_retrieved
```

If you return 10 movies but only 7 are relevant, your precision is:

```text
7/10 = 0.7 = 70%
```

**Higher precision = less junk in the results.**

## Precision@K

["Precision@K" or "P@K"](<https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Precision_at_k>) is a common metric that measures precision for the top `K` results returned by a search system. Users only look at the top `K` results, so we just focus on those.

## Assignment

1. [ ] Create a new `cli/evaluation_cli.py` script. This one won't have separate "commands" like most of our other scripts; it'll just take a single `--limit` flag to specify the value of `K` (defaulting to `5`). Here's some boilerplate:

   ```py
   import argparse


   def main() -> None:
       parser = argparse.ArgumentParser(description="Search Evaluation CLI")
       parser.add_argument(
           "--limit",
           type=int,
           default=5,
           help="Number of results to evaluate (k for precision@k, recall@k)",
       )

       args = parser.parse_args()
       limit = args.limit

       # run evaluation logic here


   if __name__ == "__main__":
       main()
   ```

2. [ ] Load the `golden_dataset.json` file using the [`json.load`](https://docs.python.org/3/library/json.html#json.load) function.
3. [ ] For each test case in the golden dataset, run RRF search. _RRF's `k` parameter should be `60`, and the "top k" (number of results) should be the value of the `--limit` flag... Sorry about all the Ks; it's a bit confusing._
4. [ ] Based on the formula above (the percentage of titles in the results that are found in the golden dataset), calculate the precision for each test case.
5. [ ] Print the results in this format:

   ```text
   k=6

   - Query: dangerous bear wilderness survival
     - Precision@6: 1.0000
     - Retrieved: The Edge, Man in the Wilderness, Claws, Unnatural, Into the Grizzly Maze, Alaska
     - Relevant: Unnatural, Alaska, The Edge, Into the Grizzly Maze, Claws, Man in the Wilderness, The Revenant

   - Query: cute british bear marmalade
     - Precision@6: 0.1667
     - Retrieved: Paddington, The Indian in the Cupboard, The Duchess, The Great Bear, The Bear, Goldilocks and the Three Bears
     - Relevant: Paddington
   ```

**Run and submit** the CLI tests.
