from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('new/', views.add_image, name='Add Image'),
    path('show/<int:id>', views.view_image, name='View Image'),
    path('<int:id>/edit', views.edit_image, name='Edit Image'),
    path('delete/<int:id>', views.delete_image, name='Delete Image'),
    path('search/',views.search_image, name='search_image')
]