import pyray as p
import xml.etree.ElementTree as Et


def spritesheet_xml_parser(xml_file: str) -> dict[str, p.Rectangle]:
    tree: Et.ElementTree = Et.parse(xml_file)
    root: Et.Element = tree.getroot()

    sprite_dict: dict[str, p.Rectangle] = {}

    for sprite in root.findall("SubTexture"):
        name: str | None = sprite.get("name")
        x: int = int(sprite.get("x", -1))
        y: int = int(sprite.get("y", -1))
        width: int = int(sprite.get("width", -1))
        height: int = int(sprite.get("height", -1))

        if name is not None and x != -1 and y != -1 and width != -1 and height != -1:
            sprite_dict[name] = p.Rectangle(x, y, width, height)

    return sprite_dict
