from rest_framework.routers import DefaultRouter
from newsusers.views import UserViewSet
from tags.views import TagViewSet
from newsletters.views import NewsletterViewSet


router = DefaultRouter()

router.register('v1/register', UserViewSet, basename='register')
router.register('v1/tags', TagViewSet, basename='tags')
router.register('v1/newsletters', NewsletterViewSet, basename='newsletters')


urlpatterns = router.urls

