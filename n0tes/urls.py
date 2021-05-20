from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^tinymce/', include('tinymce.urls')),
    path('', views.home, name='home'),

    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('notes/', views.all_notes, name='all_notes'),
    path('note/<int:note_pk>/', views.note, name='note'),
    path('important/', views.important_notes, name='important_notes'),
    path('archive/', views.archive, name='archive'),
    path('new-note/', views.add_note, name='add_note'),
    path('search/', views.search, name='search'),
    path('note/<int:note_pk>/delete', views.delete_note, name='delete_note'),
    path('note/<int:note_pk>/archive', views.archive_note, name='archive_note'),

    path('profile/', views.profile, name='profile'),
    path(r'^deleteuser/', views.delete_user, name='delete_user')
]

urlpatterns += staticfiles_urlpatterns()