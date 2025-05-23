from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
