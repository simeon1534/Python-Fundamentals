import re
data=input()
pattern=r">>(?P<fname>[a-zA-Z][a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
total_price=0
sum_data=" "
while not data=="Purchase":
    sum_data+=' '+data
    data = input()
furnitures=re.finditer(pattern,sum_data)
print(f"Bought furniture:")
for furniture in furnitures:
    f=furniture.groupdict()
    print(f"{f['fname']}")
    if "." in f["price"]:
        f["price"]=float(f["price"])
    else:
        f["price"] = int(f["price"])
    total_price+=f['price']*int(f['quantity'])
#print(sum_data)
print(f"Total money spend: {total_price:.2f}")