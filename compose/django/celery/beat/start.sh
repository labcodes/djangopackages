#!/bin/bash

set -o errexit
set -o nounset


rm -f './celerybeat.pid'
celery -A settings.celery_app beat -l INFO
