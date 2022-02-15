inventory=input().split(', ')

def collect(inv,item):
    if not item in inv:
        inv.append(item)
    return inv

def drop(inv,item):
    if item in inv:
        inv.remove(item)
    return inv

def combine(inv,old_item,new_item):
    if old_item in inv:
        inv.insert(inv.index(old_item) + 1,new_item)
    return inv

def renew(inv,item):
    if item in inv:
        inv.pop(inv.index(item))
        inv.append(item)
    return inv
data=input()
while not data=='Craft!':
    command,item= data.split(' - ')
    if command=='Collect':
        inventory=collect(inventory,item)
    elif command=='Drop':
        inventory=drop(inventory,item)
    elif command=='Combine Items':
        old_item,new_item=item.split(':')
        inventory=combine(inventory,old_item,new_item)
    elif command=='Renew':
        inventory=renew(inventory,item)
    data=input()
print(', '.join(inventory))