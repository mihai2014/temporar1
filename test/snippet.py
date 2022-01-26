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

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()