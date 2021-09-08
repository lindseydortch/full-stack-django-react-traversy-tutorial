from rest_framework import serializers
from leads.models import Lead 

# Lead Serializer 
class LeadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lead 
    fields = '__all__' # Means you want to bring in all the fields 