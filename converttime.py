import datetime

def converting(convertto):
    convertto=float(convertto)
    date = datetime.datetime.fromtimestamp(convertto)
    return date.strftime('%a %d %b %H:%M:%S.%f UTC %Y')

def convert(filename):
    convertedDates=[]
    with open(filename,'r') as file:
        for i in file:
            line=i.strip().split(":")
            if len(line)>=2:
                convertto=line[0]
                convertingto=converting(convertto)
                convertedDates.append(f'{convertingto}:{":".join(line[1:])}')
            else:
                convertedDates.append(i)
    return convertedDates


filename=input("Enter File Name: ")
convertedDates=convert(filename)

for i in convertedDates:
    print(i)