from rest_framework import serializers
from .models import blog
from .models import comment


class blogserialzer(serializers.HyperlinkedModelSerializer):
    blog_id = serializers.ReadOnlyField()
    class Meta:
        model = blog
        fields = "__all__"

class commentserialzer(serializers.HyperlinkedModelSerializer):
    comment_id = serializers.ReadOnlyField()
    class Meta:
        model = comment
        fields = "__all__"        