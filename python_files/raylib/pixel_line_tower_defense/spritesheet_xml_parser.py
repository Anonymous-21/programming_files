import xml.etree.ElementTree as Et


def xml_parser(xml_file):
    tree = Et.parse(xml_file)
    root = tree.getroot()

    sprite_dict = {}

    for sprite in root.findall("sprite"):
        name = sprite.get("n")
        x = int(sprite.get("x"))
        y = int(sprite.get("y"))
        w = int(sprite.get("w"))
        h = int(sprite.get("h"))

        sprite_dict[name] = [x, y, w, h]

    return sprite_dict
