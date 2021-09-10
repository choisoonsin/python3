import re

_target_string = """copyNode("/root/src[" + row + "]/item", "/root/dest[" + row + "]/item")"""

_pattern = re.compile(r'copyNode\(([^,]*)[,+\s+]([^)]*)\)+;?')

_r = re.search(_pattern, _target_string)

print(_r.groups())