# from django.db import models
from datetime import datetime
from mongoengine import *

class ToolInput(EmbeddedDocument):
    name = StringField(required=True)
    value = DynamicField(required=True)

class Tool(Document):
    label = StringField(required=True)
    description = StringField(required=True, null=True)
    inputs = ListField(EmbeddedDocumentField(ToolInput))

class User(Document):
    username = StringField(max_length=30)
    password = StringField(max_length=30)
    description = StringField(max_length=555)
    email = EmailField(max_length=30)
    friends = ListField(ReferenceField('self'))
    extra = DictField()
    user_level = StringField(max_length=30)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now = True)

class BlogExtension(EmbeddedDocument):
    further_read = StringField(required=True)
    references = ListField(StringField())

class Blog(DynamicDocument):
    owner = StringField(max_length=30)
    title = StringField(max_length=30)
    tags = ListField(StringField())
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Comment(EmbeddedDocument):
    author = StringField(max_length=30)
    text = StringField(max_length=555)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
class Post(Document):
    author = StringField(max_length=40)
    messanger = StringField(max_length=40)
    text = StringField(max_length=555)
    comments = ListField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now = True)

class Snippet(Document):
    created = DateTimeField(auto_now_add=True)
    title = StringField(max_length=100, blank=True, default='')
    code = StringField()
    linenos = BooleanField(default=False)
    language = StringField(max_length=100)
    style = StringField(max_length=100)

    class Meta:
        ordering = ('created',)
