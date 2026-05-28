from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "colonias"

urlpatterns = [
    path('colonias/', views.inicio, name='inicio'),
    path(
        "",
        RedirectView.as_view(pattern_name="colonias:inicio", permanent=False),
        name="home",
    ),
    path("colonias/planetas/", views.PlanetaListView.as_view(), name="planeta_list"),
    path("colonias/planetas/nuevo/", views.PlanetaCreateView.as_view(), name="planeta_create"),
    path("colonias/planetas/<int:pk>/", views.PlanetaDetailView.as_view(), name="planeta_detail"),
    path(
        "colonias/planetas/<int:pk>/editar/",
        views.PlanetaUpdateView.as_view(),
        name="planeta_update",
    ),
    path(
        "colonias/planetas/<int:pk>/borrar/",
        views.PlanetaDeleteView.as_view(),
        name="planeta_delete",
    ),
    path("colonias/colonias/", views.ColoniaListView.as_view(), name="colonia_list"),
    path("colonias/colonias/nueva/", views.ColoniaCreateView.as_view(), name="colonia_create"),
    path("colonias/colonias/<int:pk>/", views.ColoniaDetailView.as_view(), name="colonia_detail"),
    path(
        "colonias/colonias/<int:pk>/editar/",
        views.ColoniaUpdateView.as_view(),
        name="colonia_update",
    ),
    path(
        "colonias/colonias/<int:pk>/borrar/",
        views.ColoniaDeleteView.as_view(),
        name="colonia_delete",
    ),
    path("colonias/misiones/", views.MisionListView.as_view(), name="mision_list"),
    path("colonias/misiones/nueva/", views.MisionCreateView.as_view(), name="mision_create"),
    path("colonias/misiones/<int:pk>/", views.MisionDetailView.as_view(), name="mision_detail"),
    path(
        "colonias/misiones/<int:pk>/editar/",
        views.MisionUpdateView.as_view(),
        name="mision_update",
    ),
    path(
        "colonias/misiones/<int:pk>/borrar/",
        views.MisionDeleteView.as_view(),
        name="mision_delete",
    ),
]
