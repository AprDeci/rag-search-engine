# What Is Search?

![what is search](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/what-is-search-1920x1080.mp4)

Imagine if you had to scroll through every single movie on Netflix to find the movie you're looking for.

**Search is a non-negotiable feature** of nearly all content-based web applications. In this course, we'll learn how it works, then focus on using AI, LLMs, and search together for an **even better** user experience. Good search is about much more than exact keyword matches. We want to be able to:

- Find relevant results even if the search terms don't match exactly
- Match based on semantic meaning, not just keywords
- Understand user intent and context
- Provide succinct results that go beyond the raw data

To do that, we'll learn about **RAG**, or "Retrieval Augmented Generation." "Retrieval" is the first component in RAG:

- **R:** **R**etrieve information via a search algorithm
- **A:** **A**ugment our instructions with the search results
- **G:** **G**enerate better, richer, and more accurate information using LLMs

![RAG](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/DZl22fo-1280x323.jpeg)

## What Will We Build?

We're going to build pieces of a make-believe product called **Webflyx**, a Netflix-like streaming service. Specifically, we'll build the technologies that _power its search bar_.

## Assignment

Webflyx needs movie data to search through. Let's **download the dataset** we'll use throughout this course.

1. [ ] Use `uv` ([installation docs](https://docs.astral.sh/uv/getting-started/installation/)) to create a new project. It will create the directory and initialize a Git repo. In our example code, we've named the project directory `rag-search-engine`, since it's only one part of the Webflyx product.
   ```sh
   uv init --no-package rag-search-engine
   cd rag-search-engine
   ```
2. [ ] Create a virtual environment at the top level of your project directory:
   ```sh
   uv venv
   ```
   > [!info]
   > Make sure the `venv` directory is in your `.gitignore` file. `uv init` usually adds it for you.
3. [ ] Activate the virtual environment:

   ```sh
   source .venv/bin/activate
   ```

   You should see `(rag-search-engine)` at the beginning of your terminal prompt; for example, mine is:

   ```text
   (rag-search-engine) wagslane@MacBook-Pro-2 rag-search-engine %
   ```

   > [!warning]
   > Always make sure that your virtual environment is _activated_ when running the code or using the Boot.dev CLI in this course.

4. [ ] Create a `data` directory in your project root.
5. [ ] Download the [movie dataset here](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/course-rag-movies.json) and save it as `data/movies.json`.
6. [ ] Add `/data/` to your `.gitignore` file to keep large data files out of version control.

**Run and submit** the CLI tests.
