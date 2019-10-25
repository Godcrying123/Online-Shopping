"""shopsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page
# from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from product.views import IndexView

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

api_patterns = [
    # API URL List
    path('api/', include([
        path('person_entity/v1/', include('user.api.urls', namespace='persona_api')),
        path('item_entity/v1/', include('product.api.urls', namespace='item_api')),
        path('order_entity/v1/', include('order.api.urls', namespace='order_api')),
        path('docs/', include_docs_urls(title='ShopSite Apis')),
    ])),
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

translate_urlpatterns = i18n_patterns(
    # path('view/', include([
    path(_('user/'), include('user.urls', namespace='user_view')),
    path(_('item/'), include('product.urls', namespace='product_view')),
    path(_('cart/'), include('cart.urls', namespace='cart_view')),
    path(_('order/'), include('order.urls', namespace='order_view')),
    path(_('store/'), include('shop.urls', namespace='shop_view')),
    path(_('payment/'), include('payment.urls', namespace='payment_view')),
    path('rosetta/', include('rosetta.urls')),
    path('', IndexView.as_view(), name='index_view'),
    # ])),
)

urlpatterns = translate_urlpatterns + [
    # View URL List
    # Admin page url
    path('admin/', admin.site.urls),
    path('', include(api_patterns)),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
