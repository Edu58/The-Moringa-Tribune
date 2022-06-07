from django import forms
from .models import Article
from tinymce.widgets import TinyMCE


class NewletterForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=30)
    email = forms.EmailField(label="Email")


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
