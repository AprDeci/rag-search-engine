# Recall Metrics

Precision measures the _quality_ of search results. Now let's look at **recall** – a metric that answers a different question.

**Precision asks:** "How much of what you found is relevant?"
**Recall asks:** "How much of what's relevant did you _find_?"

## Understanding Recall

Recall measures completeness. It tells you what percentage of all relevant documents you actually retrieved.

```py
recall = relevant_retrieved / total_relevant
```

Imagine searching for "family friendly bear movies":

- Your database contains **8 family-friendly bear movies** in total
- Your search returns only **5 movies**
- **4 of those 5** are actually family-friendly bear movies

Recall = 4 relevant retrieved / 8 total relevant = **50%**

You found half of the relevant movies, but missed the other half!

## Why Should We Care About Recall?

1. **Thoroughness:** Users expect to find what exists. Missing relevant content creates poor user experience.
2. **Pipeline performance:** In multi-stage systems, low recall in early stages is _fatal_. Your expensive re-ranker can't fix what was never retrieved.
3. **Critical applications:** Medical research, legal discovery, and safety systems need high recall – missing important information has consequences.

## The Precision-Recall Tradeoff

Higher recall often means lower precision. Retrieving more documents increases the chance of including irrelevant ones.

The key is finding the right balance for your use case. This is as much of a product question as it is a technical one.

## Assignment

**Update the evaluation script to also print `recall@k` scores for each test case.**

1. [ ] Use the formula above (the percentage of the documents from the golden dataset that show up in the search results) to calculate recall for each test case.
2. [ ] Print the results in this format:

   ```text
   k=10

   - Query: cute british bear marmalade
     - Precision@10: 0.1000
     - Recall@10: 1.0000
     - Retrieved: Paddington, The Duchess, The Bear, The Great Bear, Care Bears Movie II: A New Generation, Care Bears Nutcracker Suite, Bugs Bunny and the Three Bears, The Edge, An Unfinished Life, The Care Bears Adventure in Wonderland
     - Relevant: Paddington

   - Query: talking teddy bear comedy
     - Precision@10: 0.2000
     - Recall@10: 1.0000
     - Retrieved: Ted, Ted 2, The Bear, Littleman, Arsenic and Old Lace, Testament, Aqua Teen Hunger Force Colon Movie Film for Theaters, Stand by Me, Desierto, Memento
     - Relevant: Ted 2, Ted
   ```

**Run and submit** the CLI tests.
