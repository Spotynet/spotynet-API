from django.urls import path
from .views import StudentView

urlpatterns = [
    path('students', StudentView.as_view(), name="students_list"),
    path('students/<int:id>', StudentView.as_view(), name="students_process")
]