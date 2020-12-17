import re
def check_password(password): return re.compile('[a-z]+[A-Z]+[0-9]+').match(password)