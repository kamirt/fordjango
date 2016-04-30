

"""
there must be login, begins on latin letter, contains of latin letters, digits, dot and minus, 
must be finished by latin letter or digit. Min.lenth of login=1, max=20.

"""


from re import match
def checking(login):
    right = False
    if 0 < len(login) <= 20:
        if match(r'^[a-zA-Z]([-.\w]*\w)?$', login):
            right = True
    return right


