from django.views.generic import ListView, DetailView
from marker.models import Marker

class MarkerLV(ListView):
    model = Marker

class MarkerDV(DetailView):
    model = Marker

# Create your views here.
