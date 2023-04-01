from rest_framework import viewsets
from customer.models import Product, Customer
from customer.serializer import Productserilizers, Customerserilizer
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import authentication,permissions


class Productview(viewsets.ModelViewSet):
    serializer_class = Productserilizers
    queryset = Product.objects.all()
    authentication_classes =[authentication.BasicAuthentication]
    permission_classes =[permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        product = self.get_object()
        if timezone.now() - product.registered_at > timezone.timedelta(days=60):
            product.is_active = False
            product.save()
            return Response({'message': 'Product deactivated'})
        else:
            return Response({'message': 'Product cannot be deactivated yet'})


class Custmerview(viewsets.ModelViewSet):
    serializer_class = Customerserilizer
    queryset = Product.objects.all()

# Create your views here.
