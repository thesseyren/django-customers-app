from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='list'),
    path('new/', views.CustomerCreateView.as_view(), name='new'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.CustomerUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.CustomerDeleteView.as_view(), name='delete'),
]
