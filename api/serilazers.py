from rest_framework import serializers
from .models import Student

class StudentSerlazers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']
        
