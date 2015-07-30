from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from responses.models import Response, Petition

class ResponseListView(ListView):
    model = Response
    template_name = "index.html"

class ResponseDetailView(DetailView):
    model = Response
    template_name = "response.html"
    context_object_name = "response"
