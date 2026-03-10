from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="home"),
    path('/admin',views.adminpage,name="adminpage"),
    path('/login',views.loginview,name="login"),
    path('/signup',views.signuppage,name="signuppage"),
    path('logout/',views.logout_view,name="logout"),
    path("add_course/", views.add_course, name="add_course"),
    path("delete-course/<int:id>/", views.delete_course, name="delete_course"),
    path('update-course/<int:id>/', views.update_course, name='update_course'),
]