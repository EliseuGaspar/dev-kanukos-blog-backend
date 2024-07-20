from api.views import *
from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'admins', AdminViews, 'admin')
router.register(r'users', UserViewsCrud, 'users')
router.register(r'comments', CommentsViewCrud, 'comments')
router.register(r'posts', PostsViewCrud, 'posts')
router.register(r'reactions', ReactionsView, 'reactions')
router.register(r'saved', SavedView, 'saved')
router.register(r'favorite', FavoriteView, 'favorites')


urlpatterns = [
    path('', include((router.urls, 'api'))),
    path('user-login/', LoginViewAuthUser.as_view(), name='login'),
    path('admin-login/', LoginViewAuthAdmin.as_view(), name='login'),
]




