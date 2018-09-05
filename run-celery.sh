#!/bin/sh

celery -A deployment.celeryapp worker -l info