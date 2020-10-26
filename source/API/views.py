from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.viewsets import ModelViewSet
from webapp.models import Quote
from .permissions import QuotePermissions
from .serializers import QuoteSerializer, QuoteCreateSerializer, QuoteUpdateSerializer


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    permission_classes = [QuotePermissions]

    def get_queryset(self):
        if self.request.method == 'GET' and \
                not self.request.user.has_perm('webapp.quote_view'):
            return Quote.get_moderated()
        return Quote.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return QuoteCreateSerializer
        elif self.request.method in ('PUT', 'PATCH'):
            return QuoteUpdateSerializer
        return QuoteSerializer







