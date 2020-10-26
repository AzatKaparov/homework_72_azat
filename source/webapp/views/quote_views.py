from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView

from webapp.models import Quote


class IndexView(ListView):
    template_name = 'quote/index.html'
    model = Quote
    queryset = Quote.objects.all()
    



