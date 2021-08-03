# from typing_extensions import Required
from rest_framework import serializers
from posts.models import (PostModel, User)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"

        extra_kwargs = {
                "like":{"required":False,"read_only":True},
            }
    def validate_title(self, title):
        if title[0] == "#":
            raise serializers.ValidationError('title cannot be start with hash-tag')
        return title

    def validate_like(self, like):
        if like == None:
            like = 0
        elif like < 0:
            raise serializers.ValidationError('like cannot be negative')
        print(like)
        return like
    
    def validate_user(self, user):
        user = User.objects.filter(id=self.context['request'].user.id)
        if user:
            return user
        else:
            raise serializers.ValidationError('Error')
    # def validate(self, attrs):
    #     if attrs['like'] < 0:
    #         raise serializers.ValidationError("like cannont be minece")
        # return attrs

    def create(self, validated_data):
        if validated_data['post_type'] == 2:
            validated_data['title'] = None
            if validated_data['parent'] == None:
                raise serializers.ValidationError('For repost parent shoulb be selecte')
        postmodel_obj = PostModel(
            title = validated_data['title'],
            txt = validated_data['txt'],
            img = validated_data['img'],
            # like = validated_data['like'],
            post_type = validated_data['post_type'],
            parent = validated_data['parent'],
            user = validated_data['user'],
            userr = self.context['request'].user,

          )
        postmodel_obj.save()
        return postmodel_obj