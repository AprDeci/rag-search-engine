# Multimodal Search Implementation

Let's put it all together with a multimodal search function. It will generate embeddings for the text in our movie dataset, then allow us to provide an image to search for similar movies.

## Combining Multiple Modalities

With CLIP models, it's even possible to construct **hybrid queries** that combine text and images. We can do this by taking a _weighted average_ of a text embedding and an image embedding, then adjusting the weighting however we like.

```py
# User uploads an image AND types text
uploaded_image = Image.open("user_upload.jpg")
text_modifier = "but with bears"

# Encode both inputs
image_embedding = model.encode_image([uploaded_image])
text_embedding = model.encode_text([text_modifier])

# Combine embeddings (weighted average)
combined_query = (0.7 * image_embedding) + (0.3 * text_embedding)
```

We won't go this far in the current project, but with different modalities embedded in the same vector space, we can mix and match them in all sorts of ways.

## Assignment

**Implement image-based search** to find movies by uploading images instead of typing queries.

1. [ ] Update your library module to search text documents with image embeddings.
   1. [ ] The `MultimodalSearch` constructor should now also accept a list of documents. Assign it to an instance variable.
   2. [ ] For better search in our movie dataset, also create a `self.texts` list, which concatenates the title and description of each movie document in the following format:
      ```py
      f"{doc['title']}: {doc['description']}"
      ```
   3. [ ] Still in the constructor, generate `self.text_embeddings` by passing `self.texts` to the model's `encode` method. Remember that you can set `show_progress_bar=True`, in case encoding takes a while.
   4. [ ] Add a new class method, e.g. `search_with_image`, which accepts an image path.
      1. [ ] Generate an embedding for the provided image.
      2. [ ] Iterate over the text embeddings, calculating cosine similarity between each of them and the image embedding.
      3. [ ] Sort the results by similarity score, in descending order, and return the first 5. It will be convenient to return a list of dicts, each containing the document ID, title, description, and similarity score.
   5. [ ] Add a new top-level function to the library module, e.g. `image_search_command`, that accepts an image path.
      1. [ ] Load the movie dataset and use it to create an instance of `MultimodalSearch`.
      2. [ ] Call the `search_with_image` method (or whatever you named it), passing in the image path. Return the results.
2. [ ] Back in `cli/multimodal_search_cli.py`, import the new function from the library module, then add an `image_search` command. It should accept a required positional argument for the image path.
3. [ ] Have `image_search` call the relevant function and print the results in this format:

   ```text
   1. Paddington (similarity: 0.722)
      Deep in the rainforests of Peru, a young bear lives peacefully with his Aunt Lucy and Uncle Pastuzo,...

   2. Murder She Said (similarity: 0.686)
      This is based on the Agatha Christie book "4:50 from Paddington" and the opening locale is Paddingto...

   3. Ted (similarity: 0.685)
      In 1985, eight-year-old John Bennett makes a Christmas wish that his teddy bear, Ted, would come to ...
   ```

**Run and submit** the CLI tests.
