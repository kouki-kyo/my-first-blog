from django import template

register = template.Library()


@register.simple_tag
def access_list_by_index(list: list, index: int):
    try:
        result = list[int(index)]
        return result
    except:
        return ""

@register.simple_tag
def access_list_of_dict_by_index_and_key(dict_list: list, index: int, key: str):
    try:
        result = dict_list[int(index)][key]
        return result
    except:
        return ""