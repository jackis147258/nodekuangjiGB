from django.shortcuts import render
from app1.models import TcSearch
# Create your views here.
from .serializers import CourseSerializer
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly


from django.http import JsonResponse

"""四、 DRF的视图集viewsets"""


class TcSearchViewSet(viewsets.ModelViewSet):
    queryset = TcSearch.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    # def perform_create(self, serializer):
    #     serializer.save(teacher=self.request.user)

@api_view(["GET", "POST"])
def get_user(request):
    if request.method == 'GET':
        usid = request.GET.get('usid','')
        if usid=='':
            return JsonResponse({'code':100101,'msg':'用户id不能为空'})
        if usid=='1':
            return JsonResponse({'code':100200,'msg':'查询成功','data':{'usid':1,'name':'james','age':36}})
        else:
            return JsonResponse({'code':100102,'msg':'未查询到用户数据'})

    else:
        return JsonResponse({'code': 100103, 'msg': '请求方法错误'})





"""一、 函数式编程 Function Based View"""


@api_view(["GET", "POST"])
@authentication_classes((BasicAuthentication, SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def course_list(request):
    """
    获取所有课程信息或新增一个课程
    :param request:
    :return:
    """
    if request.method == "GET":
        s = CourseSerializer(instance=Course.objects.all(), many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        s = CourseSerializer(data=request.data)  # 部分更新用partial=True属性
        if s.is_valid():
            s.save(teacher=request.user)
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes((BasicAuthentication, SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def course_detail(request, pk):
    """
    获取、更新、删除一个课程
    :param request:
    :param pk:
    :return:
    """
    try:
        # course = Course.objects.get(pk=pk)
        a=1
        course = 2
    except :
        return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == "GET":
            s = CourseSerializer(instance=course)
            return Response(data=s.data, status=status.HTTP_200_OK)

        elif request.method == "PUT":
            s = CourseSerializer(instance=course, data=request.data)
            if s.is_valid():
                s.save()
                return Response(data=s.data, status=status.HTTP_200_OK)
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




class CourseList(APIView):
    permission_classes = (IsAuthenticated,)  # settings.py中已设置，此处是多余的

    def get(self, request):
        """
        :param request:
        :return:
        """
        queryset = TcSearch.objects.all()
        s = CourseSerializer(instance=queryset, many=True)  # 这里是instance = xx
        # s = CourseSerializer(instance=queryset.first())
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        :param request:
        :return:
        """
        s = CourseSerializer(data=request.data)  # 这里是data = xx, return前要先调用.is_valid()
        if s.is_valid():
            s.save()
            # 分别是<class 'django.http.request.QueryDict'> <class 'rest_framework.utils.serializer_helpers.ReturnDict'>
            print(type(request.data), type(s.data))
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

def ifToken(zztoken):
    return True

# @api_view(["GET","POST"])

# @authentication_classes((BasicAuthentication, SessionAuthentication, TokenAuthentication))
# @permission_classes((IsAuthenticated,))
@api_view(["POST"])
def ifTokenApi(request):
    """
    获取所有课程信息或新增一个课程
    :param request:
    :return:
    """
    if request.method == "POST":        
        zztoken = request.data.get('zztoken') 
        # data = request.json()
        # zztoken = data.get('zztoken', 'your-default-token-value')       
       

        # 在这里进行 zztoken 的验证逻辑
        if ifToken(zztoken):
            return JsonResponse({'valid': True, 'message': 'ok token 可以'})
        else:
            return JsonResponse({'valid': False, 'message': 'Invalid zztoken'})

        return JsonResponse({'error': 'Invalid request method'})

# 处理 Ebc 定时计算
@api_view(["POST"])
def ebc1(request):
    """
    获取所有课程信息或新增一个课程
    :param request:
    :return:
    """
    if request.method == "POST":        
        zztoken = request.data.get('zztoken') 
        # data = request.json()
        # zztoken = data.get('zztoken', 'your-default-token-value')       
       

        # 在这里进行 zztoken 的验证逻辑
        if ifToken(zztoken):
            return JsonResponse({'valid': True, 'message': 'ok token 可以'})
        else:
            return JsonResponse({'valid': False, 'message': 'Invalid zztoken'})

        return JsonResponse({'error': 'Invalid request method'})

 