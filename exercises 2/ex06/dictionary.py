"""Writing functions invert, count, favorite colors to practice using dictionary data type in python."""
__author__ = "730456646"


def invert(start_dict: dict[str, str]) -> dict[str, str]:
    """Takes start_dict and inverts values of keys for values and values for keys in the returned dict."""
    end_dict: dict[str, str] = {}
    for key in start_dict:
        if start_dict[key] in end_dict:
            raise KeyError("All keys must have unique values.")
        else:
            end_dict[start_dict[key]] = key
    return end_dict


def count(initial_list: list[str]) -> dict[str, int]:
    """Given a list of strings, count the amount of times the unique strings appear and return a dict."""
    final_dict: dict[str, int] = {}
    for item in initial_list:
        if item in final_dict:
            final_dict[item] += 1
        else:
            final_dict[item] = 1
    return final_dict


def favorite_colors(start_dict: dict[str, str]) -> str:
    """Takes in string of favorite colors and returns most frequent favorite color and if tie returns the one that came first."""
    colors = []
    favorite_color_final: str = ""
    most: int = 0
    for i in start_dict:
        colors.append(start_dict[i])
    colors_count: dict[str, int] = count(colors)
    for i in colors_count:
        if colors_count[i] > most:
            favorite_color_final = i
            most = colors_count[i]
    return favorite_color_final
