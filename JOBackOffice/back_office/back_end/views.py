from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.

from rest_framework.generics import RetrieveAPIView

class AllProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class AddNewProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RetrieveProductByIdView(RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RemovedProducView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete product"))


"""
class ProductAPI(GenericAPIView):
    serializer_class = ProductSerializer

    # Retrive data to Postgresql DB
    def get(self, request, pk=None):
        id = pk

        if id is not None:
            product = Product.objects.get(id=id)
            serialize = ProductSerializer(product)
            return Response(serialize.data)
        
        product = Product.objects.all()
        serialize = ProductSerializer(product, many=True)
        return Response(serialize.data)
    
    def post(self, request, format=None):
        serialize = ProductSerializer(data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response({'msg': 'Data Create'},
                            status = status.HTTP_201_CREATED)
        return Response(serialize.errors,
                        status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        id = pk
        product = Product.objects.get(id=id)
        product.delete()
        return Response({'msg': 'Data deleted'})
    """