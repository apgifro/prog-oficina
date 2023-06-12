from django.urls import path

from .views import ClienteListView, MecanicoListView, EquipeListView, ClienteCreateView

urlpatterns = [
    path("clientes/", ClienteListView.as_view(), name="clientes_list"),
    path("clientes/criar/", ClienteCreateView.as_view(), name="clientes_criar"),
    path("mecanicos/", MecanicoListView.as_view(), name="mecanicos_list"),
    path("equipes/", EquipeListView.as_view(), name="equipes_list"),
]
