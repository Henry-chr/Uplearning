from django.utils.safestring import mark_safe
from django import template

register = template.library()    #register的名字是固定的,不可改变

@register.filter
def my_filter(v1, v2):
    return v1 * v2

@register.simple_tag
def my_tag1(v1, v2, v3):
    return v1 * v2 * v3

@register.simple_tag
def my_html(v1, v2):
    temp_html = "<input type='text' id='%s' class='%s' />" %(v1, v2)
    return mark_safe(temp_html)