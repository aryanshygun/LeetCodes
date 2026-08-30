# https://www.codewars.com/kata/52742f58faf5485cae000b9a/solutions/python?filter=me&sort=best_practice&invalids=false
def format_duration(seconds):
    if seconds == 0:
        return 'now'
    else:
        secinmin = 60
        secinhour = 60 * secinmin
        secinday = 24 * secinhour
        secinyear = 365 * secinday
        
        years = seconds // secinyear
        seconds -= years * secinyear
        
        days = seconds // secinday
        seconds -= days * secinday
        
        hours = seconds // secinhour
        seconds -= hours * secinhour
        
        minutes = seconds // secinmin
        seconds -= minutes * secinmin
    xtime = []
    if years == 1:
        xtime.append(f'{str(years)} year')
    elif years > 1:
        xtime.append(f'{str(years)} years')
        
    if days == 1:
        xtime.append(f'{str(days)} day')
    elif days > 1:
        xtime.append(f'{str(days)} days')

        
    if hours == 1:
        xtime.append(f'{str(hours)} hour')
    elif hours > 1:
        xtime.append(f'{str(hours)} hours')
    
    if minutes == 1:
        xtime.append(f'{str(minutes)} minute')  
    elif minutes > 1:
        xtime.append(f'{str(minutes)} minutes')
    
    if seconds == 1:
        xtime.append(f'{str(seconds)} second')
    elif seconds > 1:
        xtime.append(f'{str(seconds)} seconds')

    if len(xtime) == 1:
        return xtime[0]

    if len(xtime) == 2:
        return ' and '.join(xtime)
    
    for i in range(len(xtime) - 2):
        xtime[i] += ', '
    xtime[-1] = ' and ' + xtime[-1]

    return ''.join(xtime)
