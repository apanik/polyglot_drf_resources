from django.urls import path,include
from .views import subsciber,hello_world,SubscriberView,SubscriberView_2, SubscriberViewRetrive, \
    SubscriberViewRetrive_2, SubscribeDestroyAPIView, SubscriberUpdateAPIView, RetrieveUpdateAPI

urlpatterns = [
    # Hello World API 
    path('hello_world',hello_world,name="hello_world"),
    #  API for create and get all the list of Subsciber 
    path('subsciber',subsciber.as_view(),name="subscriber"),
    #  Same API functionality as above but build by generics API view
    path('gen-sub',SubscriberView.as_view(),name="gen-sub"), 
    #  Same API functionality as above but difference is it uses Model Serializer except serializers.Serializers 
    path('gen-sub-2',SubscriberView_2.as_view(),name="gen-sub-2"),
    #  Generic Retrive API View using serializers.Modelserializer
    path('gen-sub-rt/<int:id>',SubscriberViewRetrive.as_view(),name="gen-sub-rt"),
    #  Generic Retrive API View using serializers.Serializer
    path('gen-sub-rt-2/<int:id>',SubscriberViewRetrive_2.as_view(),name="gen-sub-rt-2"),
    #  Generic Destroy/Delete API View
    path('gen-sub-del/<int:id>',SubscribeDestroyAPIView.as_view(),name="gen-sub-del"),
    # Generic Update API view 
    path('gen-sub-up/<int:id>',SubscriberUpdateAPIView.as_view(),name="gen-sub-up"),
    # Update and Delete with Generic
    path('gen-sub-ru/<int:id>',RetrieveUpdateAPI.as_view(),name="gen-sub-ru"),

]
