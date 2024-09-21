import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

from .validators import ImageValidator
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        file_obj = request.FILES['file']
        ImageValidator(file_obj).validate()
        image_path = default_storage.save(file_obj.name, file_obj)
        image_url = default_storage.url(image_path)
        logger.info(f'Image uploaded to {image_url}')
        return JsonResponse({'location': image_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)


