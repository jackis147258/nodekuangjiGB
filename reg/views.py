from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from .forms import SignUpForm,UserMoveForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import  Group
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()



def register(request,parent_id=None):
    if request.method == 'POST':
        # form = SignUpForm(request.POST)
        form = SignUpForm(request.POST, parent_id=parent_id)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # 用户创建后先不激活
            user.parent_id=parent_id
            user.save()
            current_site = get_current_site(request)
            subject = '激活您的账号'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm(parent_id=parent_id)
        
    return render(request, 'signup.html', {'form': form})



def activate(request, uidb64, token):
    
    # parent_id=request.POST.get('parent_id')
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_staff = True   # 设置用户为工作人员

        
        # 获取已存在的组
        group_name = "量化用户"
        group = Group.objects.get(name=group_name)

        # 将用户添加到该组
        user.groups.add(group)
      

        user.save()
        login(request, user)
        return redirect('/')

    else:
        return render(request, 'account_activation_invalid.html')
    
    
def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')  # 确保你有一个这个名称的模板

def resend_activation_link(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        if user and not user.is_active:
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            user.email_user(subject, message)
            return render(request, 'activation_link_sent.html')
    except User.DoesNotExist:
        # User doesn't exist or is already active, handle it here
        pass

    # Redirect to a failure page or show an error message
    return render(request, 'activation_link_failed.html')


# mptt 用户上下级 关系
# from django.shortcuts import render
# from .models import CustomUser

def user_hierarchy(request):
    root_nodes = CustomUser.objects.root_nodes()
    return render(request, 'user_hierarchy.html', {'root_nodes': root_nodes})

def user_detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    descendants = user.get_descendants()
    return render(request, 'user_detail.html', {'user': user, 'descendants': descendants})



def move_user(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    if request.method == 'POST':
        form = UserMoveForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = UserMoveForm(instance=user)
    return render(request, 'move_user.html', {'form': form})


# 接口 Ebc 方面




