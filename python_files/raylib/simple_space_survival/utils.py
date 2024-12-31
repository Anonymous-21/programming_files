import xml.etree.ElementTree as Et
from pyray import Rectangle


def xml_parser(xml_file):
    tree = Et.parse(xml_file)
    root = tree.getroot()

    sprite_dict = {}

    for sprite in root.findall("SubTexture"):
        name = sprite.get("name")
        x = int(sprite.get("x"))
        y = int(sprite.get("y"))
        width = int(sprite.get("width"))
        height = int(sprite.get("height"))

        sprite_dict[name] = Rectangle(x, y, width, height)

    return sprite_dict