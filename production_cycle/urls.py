from django.urls import path
from production_cycle import views

urlpatterns = [
    path('cycles/', views.CycleListView.as_view(), name='cycles'),
    path('create-cycle/', views.CycleCreateView.as_view(), name='createCycle'),
    path('cycle-detail/<str:pk>/',
         views.CycleDetailView.as_view(), name='cycleDetail'),
    path('delete-cycle/<str:pk>/',
         views.CycleDeleteView.as_view(), name='deleteCycle'),
    path('update-cycle/<str:pk>/',
         views.CycleUpdateView.as_view(), name='updateCycle'),
    path('create-slaugter/', views.SlaughterCreateView.as_view(),
         name='createSlaughter'),
    path('update-slaugter/<str:pk>',
         views.SlautherUpdateView.as_view(), name='updateSlaughter'),
    path('delete-slaugter/<str:pk>',
         views.SlaugterDeleteView.as_view(), name='deleteSlaughter'),
    path('create-day/', views.DayCreateView.as_view(), name='createDay'),
    path('update-day/<str:pk>', views.DayUpdateView.as_view(), name='updateDay'),
    path('day/<str:pk>', views.day, name='day'),
    path('delete-day/<str:pk>', views.DayDeleteView.as_view(), name='deleteDay')
]
