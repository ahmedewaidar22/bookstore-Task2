from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        book_id = self.kwargs.get('book_pk')
        return Review.objects.filter(book_id=book_id)

    def perform_create(self, serializer):
        book = Book.objects.get(pk=self.kwargs['book_pk'])
        serializer.save(user=self.request.user, book=book)
