from rest_framework import serializers
from easyleasy2.models import *


class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class PromoSerializer(serializers.ModelSerializer):
    product = RelatedFieldAlternative(queryset=Product.objects.all(), serializer=ProductSerializer)
    class Meta:
        model = Promo
        fields = '__all__'
        depth = 1


class SupportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support_Request
        fields = '__all__'


class InterestRateSerializer(serializers.ModelSerializer):
    product = RelatedFieldAlternative(queryset=Product.objects.all(), serializer=ProductSerializer)
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
    client_profile = RelatedFieldAlternative(queryset=ClientProfile.objects.all(), serializer=ClientProfileSerializer)
    product = RelatedFieldAlternative(queryset=Product.objects.all(), serializer=ProductSerializer)
    class Meta:
        model = Application
        fields = '__all__'
        depth = 1

class DealSerializer(serializers.ModelSerializer):
    client_profile = RelatedFieldAlternative(queryset=ClientProfile.objects.all(), serializer=ClientProfileSerializer)
    product = RelatedFieldAlternative(queryset=Product.objects.all(), serializer=ProductSerializer)
    class Meta:
        model = Deal
        fields = '__all__'
        depth = 1

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        depth = 1
