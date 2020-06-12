#Write a function, shortenToDate, that takes the Website date/time in its original string format, and returns the shortened format.

def shorten_to_date(long_date):
    return long_date.split(',')[0]