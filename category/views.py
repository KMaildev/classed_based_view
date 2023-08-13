from django.views.generic import ListView, DetailView
from .models import Category
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CategoryCreateForm
from django.urls import reverse_lazy


class CategoryListView(ListView):
    model = Category
    paginate_by = 3
    template_name = 'category/category_list.html'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("category_list")


class CategoryDetailView(DetailView):
    model = Category
