from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('women/', views.WomenPage.as_view(), name='women'),
    path('women_api/', views.WomenPageAPI.as_view(), name='women_api'),
    path('men/', views.MenPage.as_view(), name='men'),
    path('men_api/', views.MenPageAPI.as_view(), name='men_api'),
    path('kids/', views.KidsPage.as_view(), name='kids'),
    path('kids_api/', views.KidsPageAPI.as_view(), name='kids_api'),
]


