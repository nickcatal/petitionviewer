from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from whresponse.responses.models import Response, Petition

import pickle

class ResponseListView(ListView):
    model = Response
    template_name = "index.html"

class ResponseDetailView(DetailView):
    model = Response
    template_name = "response.html"
    context_object_name = "response"

    def get_context_data(self, **kwargs):
        context = super(ResponseDetailView, self).get_context_data(**kwargs)

        context['petitions'] = Petition.objects.filter(response=context['response'])

        return context