from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post_create/', views.post_create, name='post_create'),
    path('edit/<int:pk>', views.post_edit, name='post_edit'),
    path('delete/<int:pk>', views.post_delete, name='post_delete')
]
