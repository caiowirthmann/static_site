#this is the main code for the project
from textnode import TextNode

print('test for project')

def main():
    class1 = TextNode("texto de teste", "bold")
    class2 = TextNode("texto body", "block", "https://bootdev.com")

    print(class1.__repr__())
    print(class2.__repr__())

main()