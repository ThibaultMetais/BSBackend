from rest_framework import serializers
from barriosolidario.models import User, NewsPost, HelpPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = (*[f.name for f in NewsPost._meta.get_fields()], "from_me")
        fields['from_me'] = request.user.id ==

class HelpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPost
        fields = '__all__'
