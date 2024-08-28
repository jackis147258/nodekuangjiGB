from django import forms
from app1.models import TcSearch,TcSport,TcWeb,TcOneTwo,T_TokenAddr,CategoryToken
class Myfrom(forms.Form):
    user=forms.CharField(label="name",max_length=100)
    sex=forms.CharField(widget=forms.TextInput)
    password = forms.CharField(max_length=32, label="密码",widget=forms.PasswordInput())

# Create your views here.

# class Myfrom1(forms.Form):
    
#     user1=forms.CharField()

FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)


class infoFrom(forms.ModelForm):

    tcWebs = forms.ModelMultipleChoiceField(label="博彩网站",queryset=TcWeb.objects.all(),
                                             widget=forms.CheckboxSelectMultiple(attrs={"class":"container-left-head-platform-content-item"}))
    
    tcSports = forms.ModelMultipleChoiceField(label="体育类",queryset=TcSport.objects.filter(type=1),
                                             widget=forms.CheckboxSelectMultiple,required=False)
    tcSportsDianJing = forms.ModelMultipleChoiceField(label="电竞类",queryset=TcSport.objects.filter(type=2),
                                             widget=forms.CheckboxSelectMultiple,required=False)
    # menOneTwos = forms.ModelMultipleChoiceField(label="两门/三门",queryset=TcOneTwo.objects.all(),
    #                                          widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=TcSearch
        fields=["profitRangeLittle","raceTime","tcWebs","tcSports","tcSportsDianJing"]
        # fields=["paiXu","profitRangeLittle","profitRangeBig","returnOnInvestmentLittle","returnOnInvestmentBig","raceTime","tcWebs","tcSports","tcSportsDianJing"]
        # fields=["paiXu","menOneTwo","tcWebs","gender"]   class="form-select form-select-sm"
        widgets={
            "paiXu":forms.Select(attrs={"class":"form-select form-select-sm"}),           
            "profitRangeLittle":forms.TextInput(attrs={"class":"form-control"}),
            # "profitRangeBig":forms.TextInput(attrs={"class":"form-control"}),
            # "returnOnInvestmentLittle":forms.TextInput(attrs={"class":"form-control"}),
            # "returnOnInvestmentBig":forms.TextInput(attrs={"class":"form-control"}),
            "raceTime":forms.Select(attrs={"class":"form-select form-select-sm"}),      
                        
            # "title2" : forms.CharField(
            # max_length=3,
            # widget=forms.Select(choices=FAVORITE_COLORS_CHOICES),
            # ),
           
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for name,field in self.fields.items():
            if name=="paiXu":
                continue
            # field.widget.attrs={"class":"form-control","placeholder":field.label}
            # field.widget.attrs={"class":"form-control"}


    # user=forms.CharField(label="name",max_length=100)
    # sex=forms.CheckboxInput()
    # password = forms.CharField(max_length=32, label="密码",widget=forms.PasswordInput())
   
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # favorite_colors = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=FAVORITE_COLORS_CHOICES,
    # )
    

class TokenForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TokenForm, self).__init__(*args, **kwargs)
        
        # 这里我们过滤分类，只显示当前用户的分类 category
        if user:
            self.fields['category'].queryset = CategoryToken.objects.filter(uid=user)

    class Meta:
        model = T_TokenAddr
        fields = '__all__'



class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryToken
        fields = '__all__'
        widgets = {
            'uid': forms.HiddenInput()
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CategoryForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['uid'].initial = user.id  # 注意，这里我们设置的是 user 的 ID
            #    self.fields['uid'].initial = user
    
   
