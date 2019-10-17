Your original file will look like this:

```
Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
```

You'll then run your script by typing this at the command line:

```
$ python fix_csv.py cars-original.csv cars.csv
```

Note : "$" is not typed; that is simply the beginning of the prompt.

Your fixed file should then look like this:

```
Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
```
