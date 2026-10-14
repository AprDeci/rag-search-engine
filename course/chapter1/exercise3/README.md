# Project Overview

We'll implement Webflyx as a collection of command line scripts that perform search operations on a local dataset of movies.

## Assignment

1. [ ] In your project's root, create a new `cli` directory. This is where we'll place the entrypoint scripts for our search implementations.
2. [ ] Delete the current `main.py` file – we won't need it.
3. [ ] In the `cli` directory, create a new file called `keyword_search_cli.py` and paste in the following code:

   ```py
   import argparse


   def main() -> None:
       parser = argparse.ArgumentParser(description="Keyword Search CLI")
       subparsers = parser.add_subparsers(dest="command", help="Available commands")

       search_parser = subparsers.add_parser("search", help="Search movies using keywords")
       search_parser.add_argument("query", type=str, help="Search query")

       args = parser.parse_args()

       match args.command:
           case "search":
               # print the search query here
               pass
           case _:
               parser.print_help()


   if __name__ == "__main__":
       main()
   ```

   This is just some boilerplate that uses the [`argparse`](https://docs.python.org/3/library/argparse.html) library to parse command line arguments.
   - `uv run cli/keyword_search_cli.py search "your search query"` will execute the "search" case and populate "your search query" into the `args.query` variable.
   - `uv run cli/keyword_search_cli.py` with no (or invalid) arguments will print the parser's help message.

   Notice that `main` is annotated with `-> None` because this CLI entrypoint doesn't return a value.

4. [ ] Update the "search" case to print the search query in this format:

   ```text
   Searching for: QUERY
   ```

   _Where `QUERY` is the value of `args.query`._

**Run and submit** the CLI tests.
