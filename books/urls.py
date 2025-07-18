from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReviewViewSet

router = DefaultRouter()
router.register('books', BookViewSet)

# nested reviews under books
from rest_framework_nested import routers
books_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
books_router.register('reviews', ReviewViewSet, basename='book-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),
]
