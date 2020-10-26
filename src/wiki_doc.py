import re
import sys

class WikiDoc:
    title=''
    author=''
    sections = []

    def __init__(self, title='New Document', author='None'):
        self.title = title
        self.author = author

    def create_section(self, level=1, title='Section X'):
        heading = '='*level
        new_sec = f'{heading} {title} {heading}'

        self.sections.append(new_sec)
        return new_sec

    def delete_section(self, section_number=1):
        return self.sections.pop(section_number - 1)

    def set_section_text(self, section_number=1, text='sample text', centre=False):
        fixed_text = re.sub(r'^\n', '', text)
        fixed_text = fixed_text.replace('\t', ':')

        fixed_text = re.sub(r'\d\.', '#', fixed_text)   
        fixed_text = _regex_looper(r':(\#)', '##', fixed_text)

        fixed_text = _regex_looper(r':(\*)', '**', fixed_text)

        if centre:
            fixed_text = '<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">' + fixed_text + '</div>'

        self.sections[section_number - 1] += '\n' + fixed_text

    def get_wiki(self):
        return {
            'title': self.title,
            'author': self.author,
            'sections': self.sections
        }

    def __str__(self):
        doc = ''
        for s in self.sections:
            doc = doc + s + '\n'
        return doc


def _regex_looper(regexp, replace_text, text):
    while re.search(regexp, text):
        text = re.sub(regexp, replace_text, text)
    return text
