from wiki_doc import WikiDoc
from utils import Utility


# CREATE DOC
doc = WikiDoc()
doc.create_section()
text_1 = """
This is a test.
	indent once
		indent twice
			indent thrice
* Bullet point 1
	* Bullet point 2
		* Bullet point 3
1. item 1
2. item 2
3. item 3
	1.item 3-1
"""
doc.set_section_text(text=text_1)

doc.create_section(2, 'Section 1.1')
text_2 = """
This text is centred
test 12345
	'''test 6789'''
"""
doc.set_section_text(2, text_2, True)

doc.create_section(1, 'Section 2')
doc.delete_section(3)


# WRITE FILES
util = Utility()
doc_txt = doc.__str__()
doc_xml = util.convert_to_xml(doc.get_wiki())
util.write_file(contents=doc_txt)
util.write_file(contents=doc_xml, file_type='xml', xsd_schema='wiki')


print('SCRIPT COMPLETED')
