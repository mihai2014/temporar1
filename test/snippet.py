# running django code outside the project

import sys, os, django

sys.path.append('/home/mihai/all/data/A_work/1_drf/src/tutorial')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'tutorial.settings'
#print(os.environ)

django.setup()


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io

# create dj object

#snippet = Snippet(code='foo = "bar"\n')
#snippet.save()

#snippet = Snippet(code='print("hello, world")\n')
#snippet.save()

# serialize

snippet = Snippet.objects.all()[0]                  #django
print(snippet)

serializer = SnippetSerializer(snippet)             #python
print(serializer.data)

content = JSONRenderer().render(serializer.data)    #bytes
print(content)

# deserialize

stream = io.BytesIO(content)                        #bytes
data = JSONParser().parse(stream)
print(data)                                         #python (dict)
serializer = SnippetSerializer(data=data)           
condition = serializer.is_valid()
if(condition):
    print(serializer.validated_data)                #python (ordered dict)
serializer.save()                                   #insert

# serializing query sets

serializer = SnippetSerializer(Snippet.objects.all(), many=True)  #dj (insert)
print(serializer.data)