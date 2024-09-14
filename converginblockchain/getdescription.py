from nltk.corpus import wordnet 
from django.db import connection
syn = wordnet.synsets("Plague") 
description = ''
print(type(syn))
if len(syn)!=0:
    description = syn[0].definition() 
    print(*syn[0].examples())
else:
    description = 'No Data found'

print('Desc',description)


