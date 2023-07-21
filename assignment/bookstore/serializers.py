from rest_framework import serializers
from .models import book
from .models import author
from .models import review


class bookserialzer(serializers.HyperlinkedModelSerializer):
    book_id = serializers.ReadOnlyField()
    class Meta:
        model = book
        fields = "__all__"

class authorserialzer(serializers.HyperlinkedModelSerializer):
    comment_id = serializers.ReadOnlyField()
    class Meta:
        model = author
        fields = "__all__"       

class reviewserialzer(serializers.HyperlinkedModelSerializer):
    comment_id = serializers.ReadOnlyField()
    class Meta:
        model = review
        fields = "__all__"          