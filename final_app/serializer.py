# from rest_framework_mongoengine import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from rest_framework_mongoengine import *
from mongoengine import *

from .models import *

class ToolSerializer(DocumentSerializer):
    class Meta:
        model = Tool
        fields = '__all__'


class ExtensionSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = BlogExtension
        fields = '__all__'
class BlogSerializer(DocumentSerializer):
    # extension = ExtensionSerializer(many=False)

    class Meta:
        model = Blog
        fields = '__all__'
class CommentSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(DocumentSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'
        depth = 2
    def update(self, instance, validated_data):
        comments = validated_data.pop('comments')
        updated_instance = super(PostSerializer, self).update(instance, validated_data)
        updated_instance.comments.append(comments[-1])
        updated_instance.save()
        return updated_instance

    def create(self, validated_data):
        comments = validated_data.pop('comments')
        Postet = Post.objects.create(**validated_data)
        Postet.comments = []
        for comment_data in comments:
            Postet.comments.append(Comment(**comment_data))
        Postet.save()
        return Postet


class User_serializer(DocumentSerializer):
    class Meta:
        model = User
        fields ='__all__'

# class Comment_serializer(EmbeddedDocumentSerializer):
#     username = ReferenceField(User)
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
# class Message_serializer(DocumentSerializer):
#     username = ReferenceField(User)
#     comments = Comment_serializer(Comment,many=True)
#
#     class Meta:
#         model = Message
#         fields = '__all__'
# # added below lines
#
class SnippetSerializer(DocumentSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'


# def update(self, instance, validated_data):
#     comments = validated_data.pop('comments')
#     # comments = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in lst)]
#     updated_instance = super(PostSerializer, self).update(instance, validated_data)
#
#     for comment_data in comments:
#         updated_instance.comments.append(comment_data)
#
#     updated_instance.save()
#     return updated_instance