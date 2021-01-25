#!/usr/local/bin/python3

import sys
import re
import csv

author_separator = ';'
email_separator = ','

'''
First Name,Last Name,Credentials,Email
John,Smith,PhD,john@smith.com<mailto:john@smith.com>
'''

inputfile = 'sigcse2021-sheridan-info-dump.csv' 

try:
  with open(inputfile, encoding='utf8') as f:
    content = csv.DictReader(f)

    output = open('sigcse2021-pathable-speakers.csv', 'w', encoding='utf8')

    output.write('Email,First Name,Last Name,Affiliation\n')
    authors = {}

    i = 0
    for row in content:
      author_fn = row['Author First Name'].strip()
      if row['Author Middle Name'].strip():
        author_fn += ' ' + row['Author Middle Name'].strip()
      author_ln =  row['Author Last Name'].strip()
      email = row['Author Email'].strip()
      affiliation = row['Affiliation'].strip()
      if email in authors and (author_fn, author_ln, affiliation) not in authors[email]:
        authors[email].append( (author_fn, author_ln, affiliation) )
      else:
        authors[email] = [(author_fn, author_ln, affiliation)]

      i += 1

    for email,entries in authors.items():
      for e in entries:
        output.write('"<mailto:%s>",%s,%s,"%s"\n' % ((email,) + e))

      
    output.close()

except Exception as e:
    print('File could not be opened.', e)
    sys.exit(3)