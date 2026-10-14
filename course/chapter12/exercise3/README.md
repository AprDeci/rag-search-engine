# Image Embeddings

Now it's time to start building multimodal search for our movie dataset. Ultimately, we want to provide an _image_ and search our _text_ database for movies that are semantically close to that image.

The first step is to choose a model that can generate comparable embeddings for text and images, then scaffold the code for multimodal search.

## CLIP

One family of models that's well suited to connecting images and text is [CLIP](https://openai.com/index/clip/) (Contrastive Language-Image Pretraining). OpenAI trained CLIP on a huge dataset of image-caption pairs collected from the internet.

The result is a model that can retrieve images from text queries, or retrieve text from image queries. Embeddings for both data types are created in the same vector space.

CLIP will work nicely for our purposes. There are also versions of the model that can be run locally, offering privacy, convenience, and other advantages.

## Local Model Limitations

Local models are a great way to experiment, learn, and develop, but they come with size and capability constraints.

For reference, large frontier LLMs can require _hundreds of GB_ of memory to run. Most laptops can't handle something that large, but public APIs for the major LLMs are widely accessible. In this course, we use OpenRouter's free model router for hosted LLM calls so you can complete the work without paying for a provider account.

Multimodal embedding models have the same tradeoff between local deployment and model capabilities – except public APIs are less widespread.

> [!tip]  
> The model we're using is small and easy to run locally, but it's far from the state of the art. Jina AI has a great API for multimodal search that can be used with minimal code (see below).

```py
import torch
from PIL import Image
from transformers import AutoModel

# Get a model
model = AutoModel.from_pretrained("jinaai/jina-clip-v2", trust_remote_code=True)

# Encode text
text_embeddings = model.encode_text(["a photo of a cat", "a dog playing fetch"])

# Encode images
image = Image.open("cat.jpg")
image_embeddings = model.encode_image([image])

# Calculate similarity
similarity = torch.cosine_similarity(text_embeddings, image_embeddings)
```

## Assignment

**Start building logic for multimodal search, and verify that you can load a CLIP model and generate image embeddings.**

1. [ ] Add the "Python Imaging Library" (PIL), or [Pillow](https://github.com/python-pillow/Pillow), to your dependencies. (Confusingly, the dependency is named `pillow`, but you import it as `PIL`.) This library loads an image file from a path into a format the CLIP model can process.
   ```sh
   uv add pillow
   ```
2. [ ] Create a new library module for multimodal search, e.g., at `cli/lib/multimodal_search.py`.
   1. [ ] Make sure to include the following imports:
      ```py
      from PIL import Image
      from sentence_transformers import SentenceTransformer
      ```
   2. [ ] Define a `MultimodalSearch` class. For now, the constructor should just create a `SentenceTransformer` instance using a provided model name, and assign it to an instance variable named `model`. Here's an example signature:
      ```py
      __init__(self, model_name="clip-ViT-B-32")
      ```
   3. [ ] You'll also need a method, e.g. `embed_image`, to generate an embedding for an image at a given path. Use [`Image.open`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open) from PIL to load the image, then pass it to the model's `encode` method. Return the embedding. (As in previous chapters, when generating an embedding for a single item, you can pass a one-element list to `encode` and take the first/only element from the resulting list of embeddings.)
   4. [ ] Finally, add a top-level function, e.g. `verify_image_embedding`, that takes an image path as input; creates an instance of `MultimodalSearch`; generates an embedding for the image; and prints the shape of the embedding in the following format:
      ```py
      f"Embedding shape: {embedding.shape[0]} dimensions"
      ```
3. [ ] Create a new script at `cli/multimodal_search_cli.py`. To start, it should have one command, `verify_image_embedding`, with a required positional argument for the image path. Call the corresponding function from your library module to generate the embedding and print its shape.

**Run and submit** the CLI tests.
