from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.

class HelloApiView(APIView):
  """Test API View"""

  def get(self,request,format = None):
    """Returns a list of APIView features."""
    an_apiview = [
      'Uses HTTP methods as functions(get,post,PUt,patch,delete)'
      'It is similar to traditional Django view'

    ]
    return Response({'message': 'Hello!','an_apiview': an_apiview})
