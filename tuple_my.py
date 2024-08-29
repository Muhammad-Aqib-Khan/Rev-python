# tuple in python 

new_tuple =("Aqib khan","Amir","tayyabKHan",)
# access tuple elements
print(new_tuple)

# change in tuples
tup_countries:tuple[str,str,str,str,str] = ("United States","China","France","Germany","Pakistan")
temp_list:list[str] =list(tup_countries)

temp_list.append("India")
#it does not mainly add the value into the already existing tuple infact creates a new tuple and then add to it
tup_countries:tuple[str] = tuple(temp_list)
print(tup_countries)
