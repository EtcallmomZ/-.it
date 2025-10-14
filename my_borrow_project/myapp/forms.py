from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BorrowRequest

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='กรอกอีเมลที่ถูกต้อง'
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class BorrowRequestForm(forms.ModelForm):
    class Meta:
        model = BorrowRequest
        # อันนี้คือ คนยืมจะกรอกใส่เข้ามา
        fields = ['quantity' , 'start_date','end_date']

        widgets = {
            'start_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'end_date' : forms.DateInput(attrs={'type' : 'date', 'class': 'form-control'})
        }