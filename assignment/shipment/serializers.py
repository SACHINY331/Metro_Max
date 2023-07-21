from rest_framework import serializers
from .models import shipment
from .models import cargo
from .models import tracking


class shipmentserialzer(serializers.HyperlinkedModelSerializer):
    shipment_id = serializers.ReadOnlyField()
    class Meta:
        model = shipment
        fields = "__all__"

class cargoserialzer(serializers.HyperlinkedModelSerializer):
    cargo_id = serializers.ReadOnlyField()
    class Meta:
        model = cargo
        fields = "__all__"       

class trackingserialzer(serializers.HyperlinkedModelSerializer):
    tracking_id = serializers.ReadOnlyField()
    class Meta:
        model = tracking
        fields = "__all__"          