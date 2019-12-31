from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required' : 'Please enter a title'                    
        }, 
        max_length=128, label="title")
    contents = forms.CharField(
        error_messages={
            'required' : 'Please enter your contents'                    
        }, 
        widget=forms.Textarea, label="contents")
    tags = forms.CharField(required=False, label="tags")