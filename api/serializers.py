from rest_framework import serializers
from .models import Subscriber

class SubscriberSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    
    """ Note : If we use serializers.Serializer then we have to override the create method"""
    def create(self,validate_data):
        return Subscriber.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name  = validated_data.get('name',instance.name)
        instance.age   = validated_data.get('age',instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class SubscribeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('id','name','age','email')
