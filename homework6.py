#работа со списками
my_list=["банан", "яблоко", "апельсин", "персик", "груша", "лимон"]
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[2:5])
my_list[3]="огурец"
print(my_list)
#работа со словарями
my_dict={'яблоко':'apple', 'банан':'banana', 'персик':'peach', 'лимон':'limon', "машина":"car", "диван":"sofa"}
print(my_dict)
print(my_dict.get("машина"))
my_dict['банан']="orange"
print(my_dict)