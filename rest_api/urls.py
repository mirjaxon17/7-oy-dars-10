from django.urls import path, include
from .views import CommentDetailApiView, SpecialDetailApiView, CategoryDetailApiView, SizeDetailApiView, ColorDetailApiView, ProductDetailApiView, ChooseColorDetailApiView, SponserDetailApiView 
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Multi Shop API",
        description="Online Market Application demo",
        default_version="v1",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='example@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

router = routers.DefaultRouter()
router.register('comment', CommentDetailApiView, basename='comment')
router.register('special', SpecialDetailApiView, basename='special')
router.register('category', CategoryDetailApiView, basename='category')
router.register('size', SizeDetailApiView, basename='size')
router.register('color', ColorDetailApiView, basename='color')
router.register('product', ProductDetailApiView, basename='product')
router.register('choose_color', ChooseColorDetailApiView, basename='choose_color')
router.register('sponser', SponserDetailApiView, basename='sponser')
#mirj@X0n

urlpatterns = [
    path('', include(router.urls)),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
]