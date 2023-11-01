from django import template
from django.utils import timezone
import logging
register = template.Library()
logger = logging.getLogger(__name__)
@register.filter(name="task_expired")
def is_expired_task(value):

    now = timezone.now()
    logger.debug(now)
    logger.debug(value)
    return value < now
