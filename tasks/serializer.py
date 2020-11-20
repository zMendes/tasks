from rest_framework import serializers
from .models import Task
 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ['title','pub_date','description']