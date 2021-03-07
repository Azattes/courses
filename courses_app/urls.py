from django.urls import path
from django.contrib import admin
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.CourseAPIView.as_view(), name = 'courses_list'),
    path('courses/<int:pk>/', views.CourseDetailAPIView.as_view(), name = 'coursesID'),
]
