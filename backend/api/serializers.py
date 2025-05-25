class OrderSerializer(serializers.ModelSerializer):
  order_id = serializers.UUIDField(read_only=True)
  items = OrderItemSerializer(many=True, read_only= True)
  total_price = serializers.SerializerMethodField(method_name='total')
  
  def total(self, obj):
    order_items = obj.items.all()
    return sum(order_item.item_subtotal for order_item in order_items)
  
  class Meta:
    model = Order
    fields = (
      'order_id',
      'created_at',
      'user',
      'status',
      'items',
      'total_price'
    )
    
class OrderCreateSerializer(serializer.ModelSerializer):
  class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
      model = OrderItem
      fields = ('product','quantity')
      
  items = OrderItemCreateSerializer(many=True)
  
  def create(self, validated_data):
    orderitem_data = validated_data.pop('items')
    order = Order.objects.create(**validated_data)
    
    for item in orderitem_data:
      OrderItem.objects.create(order=order, **item)
    
    return order
    
  class Meta:
    model = Order
    fields = (
      'user',
      'status',
      'items',
    )