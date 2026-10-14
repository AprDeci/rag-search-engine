# Question Answering

The most common use case for RAG is **question answering**, which is only _slightly_ different from summarization.

Users ask questions, and we generate direct answers from the retrieved documents. Remember, traditional search returns **documents**. Users are then expected to poke through those documents to find answers on their own.

Question answering simplifies the whole process by just **returning the answer**.

**User query:** "What year was _The Revenant_ released?"

- **Search:** _List of movie documents..._
- **RAG (question answering):** "2015"

Different questions need different approaches:

- **Factual:** "When was _The Revenant_ released?" → Direct answer
- **Analytical:** "Which bear movies are most intense?" → Comparison required
- **Opinion:** "What's the best bear movie?" → Subjective reasoning

As such, you should write your system prompt so that the LLM has a sense of how to answer each type of question.

```py
prompt = f"""Answer the following question based on the provided documents.

Question: {query}

Documents:
{context}

General instructions:
- Answer directly and concisely
- Use only information from the documents
- If the answer isn't in the documents, say "I don't have enough information"
- Cite sources when possible

Guidance on types of questions:
- Factual questions: Provide a direct answer
- Analytical questions: Compare and contrast information from the documents
- Opinion-based questions: Acknowledge subjectivity and provide a balanced view

Answer:"""
```

You could even include examples of good responses to the different types of questions.

## Assignment

**Add a conversational question-answering command for direct responses.**

1. [ ] Add a new `question` command to the `cli/augmented_generation_cli.py` script. It should accept a required `question` positional argument and an optional `--limit` argument that defaults to `5`.
2. [ ] The `question` command should:
   1. [ ] Load the movie dataset, and use it to set up a `HybridSearch` instance.
   2. [ ] Perform an RRF search using the provided question.
   3. [ ] Prompt the LLM to answer the user's question based on the search results. Here's the prompt I used:

      ```py
      prompt = f"""Answer the user's question based on the provided movies that are available on Webflyx, a streaming service.

      Question: {question}

      Documents:
      {context}

      Instructions:
      - Answer questions directly and concisely
      - Be casual and conversational
      - Don't be cringe or hype-y
      - Talk like a normal person would in a chat conversation

      Answer:"""
      ```

3. [ ] Print the question and answer in this format:

   ```text
   Search Results:
     - Jurassic Park
     - Mike and Dave Need Wedding Dates
     - House II: The Second Story
     - The Last of the Finest
     - Tokyo Babiron

   Answer:
   <ANSWER HERE>
   ```

If question-answering seems to be working properly, **submit** the CLI tests.
