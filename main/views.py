from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from datetime import datetime


@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User successfully registered"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_home_view(request):
    text = TextHome.objects.last()
    if text:
        serialized = TextSerializer(text).data
        return Response(serialized)
    return Response({"error": "No text found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_image_view(request):
    images = Image.objects.all()
    serialized = ImagesSerializer(images, many=True).data
    return Response(serialized)


@api_view(['GET'])
def get_image_id(request, pk):
    try:
        image = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ImagesSerializer(image)
    return Response(serializer.data)


@api_view(['GET'])
def get_textfill_view(request):
    textfills = TextFill.objects.all()
    serialized = TextFillSerializer(textfills, many=True).data
    return Response(serialized)


@api_view(['GET'])
def get_imsj_view(request, pk):
    imsj = IMSJ.objects.filter(status=pk)
    serialized = IMSJSerializer(imsj, many=True).data
    return Response(serialized)


@api_view(['GET'])
def get_user_view(request):
    users = Register.objects.all()
    serialized = RegisterSerializer(users, many=True).data
    for user_data in serialized:
        try:
            birth_date = datetime.strptime(user_data['birth'], '%Y-%m-%d')
            today = datetime.today()
            age = today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day)
            )
            user_data['age'] = age
        except (ValueError, TypeError):
            user_data['age'] = None  # Agar format noto'g'ri bo'lsa yoki tug'ilgan sana bo'lmasa
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
        return Response({"error": "Savol not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = IntelektSerializer(savol)
    return Response(serializer.data)


@api_view(['GET'])
def intelekt_variant_id(request, savol_pk, variant_pk):
    try:
        savol = Intelekt.objects.get(pk=savol_pk)
    except Intelekt.DoesNotExist:
        return Response({"error": "Savol not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        variant = IntelektVariant.objects.get(pk=variant_pk, savol=savol)
    except IntelektVariant.DoesNotExist:
        return Response({"error": "Variant not found or not related to this savol"}, status=status.HTTP_404_NOT_FOUND)

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
        return Response({"error": "Savol not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = MaxsusSerializer(savol)
    return Response(serializer.data)


@api_view(['GET'])
def maxsus_variant_id(request, savol_pk, variant_pk):
    try:
        savol = Maxsus.objects.get(pk=savol_pk)
    except Maxsus.DoesNotExist:
        return Response({"error": "Savol not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        variant = MaxsusVariant.objects.get(pk=variant_pk, savol=savol)
    except MaxsusVariant.DoesNotExist:
        return Response({"error": "Variant not found or not related to this savol"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaxsusVariantSerializer(variant)
    return Response(serializer.data)
