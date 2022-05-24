from rest_framework import serializers 
from .models import QAInput 

class CustomerSerializers(serializers.ModelSerializer): 
    class meta: 
        model=QAInput 
        fields='__all__'