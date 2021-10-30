from django import forms
from .models import Comments, Posts, User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username','profile_pic','password1','password2')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments 
        fields = ("comment",)
        widgets = {
          'comment': forms.Textarea(attrs={'rows':2, 'cols':15}),
        }
    
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        self._id = kwargs.pop('id')
        super(CommentForm, self).__init__(*args, **kwargs)
    def save(self, commit=True):
        inst = super(CommentForm, self).save(commit=False)
        inst.shared_by = self._user
        inst.shared_post = self._id
        if commit:
            inst.save()
            self.save_m2m()
        return inst
class PostCreate(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("title",'image','content','category',)
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(PostCreate, self).__init__(*args, **kwargs)
    def save(self, commit=True):
        inst = super(PostCreate, self).save(commit=False)
        inst.creator = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst
class profileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','profile_pic']