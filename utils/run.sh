#!/bin/sh

celery -A jumia beat -l info
celery -A jumia.celery worker -l info

