 #Sort a list  full of textbooks by subject. The sorting should NOT be case sensitive

def sorter(textbooks):
    return sorted(textbooks,key=str.lower)