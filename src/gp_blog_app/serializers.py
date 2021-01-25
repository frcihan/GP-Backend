from django.http import request
from rest_framework import serializers
from .models import Blog

class BlogListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    # detail_url = serializers.HyperlinkedIdentityField(
    #     view_name='detail',
    #     lookup_field='slug'
    # )

    class Meta:
        model = Blog
        fields = (
            # 'detail_url',
            'title',
            'content',
            # 'image',
            'status',
            'publish_date',
            'author',
            'slug',
            'comment_count',
            'view_count',
            'like_count'
        )

    def get_author(self, obj):
        return obj.author.username

class BlogCreateUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'content',
            # 'image',
            'status',
            'owner',
            'category',
        )

    def get_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False
