from django import forms


class NewBlogForm(forms.Form):
    title = forms.CharField(max_length=256, help_text="Enter A Title For Your Blog Post",
                            error_messages={'required': 'Please Enter A Title'})
