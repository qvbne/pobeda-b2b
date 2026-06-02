from django.views.generic import (
    ListView,
    DetailView
)

from .models import Product, Category


class ProductListView(ListView):

    model = Product

    template_name = 'catalog/catalog.html'

    context_object_name = 'products'

    def get_queryset(self):

        products = Product.objects.none()

        query = self.request.GET.get('q')

        category = self.request.GET.get('category')

        show_all = self.request.GET.get('all')

        if show_all:

            products = Product.objects.filter(
                available=True
            )

        elif category:

            products = Product.objects.filter(
                category_id=category,
                available=True
            )

        elif query:

            products = Product.objects.filter(
                name__icontains=query,
                available=True
            )

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = (
            Category.objects.all()
        )

        return context


class ProductDetailView(DetailView):

    model = Product

    template_name = 'catalog/product_detail.html'

    context_object_name = 'product'