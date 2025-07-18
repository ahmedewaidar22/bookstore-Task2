from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Book, Review

User = get_user_model()

class BookReviewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ahmed', password='adminadmin')
        self.book = Book.objects.create(
            title='Django 101',
            description='Intro',
            price=19.99,  # Add this line
            author='John Doe',               # Also include any other required fields
)
    def test_list_books(self):
        url = reverse('book-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_review_requires_login(self):
        url = reverse('book-reviews-list', args=[self.book.pk])
        data = {'rating':5, 'comment':'Great!'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_review(self):
        self.client.force_authenticate(self.user)
        url = reverse('book-reviews-list', args=[self.book.pk])
        resp = self.client.post(url, {'rating':4,'comment':'Nice'})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)
    def test_duplicate_review(self):
        self.client.force_authenticate(user=self.user)
        url = f'/api/books/{self.book.id}/reviews/'
        data = {'rating': 3, 'comment': 'Once'}
        self.client.post(url, data)
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 400)
    def test_review_get_queryset(self):
        Review.objects.create(book=self.book, user=self.user, rating=5, comment='Great!')
        self.client.force_authenticate(user=self.user)
        url = f'/api/books/{self.book.id}/reviews/'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 1)
