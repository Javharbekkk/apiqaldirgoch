from rest_framework import serializers
from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextHome
        fields = '__all__'


class IMSJSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMSJ
        fields = '__all__'


class TextFillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextFill
        fields = '__all__'


class IntelektVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntelektVariant
        fields = ('id', 'matn', 'is_correct')  # Variant maydonlari


class IntelektSerializer(serializers.ModelSerializer):
    variantlar = IntelektVariantSerializer(many=True, source='intelektvariant_set')
    # source: modeldagi bog'liqlikni ko'rsatadi

    class Meta:
        model = Intelekt
        fields = ('id', 'savol_matni', 'variantlar')


class MaxsusVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxsusVariant
        fields = ('id', 'matn', 'is_correct')


class MaxsusSerializer(serializers.ModelSerializer):
    variantlar = MaxsusVariantSerializer(many=True, source='maxsusvariant_set')
    # source: modeldagi bog'liqlikni ko'rsatadi

    class Meta:
        model = Maxsus
        fields = ('id', 'savol_matni', 'variantlar')
