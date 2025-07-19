while x:                             # Exit when x empty
    if match(x[0]):
        print('Found')
        break                        # Exit, go around else
    x = x[1:]
else:
    print('Not found')               # Only here if exhausted x

    #doesnt work directly from book.