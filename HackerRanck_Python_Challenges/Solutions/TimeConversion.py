"""author = Rockefeller"""


def timeConversion(s):
    #
    # Write your code here.
    if s.startswith("12") and s.endswith("AM"):
        return  "00" + s[2:-2] 
    elif s.endswith("AM"):
        return s[:-2]
    elif s.startswith("12") and s.endswith("PM"):
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:-2]
