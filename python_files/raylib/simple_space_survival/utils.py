import xml.etree.ElementTree as Et
from pyray import Rectangle


def xml_parser(xml_file: str) -> dict[str, Rectangle]:
    tree: Et.ElementTree = Et.parse(xml_file)
    root: Et.Element = tree.getroot()

    sprite_dict: dict[str, Rectangle] = {}

    for sprite in root.findall("SubTexture"):
        name: str = sprite.attrib["name"]
        x: int = int(sprite.attrib["x"])
        y: int = int(sprite.attrib["y"])
        width: int = int(sprite.attrib["width"])
        height: int = int(sprite.attrib["height"])

        sprite_dict[name] = Rectangle(x, y, width, height)

    return sprite_dict