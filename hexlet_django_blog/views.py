from django.shortcuts import render
from django.views.generic.base import TemplateView

class indexView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, "base.html")

def about(request):
    return render(request, 'about.html')