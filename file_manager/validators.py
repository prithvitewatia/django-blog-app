from abc import ABC
from django import forms


class AbstractValidator(ABC):
    def validate(self):
        # Get all methods starting with "validate_" in the subclass
        for method_name in dir(self):
            if method_name.startswith("validate_"):
                # Get the method by name and call it
                method = getattr(self, method_name)
                if callable(method):
                    method()


class ImageValidator(AbstractValidator):
    MAX_SIZE = 2 * 1024 * 1024  # 2MB

    def __init__(self, image):
        self.image = image

    def validate_image_size(self):
        if self.image.size > self.MAX_SIZE:
            raise forms.ValidationError('Image size should be less than 2MB.')

    def validate_mimetype(self):
        valid_mime_types = ['image/jpeg', 'image/png']

        if hasattr(self.image, 'content_type') and self.image.content_type not in valid_mime_types:
            raise forms.ValidationError('Invalid file type, only jpeg or png are allowed')
