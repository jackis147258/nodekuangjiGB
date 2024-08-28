
from django.urls import re_path, path, include
# import app1.views
import traceback
from . import views
from app1.views import nextPage,htmlInfo
from django.views.generic import ListView



# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth import get_user_model



User = get_user_model()


# 序列化器是用来定义API的表示形式。
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets定义视图的行为。
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 路由器提供一个简单自动的方法来决定URL的配置。
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

router.register(prefix="TcSearch", viewset=views.TcSearchViewSet)

# router.register(prefix="nextPage", views=nextPage)

urlpatterns = [
    path('', include(router.urls)),   
    # path('login/', htmlInfo, name='htmlInfo'),
    path('api-auth/', include('rest_framework.urls')),
    # url(r'^snippets/$', views.SnippetList.as_view()),
    path('getaaa/', views.get_user, name='get_user'),
    
    path("fbv/list/", views.course_list, name="fbv-list"),
    path("cbvdk/list/", views.CourseList.as_view(), name="cbv-list"),
    path("ifTokenApi/", views.ifTokenApi, name="ifTokenApi"),
    path("ebc1/", views.ebc1, name="ebc1"),

]

# urlpatterns = [
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
# ]