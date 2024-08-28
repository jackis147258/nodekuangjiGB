from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='必填。告知有效的电子邮件地址。')
    
        # 增加初始化方法来接收parent_id参数
    def __init__(self, *args, **kwargs):
        self.parent_id = kwargs.pop('parent_id', None)
        super(SignUpForm, self).__init__(*args, **kwargs)
    
    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     if self.parent_id:
    #         # 将 parent_id 赋值给 user 的 parent 字段
    #         user.parent_id = self.parent_id
    #     if commit:
    #         user.save()
    #     return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )



class UserMoveForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['parent']
