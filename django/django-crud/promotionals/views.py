from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Promotional


class PromotionalList(ListView):
    model = Promotional


class PromotionalCreate(CreateView):
    model = Promotional
    success_url = reverse_lazy('promotional_list')
    fields = ['name']


class PromotionalUpdate(UpdateView):
    model = Promotional
    success_url = reverse_lazy('promotional_list')
    fields = ['name']


class PromotionalDelete(DeleteView):
    model = Promotional
    success_url = reverse_lazy('promotional_list')
