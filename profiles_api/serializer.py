from rest_framework import serializers


# converts Data input to pyhton object visa versa.
#similar to django form which u define and it has the various fields that u want to accept for the input for your api so if we're going to add if you want to post or update funtionality to our HelloAPIView we need to create serializer to receive the content that we post to the API.
class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing our APIView"""
    # accepts a name input and add to our API view & we are going to test functionaity of our API view
    name = serializers.CharField(max_length=10)