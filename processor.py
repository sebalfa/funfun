import grabber
import common_funcs as cf

def my_function(x):
    branch = grabber.Branch(x)
    branch.pull()

    content = branch.contents

    cf.uprint(content)

my_function('https://ekstrabladet.dk/ferie/ikonisk-stenstatue-paa-paaskeoeen-er-oedelagt/8034294')
