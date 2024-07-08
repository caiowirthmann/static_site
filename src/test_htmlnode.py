import unittest
from htmlnode import (
    HTMLnode,
    LeafNode
)


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLnode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf = LeafNode("a", "this is a link to a site",{"href": "boot.dev"})
        result = leaf.to_html()
        print(result)

    def no_tag(self):
        no_tag_value = LeafNode("", "")
        print(no_tag_value.to_html())

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
        
if __name__ == "__main__":
    unittest.main()
