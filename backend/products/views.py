from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def get_premissions(self):
    self.permission_classes = [AllowAny]
    if self.request.method == 'POST':
      self.permission_classes = [IsAdminUser]
    return super().get_permissions()

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_url_kwarg = 'product_id'

  def get_permissions(self):
    self.permission_classes = [AllowAny]
    if self.request.method in ['PUT','PATCH','DELETE']:
      self.permission_classes = [IsAdminUser]
    return super().get_permissions()


# class ProductListCreateAPIView(generics.ListCreateAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer

#   def perform_create(self, serializer):
#     #serializer.save(user=self.request.user)
#     print(serializer)
#     title = serializer.validated_data.get('title')
#     content = serializer.validated_data.get('content') or None
#     if content is None:
#       content = title

#     serializer.save(content=content)

# product_list_create_view = ProductListCreateAPIView.as_view()

# class ProductDetailAPIView(generics.RetrieveAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
#   # lookup_field = 'pk'
  
#   # Product.objects.get(pk='abc')

# product_detail_view = ProductDetailAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
  """
    Not gonna use this method
  """
  
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request, *args, **kwargs):
  method = request.method

  if method == "GET":
    pass
    # url_args?
    # get request -> detail view
    # list view
    queryset = Product.objects.all()
    data = ProductSerializer(queryset,many=True).data
    return Response(data)

  if method == "POST":
    # create an item
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400)

    