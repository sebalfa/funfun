import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    """
    since some of the articles pulled by grabber contains utf-8 characters,
    we print text using this function
    """
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
