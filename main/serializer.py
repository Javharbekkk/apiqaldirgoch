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
        fields = ('id', 'matn', 'is_correct')  # is_correct maydoni qo'shildi

class IntelektSerializer(serializers.ModelSerializer):
    variantlar = IntelektVariantSerializer(many=True)

    class Meta:
        model = Intelekt
        fields = ('id', 'savol_matni', 'variantlar')

class MaxsusVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxsusVariant
        fields = ('id', 'matn', 'is_correct')


class MaxsusSerializer(serializers.ModelSerializer):
    variantlar = MaxsusVariantSerializer(many=True)

    class Meta:
        model = Maxsus
        fields = ('id', 'savol_matni', 'variantlar')




