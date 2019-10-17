def lsv_to_csv(file):
    import re
    return re.sub('\|', ",", file)


print(lsv_to_csv('''Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257'''))

'''
Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257

Process finished with exit code 0
'''
