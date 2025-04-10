import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html_single(self):
    node = HTMLNode("div", "Hello World!", None, {"class": "container"})
    expected = ' class="container"'
    self.assertEqual(node.props_to_html(), expected)
  
  def test_props_to_html_multiple(self):
    node = HTMLNode("div", "Hello World!", None, {"class": "container", "id": "main"})
    expected = ' class="container" id="main"'
    self.assertEqual(node.props_to_html(), expected)
  
  def test_props_to_html_empty(self):
    node = HTMLNode("div", "Hello World!", None, {})
    expected = ''
    self.assertEqual(node.props_to_html(), expected)
  
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    expected = '<p>Hello, world!</p>'
    self.assertEqual(node.to_html(), expected)
  
  def test_leaf_to_html_a(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
    expected = '<a href="https://www.google.com">Click me!</a>'
    self.assertEqual(node, expected)
  
  def test_leaf_to_html_empty_value(self):
    node = LeafNode("p", "")
    with self.assertRaises(ValueError):
      node.to_html()
  
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
      grandchild_node = LeafNode("b", "grandchild")
      child_node = ParentNode("span", [grandchild_node])
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(
          parent_node.to_html(),
          "<div><span><b>grandchild</b></span></div>",
      )


if __name__ == "__main__":
    unittest.main()