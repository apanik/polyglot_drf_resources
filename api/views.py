from django.shortcuts import render,get_object_or_404
from .models import Subscriber
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, \
    UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import SubscriberSerializer, SubscribeModelSerializer
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(["POST"])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username = username, password = password)
    if not user:
        return Response({"error: Login Failed"},status=HTTP_401_UNAUTHORIZED)
    token,_ = Token.objects.get_or_create(user=user)
    return Response({"token":token.key})




@api_view(['GET','POST'])
def  hello_world(request):
    """ Example API """
    if request.method == "POST":
        return Response({"Message" : "Hello World"})
    else:
        name = request.data.get("name")
        if not name:
            return Response({"Message" : "No name passed"})
        return Response({"Message":"Hello {}".format(name)})

# Using APIView
class subsciber(APIView):
    def get(self,request):
        """ Getting all subsciber list if the request is GET """
        all_subscriber = Subscriber.objects.all()
        serialized_subscribers = SubscriberSerializer(all_subscriber,many=True)
        return Response(serialized_subscribers.data
        )
        

    def post(self,request):
        """ Getting the posted data form user/server and after checking saving into db """
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
           subscriber_instance = Subscriber.objects.create(**serializer.data)
           return Response(
               {
                   "message" : "Created a New Subscirber",
                   "id" : subscriber_instance.id
               }
           )
        else:
            return Response({"Errors": serializer.errors })

# Using generics API View  
class SubscriberView(CreateAPIView,ListAPIView):
    """ Usage : create a new Object and Generate a List of all Subscribers """
    serializer_class = SubscriberSerializer # serializers.Serializer
    queryset = Subscriber.objects.all() 
    
# Using generics API View  
class SubscriberView_2(CreateAPIView,ListAPIView):
    """ Usage : create a new Object and Generate a List of all Subscribers """
    serializer_class = SubscribeModelSerializer # serializers.ModelSerializer
    queryset = Subscriber.objects.all()

# Using generics API View  
class SubscriberViewRetrive(RetrieveAPIView):
    """ Usage : Gives Single object matched by ID """
    serializer_class = SubscribeModelSerializer # serializers.ModelSerializer
    queryset = Subscriber.objects.all()
    lookup_field = 'id' # will fetch by given id

# Using generics API View  
class SubscriberViewRetrive_2(RetrieveAPIView):
    """ Usage : Gives Single object matched by ID """
    serializer_class = SubscriberSerializer # serializers.Serializer
    queryset = Subscriber.objects.all() 
    lookup_field = 'id' # will fetch by given id


class SubscribeDestroyAPIView(DestroyAPIView):
    """ Usage : Delete an obj """
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    lookup_field = 'id'

class SubscriberUpdateAPIView(UpdateAPIView):
    """ Usage : Update an obj """
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    lookup_field = 'id'

class RetrieveUpdateAPI(RetrieveUpdateAPIView):
    """ Usage : Rertrive & Update With same time """
    serializer_class = SubscribeModelSerializer # Model Serializer
    queryset = Subscriber.objects.all()
    lookup_field = 'id'


class RetrieveUpdateAPI(RetrieveUpdateAPIView):
    """ Usage : Rertrive & Update With same time """ 
    serializer_class = SubscriberSerializer # serializers.Serializer
    queryset = Subscriber.objects.all()
    permisson_classes = (IsAuthenticated,)
    lookup_field = 'id'


class MultipleFieldLookupMixin:
    """ Apply this mixin to any view or viewset to get multiple field filtering based on lookup field"""
    def get_object(self):
        queryset = self.get_queryset() # Get Base Queryset
        queryset = self.filter_queryset(queryset) # Apply Any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset,**filter)
        self.check_object_permissons(self.request,obj)
        return obj

