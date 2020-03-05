import grabber
import common_funcs as cf

spider = grabber.Spider()
spider.pull()
spider.getrawlinks()
cf.uprint(spider.rawlinks)
