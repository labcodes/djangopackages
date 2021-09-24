from settings import celery_app
from celery.utils.log import get_task_logger

from .models import Package


logger = get_task_logger(__name__)


@celery_app.task()
def update_package_task(package_id):
    package = Package.objects.get(id=package_id)
    logger.info(f'Start updating package {package.id}')

