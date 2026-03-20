from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from ad.models import Ad


class AdListView(ListView):
    """Отбражение списка объявлений"""

    model = Ad
    template_name = 'ad/ad_list.html'
    context_object_name = 'ad'

class AdCreateView(CreateView):
    """Создание объявления"""

    model = Ad
    template_name = 'ad/ad_form.html'
    fields = ['__all__']
    success_url = reverse_lazy("ad:ad_list")

class AdDetailView(DetailView):
    """Детали объявления"""

    model = Ad
    template_name = 'ad/ad_list.html'
    context_object_name = 'ad'

class AdUpdateView(UpdateView):
    model = Ad
    fields = ['__all__']

    def get_success_url(self):
        return reverse("ad:ad_detail", kwargs={"pk": self.object.pk})

class AdDeleteView(DeleteView):
    model = Ad
    template_name = "ad/ad_confirm_delete.html"
    success_url = reverse_lazy("ad:ad_list")
