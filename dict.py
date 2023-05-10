person_1 = {}
person_2 = {}
l = ["имя","Giga Chel","фамилия", "Legendovich",
     "машина", "Porsche","имя","BEbra","фамилия", "Legendovna", "машина", "Chevrolet"]
for n in range(len(l)):
    if n == 3:
        l.pop(0)
        l.pop(0)
        l.pop(0)
        break
    person_1[l[n]] = l[n+1]
    l.pop(n)
for n in range(len(l)):
    if n == 3:
        break
    person_2[l[n]] = l[n+1]
    l.pop(n)
people = {"user_1": person_1, "user_2": person_2}
print(person_1.get("имя"))
print(person_1.keys())
#
# for user_number, user_info in people.items():
#     print(f"User: {user_number}")
#     car = user_info["машина"]
#     print(f"Авто: {car}\n")
#

#
# if person_1 in people.values():
#     print('est')
# else:
#     print("net")
# print("beb\n beb2")

# print(person_1.get("машин", "иуи"))

# возврщ значение ключ | содает ключ со знач none | создает ключ с указанным знач
# print(person_1.setdefault("машин", "велосипед"), person_1)

# person_1_copy = person_1.copy()
# print(person_1_copy)

# person_1.update({"любимое блюдо": "яйцо"})
# print(person_1)
# person_1.update({"любимое блюдо": "бекон"})
# print(person_1)

# удалят и возврщ знач | возвр none | возвр заданное знач
# print(person_1.pop("любимое блюдо"))
# print(person_1.pop("любимое бюдо", "ты дурак"))

#удаляет и возвращ случайную пару
# print(person_1.popitem())

# print(person_1.keys(),"\n", person_1.values(),"\n", person_1.items())

#clear
# print(person_1)
# person_1.clear()
# print(person_1)