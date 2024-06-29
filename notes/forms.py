from django import forms
from  .  import models
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ('title', 'text')
        labels = {
            'title' : "Write Your Note Subject Here",
            'text' : "Write Your Thoughts Heres"    
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text' : forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("We only accept Notes about Django!")
        return title
        
        