#!c:\ProgramData\Anaconda3\python.exe

from xml.etree import cElementTree as ET

tree = ET.parse('../data/movies.xml')
root = tree.getroot()

tags_dict = {'type':'Type',
             'year':'Year',
             'format':'Format',
             'description':'Description',
             'rating':'Rating',
             'stars': 'Stars',
             'episodes' : 'Episodes'
            }

for child in root:
    if child.tag == 'movie':
        print ('***** Movie *****')
        print ('Title: %s' % child.attrib['title'])
        for subchild in child:
            print ('%s: %s' % (tags_dict[subchild.tag],subchild.text))





