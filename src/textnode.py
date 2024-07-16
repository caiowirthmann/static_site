from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

teste_classe = TextNode("texto de exemplo", "texto é um header")
teste_classe2 = TextNode("texto de exemplo", "texto é um header")


    
def text_node_to_html_node(TextNode):
    if TextNode.text_type == text_type_text:
        return LeafNode(None, TextNode.text)
    if TextNode.text_type == text_type_bold:
        return LeafNode("b", TextNode.text)
    if TextNode.text_type == text_type_italic:
        return LeafNode("i", TextNode.text, None, None)
    if TextNode.text_type == text_type_code:
        return LeafNode("code", TextNode.text, None, None)
    if TextNode.text_type == text_type_link:
        return LeafNode("a", TextNode.text, None, {"href" : TextNode.url}) # <--- completar metodo
    if TextNode.text_type == text_type_image:
        return LeafNode("img", None, None, {"src" : TextNode.url, "alt" : TextNode.text})
    raise Exception (f"Text Type {TextNode.text_type} does not match any available type. Check TextNode.text_type attribute")



# print(teste_classe.__repr__())
# print(teste_classe2.__repr__())

# print (teste_classe.__eq__(teste_classe2))
