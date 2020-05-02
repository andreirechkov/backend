from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from rest_framework import routers

from api import views
from api.views import GetAuthToken

router = routers.DefaultRouter()
router.register(r'test', views.TestViewSet)
router.register(r'api/users', views.UsersViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path('api/chat/', include('api.urls', namespace='chat')),
    path(r'api/auth/', GetAuthToken.as_view()),
]