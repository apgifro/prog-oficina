from django.urls import path

from .views import ClienteReadView, MecanicoListView, EquipeListView, ClienteCreateView, ClienteUpdateView, \
    ClienteDeleteView

urlpatterns = [
    path("clientes/", ClienteReadView.as_view(), name="clientes_list"),
    path("clientes/criar/", ClienteCreateView.as_view(), name="clientes_criar"),
    path("clientes/editar/<int:pk>/", ClienteUpdateView.as_view(), name="clientes_atualizar"),
    path("clientes/excluir/<int:pk>/", ClienteDeleteView.as_view(), name="clientes_excluir"),

    path("mecanicos/", MecanicoListView.as_view(), name="mecanicos_list"),
    path("equipes/", EquipeListView.as_view(), name="equipes_list"),
]
