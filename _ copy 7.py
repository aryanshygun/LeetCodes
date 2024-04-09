x = "the-stealth-warrior"
import re
def to_camel_case(text):
    result = re.split(r'[_-]', text)
    xlist = [*text]
    for i in range(1, len(result)):
        result[i] = result[i].title()
        
        
    # if xlist[0].isupper():
    #     result[0][0] = result[0][0].upper()
    # else:
    #     result[0][0] = result[0][0].lower()
    return ''.join(result)
print(to_camel_case(x))