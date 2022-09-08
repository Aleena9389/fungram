from django import forms  
#from django.contrib.auth.models import UserCreationForm
#from django.db import forms
from SignUp.models import SignUp,Comment
 
class SignUpForm(forms.ModelForm):  
    class Meta:  
        model = SignUp  
        fields = ('name','username','birthdate','email','phone','password',)
         
class commentForm(forms.ModelForm):  
    class Meta:  
        model = Comment  
        fields = ('comment',)