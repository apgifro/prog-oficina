from django.urls import path

from ordens.views import PecasReadView, ServicosReadView, VeiculoCreateView, VeiculoDeleteView, VeiculosReadView, \
    OrdemReadView, VeiculoUpdateView, PecasCreateView, PecasUpdateView, PecasDeleteView, ServicosCreateView, \
    ServicosUpdateView, ServicosDeleteView, OrdemCreateView, OrdemUpdateView, OrdemDeleteView

urlpatterns = [
    path("pecas/", PecasReadView.as_view(), name="pecas_list"),
    path("pecas/criar", PecasCreateView.as_view(), name="pecas_criar"),
    path("pecas/editar/<int:pk>/", PecasUpdateView.as_view(), name="pecas_atualizar"),
    path("pecas/excluir/<int:pk>/", PecasDeleteView.as_view(), name="pecas_excluir"),

    path("servicos/", ServicosReadView.as_view(), name="servicos_list"),
    path("servicos/criar", ServicosCreateView.as_view(), name="servicos_criar"),
    path("servicos/editar/<int:pk>/", ServicosUpdateView.as_view(), name="servicos_atualizar"),
    path("servicos/excluir/<int:pk>/", ServicosDeleteView.as_view(), name="servicos_excluir"),

    path("veiculos/", VeiculosReadView.as_view(), name="veiculos_list"),
    path('veiculos/cadastrar/', VeiculoCreateView.as_view(), name='cadastrar_veiculo'),
    path('veiculos/<str:placa>/update/', VeiculoUpdateView.as_view(), name='veiculo_update'),
    path('veiculos/<str:placa>/delete/', VeiculoDeleteView.as_view(), name='veiculo_delete'),

    path("ordens/", OrdemReadView.as_view(), name="ordem_list"),
    path("ordens/criar", OrdemCreateView.as_view(), name="ordem_criar"),
    path("ordens/editar/<int:pk>", OrdemUpdateView.as_view(), name="ordem_atualizar"),
    path("ordens/excluir/<int:pk>", OrdemDeleteView.as_view(), name="ordem_excluir"),
]
