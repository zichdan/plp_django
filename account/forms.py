from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile, Post, Comment, Like


class RegisterForm(UserCreationForm):
    # add extre field
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', '<PASSWORD>', '<PASSWORD>']

    # a function to save cleaned data from the form
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False) # super function is refering to Parent class
        user.email = self.cleaned_data["email"] # handling additional fields
        if commit:
            user.save()
        return user




































        # class PostForm(forms.ModelForm):
        #     class Meta:
        #         model = Post
        #         fields = ['image', 'caption']
        #         widgets = {
        #             'image': forms.FileInput(attrs={'class': 'form-control'}),
        #             'caption': forms.TextInput(attrs={'class': 'form-control'}),
        #             }
        #         class CommentForm(forms.ModelForm):
        #             class Meta:
        #                 model = Comment
        #                 fields = ['comment']
        #                 widgets = {
        #                     'comment': forms.TextInput(attrs={'class': 'form-control'}),
        #                     }
        #                 class LikeForm(forms.ModelForm):
        #                     class Meta:
        #                         model = Like
        #                         fields = ['like']
        #                         widgets = {
        #                             'like': forms.TextInput(attrs={'class': 'form-control'}),
        #                             }<|endoftext|>
        #                         <fim_prefix><fim_suffix>e_name='ID')),
        #                         ('name', models.CharField(max_length=200)),
        #                         ('description', models.TextField()),
        #                         ('price', models.DecimalField(decimal_places=2, max_digits=10)),
        #                         ('image', models.ImageField(upload_to='images/')),

                                    
