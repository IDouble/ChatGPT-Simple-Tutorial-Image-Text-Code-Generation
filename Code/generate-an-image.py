response = openai.Image.create(
  prompt="a happy dog",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']