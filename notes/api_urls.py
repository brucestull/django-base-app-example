# notes\api_urls.py

from rest_framework.routers import DefaultRouter
from .api_views import NoteViewSet

router = DefaultRouter()
router.register(r"notes", NoteViewSet, basename="note")

urlpatterns = router.urls
