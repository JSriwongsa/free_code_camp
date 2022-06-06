#!/usr/bin/env python3
# ----- Web services -----
# There are two commonly used formats: XML and JSON
#XML (Extensible markup language)
     # - start tag > end tag > text content > attribute > self closing tag
# JSON (JavaScript Object Notation)
# Ex_JSON

import json
data = '''{
    "name" : "Muay",
    "phone" : {
        "tyoe" : "intl",
        "number" : "312 000 0000"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
info = json.loads(data)
print('Name:',info['name'] )
print('Hide:',info['email']['hide'])



import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])
