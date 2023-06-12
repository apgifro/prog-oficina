from django.urls import path

from .views import ClienteListView, MecanicoListView, EquipeListView, ClienteCreateView, ClienteUpdateView

urlpatterns = [
    path("clientes/", ClienteListView.as_view(), name="clientes_list"),
    path("clientes/criar/", ClienteCreateView.as_view(), name="clientes_criar"),
    path("clientes/editar/<int:pk>/", ClienteUpdateView.as_view(), name="clientes_atualizar"),
    path("mecanicos/", MecanicoListView.as_view(), name="mecanicos_list"),
    path("equipes/", EquipeListView.as_view(), name="equipes_list"),
]
