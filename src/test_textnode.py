import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
    def test_eqmethod(self):
        node_eq1 = TextNode("text 1", "bold", "https://youtube.com")
        node_eq2 = TextNode("text 2", "bold", "https://youtube.com")
        self.assertFalse(node_eq1.__eq__(node_eq2))
        self.assertFalse(node_eq2.__eq__(node_eq1))
    
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node3= TextNode("testing if nodes are not equal", "italic", "http://google.com")
        node4 = TextNode("This should be different from node3", "header1")
        self.assertNotEqual(node3, node4)

    def test_url_image_none(self):
        nodeURL = TextNode("this node doesn't have a url attatched", "italic")
        nodeURL2 = TextNode("this node HAVE a url attatched", "bold", "https://boot.dev")
        self.assertTrue(nodeURL.url is None)
        self.assertFalse(nodeURL2.url is None)

    def test_empty(self):
        node_empty = TextNode("","bold")
        node_no_texttype = TextNode("node text", "")
        self.assertTrue(not node_empty.text)
        self.assertTrue(not node_no_texttype.text_type)

    def test_nonmatching_texttype(self):
        node_nmt = TextNode("sample text", "italic")
        node_nmt2 = TextNode("sample text", "bold")
        self.assertNotEqual(node_nmt, node_nmt2)

    def test_onlyURL(self):
        node_url = TextNode("text", "bold", "https://boot.dev")
        node_url2 = TextNode("text", "bold", "https://github.com")
        self.assertNotEqual(node_url, node_url2)


if __name__ == "__main__":
    unittest.main()
