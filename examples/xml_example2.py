#!c:\ProgramData\Anaconda3\python.exe

from xml.etree.ElementTree import Element, SubElement, Comment,tostring,ElementTree
from xml.dom import minidom
#from ElementTree_pretty import prettify


root_tag = 'house'
content_dict = [ 
                   {
                       'Address':'1234 Main Street',
                       'Rooms': '4',
                       'SquareFeet': '1200',
                       'description':'Awesome House!',
                   }
                ] 

root = Element(root_tag)
comment = Comment('Example of writing XML')
root.append(comment)
for house in content_dict:
    print (house)
    for key in house.keys():
        print (key)
        foo = house[key]
        print (foo)
        child = SubElement(root,key)
        child.text = foo

raw_string = tostring(root)
parsed_string = minidom.parseString(raw_string)
print (parsed_string.toprettyxml(indent='    '))
tree = ElementTree(root)
tree.write('outexample.xml')



