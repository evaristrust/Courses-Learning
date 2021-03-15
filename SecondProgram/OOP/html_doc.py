class Tag(object):
    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents
    def __str__(self):
        return '{0.start_tag}{0.contents}{0.end_tag}'.format(self)
        # return '{}{}{}'.format(self.start_tag, self.contents, self.end_tag)
    def display(self, file=None):
        print(self, file=file)
#creating the doctype class
class DocType(Tag):
    def __init__(self):
        super().__int__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"' , '')
        self.end_tag = '' # the doctype doesn't have an end tag
# creating a Head clas
class Head(Tag):
    def __init__(self):
        super().__int__('Head', '') # Initially setting the content empty
#creating a body class
class Body(Tag):
    def __init__(self):
        super().__int__('Body', '') # Body contents will be built separately
        self._body_contents = []
    #let's now add tags
    def addTag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)
    #display the contents
    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
        super().display(file=file)
#Create htmldoc class
class HtmlDoc(object):
    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def addTag(self, name, contents):
        self._body.addTag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)

if __name__ == '--main__':
    my_page = HtmlDoc()
    my_page.addTag('h1', 'This is the first header')
    my_page.addTag('h2', 'This is the second header')
    my_page.addTag('p', 'The paragraph looks like this')
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)







