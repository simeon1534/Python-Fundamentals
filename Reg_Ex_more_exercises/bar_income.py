import re

data=input()
pattern_name=r"(?<=%)[A-Z][a-z]+(?=%)"
pattern_product=r"(?<=<)\w+(?=>)"
pattern_count=r"(?<=\|)\d+(?=\|)"
pattern_price=r"\d+\.\d+(?=\$)|\d+\d+(?=\$)"

total=0
while not data=="end of shift":

    name_proverka=re.findall(pattern_name,data)
    product_proverka=re.findall(pattern_product,data)
    count_proverka=re.findall(pattern_count,data)
    price_proverka=re.findall(pattern_price,data)

    if name_proverka!=[] and product_proverka!=[] and count_proverka!=[] and price_proverka!=[]:
        if "." in price_proverka[0]:
            price_count_cena=int(count_proverka[0])*float(price_proverka[0])
            print(f"{name_proverka[0]}: {product_proverka[0]} - {price_count_cena:.2f}")
        else:
            price_count_cena = int(count_proverka[0]) * int(price_proverka[0])
            print(f"{name_proverka[0]}: {product_proverka[0]} - {price_count_cena:.2f}")
        total+=price_count_cena

    data=input()

print(f"Total income: {total:.2f}")