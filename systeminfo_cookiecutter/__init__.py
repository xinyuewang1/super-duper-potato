# -*- coding: utf-8 -*-

"""Top-level package for systeminfo_cookieCutter."""

__author__ = """~/eclipse-workspace/softwareEng/cookieCutter"""
__email__ = 'xinyue.wang1@ucdconnect.ie'
__version__ = '0.2.0'

import platform
#import shutil

def main():
    #print(platform.platform())
    #total, used, free = shutil.disk_usage(__file__)
    #print('total, used, free: ', total, used, free)
#    print( 'The platform is ',platform.platform())
    a = 'The platform is '+str(platform.platform())
#    print(type(a))
    return a


if __name__ == "__main__":
    main()
