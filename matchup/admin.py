from django import forms
from django.contrib import admin
from .models import LookingForPost
from games.models import OwnedGame

class LookingForPostForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super (LookingForPostForm,self).__init__(*args, **kwargs) # populate
        self.fields['games'].queryset = OwnedGame.object.filter(user=user)

    class Meta:
        exclude = ['']
        model = LookingForPost

class LookingForPostAdminForm(admin.ModelAdmin):
    form = LookingForPostForm

admin.site.register(LookingForPost)
