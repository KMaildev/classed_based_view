from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path("", CategoryListView.as_view(), name='category_list'),
    path("create", CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<slug:slug>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category_delete'),
]
