from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render


POST_TEXT = (
    "Duis ex ad cupidatat tempor Excepteur cillum cupidatat fugiat "
    "nostrud cupidatat dolor sunt sint sit nisi est eu exercitation "
    "incididunt adipisicing veniam velit id fugiat enim mollit amet "
    "anim veniam dolor dolor irure velit commodo cillum sit nulla "
    "ullamco magna amet magna cupidatat qui labore cillum sit in "
    "tempor veniam consequat non laborum adipisicing aliqua ea nisi "
    "sint ut quis proident ullamco ut dolore culpa occaecat ut laboris "
    "in sit minim cupidatat ut dolor voluptate enim veniam consequat "
    "occaecat fugiat in adipisicing in amet Ut nulla nisi non ut enim "
    "aliqua laborum mollit quis nostrud sed sed."
)

POSTS = [
    {
        "number": 1,
        "title": "Hey, We Love Open Sans!",
        "date": "July 12, 2014",
        "author": "John Doe",
        "categories": ["Ghost"],
        "text": POST_TEXT,
    },
    {
        "number": 2,
        "title": "We All Love Good Typography.",
        "date": "July 11, 2014",
        "author": "Jane Doe",
        "categories": ["Wordpress", "Ghost"],
        "text": POST_TEXT.split(" fugiat in adipisicing")[0] + " fugiat in.",
    },
    {
        "number": 3,
        "title": "White Space Everywhere.",
        "date": "July 10, 2014",
        "author": "Naruto Uzumaki",
        "categories": ["Joomla", "Drupal"],
        "text": POST_TEXT,
    },
    {
        "number": 4,
        "title": "Simple And Minimalist Designs.",
        "date": "July 09, 2014",
        "author": "Naruto Uzumaki",
        "categories": ["Ghost"],
        "text": POST_TEXT,
    },
]

CATEGORIES = [
    "Wordpress",
    "Ghost",
    "Joomla",
    "Drupal",
    "Magento",
    "Uncategorized",
]


def home(request):
    return render(request, "blog/index.html")


def entries(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    posts = POSTS

    if query:
        posts = [
            post
            for post in posts
            if query.casefold() in post["title"].casefold()
            or query.casefold() in post["text"].casefold()
        ]

    if category:
        posts = [
            post
            for post in posts
            if category in post["categories"]
        ]

    paginator = Paginator(posts, 2)
    page_obj = paginator.get_page(request.GET.get("page"))

    category_counts = [
        {
            "name": name,
            "count": sum(
                1 for post in POSTS
                if name in post["categories"]
            ),
        }
        for name in CATEGORIES
    ]

    context = {
        "posts": page_obj,
        "page_obj": page_obj,
        "query": query,
        "selected_category": category,
        "categories": category_counts,
    }

    return render(request, "blog/blog.html", context)


def single(request):
    try:
        post_number = int(request.GET.get("post", "2"))
    except (TypeError, ValueError):
        post_number = 2

    if not 1 <= post_number <= len(POSTS):
        raise Http404("Post not found")

    post = POSTS[post_number - 1]

    previous_post = None
    next_post = None

    if post_number > 1:
        previous_post = {
            "number": POSTS[post_number - 2]["number"],
            "title": POSTS[post_number - 2]["title"],
        }

    if post_number < len(POSTS):
        next_post = {
            "number": POSTS[post_number]["number"],
            "title": POSTS[post_number]["title"],
        }

    context = {
        "post": post,
        "previous_post": previous_post,
        "next_post": next_post,
    }

    return render(request, "blog/single.html", context)


def archives(request):
    return render(request, "blog/archives.html")


def page(request):
    return render(request, "blog/page.html")


def demo(request):
    return render(request, "blog/demo.html")