from rest_framework import serializers

from tasks.models import *


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserReg
        fields=["name","phone_number"]
       

   
    