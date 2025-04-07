from textnode import TextNode, TextType

def main():
  dummy_object = TextNode("Hello World!", TextType.NORMAL_TEXT)

  print(dummy_object)

if __name__ == "__main__":
  main()