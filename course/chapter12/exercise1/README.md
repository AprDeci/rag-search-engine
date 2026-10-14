# Multimodal Search

Search has a problem: **users don't always ask with text**. Instead of typing, "What should I do if my leg is turning purple?" they want to ask, "What should I do?" and _upload a photo_ of their purple leg.

Some LLMs are _multimodal_: they can understand both text _and_ images, which opens up new search possibilities. One way to handle non-text input in RAG is **multimodal query rewriting**. It's as easy as it sounds: we ask the LLM to do the rewrite.

> Analyze this image and rewrite the text query for better search results.
>
> Image: [Uploaded image]
>
> Text Query: "{text_query}"
>
> Instructions:
>
> - Describe what you see in the image
> - Combine visual and textual information
> - Generate searchable keywords
> - Focus on movie-specific details (actors, scenes, style)

## Assignment

**Implement multimodal query rewriting** using a multimodal model on OpenRouter to convert an image and a text query into a better searchable query.

1. [ ] You'll need an image. Download [this JPEG](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/0LmrJI7-194x260.jpeg) and save it to `data/paddington.jpeg`.
2. [ ] Create a new script file named `describe_image_cli.py` in your `cli` directory.
3. [ ] The script should take two required _named_ arguments:
   - [ ] `--image` – the path to an image file
   - [ ] `--query` – a text query to rewrite based on the image
4. [ ] Use [`mimetypes.guess_type`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type) to determine the [MIME type](https://en.wikipedia.org/wiki/Media_type) of the image file, defaulting to `"image/jpeg"`:
   ```py
   mime, _ = mimetypes.guess_type(args.image)
   mime = mime or "image/jpeg"
   ```
5. [ ] [`open`](https://docs.python.org/3/library/functions.html#open) the image file in binary mode (`"rb"`), then [`read`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) its contents.
6. [ ] Set up an OpenAI client pointed at OpenRouter (`OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)`) using your API key.
7. [ ] Write your system prompt to describe the task of analyzing the image and rewriting the query. Here's the one I used:
   ```text
   Given the included image and text query, rewrite the text query to improve search results from a movie database. Make sure to:
   - Synthesize visual and textual information
   - Focus on movie-specific details (actors, scenes, style, etc.)
   - Return only the rewritten query, without any additional commentary
   ```
8. [ ] OpenRouter accepts images as base64-encoded [data URLs](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data). Encode the image, then build a `messages` list with a single user message whose `content` is a _list_ of parts - your instructions, the image, and the text query:

   ```py
   import base64

   data_url = f"data:{mime};base64,{base64.b64encode(img).decode()}"
   messages = [
       {
           "role": "user",
           "content": [
               {"type": "text", "text": system_prompt.strip()},
               {"type": "image_url", "image_url": {"url": data_url}},
               {"type": "text", "text": args.query.strip()},
           ],
       }
   ]
   ```

9. [ ] Send the request using [`client.chat.completions.create`](https://platform.openai.com/docs/api-reference/chat/create), passing `model="openrouter/free"` and your `messages`.
10. [ ] Print the rewritten query and the total number of tokens used, in the following format:
    ```py
    content = response.choices[0].message.content
    print(f"Rewritten query: {content.strip()}")
    if response.usage is not None:
        print(f"Total tokens:    {response.usage.total_tokens}")
    ```

If everything seems to be working, **submit** the CLI tests.
