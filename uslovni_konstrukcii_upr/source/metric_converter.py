razstoqnie = float(input())
vhodna_merna_edinica = str(input())
izhodna_merna_edinica = str(input())

if vhodna_merna_edinica == 'm' and izhodna_merna_edinica == 'cm':
    print(f'{razstoqnie*100:.3f}')
elif vhodna_merna_edinica == 'm' and izhodna_merna_edinica == 'mm':
    print(f'{razstoqnie*1000:.3f}')

if vhodna_merna_edinica == 'cm' and izhodna_merna_edinica == 'm':
    print(f'{razstoqnie/100:.3f}')
elif vhodna_merna_edinica == 'cm' and izhodna_merna_edinica == 'mm':
    print(f'{razstoqnie*10:.3f}')

if vhodna_merna_edinica == 'mm' and izhodna_merna_edinica == 'cm':
    print(f'{razstoqnie/10:.3f}')
elif vhodna_merna_edinica == 'mm' and izhodna_merna_edinica == 'm':
    print(f'{razstoqnie/1000:.3f}')