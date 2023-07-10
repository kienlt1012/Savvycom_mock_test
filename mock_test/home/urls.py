from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', auth_view.LoginView.as_view(template_name="pages/login.html"), name='login'),
    path('post', views.index, name = 'home'),
    path('register/',views.register, name='register'),
    path('<int:id>/', views.post),
    path('create/', views.create_post, name = "create_post"),
    path('<int:id>/delete/', views.delete_post, name = "delete_post"),
    path('<int:id>/update/', views.update_post, name = "update_post")
]
