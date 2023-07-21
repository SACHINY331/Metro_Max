from rest_framework import serializers
from .models import account
from .models import customer


class accountserialzer(serializers.HyperlinkedModelSerializer):
    account_id = serializers.ReadOnlyField()
    class Meta:
        model = account
        fields = "__all__"

class customerserialzer(serializers.HyperlinkedModelSerializer):
    customer_id = serializers.ReadOnlyField()
    class Meta:
        model = customer
        fields = "__all__"        