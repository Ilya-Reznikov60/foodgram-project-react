from rest_framework import routers
from django.urls import include, path

from api.views import (
    IngredientsViewSet, TagsViewSet, RecipeViewSet, UserViewSet,
    FollowListView, UserFollowView, get_me,
)

app_name = 'api'

router = routers.DefaultRouter()


router.register(
    'ingredients',
    IngredientsViewSet,
    basename='ingredient'
)
router.register(
    'users',
    UserViewSet,
    basename='user'
)
router.register(
    'tags',
    TagsViewSet,
    basename='tag'
)
router.register(
    'recipes',
    RecipeViewSet,
    basename='recipe'
)

urlpatterns = [
    path('users/<int:user_id>/subscribe/', UserFollowView.as_view(),
         name='user-subscribe'),
    path('users/subscriptions/', FollowListView.as_view(),
         name='user-subscriptions'),
    path('users/me/', get_me, name='user-me'),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
]
