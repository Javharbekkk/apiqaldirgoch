from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('register-view/', register_view),
    path('get-home/', get_home_view),
    path('get-images-ico/', get_image_view),
    path('get-images/<int:pk>', get_image_id),
    path('get-text-fill/', get_textfill_view),
    path('get-imsj/<int:pk>', get_imsj_view),
    path('get-user/',get_user_view),
    path('get-intelekt/', intelekt_savol),
    path('get-intelekt/<int:pk>/', intelekt_savol_id),
    path('get-intelekt/<int:savol_pk>/<int:variant_pk>/', intelekt_variant_id,),
    path('get-maxsus/', maxsus_savol),
    path('get-maxsus/<int:pk>/', maxsus_savol_id),
    path('get-maxsus/<int:savol_pk>/<int:variant_pk>/', maxsus_variant_id,)


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

