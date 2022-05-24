from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()

urlpatterns = [
    path('test/', views.test_model.as_view()),
    path('api/', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)