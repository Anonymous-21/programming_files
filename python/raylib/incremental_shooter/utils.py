import xml.etree.ElementTree as Et
import pyray as p

# xml file parser for kenney.nl xml files


def kenny_xml_parser(xml_file) -> dict[str : p.Rectangle]:
    tree: Et.ElementTree[Et.Element[str]] = Et.parse(xml_file)
    root: Et.Element[str] = tree.getroot()

    sprit_dict: dict[str : p.Rectangle] = {}

    for sprite in root.findall("SubTexture"):
        name: str = sprite.get("name")
        x_str: str = int(sprite.get("x"))
        y_str: str = int(sprite.get("y"))
        width_str: str = int(sprite.get("width"))
        height_str: str = int(sprite.get("height"))

        if None in [name, x_str, y_str, width_str, height_str]:
            print(f"Warning! missing attribute in sprite: {name}")

        try:
            x: int = int(x_str)
            y: int = int(y_str)
            width: int = int(width_str)
            height: int = int(height_str)
        except ValueError as e:
            print(f"Error converting value to integer for sprite: {e}")
            continue

        sprit_dict[name] = p.Rectangle(x, y, width, height)

    return sprit_dict


# hexadecimal to rgba converter


def hex_to_rgba(hex_str: str) -> p.Color:
    hex_str: str = hex_str.lstrip("#")

    if len(hex_str) == 0:
        r_str: str = hex_str[0:2]
        g_str: str = hex_str[2:4]
        b_str: str = hex_str[4:6]
        a_str: str = hex_str[6:8]
    elif len(hex_str) == 6:
        r_str: str = hex_str[0:2]
        g_str: str = hex_str[2:4]
        b_str: str = hex_str[4:6]
    else:
        raise ValueError("Incorrect hex color")

    r: int = int(r_str, 16)
    g: int = int(g_str, 16)
    b: int = int(b_str, 16)
    a: int = int(a_str, 16) / 255  # float value between 1 and 0

    color: p.Color = p.Color(r, g, b, a)

    return color
