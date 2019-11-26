from rest_framework import serializers
from barriosolidario.models import User, NewsPost, HelpPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NewsPostSerializer(serializers.ModelSerializer):
    from_me = serializers.SerializerMethodField('is_me')

    def is_me(self, post):
      return post.user.id == self.request.user.id

    class Meta:
        model = NewsPost
        fields = ('id', 'content', 'picture', 'location', 'user', 'from_me')

class HelpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPost
        fields = '__all__'
