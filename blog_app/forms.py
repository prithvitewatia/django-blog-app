from django import forms

from .models import BlogPost


class BlogPostCreateUpdateForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=200)
    body = forms.Textarea()

    def clean(self):
        super().clean()
        if not self.errors:
            # If there are no errors, you can also validate the form data here
            pass

    class Meta:
        model = BlogPost
        fields = ["title", "body"]
