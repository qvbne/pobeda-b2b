from catalog.models import Product
from decimal import Decimal


class Cart:

    def __init__(self, request):

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:

            cart = self.session['cart'] = {}

        self.cart = cart

    def add(
            self,
            product_id,
            quantity
    ):

        self.cart[str(product_id)] = str(quantity)

        self.save()

    def remove(
            self,
            product_id
    ):

        product_id = str(product_id)

        if product_id in self.cart:

            del self.cart[product_id]

            self.save()

    def save(self):

        self.session.modified = True

    def clear(self):

        self.session['cart'] = {}

        self.save()

    def get_products(self):

        return Product.objects.filter(
            id__in=self.cart.keys()
        )

    def get_total(self):

        total = Decimal('0')

        products = self.get_products()

        for product in products:
            qty = Decimal(
                str(self.cart[str(product.id)])
            )

            total += (
                    product.price_per_unit *
                    qty
            )

        return total