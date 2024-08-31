from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from marker.models import Marker
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

class MarkerLV(ListView):
    model = Marker

class MarkerDV(DetailView):
    model = Marker

class MarkerCreateView(LoginRequiredMixin, CreateView):
    model = Marker
    fields = ['title', 'url']
    success_url = reverse_lazy('marker:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MarkerChangeLV(LoginRequiredMixin, ListView):
    template_name = 'marker/marker_change_list.html'

    def get_queryset(self):
        return Marker.objects.filter(owner=self.request.user)

class MarkerUpdateView(OwnerOnlyMixin, UpdateView):
    model = Marker
    fields = ['title', 'url']
    success_url = reverse_lazy('marker:index')

class MarkerDeleteView(OwnerOnlyMixin, DeleteView):
    model = Marker
    success_url = reverse_lazy('marker:index')
