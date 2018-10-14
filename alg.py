import networkx as nx
import matplotlib.pyplot as plt
from operator import attrgetter


def user_input():
    res_E = list()
    inp = int(input("введите количнство рёбер: "))
    while inp <= 0:
        inp = int(input("введите положительное число"))
    for i in range(inp):
        c = list(input("введите крайние вершины ребра {:^3} через запятую: ".format(i + 1)))
        if ',' in c:
            c.remove(',')
        if ' ' in c:
            c.remove(' ')
        c.sort()
        c = tuple(c)
        w = int(input("введите вес ребра {:^3}: ".format(i + 1)))
        res_E.append(dict(coords=c, weight=w))
    return res_E


def pre_input():
    res_E = list()
    res_E.append(dict(coords=(1, 1), weight=1))
    res_E.append(dict(coords=(1, 2), weight=3))
    res_E.append(dict(coords=(2, 3), weight=6))
    res_E.append(dict(coords=(1, 3), weight=9))
    res_E.append(dict(coords=(1, 3), weight=90))
    res_E.append(dict(coords=(1, 4), weight=15))
    res_E.append(dict(coords=(2, 4), weight=2))
    res_E.append(dict(coords=(3, 4), weight=19))
    res_E.append(dict(coords=(3, 4), weight=190))
    # res_E.append(dict(coords=list(, ), weight=))
    return res_E


def special_sort(list_of_points):
    p_lop = list()
    for i in range(len(list_of_points)):
        if list_of_points[i]["coords"][0] != list_of_points[i]["coords"][1]:
            p_lop.append(list_of_points[i])

    list_to_pop = list()
    for i in range(len(p_lop)):
        for j in range(i):
            if p_lop[i]["coords"] == p_lop[j]["coords"]:
                list_to_pop.append(j)
                p_lop[i]["weight"] = max(p_lop[i]["weight"], p_lop[j]["weight"])

    list_to_pop.reverse()
    for i in list_to_pop:
        p_lop.pop(i)

    p_lop = sorted(p_lop, key=lambda k: k["weight"], reverse=True)

    return p_lop


def alg_Kraskala(list_of_points):  # TODO дописать реализацию алгоритма
    res = list()
    buckets = list()
    checked = False
    for i, el in enumerate(list_of_points):
        for b in buckets:
            if (el["coords"][0] not in b) and (el["coords"][1] in b):
                checked = True
                b.append(el["coords"][0])
                res.append(el)
            elif (el["coords"][0] in b) and (el["coords"][1] not in b):
                checked = True
                b.append(el["coords"][1])
                res.append(el)
            elif (el["coords"][0] in b) and (el["coords"][1] in b):
                checked = True
                pass
        if checked == False:
            buckets.append([el["coords"][0], el["coords"][1]])
            res.append(el)
    return res


def graph_print(list_of_points):
    for i in list_of_points:
        print("ребро:", i["coords"], "\t, вес: ", i["weight"])


def graph_draw(list_of_points):  # TODO заюзать библиотеку для отрисовки граффов
    return


E = list()
print("выберите способ задания графа одной из предложенных букв:\n\t-заранее: з\n\t-вручную: в")
inp = input("введите выбраный способ: ")
inp_options = {
    'з': pre_input,
    'в': user_input
}
try:
    E = inp_options[inp]()
except KeyError as e:
    # можно также присвоить значение по умолчанию вместо бросания исключения
    print("Ошибка ввода")
    raise ValueError('Undefined unit: {}'.format(e.args[0]))

print("введённый граф:")
graph_print(E)

p_E = special_sort(E)

print("подготовленный граф:")
graph_print(p_E)

E_res = alg_Kraskala(p_E)

print("полученный граф:")
graph_print(E_res)

print("показать введённый и полученный спооб?(д/н)")
inp = input()

if inp == "д":
    graph_draw(E)
    graph_draw(E_res)
elif inp == "н":
    pass
else:
    print("Ошибка ввода")
    raise ValueError('Undefined unit: {}'.format(inp))
