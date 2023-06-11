from django.urls import path

from .views import ClienteListView, MecanicoListView, EquipeListView

urlpatterns = [
    path("clientes/", ClienteListView.as_view(), name="clientes_list"),
    path("mecanicos/", MecanicoListView.as_view(), name="mecanicos_list"),
    path("equipes/", EquipeListView.as_view(), name="equipes_list"),
]
