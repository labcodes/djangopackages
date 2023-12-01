from settings import celery_app
from celery.utils.log import get_task_logger

from .exceptions import PackageUpdaterException
from .models import Package


logger = get_task_logger(__name__)


@celery_app.task()
def update_package_task(package_id):
    package = Package.objects.get(id=package_id)
    logger.info(f'Start updating package {package.id}')

    try:
        try:
            package.fetch_metadata(fetch_pypi=False)
            package.fetch_commits()
        except Exception as e:
            logger.error(
                f"Error while fetching package details for {package.title}."
            )
            raise PackageUpdaterException(e, package.title)
    except PackageUpdaterException:
        logger.error(f"Unable to update {package.title}", exc_info=True)
