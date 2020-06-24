from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^tinymce/', include('tinymce.urls')),
    path('', views.home, name='home'),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('notes/', views.notes, name='notes'),
    path('note/<int:note_pk>/', views.note, name='note'),
    path('important/', views.important, name='important'),
    path('archive/', views.archive, name='archive'),
    path('add/', views.add, name='add'),
    path('note/<int:note_pk>/delete', views.delete, name='delete'),
]

urlpatterns += staticfiles_urlpatterns()