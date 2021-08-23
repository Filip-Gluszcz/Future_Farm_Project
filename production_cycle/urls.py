from django.urls import path
from production_cycle import views

urlpatterns = [
    path('cycles/', views.cycles, name='cycles'),
    path('createCycle/', views.CreateCycleView.as_view(), name='createCycle'),
    path('cycleDetail/<str:pk>/',
         views.CycleDetailView.as_view(), name='cycleDetail'),
    path('deleteCycle/<str:pk>/',
         views.DeleteCycleView.as_view(), name='deleteCycle'),
    path('updateCycle/<str:pk>/',
         views.CycleUpdateView.as_view(), name='updateCycle'),
    path('createSlaughter/<str:pk>',
         views.create_slaughter, name='createSlaughter'),
    path('createDay/<str:pk>', views.create_day, name='createDay'),
    path('updateDay/<str:pk>', views.update_day, name='updateDay'),
    path('day/<str:pk>', views.day, name='day'),
    path('deleteDay/<str:pk>', views.delete_day, name='deleteDay')
]
