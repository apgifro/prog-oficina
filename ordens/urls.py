from django.urls import path

from ordens.views import PecasReadView, ServicosReadView, VeiculosReadView, OrdemReadView

urlpatterns = [
    path("pecas/", PecasReadView.as_view(), name="pecas_list"),
    path("servicos/", ServicosReadView.as_view(), name="servicos_list"),
    path("veiculos/", VeiculosReadView.as_view(), name="veiculos_list"),
    path("ordens/", OrdemReadView.as_view(), name="ordem_list"),
]
