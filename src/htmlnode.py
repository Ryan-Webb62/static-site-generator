

class HTMLNode:
  def __init__(self,tag=None,value=None,children=None,props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    result = ''
    if self.props:
      for key, value in self.props.items():
        result += f' {key}="{value}"'
    return result
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  
class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    # Explicitly set children to None
    super().__init__(tag=tag, value=value,children=None, props=props)

  def to_html(self):
    if not self.value: # This checks for None or empty strings  
      raise ValueError("Value is required for LeafNode")
    if self.tag is not None:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    else:
      return f"{self.value}"
  
class ParentNode(HTMLNode):
  def __init__(self, tag=None, children=None, props=None):
    # Explicitly set value to None
    super().__init__(tag=tag, children=children, props=props)
  
  def to_html(self):
    return_string = ""
    if not self.tag:
      raise ValueError("Tag is required for ParentNode")
    if not self.children:
      raise ValueError("Children are required for ParentNode")
    return_string += f"<{self.tag}{self.props_to_html()}>"
    for child in self.children:
      return_string += f"{child.to_html()}"
    return_string += f"</{self.tag}>"
    return return_string
