 ["TagWidget()", "tags", "widgets"]
["CommentForm(forms.ModelForm)", "model = Comment", "content"]
from django.forms import ModelForm
from . models import *

class login_user_form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
