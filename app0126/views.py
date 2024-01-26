from rest_framework.response import Response
from rest_framework.decorators import api_view

#get요청이 오면 함수를 호출
@api_view(['GET'])
def hello(request):
    return Response("Hello Rest API")
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Book
from .serializers import BookSerializer

#get과 post모두 처리
@api_view(['GET', 'POST'])
def booksAPI(request):
    #get방식의 처리 - 조회를 요청하는 경우
    if request.method == 'GET':
        books = Book.objects.all()
        #테이블 데이터 전부 가져오기
        serializer = BookSerializer(books, many = True)
        #출력하기 위해서 브라우저의 형식으로 데이터 변환
        return Response(serializer.data)
        #출력
    
    #post방식의 처리 - 삽입하는 경우
    elif request.method == 'POST':
        #클라이언트에서 전송된데이터를 가지고 Model1 인스턴스 생성
        serializer = BookSerializer( data = request.data)
        serializer.save()
        return Response(serializer.data)