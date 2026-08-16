from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    #path('', homePageView, name = 'home') non class based view
    #class vased view below
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name = 'home')
]