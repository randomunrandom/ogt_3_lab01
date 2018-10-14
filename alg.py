def user_input():
    res_e = list()
    ui_inp = int(input("введите количнство рёбер: "))
    while ui_inp <= 0:
        ui_inp = int(input("введите положительное число"))
    for i in range(ui_inp):
        c = list(input("введите крайние вершины ребра {:^3} через запятую: ".format(i + 1)))
        if ',' in c:
            c.remove(',')
        if ' ' in c:
            c.remove(' ')
        c.sort()
        c = tuple(c)
        w = int(input("введите вес ребра {:^3}: ".format(i + 1)))
        res_e.append(dict(cords=c, weight=w))
    return res_e


def pre_input():
    res_e = list()
    res_e.append(dict(cords=(1, 2), weight=2))
    res_e.append(dict(cords=(1, 4), weight=7))
    res_e.append(dict(cords=(2, 3), weight=8))
    res_e.append(dict(cords=(3, 4), weight=5))
    res_e.append(dict(cords=(3, 4), weight=50))
    res_e.append(dict(cords=(3, 5), weight=4))
    res_e.append(dict(cords=(4, 5), weight=3))
    res_e.append(dict(cords=(4, 6), weight=5))
    res_e.append(dict(cords=(4, 8), weight=3))
    res_e.append(dict(cords=(5, 8), weight=6))
    res_e.append(dict(cords=(5, 9), weight=7))
    res_e.append(dict(cords=(6, 7), weight=4))
    res_e.append(dict(cords=(8, 9), weight=2))

    # res_e.append(dict(cords=(, ), weight=))
    return res_e


def special_sort(list_of_points):
    p_lop = list()
    for i in range(len(list_of_points)):
        if list_of_points[i]["cords"][0] != list_of_points[i]["cords"][1]:
            p_lop.append(list_of_points[i])

    list_to_pop = list()
    for i in range(len(p_lop)):
        for j in range(i):
            if p_lop[i]["cords"] == p_lop[j]["cords"]:
                list_to_pop.append(j)
                p_lop[i]["weight"] = max(p_lop[i]["weight"], p_lop[j]["weight"])

    list_to_pop.reverse()
    for i in list_to_pop:
        p_lop.pop(i)

    p_lop = sorted(p_lop, key=lambda k: k["weight"], reverse=True)

    return p_lop


def alg_Kraskala(list_of_points):
    res = list()
    buckets = list()
    for l_i, l_el in enumerate(list_of_points):
        c0_b = False
        c1_b = False
        c0_i = -1
        c1_i = -1
        for b_i, b_el in enumerate(buckets):
            b_el.sort()
            if l_el["cords"][0] in b_el:
                c0_b = True
                c0_i = b_i
            if l_el["cords"][1] in b_el:
                c1_b = True
                c1_i = b_i
        if (not c0_b) and (not c1_b):
            buckets.append([l_el["cords"][0], l_el["cords"][1]])
            res.append(l_el)
        elif (not c0_b) and c1_b:
            buckets[c1_i].append(l_el["cords"][0])
            res.append(l_el)
        elif c0_b and (not c1_b):
            buckets[c0_i].append(l_el["cords"][1])
            res.append(l_el)
        elif c0_b and c1_b and (c0_i != c1_i):
            buckets[c0_i] += buckets[c1_i]
            buckets.pop(c1_i)
            buckets[c0_i].sort()
            res.append(l_el)
    return res


def graph_print(list_of_points):
    for i in list_of_points:
        print("ребро:", i["cords"], "\t, вес: ", i["weight"])


def graph_draw(list_of_points):
    import graphviz as gv
    g = gv.Graph()
    for i in list_of_points:
        g.edge(str(i["cords"][0]), str(i["cords"][1]), weight=str(i["weight"]))
    g.render("Graph_{}".format(graph_num), view=True)
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

print("введённый граф: ")
graph_print(E)

p_E = special_sort(E)

print("подготовленный граф: ")
graph_print(p_E)

E_res = alg_Kraskala(p_E)

print("полученный граф: ")
graph_print(E_res)

inp = input("показать введённый и полученный спооб?(д/н) ")

if inp == "д":
    graph_num = int(1)
    graph_draw(E)
    graph_num += 1
    graph_draw(p_E)
    graph_num += 1
    graph_draw(E_res)
elif inp == "н":
    pass
else:
    print("Ошибка ввода")
    raise ValueError('Undefined unit: {}'.format(inp))
