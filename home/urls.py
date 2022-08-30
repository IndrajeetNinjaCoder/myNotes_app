from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.handleSignup, name="handleSignup"),
    path('login/', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('addnote/', views.addNote, name="addNote"),
    path('editnote/', views.editNote, name="editNote"),
    path('deletenote/<int:id>', views.deleteNote, name="deleteNote"),
    path('search/', views.search, name="search"),
]
