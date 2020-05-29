#!/usr/bin/env python3
a = """#!/usr/bin/env python3
a = {2}{1}{2}
print(a.format('', a, '{3}"{3}"{3}"', '{3}{3}'))
# {2} """
print(a.format('', a, '\"\"\"', '\\'))
# """
