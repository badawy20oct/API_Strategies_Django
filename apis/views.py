from django.http import Http404
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Book , Review
from rest_framework.decorators import api_view
from .serializers import BookSerializer , ReviewSerializer
from rest_framework.response import Response
from rest_framework import status , mixins ,generics , viewsets
from rest_framework.views import APIView


#1 Pure Django Json No Model

def Pure_Json(request): 
    books = [
        {
            "id": 1,
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "reviews": []
        },
        {
            "id": 2,
            "title": "1984",
            "author": "George Orwell",
            "reviews": []
        }
    ]
    return JsonResponse(books , safe=False)

#2 Pure Djanog Json With Model

def Pure_Json_Model(request):

    data = Review.objects.all()
    response = {
        'review' : list(data.values('book','reviewer','text','rating'))
    }
    return JsonResponse(response)


#//////////////////////////////////////   REST Framework /////////////////////////////////////////////////////////


#3 Function Based View (fbv)
# GET POST  
@api_view(['GET', 'POST'])
def fbv_list(request):
    #GET
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books , many = True)
        return Response(serializer.data)
    #POST
    elif request.method == 'POST':
        serializer = BookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data  , status= status.HTTP_201_CREATED)
        return Response(serializer.data , status= status.HTTP_400_BAD_REQUEST)

# GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def fbv_pk(request , pk): 
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Get
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT':
        serializer = BookSerializer(book , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#4 Class Based View (cbv)
#GET POST
class cbv_list(APIView):
    def get(self , request):
            books = Book.objects.all()
            serializer = BookSerializer(books , many = True)
            return Response(serializer.data)
    def post(self , request):
        serializer = BookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data  , status= status.HTTP_201_CREATED)
        return Response(serializer.data , status= status.HTTP_400_BAD_REQUEST)
    

#GET PUT DELETE
class cbv_pk(APIView):

    def get_object(self , pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
    def get(self , request , pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    def put(self,request , pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request , pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


#5 MIXINS
    #GET POST
class mixins_list(mixins.ListModelMixin ,mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self , request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    
# GET PUT DELETE 
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self , request , pk):
        return self.retrieve(request)
    def put(self , request , pk):
        return self.update(request)
    def delete(self , request , pk):
        return self.destroy(request)
    

#6 Generics 
    #GET POST
class generics_list(generics.ListCreateAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer
    #GET PUT DELETE 
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

#7 ViewSet
    # GET POST PUT DELETE 
class viewsetsBook(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer