from rest_framework import serializers
from ads.models import Ad

class AdSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    category = serializers.CharField()
    class Meta:
        model = Ad                                                 # по умолчанию ВЫВОДИТ ИНДЕКС!
        fields = ["id", "name", "price", "description", "author", "category"]

class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    category = serializers.CharField()
    class Meta:
        model = Ad                                                 # ВЫВОДИТ ИНДЕКС!
        fields = '__all__'