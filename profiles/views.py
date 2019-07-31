import serializers as serializers
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from . import serializers
from . import models
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.

class HelloApiView(APIView):
  """Test API View"""

  serializer_class = serializers.HelloSerializer

  def get(self,request,format = None):
    """Returns a list of APIView features."""
    an_apiview = [
      'Uses HTTP methods as functions(get,post,PUt,patch,delete)'
      'It is similar to traditional Django view'

    ]
    return Response({'message': 'Hello!','an_apiview': an_apiview})
  def post(self,request):
    """Create a hello message with our name"""

    serializer = serializers.HelloSerializer(data = request.data)
    if serializer.is_valid():
      name = serializer.data.get('name')
      message = 'Hello {0}'.format(name)
      return Response({'message':message})
    else:
      return Response(serializer.errors,status =  status.HTTP_400_BAD_REQUEST)

  def put(self,request,pk=None):
    """Handles updating an object"""
    return Response({'method': 'put'})

  def patch(self,request,pk=None):
    """only updates fields provided in the request"""
    return Response({'method': 'patch'})

  def delete(self,request,pk=None):
    """Delete an object"""
    return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
  """Test API ViewSet"""
  serializer_class = serializers.HelloSerializer

  def list(self,request):
    a_viewset = [
      'User actions (list,create,retrieve,update,partial_update)',
      'Automatically maps to URLS using routes'
      'Provides more functionality with less code'
    ]
    return Response({'message':'Hello','a_viewset': a_viewset})

  def create(self,request):
    """Create a new hello message."""
    serializer = serializers.HelloSerializer(data=request.data)
    if serializer.is_valid():
      name = serializer.data.get('name')
      message = 'Hello {0}'.format(name)
      return Response({'message':message})
    else:
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  def retrieve(self,request,pk=None):
    """Handles getting an object by its ID"""
    return Response({'http_method':'Get'})
  def update(self,request,pk=None):
    """Handles updating an object."""
    return Response({'http_method':'PUT'})

  def partial_update(self,request,pk=None):
    """Handles updating part of an object."""
    return Response({'http_method':'Patch'})

  def destroy(self,request,pk=None):
    """Hanles removing an object """
    return Response({'http_method':'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
  """Handling creating, reading and updating profiles."""

  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name','email',)

class LoginViewSet(viewsets.ViewSet):
  """"Checks email and password and returns an auth token"""
  serializer_class = AuthTokenSerializer

  def create(self,request):
    """Use the ObtainAuthToken APIView to validate and create a token"""
    return ObtainAuthToken().post(request)
