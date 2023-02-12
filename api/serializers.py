from rest_framework import serializers
from easyleasy2.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'
        depth = 1


class SupportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support_Request
        fields = '__all__'


class InterestRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest_Rate
        fields = '__all__'
        depth = 1


class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'
        depth = 1


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        depth = 1

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'
        depth = 1

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        depth = 1
