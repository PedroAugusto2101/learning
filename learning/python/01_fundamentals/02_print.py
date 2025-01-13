# \r\n -> CRLF (windows)
# \n -> Linux and MacOS
print(12, 34, 1011, sep='-', end='\n##')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n') # 9, 10 -> non-nammed arguments; sep, end -> nammed arguments
# python functions are always all lowercase