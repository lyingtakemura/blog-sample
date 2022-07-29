from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    '''
    Read-only fields are included in the API output but should not be included
    in the input during create or update operations. Any 'read_only' fields
    that are incorrectly included in the serializer input will be ignored.

    Set this to True to ensure that the field is used when serializing
    a representation, but is not used when creating or updating an instance
    during deserialization.
    '''
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=128)
    body = serializers.CharField(max_length=512)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ("user", "title", "body", "created_at")
