from django.urls import path
from marker import views

app_name = 'marker'
urlpatterns = [
    path('', views.MarkerLV.as_view(), name='index'),
    path('<int:pk>', views.MarkerDV.as_view(), name='detail'),

    # Example: /marker/add/
    path('add/', views.MarkerCreateView.as_view(), name="add",),

    # Example: /marker/change/
    path('change/', views.MarkerChangeLV.as_view(), name="change",),

    # Example: /marker/99/update/
    path('<int:pk>/update/', views.MarkerUpdateView.as_view(), name="update",),

    # Example: /marker/99/delete/
    path('<int:pk>/delete/', views.MarkerDeleteView.as_view(), name="delete",),
]

