from rest_framework import serializers
from crystals.models import Crystal

class CrystalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crystal
        fields = '__all__'
        # fields = ('id','category','weight','lenght','height','origin','title','price')