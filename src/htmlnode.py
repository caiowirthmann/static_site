from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

text_type_list = [
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
]

# text_type_text: This should become a LeafNode with no tag, just a raw text value.
# text_type_bold: This should become a LeafNode with a "b" tag and the text
# text_type_italic: "i" tag, text
# text_type_code: "code" tag, text
# text_type_link: "a" tag, anchor text, and "href" prop
# text_type_image: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)

# creating a function that receives text_type for each type seems a better approach
# instead of creating multiple if on the same function

# function that will convert TextNode.text_type to a HTMLnode
#
def text_node_to_html_node(TextNode):
    if TextNode.text_type not in text_type_list:
        raise Exception ("Text Type does not match any available type. Check TextNode.text_type attribute")
    text_node_html_converter(TextNode)
    pass

def text_node_html_converter(TextNode):
    if TextNode.text_type == text_type_text:
        node_text = LeafNode(None, TextNode.text)
        return node_text
    if TextNode.text_type == text_type_bold:
        node_bold = LeafNode("b", TextNode.text)
        return node_bold
    if TextNode.text_type == text_type_italic:
        node_italic = HTMLnode("i", TextNode.text, None, None)
        return node_italic
    if TextNode.text_type == text_type_code:
        node_code = HTMLnode("code", TextNode.text, None, None)
        return node_code
    if TextNode.text_type == text_type_link:
        node_link = HTMLnode("a", TextNode.text, None) # <--- completar metodo
        return node_link
    if TextNode.text_type == text_type_image:
        node_image = HTMLnode("code", )
        return node_image
    



class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props #    props is a dict{} with attributes of html tag

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError ("to html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
          props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    

class LeafNode(HTMLnode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props=props)
        # print(f"This is the LeafNode tag = {self.tag} // value = {self.value} // props = {self.props}")
        # print("LeafNode initialized with props:", self.props)
        
    def __repr__(self):
        return f"Leaf Node: ({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError ("leaf nodes require a value to render as a HTML")
        
        if self.tag is None:
            return f"{self.value}"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        # #starts constructing the HTML string <....
        # html_string = f"<{self.tag}"

        # if self.props:
        #     for key, val in self.props.items():
        #         # add HTML tag and corresponding value. example--> "href" tag and link
        #         html_string += f' {key}="   {val}"'
        # #close first tag <.., and value from node and close tag with </tag>
        # html_string += f">{self.value}</{self.tag}>"

        # return html_string
    
#classe faz o agrupamentos dos LeafNode
class ParentNode(HTMLnode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children=children, props=props)
    
    def __repr__(self):
        return f"Parent Node: ({self.tag}, {self.children}, {self.props})"
    
    def to_html(self):
        if self.tag == None:
            raise ValueError ("HTMLnode: No tag provided")
        if self.children == None:
            raise ValueError ("HTMLnode> No children provided")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props.to_html()}>{children_html}</{self.tag}>"

testLeaf = LeafNode(None ,"click me!", {"href" : "https://google.com"})
print(testLeaf.__repr__())
