import unittest
from utilities import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode
class TestUtilites(unittest.TestCase): # Name starts with "Test"
  def test_text(self):
      node = TextNode("This is a text node", TextType.NORMAL)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, None)
      self.assertEqual(html_node.value, "This is a text node")

  def test_bold(self):
      node= TextNode("This is a bold text node", TextType.BOLD)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "b")
      self.assertEqual(html_node.value, "This is a bold text node")

  def test_italic(self):
      node= TextNode("This is a italic text node", TextType.ITALIC)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "i")
      self.assertEqual(html_node.value, "This is a italic text node")
  
  def test_code(self):
      node= TextNode("This is a code text node", TextType.CODE)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "code")
      self.assertEqual(html_node.value, "This is a code text node")
  
  def test_link(self):
      node= TextNode("This is a link text node", TextType.LINK, "https://boot.dev")
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "a")
      self.assertEqual(html_node.value, "This is a link text node")
      self.assertEqual(html_node.props, {"href": "https://boot.dev"})
  
  def test_image(self):
      node= TextNode("This is a image text node", TextType.IMAGE, "https://boot.dev")
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "img")
      self.assertEqual(html_node.value, None)
      self.assertEqual(html_node.props, {"src": "https://boot.dev"})

if __name__ == "__main__":
    unittest.main()