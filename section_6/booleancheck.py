#!/usr/bin/env python

print("""False: {0}
None: {1}
Empty list: {2}
Empty dictionary: {3}
Empty tuple: {4}
Empty string: {5}
""".format(False, bool(None), bool([]), bool({}), bool(()), bool('')))