import grabber
import common_funcs as cf

branch = grabber.Branch('https://ekstrabladet.dk/opinionen/madskastrup/saa-piskede-mette-en-stemning-op/8035340')
branch.pull()

content = branch.contents

cf.uprint(content)
