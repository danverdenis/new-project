#1 task
# nums_finish = int(input("Введите число: "))
# num_list = []
# for num in range(nums_finish+1):
#     if num % 2 == 1:
#         num_list.append(num)
# print(f"Список из нечетный чисел от одного до N:{num_list}")

# 2 task
# names_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
# first_tour = []
#
# for i in range(len(names_list)):
#     if i % 2 == 0:
#         first_tour.append(names_list[i])
# print(f"Первый день: {first_tour}")

# 3 Task
# cell_count = int(input("Количество клеток: "))
# bad_cell = []
#
# for i in range(cell_count):
#     eff_cell = int(input(f"Эффективность {i + 1} клетки: "))
#     if eff_cell < (i + 1):
#         bad_cell.append(eff_cell)
# print(f"Неподходящие значения: ", end="")
# for cell in bad_cell:
#     print(cell, end=" ")

# 4 Task
# video_cards_count = int(input("Количество видеокарт: "))
# video_cards = []
# new_list = []
# highest_video_cards = 0
# for i in range(video_cards_count):
#     video = int(input(f"{i + 1} Видеокарта: "))
#     video_cards.append(video)
#     if highest_video_cards < video:
#         highest_video_cards = video
# for video_card in video_cards:
#     if video_card != highest_video_cards:
#         new_list.append(video_card)
# print(f"Старый список видеокарт: {video_cards}")
# print(f"Новый список видеокарт: {new_list}")

#5 Task
# films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон",
#          "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
# likes_films = []
#
# film_counter = int(input("Сколько фильмов хотите добавить? "))
# for _ in range(film_counter):
#     like_film = input("Введите название фильма: ")
#     if like_film in films:
#         likes_films.append(like_film)
#     else:
#             print(f"Ошибка: фильма {like_film} у нас нет :(")
# print(f"Ваш список любимых фильмов: ", ", ".join(likes_films))

