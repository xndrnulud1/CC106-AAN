from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_registration, name='student_registration'),
    path('success/', views.registration_success, name='registration_success'),
<<<<<<< HEAD
    path('dashboard/', views.staff_dashboard, name='staff_dashboard'),
=======
>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
]