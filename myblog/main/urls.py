from django.urls import path

from .views import index, by_category, detail

app_name = 'main'

urlpatterns = [
    path('<int:category_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_category, name='by_category'),
    path('', index, name='index')
]