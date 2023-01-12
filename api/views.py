from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
 

# Create your views here.
class UserRegister(APIView):
    

    def post(self,request):
        
        serializer=RegisterSerializer(data=request.data)
        
        data={}
        if serializer.is_valid():
           
            serializer.save()
            data["message"]="registered"
            data["data"]=serializer.data
            print(serializer.data)
        else:
            data=serializer.errors
        return Response(data)





