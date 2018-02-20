# -*- coding: utf-8 -*-

"""Main module."""

import platform
#import shutil

def get_platform():
    #print(platform.platform())
    #total, used, free = shutil.disk_usage(__file__)
    #print('total, used, free: ', total, used, free)
    a= str('The platform is '+platform.platform())
#    print(type(a))
    return a 


if __name__ == "__main__":
    get_platform()