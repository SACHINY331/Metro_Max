from rest_framework import serializers
from .models import product
from .models import category


class productserialzer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.ReadOnlyField()
    class Meta:
        model = product
        fields = "__all__"

class categoryserialzer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.ReadOnlyField()
    class Meta:
        model = category
        fields = "__all__"        