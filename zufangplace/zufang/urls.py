from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.conf.urls import include

from . import views


router = DefaultRouter()
router.register(r'userprofile', views.UserProfileViewSet)
router.register(r'fang', views.FangViewSet)
router.register(r'picture', views.PictureViewSet)
router.register(r'like', views.LikeViewSet)


urlpatterns = [
    url('^', include(router.urls)),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
