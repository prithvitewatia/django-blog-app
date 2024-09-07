from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import BlogPost


class BlogPostCreateUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BlogPostCreateUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.form_id = 'blog_post_create_update_form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout.append(Submit('submit', 'Submit'))

    class Meta:
        model = BlogPost
        fields = ['title', 'body']

    def clean(self):
        cleaned_data = super().clean()
        post = self.instance
        if post.pk:
            if post.author.user != self.user:
                raise forms.ValidationError('You cannot edit this post.')
        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)
        if not post.pk:
            post.author = self.user.profile
        if commit:
            post.save()
        return post
