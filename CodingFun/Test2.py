
acronyms = {'LOL': 'laugh out loud',
            'IDK': "I don't know",
            'TBH': 'to be honest'}

print(acronyms['LOL'])       

acronyms['XD'] = 'laughing emoji'

print(acronyms['XD'])

del acronyms['XD']

print(acronyms)

definition = acronyms.get('XD')

if definition:
    print(definition)
else:
  print("Key doesn't exist")
  
sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)
