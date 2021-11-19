from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('answers', views.AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
