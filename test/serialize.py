import sys, os, django

sys.path.append('/home/mihai/all/data/A_work/1_drf/newsapi')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsapi.settings")
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
#from django.conf import settings
django.setup()

print(os.environ)

os.chdir("../newsapi")
print(os.getcwd())
print(os.listdir())
#print(os.system("ls"))

from news.models import Article
from news.api.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser




article_instance = Article.objects.first()
print(article_instance)