import xml.etree.ElementTree as Et
from pyray import Rectangle


def xml_parser(xml_file: str) -> dict[str, Rectangle]:
    tree: Et.ElementTree = Et.parse(xml_file)
    root: Et.Element = tree.getroot()

    sprite_dict: dict[str, Rectangle] = {}

    for sprite in root.findall("SubTexture"):
        name: str | None = sprite.get("name")
        x: str | None = sprite.get("x")
        y: str | None = sprite.get("y")
        width: str | None = sprite.get("width")
        height: str | None = sprite.get("height")

        if (
            name is not None
            and x is not None
            and y is not None
            and width is not None
            and height is not None
        ):
            sprite_dict[name] = Rectangle(int(x), int(y), int(width), int(height))

    return sprite_dict
