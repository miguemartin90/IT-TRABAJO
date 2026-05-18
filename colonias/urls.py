from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "colonias"

urlpatterns = [
    path(
        "",
        RedirectView.as_view(pattern_name="colonias:colonia_list", permanent=False),
        name="home",
    ),
    path("planetas/", views.PlanetaListView.as_view(), name="planeta_list"),
    path("planetas/nuevo/", views.PlanetaCreateView.as_view(), name="planeta_create"),
    path("planetas/<int:pk>/", views.PlanetaDetailView.as_view(), name="planeta_detail"),
    path(
        "planetas/<int:pk>/editar/",
        views.PlanetaUpdateView.as_view(),
        name="planeta_update",
    ),
    path(
        "planetas/<int:pk>/borrar/",
        views.PlanetaDeleteView.as_view(),
        name="planeta_delete",
    ),
    path("colonias/", views.ColoniaListView.as_view(), name="colonia_list"),
    path("colonias/nueva/", views.ColoniaCreateView.as_view(), name="colonia_create"),
    path("colonias/<int:pk>/", views.ColoniaDetailView.as_view(), name="colonia_detail"),
    path(
        "colonias/<int:pk>/editar/",
        views.ColoniaUpdateView.as_view(),
        name="colonia_update",
    ),
    path(
        "colonias/<int:pk>/borrar/",
        views.ColoniaDeleteView.as_view(),
        name="colonia_delete",
    ),
    path("misiones/", views.MisionListView.as_view(), name="mision_list"),
    path("misiones/nueva/", views.MisionCreateView.as_view(), name="mision_create"),
    path("misiones/<int:pk>/", views.MisionDetailView.as_view(), name="mision_detail"),
    path(
        "misiones/<int:pk>/editar/",
        views.MisionUpdateView.as_view(),
        name="mision_update",
    ),
    path(
        "misiones/<int:pk>/borrar/",
        views.MisionDeleteView.as_view(),
        name="mision_delete",
    ),
]
