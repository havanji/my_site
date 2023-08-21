from django.shortcuts import render
from datetime import date

all_posts = [
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
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Andrii",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Andrii",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
  return post['date']

def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, "blog/index.html", {
    "posts":latest_posts
  })

def posts(request):
  return render(request, "blog/all-posts.html", {
    "all_posts": all_posts
  })

def post_detail(request, slug):
  identefied_post = next(post for post in all_posts if post['slug'] == slug)
  return render(request, "blog/post-detail.html", {
    "post": identefied_post
  })

