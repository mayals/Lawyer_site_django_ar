from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.core.exceptions import ValidationError

# ----------register form ---------------------#
class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم', max_length=100, required=True,help_text='لا يُسمح بالفراغات')
    first_name = forms.CharField(label='الإسم الأول', max_length=100, required=True)
    last_name  = forms.CharField(label='الإسم الأخير', max_length=100, required=False)
    email = forms.CharField(label='البريد الألكتروني', max_length=200, required=True)
    password1 = forms.CharField(label='مفتاح الدخول', min_length=8, required=True,help_text='إستخدم 8 وأكثر', widget=forms.PasswordInput())
    password2 = forms.CharField(label='تأكيد مفتاح الدخول', min_length=8,required=True, help_text='إستخدم 8 وأكثر', widget=forms.PasswordInput())
#----- to costumize the RegisterForm fields -----# 
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
# ------- to check that password2 equal password1 -----#
    def clean_password2(self):
        if  self.cleaned_data['password1']!= self.cleaned_data['password2']:
            ValidationError('password2', code='invalid password')
            # raise forms.ValidationError('خطأ ، مفتاح الدخول غير متطابق')
        return self.cleaned_data['password2']
# ------- to check that username (unique) not used before -----#
    def clean_username(self):
        if User.objects.filter(username = self.cleaned_data['username']).exists():
            ValidationError('username', code='invalid username')
            # raise forms.ValidationError('أدخل أسم آخر ، نأسف لايمكن تكرار إسم المستخدم،أسم المستخدم الذي أخترته موجود مسبقا')
        return self.cleaned_data['username']






# ----------login form ---------------------#
class LoginForm(forms.ModelForm):
    username = forms.CharField(label='أسم المستخدم', max_length=100, required=True)
    password = forms.CharField(label='مفتاح الدخول', min_length=8, required=True, widget=forms.PasswordInput())  

#----- to costumize the LoginForm fields -----#   
    class Meta:
        model = User
        fields = ['username','password']







#--- the next two update class forms will put in the same view fhunction __ and display in the same html form--

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='الإسم الأول', max_length=100, required=True)
    last_name  = forms.CharField(label='الإسم الأخير', max_length=100, required=False)
    # email = forms.CharField(label='Email', max_length=200, required=True, disabled=False)
    email = forms.CharField(label='البريد الألكتروني', max_length=200, required=True)
    
    class Meta:
        model = User
        #fields = ('_all_',) -- not work in one to one relationship !!
        fields = ['first_name','last_name','email']


class UpdateProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        #fields = ('_all_',)-- not work in one to one relationship !!
        fields = ['prof_image','prof_mob', 'gender']


#----------------------------------------------------------------------------
