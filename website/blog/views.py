from django.shortcuts import render


def home(request):
    return render(request, "blog/index.html")


def entries(request):
    return render(request, "blog/blog.html")


def single(request):
    return render(request, "blog/single.html")


def archives(request):
    return render(request, "blog/archives.html")


def page(request):
    return render(request, "blog/page.html")


def demo(request):
    return render(request, "blog/demo.html")