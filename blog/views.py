from django.shortcuts import render
from datetime import date

posts = [
  {
    "slug": "hike-in-the-mountsins",
    "image": "mountains.jpg",
    "author": "Andrii",
    "date": date(2023, 8, 20),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepaired for what happened whilst I was enjoying the view!",
    "content": """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
  },
  {
    "slug": "hike-in-the-mountsins",
    "image": "mountains.jpg",
    "author": "Andrii",
    "date": date(2023, 8, 20),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepaired for what happened whilst I was enjoying the view!",
    "content": """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
  },
  {
    "slug": "hike-in-the-mountsins",
    "image": "mountains.jpg",
    "author": "Andrii",
    "date": date(2023, 8, 20),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepaired for what happened whilst I was enjoying the view!",
    "content": """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

    
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled 
    it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
    passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
  }
]

# Create your views here.

def starting_page(request):
  return render(request, "blog/index.html")

def posts(request):
  return render(request, "blog/all-posts.html")

def post_detail(request, slug):
  return render(request, "blog/post-detail.html")

