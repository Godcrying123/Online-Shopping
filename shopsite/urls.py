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
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings

from product.views import IndexView


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

extra_patterns = [
    # API URL List
    path('api/', include([
        path('person_entity/v1/', include('user.api.urls', namespace='persona_api')),
        path('item_entity/v1/', include('product.api.urls', namespace='item_api')),
        path('order_entity/v1/', include('order.api.urls', namespace='order_api')),
        path('docs/', include_docs_urls(title='ShopSite Apis')),
    ])),
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = [
    # View URL List
    # Admin page url
    path('admin/', admin.site.urls),
    path('view/', include([
        path('', IndexView.as_view()),
        path('user/', include('user.urls', namespace='user_view')),
        path('item/', include('product.urls', namespace='product_view')),
        path('cart/', include('cart.urls', namespace='cart_view')),
    ])),
    path('', include(extra_patterns)),
    # path('', include('snippets.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
