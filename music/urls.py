from django.urls import path

from music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instruments/<int:pk>/', views.InstrumentDetailView.as_view(), name='instrument_detail'),
]
