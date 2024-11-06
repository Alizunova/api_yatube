from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet

app_name = "api"

v1_router = routers.DefaultRouter()
v1_router.register("posts", PostViewSet, basename="posts")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)
list = [
    path("", include(v1_router.urls)),
    path("api-token-auth/", views.obtain_auth_token, name="api-token-auth"),
]
urlpatterns = [
    path("v1/", include(list)),
]
