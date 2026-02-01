def show():
    with open('nameList.txt', 'r') as file:
        nfile = file.readlines()
        nfile = [name.replace("\n", "") for name in nfile]
#       print(nfile)
        return (nfile)

def update(list):
    with open('nameList.txt', 'w') as file:
        nfile = file.writelines(list)
    return (nfile)
def add(name):
    with open('nameList.txt', 'r') as file:
        nfile = file.readlines()
        nfile.append(name + '\n')
    with open('nameList.txt', 'w') as file:
        file.writelines(nfile)
        file.close()
    return f'{name +" has Been Added to nameList file"}'

def replace(old, new):
    with open('nameList.txt', 'r') as file:
        nfile = file.read()
        nfile = (nfile.split())
#       print(nfile)
    print()
    for n, name in enumerate(nfile):
        if name == old:
            nfile[n] = new
    with open('nameList.txt', 'w') as file:
        for m in nfile:
            file.write(f'{m}\n')
    return nfile

def delete(name):
    with open('nameList.txt', 'r') as file:
        nfile = file.read()
        nfile = (nfile.split())
#       print(nfile)
    for newname in nfile:
        if newname == name:
            nfile.remove(newname)
    with open('nameList.txt', 'w') as file:
        for m in nfile:
            file.write(f'{m}\n')
    return nfile

def deleteALL():
    with open('nameList.txt', 'w') as file:
       nfile = file.write('')
    return nfile



