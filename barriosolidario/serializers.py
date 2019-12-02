from rest_framework import serializers
from barriosolidario.models import User, NewsPost, HelpPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NewsPostSerializer(serializers.ModelSerializer):
    from_me = serializers.SerializerMethodField('is_me')
    username = serializers.SerializerMethodField('get_username')

    def is_me(self, post):
        #return post.user.id == self.context['request'].user.id
        # We don't have login feature right now (AnonymousUser used), so we are using a temporary solution
        return str(post.user.id) == "9781200a-4862-4daa-9231-a759c28d7ff7"

    def get_username(self, post):
        return User.objects.get(id=post.user.id).username

    class Meta:
        model = NewsPost
        fields = ('id', 'content', 'picture', 'location', 'user', 'from_me', 'username', 'created')

class HelpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPost
        fields = '__all__'
