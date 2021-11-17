def formatnumber(number,ndigits=2):
    if (ndigits == 4):
        formnum = "{:,.4f}".format(number)
    elif (ndigits == 8):
        formnum = "{:,.8f}".format(number)   
    else:
        formnum = "{:,.2f}".format(number)
        
    return str(formnum)


def formatnumberold(number,ndigits=2):
    # Format the number with x digits behind the comma
    number = round(number, ndigits)
    numberparts = str(number).split('.')

    # Format the number before the decimal with a comma as 1000 seperator
    l = len(numberparts[0]) - 1
    blocks = int(l / 3)
    offset = len(numberparts[0]) % 3

    if (offset == 0):
        output = numberparts[0][:3]
    else:
        output = numberparts[0][:offset]

    for r in range(blocks):
        output += ','
        output += numberparts[0][offset:offset + 3]
        offset += 3

    # If numbers has decimals
    if len(numberparts) == 2:
        output = output + "." + numberparts[1]

    return output


print(formatnumber(1933.213))
