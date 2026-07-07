from django.urls import path
from . import views

urlpatterns = [

    path("register/", views.register_job, name="register"),

    path("success/", views.success, name="success"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("candidate/<int:pk>/", views.detail, name="detail"),

    path("candidate/delete/<int:pk>/", views.delete_candidate, name="delete_candidate"),

    path("logout/", views.logout_view, name="logout"),

]