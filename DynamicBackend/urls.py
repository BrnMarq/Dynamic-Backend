from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet, GroupViewSet
from members.views import MemberViewSet
from portfolio.views import ItemViewSet
from category.views import CategoryViewSet
from blog.views import PostViewSet
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'members', MemberViewSet)
router.register(r'portfolio-items', ItemViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

