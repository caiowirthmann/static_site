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



# print(teste_classe.__repr__())
# print(teste_classe2.__repr__())

# print (teste_classe.__eq__(teste_classe2))
