from django.urls import path

from ordens.views import PecasReadView, ServicosReadView, VeiculoCreateView, VeiculoDeleteView, VeiculosReadView, \
    OrdemReadView, VeiculoUpdateView

urlpatterns = [
    path("pecas/", PecasReadView.as_view(), name="pecas_list"),
    path("servicos/", ServicosReadView.as_view(), name="servicos_list"),
    path("veiculos/", VeiculosReadView.as_view(), name="veiculos_list"),
    path('veiculos/cadastrar/', VeiculoCreateView.as_view(), name='cadastrar_veiculo'),
    path('veiculos/<str:placa>/update/', VeiculoUpdateView.as_view(), name='veiculo_update'),
    path('veiculos/<str:placa>/delete/', VeiculoDeleteView.as_view(), name='veiculo_delete'),
    path("ordens/", OrdemReadView.as_view(), name="ordem_list"),
]
