from django.urls import path

from music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instruments/', views.InstrumentListView.as_view(), name='instrument_list'),
    path('instruments/<int:pk>/', views.InstrumentDetailView.as_view(), name='instrument-detail'),
    path('instruments/types/<str:type_name>/', views.InstrumentListView.as_view(), name='instrument-type'),
    path('instruments/create/', views.InstrumentCreateView.as_view(), name='instrument-create'),
    path('instruments/<int:pk>/update/', views.InstrumentUpdateView.as_view(), name='instrument-update'),
    path('instruments/<int:pk>/delete/', views.InstrumentDeleteView.as_view(), name='instrument-delete'),
]
