from django.urls import path
from .views import LandingPageView, MarketView, add_post_view, gallery_view

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('market/', MarketView.as_view(), name='market'),
    path('add_post/', add_post_view, name='add_post'),
    path('post/<int:pk>/', gallery_view, name='gallery')
]
