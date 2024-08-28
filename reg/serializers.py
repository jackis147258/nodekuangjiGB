#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"


from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework import serializers

from app1.models import TcSearch,webInfo
from .models import CustomUser ,ebcJiaSuShouYiJiLu,tokenZhiYaJiShi,payToken,userToken
from typing import Optional
from .utils import get_message

 

class CourseSerializer(serializers.ModelSerializer):
    # teacher = serializers.ReadOnlyField(source='teacher.username')  # 外键字段 只读
    

    class Meta:
        model = TcSearch  # 写法和上面的CourseForm类似
        # exclude = ('id', )  # 注意元组中只有1个元素时不能写成("id")
        # fields = ('id', 'name', 'introduction', 'teacher', 'price', 'created_at', 'updated_at')
        fields = '__all__'
        depth = 2

 
class CustomUserSerializer(serializers.ModelSerializer):
    cengShu = serializers.SerializerMethodField()
    # additional_data = serializers.SerializerMethodField()
    tokenNum = serializers.SerializerMethodField()



    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ("id","username", "userStakesA","userStakesB", "userStakesBfanHuan", "fanHuan","EbcCreated_at", "EbcLastFanHuan_at", "status", "parent","kapaiLevel","userLevel","tuanduiLevel","kapaiA","kapaiB","kapaiC","cengShu","tokenNum" )


    def get_tokenNum(self, obj):
        now_userToken = obj.usertoken_set.first() # type: Optional[userToken] 
        if not now_userToken:
            return {
            "USDT2": 0 ,
            "YL": 0 ,
            "JZ":0 ,            
        }
        
        return {
            "USDT2": now_userToken.usdtToken ,
            "YL": now_userToken.ylToken  ,
            "JZ":now_userToken.jzToken ,
        }
 
    # 获得可购买矿机
    def get_cengShu(self, obj):
        cengShu = obj.cengShu
        # 在这里进行基于 cengShu 的计算
        calculated_data = self.calculate_data_based_on_cengShu(cengShu)
        return calculated_data

    def calculate_data_based_on_cengShu(self, cengShu):
        # 根据 cengShu 进行自定义计算
        # 这里是示例代码，替换为实际计算逻辑

        # return {
        #     "cengShu": cengShu ,
        #     "jiaGe": 1 ,
        #     "tiaoJiao":2 ,
        #     "riShouYi":4 ,
        # }
        from .viewsNodeKJ import nodes_att_daily_rate,nodes_arr_siyang_payment,lou_ceng_gao_du 

        lang_value = self.context.get('lang')  # 从上下文中获取 lang 值 
        return {
            "kuangJiShu": cengShu ,
            "jiaGe": str(nodes_arr_siyang_payment['nodeKJ'+str(cengShu)])+'/GB'  ,
            "tiaoJiao":   get_message(lang_value, 'tiaoJiao_'+str(cengShu)) ,  #lou_ceng_gao_du[cengShu] ,
            "riShouYi": 'Daily Earnings '+str(nodes_att_daily_rate['nodeKJ'+str(cengShu)])+'%' ,
        }



class ebcJiaSuShouYiJiLuSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = ebcJiaSuShouYiJiLu
        # fields = '__all__'
        fields = ('id','uidA','uidB','status' ,'created_at', 'liuShuiId','Layer','fanHuan','Remark' ,)        
        
    def get_status(self, obj):
        # 将整数状态映射到相应的字符串表示
        return "已生效" if obj.status == 1 else "未生效"



class tokenZhiYaJiShiSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = tokenZhiYaJiShi
        # fields = '__all__'
        fields = ('id','tokenName','number','zhiYaTime' ,'kaiShiTime','status','uid' ,'Remark','uTime','amount' ,'amountType',)        
        
    def get_status(self, obj):
        # 将整数状态映射到相应的字符串表示
        return "已释放" if obj.status == 1 else "质押中"
    

class payTokenSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = payToken
        # fields = '__all__'
        fields = ('id', 'uidB','status' ,'created_at',  'Layer','amount','Remark' ,)        
        
    def get_status(self, obj):
        # 将整数状态映射到相应的字符串表示
        t_back="未生效"
        if obj.status == 1:
            t_back="返还"

        if obj.status == 2:
            t_back="hash验证失败"

        if obj.status == 3:
            t_back="hash验证成功"

        
        # return "到账" if obj.status == 3 else "未到账"
        return t_back
    

class webInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = webInfo
        fields = '__all__'
        # fields = ("id","username", "userStakesA","userStakesB", "userStakesBfanHuan", "fanHuan","EbcCreated_at", "EbcLastFanHuan_at", "status", "parent","kapaiLevel","userLevel","tuanduiLevel","kapaiA","kapaiB","kapaiC",  )

 