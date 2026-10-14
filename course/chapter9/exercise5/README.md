# F1 Score

Precision and recall often pull in opposite directions. So, how do you optimize for both simultaneously?

Enter the [**F1 score**](https://en.wikipedia.org/wiki/F-score) – a single metric that balances precision and recall when both are equally important.

F1 score is the [**harmonic mean**](https://en.wikipedia.org/wiki/Harmonic_mean) of precision and recall. It gives you one number that represents the overall performance of your search system.

```py
f1 = 2 * (precision * recall) / (precision + recall)
```

The "harmonic" mean is often better than a "regular" mean (average) because it punishes extreme disparities more:

| Precision | Recall | Mean | F1 Score |
| --------- | ------ | ---- | -------- |
| 100%      | 100%   | 100% | 100%     |
| 50%       | 50%    | 50%  | 50%      |
| 90%       | 30%    | 60%  | 45%      |
| 75%       | 25%    | 50%  | 37.5%    |
| 100%      | 0%     | 50%  | 0%       |

**F1 encourages you to improve both metrics!** A system that's great at precision but terrible at recall gets a lower F1 score. F1 is perfect when:

- Precision and recall are equally important
- You want a single metric to optimize
- You're comparing different systems

However, if one metric matters more than the other, consider [weighted F-scores](https://en.wikipedia.org/wiki/F-score#F%CE%B2_score) or just focus on the more important metric directly.

## Assignment

**Update the evaluation script to also print `F1` scores for each test case.**

1. [ ] Use the formula above to calculate the F1 score for each test case.
2. [ ] Print the results in this format:

   ```text
   k=4

   - Query: terrifying bear forest attack
     - Precision@4: 0.7500
     - Recall@4: 0.5000
     - F1 Score: 0.6000
     - Retrieved: Grizzly, Claws, Prophecy, Day of the Animals
     - Relevant: Grizzly, Bear, Into the Grizzly Maze, Claws, Unnatural, Day of the Animals

   - Query: true wildlife bear documentary
     - Precision@4: 0.2500
     - Recall@4: 0.5000
     - F1 Score: 0.3333
     - Retrieved: Grizzly Man, Grizzly, Prophecy, Ultime grida dalla savana
   ```

**Run and submit** the CLI tests.
