from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.urls import reverse

def index(request):
    return HttpResponseRedirect(reverse('article', kwargs={'tags': 'python',
    'article_id': '42'}))


def get_article(request, tags, article_id):
    return render(
    request,
    'article/article.html', context={
    'tags': tags,
    'article_id': article_id
    }
)

