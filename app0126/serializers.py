from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'publisheddate']
        #클라이언트에서 자기가 입력해야되는 것만 쓰기!
        #나열한 데이터를 입력하면 Book클래스의 인스턴스를 자동 생성

