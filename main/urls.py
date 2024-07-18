from django.contrib import admin
from django.urls import include, path

from main import views

urlpatterns = [
    path('', views.MainScreen, name="MainScreen"),
    path('tunemood/', views.TuneMoodScreen, name="TuneMood"),
    path("careerExplorer/", views.CareerExplorerScreen, name="CareerExplorer"),
    path("explorerInns/", views.ExplorerInnsScreen, name="ExplorerInns"),
    path("eseva/", views.EsevaScreen, name="Eseva"),
]