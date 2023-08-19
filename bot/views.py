from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

class ViewId(APIView):
    serializer_class = MessageTextModelSerilizer

    def get(self,request,pk):
        try:
            queryset = self.get_queryset(pk)
        except ObjectDoesNotExist:
            return Response({"error":"Такого идентификатора не существует"},status = status.HTTP_404_NOT_FOUND)
        serializer = MessageTextModelSerilizer(queryset, many = True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def get_queryset(self,pk):

        return MessageText.objects.filter(user_id = UserId.objects.get( user_id=pk))
    

# Create your views here.
class MainView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
 
    serializer_class = MainSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id_value = int(request.data['user_id']) 
        print(user_id_value)
        data = UserId.objects.filter(user_id = user_id_value)
        if data.exists():
            create = MessageText.objects.create(
                                user_id = data.first(),
                                userText = request.data['userText'],
                                assistantText = request.data['assistantText'],
                                                )
            
            return Response(MessageTextModelSerilizer(create).data, status=status.HTTP_200_OK)
        if not data.exists():
            create = MessageText.objects.create(
                                user_id = UserId.objects.create(user_id = user_id_value),
                                userText = request.data['userText'],
                                assistantText = request.data['assistantText'],
                                                )
            return Response(MessageTextModelSerilizer(create).data, status=status.HTTP_200_OK)
       
        return Response(status=status.HTTP_400_BAD_REQUEST)




class ItemList(generics.ListAPIView):
    queryset = SystemTextModal.objects.all()
    serializer_class = SystemTextModalSerilaizer
