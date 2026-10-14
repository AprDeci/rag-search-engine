# LLM Evaluation

Manual evaluation is slow. Automated metrics miss nuance.

Can an LLM "manually" judge search quality... automatically? For example, can we use a prompt like this?

```py
prompt = f"""Rate how relevant each result is to this query:

Query: "{query}"
Results: {format_results(results)}

Rate each 0-3 where:
- 3: Highly relevant
- 2: Relevant
- 1: Marginally relevant
- 0: Not relevant"""
```

## Defining Success

It turns out, the LLM can produce reasonable scores, but what's even more helpful is that building this kind of system **forces you to define what "good" means**.

To create an LLM judge, you must:

- Define clear evaluation criteria
- Specify what makes a result relevant
- Articulate your quality standards

This clarity improves your entire evaluation system, even if you end up _not_ using the LLM.

## Domain Experts Are Critical

LLMs almost certainly don't understand your domain as well as human experts do. But human experts are slow and sometimes inconsistent.

The best practice? **Have the domain experts create the evaluation prompt and criteria.** Then have _them_ judge whether the LLM's scores are up to par.

## What's It Good For?

An LLM as a judge is not going to be as good as a human expert, so why use one?

- **Speed and scale:** You can evaluate much larger datasets faster. This means for critical tasks, you can use an LLM as a judge _in production_ to catch possible bad answers before they're provided to the user.
- **Cost:** While human experts are better and necessary, they can't look at every single result. LLMs can be helpful in finding problematic areas so that the human experts know where to focus.
- **Development:** It would be hard to develop a search system if you had to ask an expert if each change helped. In many domains, such as legal or medical, a carefully created LLM judge may be more accurate than a software engineer.

## Implementation Strategy

1. **Start with experts** – Define clear evaluation criteria
2. **Create detailed prompts** – Include domain knowledge
3. **Validate on samples** – Check that the LLM agrees with experts
4. **Use for scale** – Let the LLM handle bulk evaluation
5. **Spot-check results** – Have experts review surprising scores

## Assignment

1. [ ] Add an optional `--evaluate` flag (boolean) to your `rrf-search` command to rate the search results.
2. [ ] If the flag is provided, after running RRF and printing the results, use an LLM to evaluate the results. It should score them from 0-3, where:
   - 3: Highly relevant
   - 2: Relevant
   - 1: Marginally relevant
   - 0: Not relevant

   Here's the system prompt I used:

   ```py
   f"""Rate how relevant each result is to this query on a 0-3 scale:

   Query: "{query}"

   Results:
   {chr(10).join(formatted_results)}

   Scale:
   - 3: Highly relevant
   - 2: Relevant
   - 1: Marginally relevant
   - 0: Not relevant

   Do NOT give any numbers other than 0, 1, 2, or 3.

   Return ONLY the scores in the same order you were given the documents. Return a valid JSON list, nothing else. For example:

   [2, 0, 3, 2, 0, 1]"""
   ```

3. [ ] Parse the JSON response, and match up each score to the corresponding result.
4. [ ] Print a final evaluation report in **exactly** this format:
   ```text
   1. Bugs Bunny and the Three Bears: 2/3
   2. Care Bears Movie II: A New Generation: 2/3
   3. Swiss Army Man: 0/3
   4. Disaster Movie: 0/3
   ```

**Submit** the CLI tests.
