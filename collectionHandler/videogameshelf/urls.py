from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('editor/<int:editorId>/', views.editor, name='vote'),
]
