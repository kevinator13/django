from rest_framework import serializers
from .models import App

class AppSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = App
		fields = ('id', 'url', 'name', 'paradigm')

#class AppSerializer(serializers.ModelSerializer):
#	class Meta:
#		model = App
#		fields = ('id', 'name', 'paradigm')

