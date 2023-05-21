import json

from .models import SearchList
from django.views import View

from django.http import HttpResponse, JsonResponse

# 크롤링용 임포트
import requests

from bs4 import BeautifulSoup
