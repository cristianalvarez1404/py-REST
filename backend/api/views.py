import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from products.models import Product
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from api.filters import ProductFilter,InStockFilterBackend
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['POST'])
def api_home(request,*args,**kwargs):
  """
    DRF API View
  """
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    # instance = serializer.save()
    return Response(serializer.data)
  return Response({"invalid":"not good data"},status=400)

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset= Product.objects.all()
  serializer_class = ProductSerializer
  #filterset_fields = ('name','price')
  filterset_class = ProductFilter
  filter_backends = [
    DjangoFilterBackend, 
    filters.SearchFilter,
    filters.OrderingFilter,
    InStockFilterBackend
  ]
  search_fields = ['name','description']
  ordering_fields = ['name','price','stock']

  def get_permissions(self):
    self.permission_classes = [AllowAny],
    if self.request.method == 'POST':
      self.permission_classes = [IsAdminUser]
    return super().get_permissions()


# @api_view(["GET"])
# def api_home(request,*args,**kwargs):
#   """
#     DRF API View
#   """
#   # if request.method != "POST":
#   #   return Response({"detail":"GET not allowed"},status=404)
#   instance = Product.objects.all().order_by("?").first()
#   data = {}
#   if instance:
#     # data = model_to_dict(instance,fields=['id','title','price','sale_price'])
#     data = ProductSerializer(instance).data
#   return Response(data)



# @api_view(["GET"])
# def api_home(request,*args,**kwargs):
#   """
#     DRF API View
#   """
#   # if request.method != "POST":
#   #   return Response({"detail":"GET not allowed"},status=404)
#   model_data = Product.objects.all().order_by("?").first()
#   data = {}
#   if model_data:
#     data = model_to_dict(model_data,fields=['id','title','price','sale_price'])
#   return Response(data)

# def api_home(request,*args,**kwargs):
#   model_data = Product.objects.all().order_by("?").first()
#   data = {}
#   if model_data:
#     data = model_to_dict(model_data,fields=['id','title','price'])
#     # data = dict(data)
#     # json_data_str = json.dumps(data)
#   # return HttpResponse(json_data_str, headers={"content-type":"application/json"})
#   return JsonResponse(data)

# def api_home(request, *args, **kwargs):
#   model_data = Product.objects.all().order_by("?").first()
#   data = {}
#   # if model_data:
#   #   data['id'] = model_data.id
#   #   data['title'] = model_data.title
#   #   data['content'] = model_data.content
#   #   data['price'] = model_data.price
#     # model instance (model_data)
#     # turn a Python dict
#     # return JSON to my client
  
#   return JsonResponse(data)




# def api_home(request, *args, **kwargs):
#   #request -> HttpRequest -> Django
#   # print(dir(request))
#   #request.body
#   body = request.body #JSON DATA but this object recibes byte string
#   data = {}
#   try:
#     data = json.loads(body) #string of Json data -> Python Dict
#   except:
#     pass 
#   # print(type(data))
#   # print(data.keys())
#   print(request.GET)
  
#   data['params'] = dict(request.GET)
#   data['headers'] = dict(request.headers)
#   data['content_type'] = request.content_type
  
#   return JsonResponse(data)

