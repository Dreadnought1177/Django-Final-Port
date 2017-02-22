from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
# from rest_framework_mongoengine import generics as drfme_generics

from .models import *
from .serializer import *

class ToolViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = ToolSerializer

    def get_queryset(self):
        return Tool.objects.all()

    def put(self, request, pk):
        tool = self.get_object(pk)
        serializer = User_serializer(tool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(viewsets.ModelViewSet):
    serializer_class = User_serializer
    queryset = User.objects.all()
    lookup_field = 'id'

    def get(self, request):
        users = User.objects.all()
        serializer = User_serializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = User_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogList(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'id'

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentList(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Post.comments
    lookup_field = 'id'

    def get(self, request):
        comments = Post.comments
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # class User_view_set(viewsets.ModelViewSet):
#     lookup_field = 'id'
#     serializer_class = User_serializer
#
#     def get_queryset(self):
#         return User.objects.all()
#
# class MessageList(viewsets.ModelViewSet):
#     serializer_class = Message_serializer
#     queryset = Message.objects.all()
#
#     def get(self, request):
#         messages = Message.objects.all()
#         serializer = Message_serializer(messages, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = Message_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         message = self.get_object(pk=pk)
#         message.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, pk):
#         message = self.get_object(pk)
#         serializer = Message_serializer(message, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     class CommentList(viewsets.ModelViewSet):
#         serializer_class = Comment_serializer
#         queryset = Message.objects.all()
#
#         def get(self, request):
#             comments = Comment.objects.all()
#             serializer = Comment_serializer(comments, many=True)
#             return Response(serializer.data)
#
#         def post(self, request):
#             serializer = Comment_serializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         def delete(self, request, pk):
#             comment = self.get_object(pk=pk)
#             comment.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#
#         def put(self, request, pk):
#             comment = self.get_object(pk)
#             serializer = Comment_serializer(comment, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# #added the below lines of code
class SnippetList(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    lookup_field = 'id'

    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def homepage(request):
    # user = User(username='sky', email='chsbxtr@gmail.com', password = "Flakes1177").save()
    # tool = Tool(label="Not Chase", description="this is the description").save()
    # snippet = Snippet(title='Code snippet', code='this is not the code', linenos=False, language='Javascript', style='Beep').save()

    return render(request, 'index.html')