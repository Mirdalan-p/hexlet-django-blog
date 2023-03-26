from django.shortcuts import render


def index(request):
    return render(
        request,
        'article/article.html', context={
        'text': 'Article',
    }
    )