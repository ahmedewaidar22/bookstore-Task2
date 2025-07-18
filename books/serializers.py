# books/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer # Import the base
from .models import Book, Review

User = get_user_model()

# Your custom RegisterSerializer
class CustomRegisterSerializer(RegisterSerializer):

    _has_phone_field = False # Explicitly tell allauth that this serializer does NOT have a phone field





class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        read_only_fields = ('email',) # Often you don't want email to be changeable directly here

class ReviewSerializer(serializers.ModelSerializer):
    user = CurrentUserSerializer(read_only=True) # Use the simpler UserSerializer
    class Meta:
        model = Review
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            # Use Django's Avg aggregation, ensuring it's from django.db.models
            from django.db.models import Avg
            return reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
        return 0