# Golden Dataset

Now that we've done a vibe-check, it's still important to have actual criteria for evaluating our search system – we want some kind of numerical score that we can work to improve over time.

And the foundation of any good evaluation is **curated test data**; we'll call it a "**golden dataset**." It should contain:

- **Queries:** Real user questions
- **Relevant documents:** Known correct answers

A single "golden dataset" is useful because it offers:

- **Consistent evaluation** across experiments
- **Automated testing** of search improvements
- **Baseline comparison** between different methods

## How Do I Create a Golden Dataset?

You need a domain expert!

- If you're building a movie database, you might need a movie critic or film studies expert.
- If you're building a legal case-study search engine, you need a lawyer or legal expert.
- If you're building a medical search engine, you need a doctor or medical professional.

The point is you need _someone_ who knows the data well enough to curate a set of "correct" matches for a set of plausible queries.

> [!isaac]
> In practice on commercial projects, your golden dataset will almost certainly NOT be perfect and you will never score 100% on your evaluations. If you see that, you should be incredibly suspicious. You most likely either have a bug in your evaluations, or your dataset is not representative of real-world usage.

## Assignment

Copy and paste the `golden_dataset.json` file from the bottom of this page into `data/golden_dataset.json` in your project.

**Run and submit** the CLI tests from the root of your project.

## Golden Dataset JSON

```json
{
  "test_cases": [
    {
      "query": "cute british bear marmalade",
      "relevant_docs": ["Paddington"]
    },
    {
      "query": "talking teddy bear comedy",
      "relevant_docs": ["Ted", "Ted 2"]
    },
    {
      "query": "children's animated bear adventure",
      "relevant_docs": [
        "Brother Bear",
        "The Jungle Book",
        "The Many Adventures of Winnie the Pooh",
        "Yogi Bear",
        "The Care Bears Movie",
        "Care Bears Movie II: A New Generation",
        "Care Bears Nutcracker Suite",
        "The Little Polar Bear",
        "The Little Polar Bear 2: The Mysterious Island",
        "Open Season",
        "The Country Bears",
        "The Berenstain Bears' Christmas Tree",
        "Winnie the Pooh"
      ]
    },
    {
      "query": "friendship transformation magic with bears",
      "relevant_docs": [
        "Brother Bear",
        "The Care Bears Movie",
        "The Jungle Book"
      ]
    },
    {
      "query": "dinosaur park",
      "relevant_docs": ["Jurassic Park"]
    },
    {
      "query": "wizards and magic",
      "relevant_docs": [
        "Harry Potter and the Sorcerer's Stone",
        "Harry Potter and the Prisoner of Azkaban",
        "Harry Potter and the Goblet of Fire",
        "Harry Potter and the Order of the Phoenix",
        "Harry Potter and the Deathly Hallows: Part 1",
        "Harry Potter and the Deathly Hallows: Part 2",
        "The Sword in the Stone",
        "Oz the Great and Powerful",
        "The Lord of the Rings: The Fellowship of the Ring"
      ]
    },
    {
      "query": "superhero saves the world",
      "relevant_docs": [
        "The Incredibles",
        "Superman II",
        "Superman/Batman: Public Enemies",
        "Justice League: The Flashpoint Paradox",
        "Up, Up, and Away!",
        "Megamind",
        "Kick-Ass",
        "Sky High"
      ]
    },
    {
      "query": "zombie apocalypse",
      "relevant_docs": [
        "Shaun of the Dead",
        "Dance of the Dead",
        "The Return of the Living Dead",
        "Pride and Prejudice and Zombies",
        "I Am Legend",
        "Resident Evil: Apocalypse",
        "Colin",
        "Død snø"
      ]
    },
    {
      "query": "car racing",
      "relevant_docs": [
        "The Fast and the Furious",
        "Rush",
        "Need for Speed",
        "Talladega Nights: The Ballad of Ricky Bobby",
        "The Love Bug",
        "Cars",
        "Furious Seven"
      ]
    },
    {
      "query": "romantic comedy wedding",
      "relevant_docs": [
        "Runaway Bride",
        "27 Dresses",
        "Just Go with It",
        "The Wedding Planner",
        "Wedding Crashers",
        "The Accidental Husband",
        "You, Me and Dupree"
      ]
    }
  ]
}
```
