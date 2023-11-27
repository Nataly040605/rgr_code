def num_fun(): #задаем количество функций/аргументов с нужными нам условиями
    n = input()
    try:
        int(n)
        if int(n) > 0:
            return n
        else:
            print("Нужно ввести натуральное число ", end='')
            print()
            return num_fun()
    except ValueError:
        print("Нужно ввести натуральное число ", end='')
        print()
        return num_fun()

def value_vect(): #задаем значения векторов с нужными нам условиями
    n = input()
    try:
        int(n)
        if int(n) == 0 or int(n) == 1:
            return n
        else:
            print("Введите 0 или 1", end='')
            print()
            return value_vect()
    except ValueError:
        print("Введите 0 или 1", end='')
        print()
        return value_vect()


def T0(vec): #функция для класса Т0
    if vec[0] == 0:
        return 1
    else:
        return 0

def T1(vec): #функция для класса Т1
    if vec[-1] == 1:
        return 1
    else:
        return 0

def S(vec): #функция для класса S
    for i in range(int(float(len(vec)) / 2)):
        if (vec[i] == 1 and vec[len(vec) - 1 - i] == 0) or (vec[i] == 0 and vec[len(vec) - 1 - i] == 1):
            if vec.count(0) == vec.count(1):
                return 1
    return 0


def M(vec): #функция для класса М
    another_vec = vec.copy()
    another_vec.sort()
    if vec == another_vec:
        return 1
    return 0

def L(vec, mas, num): #функция для класса L
    x = []
    eyeFun = mas[num]
    vec1 = vec
    for i in range(len(vec) - 1):
        y = []
        for j in range(len(vec) - 1 - i):
            y.append((vec1[j] + vec1[j + 1]) % 2)
        x.append(y)
        vec1 = y
    for i in range(len(x)):
        if x[i][0] == 1:
            a = 0
            for j in range(len(eyeFun)):
                if eyeFun[j][i + 1] == 1:
                    a += 1
            if a > 1:
                return 0
    return 1

def Class(vec, a, clas):
    print(f"БФ №{vec} ", end='')
    if a == 0:
        print('не ', end='')
    print(f'принадлежит {clas}')

print("Введите количество БФ: ", end='')
vectors=[]
funnies=[]
func = int(num_fun())
for num_func in range(1, int(func) + 1):
    print(f"Введите количество аргументов у {num_func} БФ: ", end='')
    arg = int(num_fun())
    step = 2 ** arg  # строки функции
    print("Заполните значения (они должны быть равны 1 или 0):")
    fun = [] * arg
    for i in range(arg):  # заполнение массива
        x = 2 ** i
        a = []
        step_dl = 0
        while (step_dl != step):
            for i in range(x):
                a.append(0)
                step_dl += 1
            for i in range(x):
                a.append(1)
                step_dl += 1
        fun.append(a)
    funnies.append(fun)
    values_mas = []
    for i in range(step):  # значения бф
        for j in range(arg):
            print(fun[arg - 1 - j][i], end='')
        print(":", end='')
        vec = int(value_vect())
        values_mas.append(vec)
    vectors.append(values_mas)
    print(values_mas)
post = []
for vec in range(func): #определяется принадлежность к классам
    s_p = []
    s_p.append(T0(vectors[vec]))
    Class(vec + 1, s_p[0], "классу T0")
    s_p.append(T1(vectors[vec]))
    Class(vec + 1, s_p[1], "классу T1")
    s_p.append(M(vectors[vec]))
    Class(vec + 1, s_p[2], "классу монотоности")
    s_p.append(S(vectors[vec]))
    Class(vec + 1, s_p[3], "классу самодвойственности")
    s_p.append(L(vectors[vec], funnies, vec))
    Class(vec + 1, s_p[4], "классу линейности")
    post.append(s_p)
ne_post = 1
if len(post) == 1:
    print("Нельзя построить ПФН из одной функции")
else:
    for i in range(5):
        s = 0
        for j in range(len(post)):
            if post[j][i] == 1:
                s += 1
        if s == len(post):
            ne_post = 0
    if ne_post == 1:
        print("Данный набор функций - ПФН")
    else:
        print("Данный набор функций - не ПФН")