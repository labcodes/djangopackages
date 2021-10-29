import logging
from time import sleep

from django.conf import settings
from django.core.management.base import BaseCommand

from github3 import login as github_login

from package.models import Package
from package.tasks import update_package_task
from core.utils import healthcheck

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Updates all the packages in the system. Commands belongs to django-packages.package"

    def handle(self, *args, **options):

        github = github_login(token=settings.GITHUB_TOKEN)

        for index, package in enumerate(Package.objects.iterator()):

            # Simple attempt to deal with Github rate limiting
            while True:
                print(f"github.ratelimit_remaining=={github.ratelimit_remaining}")
                if github.ratelimit_remaining < 50:
                    print(f"{__file__}::handle::sleep(120)")
                    sleep(120)
                break

            update_package_task.delay(package.id)

            print(f"{__file__}::handle::sleep(5)")
            sleep(5)
        healthcheck(settings.PACKAGE_HEALTHCHECK_URL)
