# running django code outside the project

import sys, os, django

sys.path.append('/home/mihai/all/data/A_work/1_drf/src/newsapi')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsapi.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'newsapi.settings'
#print(os.environ)

django.setup()

#os.chdir("../newsapi")
print(f"pwd: {os.getcwd()}")
print(f"ls: {os.listdir()}")
#print(os.system("ls"))

#                            SERIALIZE 
#                            --------->
# (query sets,
# model instances, etc)                                (request, response)
# Dj Data types     ===>    Python Data types    ===>  Bytes (JSON encode) 
#         Serializer(Dj instance)            JSONRenderer
#         Serializer(data=python data)        JSONParser
#                   <===                         <===
#                            <-----------                             
#                             DESERIALIZE

from news.models import Article
from news.api.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

# SERIALIZE

article_instance = Article.objects.first()              #[django instance]
print(f"article(django instance): {article_instance}")
serializer = ArticleSerializer(article_instance)        #[python data type]
print(f"dictionary(python data): {serializer.data}")
json = JSONRenderer().render(serializer.data)           #[bytes]
print(json)

# DESERIALIZE

stream = io.BytesIO(json)                               #[bytes]
data = JSONParser().parse(stream)                       #[I) python data type]
print("I) dict(python data)",data)
serializer = ArticleSerializer(data=data)
print(serializer.is_valid())
if(serializer.is_valid()):
    print(f"II) ordered dict(python data){serializer.validated_data}")               #[II) python data type]
    serializer.save()
    article_instance = Article.objects.first()          #[django instance]
    print(f"article(django instance): {article_instance}")



