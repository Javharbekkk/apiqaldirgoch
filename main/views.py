from django.template.context_processors import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from datetime import datetime

@api_view(['POST'])
def register_view(request):
    new_user = Register.objects.create(
        region=request.data.get("region"),
        city=request.data.get("city"),
        surname=request.data.get("surname"),
        name=request.data.get("name"),
        birth=request.data.get("birth"),
        phone=request.data.get("phone"),
        full_adress=request.data.get("full_adress"),
    )




@api_view(['GET'])
def get_home_view(request):
    text = TextHome.objects.last()
    serialized = TextSerializer(text).data
    return Response(serialized)

@api_view(['GET'])
def get_image_view(request):
    image = Image.objects.all()
    serialized = ImagesSerializer(image, many=True).data
    return Response(serialized)

@api_view(['GET'])
def get_image_id(request, pk):
    ico = Image.objects.get(pk=pk)
    serializer = ImagesSerializer(ico)
    return Response(serializer.data)

@api_view(['GET'])
def get_textfill_view(request):
    textfill = TextFill.objects.all()
    serialized = TextFillSerializer(textfill, many=True).data
    return Response(serialized)

@api_view(['GET'])
def get_imsj_view(request,pk):
    imsj = IMSJ.objects.filter(status=pk)
    serialized = IMSJSerializer(imsj, many=True).data
    return Response(serialized)

@api_view(['GET'])
def get_user_view(request):
    users = Register.objects.all()
    serialized = RegisterSerializer(users, many=True).data
    for user_data in serialized:
        birth_date = datetime.strptime(user_data['birth'],'%Y-%m-%d')
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        user_data['age'] = age
    return Response(serialized)


@api_view(['GET'])
def intelekt_savol(request):
    savollar = Intelekt.objects.all()
    serializer = IntelektSerializer(savollar, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def intelekt_savol_id(request, pk):
    try:
        savol = Intelekt.objects.get(pk=pk)
    except Intelekt.DoesNotExist:
        return Response(status=404)
    serializer = IntelektSerializer(savol)
    return Response(serializer.data)


@api_view(['GET'])
def intelekt_variant_id(request, savol_pk, variant_pk):
    try:
        savol = Intelekt.objects.get(pk=savol_pk)
    except Intelekt.DoesNotExist:
        return Response({"error": "Savol topilmadi"}, status=404)

    try:
        variant = IntelektVariant.objects.get(pk=variant_pk, savol=savol)
    except IntelektVariant.DoesNotExist:
        return Response({"error": "Variant topilmadi yoki bu savolga tegishli emas"}, status=404)

    serializer = IntelektVariantSerializer(variant)
    return Response(serializer.data)

@api_view(['GET'])
def maxsus_savol(request):
    savollar = Maxsus.objects.all()
    serializer = MaxsusSerializer(savollar, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def maxsus_savol_id(request, pk):
    try:
        savol = Maxsus.objects.get(pk=pk)
    except Maxsus.DoesNotExist:
        return Response(status=404)
    serializer = MaxsusSerializer(savol)
    return Response(serializer.data)

@api_view(['GET'])
def maxsus_variant_id(request, savol_pk, variant_pk):
    try:
        savol = Maxsus.objects.get(pk=savol_pk)
    except Maxsus.DoesNotExist:
        return Response({"error": "Savol topilmadi"}, status=404)

    try:
        variant = MaxsusVariant.objects.get(pk=variant_pk, savol=savol)
    except MaxsusVariant.DoesNotExist:
        return Response({"error": "Variant topilmadi yoki bu savolga tegishli emas"}, status=404)

    serializer = MaxsusVariantSerializer(variant)
    return Response(serializer.data)