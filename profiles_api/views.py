from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from profiles_api import serializers


# status import is list of handy HTTP status codes that can use when returning responses fom your API
# these status codes will be used in our post in post function handler
class HelloApiView(APIView):
    """Test API View"""
    serializers_class = serializers.HelloSerializer
    
    # Read Method
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP Method as function (get, post, patch, put, delete)', 
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        # HTTP converted to json file and responds needs to be store in dictinary
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    # Create Method
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializers.HelloSerializer(data=request.data)
        
        #
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})                  
            
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            