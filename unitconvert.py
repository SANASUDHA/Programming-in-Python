# unit converters
unit1=input('Which unit would you like to convert from("bits,bytes,kilobytes"): ')
unit2=input('Which unit would you like to convert to("bits,bytes,kilobytes"): ')
value=int(input('enter your value:'))

if unit1=='bits' and unit2=='bytes':
   print("%s bytes" %(value/8))

elif unit1=='bytes' and unit2=='bits':
   print("%s bits" %(value*8))

elif unit1=='bits' and unit2=='kilobytes':
   print("%s kilobytes" %(value/8192))

elif unit1=='bytes' and unit2=='kilobytes':
   print("%s kilobytes" %(value/1024))

elif unit1=='kilobytes' and unit2=='bits':
   print("%s bits" %(value*8192))

elif unit1=='kilobytes' and unit2=='bytes':
   print("%s bytes" %(value*1024))

else:
   print('invalid unit1 and unit 2')
