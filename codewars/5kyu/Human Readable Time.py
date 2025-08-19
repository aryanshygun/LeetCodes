# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):

    hours = seconds // 3600
    seconds -= hours * 3600

    minutes = seconds // 60
    seconds -= minutes * 60
    
    xlist = [hours, minutes, seconds]
    return ':'.join(str(i).zfill(2) for i in xlist)