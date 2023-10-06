from django.urls import path
from . import views

urlpatterns = {
    path("group/", views.group_form, name="group_form"),
    path("teacher/", views.teacher_form, name="teacher_form"),
}
