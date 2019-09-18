import requests
from lxml import html
from collections import Counter
from celery import shared_task 

from django.conf import settings

@shared_task
def demo(url): 
    page = requests.get(url)
    tree = html.fromstring(page.content)
    all_elms = tree.cssselect('*')
    all_tags = [x.tag for x in all_elms]
    baba = Counter(all_tags)
    return baba