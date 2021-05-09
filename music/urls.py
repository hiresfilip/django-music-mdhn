from django.urls import path

from music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instruments/', views.InstrumentListView.as_view(), name='instrument_list'),
    path('instruments/<int:pk>/', views.InstrumentDetailView.as_view(), name='instrument_detail'),
]
