from django import forms
from django.contrib.auth.hashers import check_password
from .models import Fcuser
from django.core.exceptions import ObjectDoesNotExist
class RegisterForm(forms.Form):
    email = forms.EmailField(
            error_messages={
                'required': '이메일을 입력하세요.'
            },
            max_length = 64, label ='e-mail'
    )
    password = forms.CharField(
                error_messages={
                    'required': '비밀번호를 입력하세요.'
                },
                widget= forms.PasswordInput, label= "password"
    )
    re_password = forms.CharField(
                error_messages={
                    'required': '비밀번호를 입력하세요.'
                },
                widget= forms.PasswordInput, label= 'password check'
    )

    def clean(self):
        cleaned_data= super().clean() 
        email = cleaned_data.get('email')
        password = cleaned_data.get('password') 
        re_password = cleaned_data.get('re_password') 
        
        
        if password and re_password:
            if password !=re_password:
                self.add_error('password','비민번호가 서로 다릅니다.')
                self.add_error('re_password','비민번호가 서로 다릅니다.')
            

class LoginForm(forms.Form):
    email = forms.EmailField(
            error_messages={
                'required': '이메일을 입력하세요.'
            },
            max_length = 64, label ='e-mail'
    )
    password = forms.CharField(
                error_messages={
                    'required': '비밀번호를 입력하세요.'
                },
                widget= forms.PasswordInput, label= "password"
    )
   
    def clean(self):
        cleaned_data= super().clean() 
        email  = cleaned_data.get('email')
        password = cleaned_data.get('password') 

        if email and password:
            try:
                fcuser = Fcuser.objects.get(email=email)
            #except Fcuser.DoesNotExist:
            except ObjectDoesNotExist:
                self.add_error('email','아이디가 없습니다.')
                return

            if not check_password(password, fcuser.password):
                self.add_error('password','비밀번호가 틀렸습니다.')
          

    