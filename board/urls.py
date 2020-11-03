from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work-orders-in-progress/', views.WorkOrdersInProgressListView.as_view(), name='work-orders-in-progress'),
    path('labor-today/', views.LaborTodayListView.as_view(), name='labor-today'),
]

