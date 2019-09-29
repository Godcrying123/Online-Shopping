from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins

from order.api.serializers import OrderSerializer, OrderItemSerializer, OrderByUserNameSerializer
from order.models import Order, OrderItem
from product.models import Product
from user.models import Users


class OrderCreate(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    create a order
    """
    serializer_class = OrderSerializer

    def get_instance_by_model(self, Object, pk):
        try:
            return Object.objects.get(pk=pk)
        except Object.DoesNotExist:
            return None

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        retresult = {
            'Order_ID': None,
            'Order_Owner': None,
            'Order_Paid_Status': None,
            'Order_Item_Results': []
        }
        owner_id = self.request.data.get('owner')
        products = self.request.data.get('products')
        user = self.get_instance_by_model(Users, owner_id)
        if user is not None:
            retresult['Order_Owner'] = user.id
        else:
            return Response(retresult)
        ordercreated = Order.objects.create(owner=user)
        retresult['Order_ID'] = ordercreated.id
        retresult['Order_Paid_Status'] = ordercreated.status_order
        for orderproduct in products:
            orderdetail = {
                'OrderItemID': None,
                'OrderProductID': None,
                'OrderProductName': None,
                'OrderImg': None,
                'OrderQuantity': None,
                'OrderPrice': None,
                'OrderResult': None
            }
            product_id = orderproduct.get('id')
            quantity = orderproduct.get('quantity')
            price = orderproduct.get('price')
            product = self.get_instance_by_model(Product, product_id)
            orderdetail['OrderProductID'] = product_id
            orderdetail['OrderPrice'] = price
            orderdetail['OrderQuantity'] = quantity
            if product is None:
                orderdetail['OrderResult'] = False
                continue
            orderitem = OrderItem.objects.create(order=ordercreated, product=product, quantity=quantity, price=price)
            orderdetail['OrderItemID'] = orderitem.id
            orderdetail['OrderProductName'] = product.name
            orderdetail['OrderImg'] = product.image.url
            orderdetail['OrderResult'] = True
            retresult['Order_Item_Results'].append(orderdetail)
        return Response(retresult)


class OrderListByUser(generics.RetrieveAPIView):
    """
    Listing all order details for specific user
    """
    queryset = Users.objects.all()
    serializer_class = OrderByUserNameSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        for order in serializer.data.get('own_orders'):
            # print(order.get('orderitems'))
            for orderitem in order.get('orderitems'):
                productdetail = {
                    'product_id': None,
                    'product_name': None,
                    'product_image': None
                }
                product = Product.objects.get(pk=orderitem['product'])
                productdetail['product_id'] = orderitem['product']
                productdetail['product_name'] = product.name
                # productdetail['product_image'] = product.image
                orderitem['product'] = productdetail
        return Response(serializer.data)


class OrderItemDetail(generics.RetrieveUpdateAPIView):
    """
    order detail list
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

