# nums_finish = int(input("Введите число: "))
# num_list = []
# for num in range(nums_finish+1):
#     if num % 2 == 1:
#         num_list.append(num)
# print(f"Список из нечетный чисел от одного до N:{num_list}")

names_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
first_tour = []

for i in range(len(names_list)):
    if i % 2 == 0:
        first_tour.append(names_list[i])
print(f"Первый день: {first_tour}")
