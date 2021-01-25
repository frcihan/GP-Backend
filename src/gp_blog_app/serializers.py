from django.db.models import fields
from django.http import request
from rest_framework import serializers
from gp_user_app.models import Profile
from .models import Blog, Comment, Like, Category
from django.db.models import Q

class CommentSerializer(serializers.ModelSerializer):
    # status = serializers.ChoiceField(choices=Blog.options)
    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'blog',
            'time_stamp',
            'content',
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)


class BlogListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='gp_blog_app:detail',
        lookup_field='slug'
    )

    class Meta:
        model = Blog
        fields = (
            'detail_url',
            'title',
            'content',
            'image',
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
            'image',
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
        
class BlogDetailSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Blog.OPTIONS)
    author = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    # like = LikeSerializer(many=True)
    owner = serializers.SerializerMethodField(read_only=True)
    update_url = serializers.HyperlinkedIdentityField(
        view_name='gp_blog_app:update',
        lookup_field='slug'
    )
    like_url = serializers.HyperlinkedIdentityField(
        view_name='gp_blog_app:like',
        lookup_field='slug'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='gp_blog_app:delete',
        lookup_field='slug'
    )
    comment_url = serializers.HyperlinkedIdentityField(
        view_name='gp_blog_app:comment',
        lookup_field='slug'
    )

    class Meta:
        model = Blog
        fields = (
            'like_url',
            'update_url',
            'delete_url',
            'comment_url',
            'id',
            'title',
            'content',
            'image',
            'status',
            'publish_date',
            'last_updated',
            'author',
            'status',
            'comments',
            'slug',
            'comment_count',
            'view_count',
            'like_count',
            'owner',
            'has_liked'
        )

    def get_author(self, obj):
        return obj.author.username

    def get_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False

    def get_has_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if Blog.objects.filter(Q(like__user=request.user) & Q(like__blog=obj)).exists():
                return True
            return False


