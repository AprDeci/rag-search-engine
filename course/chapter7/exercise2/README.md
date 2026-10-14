# OpenRouter API Setup

For our purposes, we don't need to be super specific about which LLM we use. Any decent, modern model should work. What we want is:

- An API that we can easily call from Python code
- A model of sufficient quality for search query enhancement, with a generous enough free tier

We'll use [OpenRouter](https://openrouter.ai/), a single gateway that exposes hundreds of models - including a rotating selection of _free_ ones - behind an **OpenAI-compatible API**. That means we can use the official [`openai` Python SDK](https://github.com/openai/openai-python) to talk to it, a skill that transfers to nearly every other provider.

Instead of pinning one specific model, we'll use the special model ID `openrouter/free`, a [router](https://openrouter.ai/docs/guides/routing/routers/free-router) that automatically picks an available free model that supports the features our request needs.

> [!info]
> The free tier is rate-limited to roughly **50 requests per day** (20 per minute). That's plenty for this course if you're a little patient. If you'd like a smoother experience, adding **$10 of credit** to your OpenRouter account (a one-time top-up) raises the limit to roughly **1,000 requests per day**. The free tier still costs nothing - the $10 is purely for convenience.

So let's get set up with an OpenRouter API key and verify that it works by writing a small test script. High-level steps:

1. Get a key to access OpenRouter.
2. Create a `.env` file to store the API key, which should be kept secret.
3. Use the [`dotenv` library](https://saurabh-kumar.com/python-dotenv/) in your Python code to load the environment variable.
4. Use the [`openai` library](https://github.com/openai/openai-python) (pointed at OpenRouter) to make API requests.

## Assignment

1. [ ] Create an account on [OpenRouter](https://openrouter.ai/) if you don't already have one.
2. [ ] Go to the [Keys page](https://openrouter.ai/keys) and click "Create Key".

   > [!tip]
   > While creating the key you can set a **credit limit** on it (e.g. `$1`) to cap how much it could ever spend. On the pure free tier it can't spend anything anyway, but it's a good habit.

3. [ ] Copy the API key, then paste it into a new `.env` file in your project directory. The file should look like this:

   ```sh
   OPENROUTER_API_KEY="your_api_key_here"
   ```

4. [ ] Add the `.env` file to your `.gitignore`!

   > [!danger]
   > We never want to commit API keys, passwords, or other sensitive information to Git.

5. [ ] Add `python-dotenv` and `openai` as dependencies:

   ```sh
   uv add python-dotenv==1.1.0
   uv add openai==2.44.0
   ```

6. [ ] Create a `test_llm.py` file. Load the environment variables from the `.env` file using the `dotenv` library and read the API key:

   ```py
   import os
   from dotenv import load_dotenv

   load_dotenv()
   api_key = os.environ.get("OPENROUTER_API_KEY")
   if not api_key:
       raise RuntimeError("OPENROUTER_API_KEY environment variable not set")
   ```

7. [ ] Import the `OpenAI` class and create a client pointed at OpenRouter:

   ```py
   from openai import OpenAI

   client = OpenAI(
       base_url="https://openrouter.ai/api/v1",
       api_key=api_key,
   )
   ```

8. [ ] Use the [`client.chat.completions.create()` method](https://platform.openai.com/docs/api-reference/chat/create) to get a response from the model. You'll need two _named_ parameters:
   - `model`: the model ID, `openrouter/free`
   - `messages`: a list with a single user message. For now, hardcode the prompt:

     ```py
     messages = [
         {
             "role": "user",
             "content": "Why is Boot.dev such a great place to learn about RAG? Use one paragraph maximum.",
         }
     ]
     ```

   The method returns a [chat completion object](<https://developers.openai.com/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)>). Print `response.choices[0].message.content` to see the model's answer.

   If everything is working as intended, you should be able to run your script and see the model's response in your terminal!

9. [ ] In addition to printing the text response, print the number of tokens consumed by the interaction in this format:

   ```text
   Prompt tokens: X
   Response tokens: Y
   ```

   The response has a [`.usage`](<https://developers.openai.com/api/reference/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)%20%3E%20(property)%20usage>) property that has both:
   - a `prompt_tokens` property (tokens in the prompt)
   - a `completion_tokens` property (tokens in the response)

> [!info]
> OpenRouter is an external web service, and it may rate limit your project (especially on the free tier). On lessons like this one, failed submissions won't penalize you, so it's safe to retry if something goes wrong on the provider's end.
>
> Not every lesson in this course is no-penalty, so read the instructions carefully and follow the submit flow each lesson asks for.

**Submit** the CLI tests.
