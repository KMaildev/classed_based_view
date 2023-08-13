from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CategoryDetailView

urlpatterns = [
    path("", CategoryListView.as_view(), name='category_list'),
    path("create", CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<slug:slug>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/detail/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]
