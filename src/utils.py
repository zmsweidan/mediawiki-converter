import os
from dicttoxml import dicttoxml
import xmlschema

class Utility:

    def write_file(self, file_name='doc', file_type='txt', contents='', write_option='w', xsd_schema=None):

        # "x" - Create a file only if it does not exist
        # "a" - Append to an existing file, or create a file if it does not exist
        # "w" - Write to an existing file, or create a file if it does not exist
        FULL_FILE_NAME = f'{file_name}.{file_type}'
        f = open(f'../exports/{FULL_FILE_NAME}', write_option)
        f.write(contents)
        f.close()

        print(f'/exports/{FULL_FILE_NAME} generated')
        
        if (file_type == 'xml' and xsd_schema):
            print('\txml schema is valid?',self.xsd_check(xsd_schema, file_name))

    def convert_to_xml(self, doc, is_string=True):
        xml_doc = dicttoxml(doc, custom_root='root', attr_type=False)
        xml_str = xml_doc.decode("utf-8") #.replace('\n', '<br />')
        return xml_str if is_string else xml_doc

    def xsd_check(self, xsd_file, xml_file):
        schema = xmlschema.XMLSchema(f'schemas/{xsd_file}.xsd')
        return schema.is_valid(f'../exports/{xml_file}.xml')
