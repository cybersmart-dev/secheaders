import argparse

parser = argparse.ArgumentParser(description='SecHeaders')
parser.add_argument('-u', '--url', help='Target url')
parser.add_argument("-l", "--list", help='Target list input') 
args = parser.parse_args()

def get_domain(url):
    remove_scheme = url.split("//")[1]
    domain = ''
    for char in remove_scheme:
        if char == '/':
            break
        else:
            domain = domain + char
    return domain
    