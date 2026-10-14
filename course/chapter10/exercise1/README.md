# Augmented Generation

So far, we've been solely focused on **retrieving** information. Now we'll explore **generating** results _based on_ the retrieved information.

[Retrieval-Augmented Generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG) combines search with LLM generation. Instead of asking an LLM to generate answers from its training data alone, we:

1. **Retrieve** relevant documents using search
2. **Augment** the LLM's context with those documents
3. **Generate** responses based on the retrieved information

This gives us (in principle) the best of both worlds:

- **Accurate** information from our search
- **Natural** language responses from LLMs

![Document Retrieval](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/oiCQu6G-593x421.png)

## The RAG Pipeline

1. The user enters a query.
2. The search system retrieves relevant documents.
3. The LLM processes the query and retrieved documents.
   - Summarizes information
   - Answers questions
4. The generated response is returned to the user.

## Assignment

**Implement a RAG pipeline that combines search results with LLM output to produce context-aware answers.**

1. [ ] Create a new CLI script at `cli/augmented_generation_cli.py`. Here's some boilerplate for you to start with:

   ```py
   import argparse


   def main() -> None:
       parser = argparse.ArgumentParser(description="Retrieval Augmented Generation CLI")
       subparsers = parser.add_subparsers(dest="command", help="Available commands")

       rag_parser = subparsers.add_parser(
           "rag", help="Perform RAG (search + generate answer)"
       )
       rag_parser.add_argument("query", type=str, help="Search query for RAG")

       args = parser.parse_args()

       match args.command:
           case "rag":
               query = args.query
               # do RAG stuff here
           case _:
               parser.print_help()


   if __name__ == "__main__":
       main()
   ```

2. [ ] The `rag` command should:
   1. [ ] Load the movies and perform an RRF search using the provided query. Search for the top 5 results.
   2. [ ] Prompt the LLM with the query, the search results, and instructions for the LLM to generate an answer based on the retrieved documents. Here's the prompt I used:

      ```py
      prompt = f"""You are a RAG agent for Webflyx, a movie streaming service.
      Your task is to provide a natural-language answer to the user's query based on documents retrieved during search.
      Provide a comprehensive answer that addresses the user's query.

      Query: {query}

      Documents:
      {docs}

      Answer:"""
      ```

3. [ ] Print the results and the generated answer in this format:

   ```text
   Search Results:
   - We're Back! A Dinosaur's Story
   - Jurassic Park
   - The Lost World
   - Carnosaur
   - A Sound of Thunder

   RAG Response:
   <RESPONSE HERE>
   ```

If everything seems to be working, **submit** the CLI tests.
