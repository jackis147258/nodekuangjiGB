#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"


from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework import serializers

from app1.models import TcSearch


class CourseForm(forms.ModelForm):
    class Meta:
        model = TcSearch
        fields = ('uid', 'paiXu')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # teacher = serializers.ReadOnlyField(source='teacher.username')  # 外键字段 只读

    class Meta:
        model = TcSearch  # 写法和上面的CourseForm类似
        # exclude = ('id', )  # 注意元组中只有1个元素时不能写成("id")
        # fields = ('id', 'name', 'introduction', 'teacher', 'price', 'created_at', 'updated_at')
        fields = '__all__'
        depth = 2

# class CourseSerializer(serializers.HyperlinkedModelSerializer):
#     teacher = serializers.ReadOnlyField(source='teacher.username')
#
#     class Meta:
#         model = Course
#         # url是默认值，可在settings.py中设置URL_FIELD_NAME使全局生效
#         fields = ('id', 'url', 'name', 'introduction', 'teacher', 'price', 'created_at', 'updated_at')
