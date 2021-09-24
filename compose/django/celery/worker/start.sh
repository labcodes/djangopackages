#!/bin/bash

set -o errexit
set -o nounset


# watchgod celery.__main__.main --args -A celery_app worker -l INFO
celery -A settings.celery_app worker -l INFO
