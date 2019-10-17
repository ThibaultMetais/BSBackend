from rest_framework import serializers
from barriosolidario.models import User, NewsPost, HelpPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = '__all__'

class HelpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPost
        fields = '__all__'
