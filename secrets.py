"""
    Add your twitter handle's email and password in the credentials.txt file.
    This will be used to automate the login.
"""

def get_credentials() -> dict:
    d = dict()
    with open('credentials.txt') as f:
        for line in f.readlines():
            try:
                key, value = line.split(": ")
            except ValueError:
                print('Add your email and password in credentials.txt file')
                exit(0)
            d[key] = value.rstrip(" \n")

    return d
