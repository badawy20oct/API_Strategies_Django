from .models import Book , Review
from rest_framework import serializers



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Review
        fields = '__all__'