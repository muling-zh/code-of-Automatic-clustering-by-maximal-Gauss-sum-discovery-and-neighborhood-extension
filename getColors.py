import colorsys
import random


def colorsList():
    colors = [
        '#0000FF',  # Blue
        '#00FFFF',  # Cyan
        '#FFA500',  # Orange
        '#FFFF00',  # Yellow
        '#FF00FF',  # Magenta
        '#00FF00',  # Lime
        '#FF4500',  # OrangeRed
        '#00FF7F',  # MediumSpringGreen
        '#1E90FF',  # DoderBlue
        '#C71585',  # MediumVioletRed
        '#DA70D6',  # Orchid
        '#9400D3',  # DarkVoilet
        '#4B0082',  # Indigo
        '#7B68EE',  # MediumSlateBlue
        '#4169E1',  # RoyalBlue
        '#800080',  # Purple
        '#5F9EA0',  # CadetBlue
        '#E1FFFF',  # LightCyan
        '#FFC0CB',  # Pink
        '#008B8B',  # DarkCyan
        '#DC143C',  # Crimson
        '#3CB371',  # SpringGreen
        '#ADFF2F',  # GreenYellow
        '#FF1493',  # DeepPink
        '#FFD700',  # Gold
        '#FF0000',  # Red
        '#A9A9A9',  # DarkGray
        '#4682B4',  # SteelBlue
    ]
    return colors


def color(value):
    """interconvert [R,G,B] and '#xxxxxx'
    :param value: [R,G,B] or '#xxxxxx'
    :return: '#xxxxxx' or [R,G,B]
    """
    digit = list(map(str, range(10))) + list("ABCDEF")
    if isinstance(value, list):
        string = '#'
        for i in value:
            a1 = i // 16
            a2 = i % 16
            string += digit[a1] + digit[a2]
        return string
    elif isinstance(value, str):
        a1 = digit.index(value[1]) * 16 + digit.index(value[2])
        a2 = digit.index(value[3]) * 16 + digit.index(value[4])
        a3 = digit.index(value[5]) * 16 + digit.index(value[6])
        return [a1, a2, a3]


def get_n_hls_colors(num):
    hls_colors = []
    i = 0
    step = 360.0 / num
    while i < 360:
        h = i
        s = 90 + random.random() * 10
        l = 50 + random.random() * 10
        _hlsc = [h / 360.0, l / 100.0, s / 100.0]
        hls_colors.append(_hlsc)
        i += step

    return hls_colors


def ncolors(num):
    """
    :param num: number of colors
    :return: colors list
    """
    rgb_colors = []
    if num < 1:
        return rgb_colors
    hls_colors = get_n_hls_colors(num)
    for hlsc in hls_colors:
        _r, _g, _b = colorsys.hls_to_rgb(hlsc[0], hlsc[1], hlsc[2])
        r, g, b = [int(x * 255.0) for x in (_r, _g, _b)]
        rgb_colors.append(color([r, g, b]))

    return rgb_colors

# print(ncolors(20))