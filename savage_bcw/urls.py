from django.urls import re_path

from .views import (index, TeamView, GameView, SelectedGameView, ProductsView, SelectedProductView, BackCallView,
                    AboutView)

urlpatterns = [
    re_path(r'^$', index, name='home'),
    re_path(r'^teams/$', GameView.as_view(), name='teams'),
    re_path(r'^teams/game/(?P<game_id>\d+)', SelectedGameView.as_view(), name='selected_game'),
    re_path(r'^games/team/', TeamView.as_view(), name='team'),
    re_path(r'^product/', ProductsView.as_view(), name='products'),
    re_path(r'^prduct/selected-product/(?P<product_id>\d+)$', SelectedProductView.as_view(),
            name='selected_product'),
    re_path(r'^back-call/$', BackCallView.as_view(), name='back_call'),
    re_path(r'^about$', AboutView.as_view(), name='about')
]
