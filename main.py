class Dish: # Класс блюда - название и его тип

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind


class Feat(Dish): # Класс блюда с мясом или рыбой
    def __init__(self, name, meat, fish, kind):
        Dish.__init__(self, name, kind)
        self.meat = meat
        self.fish = fish


class Porrige(Feat): # Класс каши (содержит список с сортами каши)
    def __init__(self, name, meat, fish, list_porrige, kind, sort):
        Feat.__init__(self, name, meat, fish, kind)
        self.list_porrige = list_porrige
        self.sort = sort


class Nosh(Dish): # Класс перекуса

    def __init__(self, name, kind):
        Dish.__init__(self, name, kind)


class Fruits:

    def __init__(self, name):
        self.name = name


class Drinks: # Класс напитков - название, тип и температура

    def __init__(self, name, temp, kind):
        self.name = name
        self.kind = kind
        self.temp = temp


sausage = 'Сосиска'
crabsticks = 'Крабовые палочки'
chiken = 'Курица'
fish = 'Рыба'

lipor = ['гречневая', 'пшеничная', 'рисовая'] #список видов каши


# Типы блюд, которые использует поле kind
onlydin = "Только ужин"
onlylun = "Только обед"
lundin = "Обед + ужин"
onlybreak = "Только завтрак"
breaklun = "Завтрак + обед"
breakdin = "Завтрак + ужин"
allin = "все включено"

#Объявление блюд
omlette = Feat('Омлет', sausage, crabsticks, allin)
dumplings = Dish('Пельмени', lundin)
porrige = Porrige('Каша', chiken, fish, lipor, lundin, lipor[0])
potato = Dish('Картошка', lundin)
pasta = Feat('Макароны', chiken, fish, lundin)
veg_mix = Dish('Овощная смесь', lundin)

sandwich = Nosh('Бутерброд', allin)
muesli = Nosh('Мюсли', onlybreak)
salad = Nosh('Салат', lundin)
curd = Nosh('Творог', breakdin)

banana = Fruits('Банан')
apple = Fruits('Яблоко')

soda = Drinks('Минералка', 0, allin)
cofee = Drinks('Кофе', 1, breaklun)
milk = Drinks('Молоко', 0, allin)
cacao = Drinks('Какао', 1, allin)
juice = Drinks('Сок', 0, allin)
tea = Drinks('Чай', 1, allin)
alc = Drinks('Сидр', 0, onlydin)

#Буферная переменная для редактирования дневного рациона
dayfood = []

def editing(df): # функция редакции блюда. На данный момент редакция происходит только по признаку поля kind
    ##Чтобы то, что лучше всего подходит в качестве ужина не оказалось на месте завтрака
    for iter in range(1, 3): #Редакция происходит в нескольких итерациях по нисходящей
        # - от более мягких ограничений к более строгим
        if iter == 1:
            for box in df:

                for el in box:
                    if isinstance(el, (Dish, Drinks)):

                        if el.kind == lundin and df.index(box) == 0:
                            founded = False
                            for ch in df[1]:
                                if ch.kind == onlybreak or ch.kind == breaklun or ch.kind == breakdin or ch.kind == allin:
                                    df[0], df[1] = df[1], df[0]
                                    founded = True
                                    break
                            if not founded:
                                for ch in df[2]:
                                    if ch.kind == onlybreak or ch.kind == breaklun or ch.kind == breakdin or ch.kind == allin:
                                        df[0], df[2] = df[2], df[0]
                                        founded = True
                                        break

                        if el.kind == breaklun and df.index(box) == 2:
                            founded = False
                            for ch in df[0]:
                                if ch.kind == onlydin or ch.kind == breakdin or ch.kind == lundin or ch.kind == allin:
                                    df[0], df[2] = df[2], df[0]
                                    founded = True
                                    break
                            if not founded:
                                for ch in df[1]:
                                    if ch.kind == onlydin or ch.kind == breakdin or ch.kind == lundin or ch.kind == allin:
                                        df[0], df[1] = df[1], df[0]
                                        founded = True
                                        break

                        if el.kind == breakdin and df.index(box) == 1:
                            founded = False
                            for ch in df[0]:
                                if ch.kind == breaklun or ch.kind == lundin or ch.kind == allin:
                                    df[0], df[1] = df[1], df[0]
                                    founded = True
                                    break
                            if not founded:
                                for ch in df[2]:
                                    if ch.kind == breaklun or ch.kind == lundin or ch.kind == allin:
                                        df[0], df[1] = df[1], df[0]
                                        founded = True
                                        break

        if iter == 2:
            for box in df:

                for el in box:
                    if isinstance(el, (Dish, Drinks)):
                        if el.kind == onlybreak and df.index(box) != 0:
                            df[0], df[df.index(box)] = df[df.index(box)], df[0]
                            break

                        if el.kind == onlydin and df.index(box) != 2:
                            df[2], df[df.index(box)] = df[df.index(box)], df[2]
                            break

    return df


def daylee(main, sec, _drink, _dinosh, switcher, por, f): #Функция для сбора порции
    portion = []

    if not _dinosh:
        food = sec
        portion.append(food)

    else:
        food = main
        portion.append(food)
        if isinstance(food, Porrige):
            por = food.sort
            portion.append(por)
        if isinstance(food, Feat):
            if switcher:
                feat = food.meat
            else:
                feat = food.fish
            portion.append(feat)
            switcher = not switcher

    todrink = _drink

    portion.append(todrink)
   # print(portion)

    dayfood.append(portion)

  #  for word in portion:
  #      f.write(word)
  #      f.write(', ')
  #  f.write('\n')
    return [switcher, main, sec, _drink]

def dfprint (df): # функция для печати
    collect = []

    for box in df:
        for el in box:
            if isinstance(el, (Dish, Drinks)):
                f.write(el.name)
                f.write(', ')
                collect.append(el.name)
                if isinstance(el, Feat):
                    f.write(box[1])
                    collect.append(box[1])
                    if isinstance(el, Porrige):
                        f.write(box[2])
                        f.write(', ')
                        collect.append(box[2])

        print(", ".join(collect))
        collect.clear()
        f.write('\n')

def schedule(list_main, list_sec, list_fr, list_dr, f): #функция для следнования порядку очередности в блюдах

    #начальный набор позиций в списках
    main_food = list_main[4]
    sec_food = list_sec[1]
    fruit_day = list_fr[1]
    drink_day = list_dr[0]

    dinosh = True  # 0 - Nosh, 1 - Dish
    switcher = True  # 0 - Fish, 1 - Meat

    day = 1

    for d in range(30):
        print('День', day, fruit_day.name)
        string = 'День ' + str(day) + ' ' + fruit_day.name + '\n'
        f.write(string)

        for i in range(1, 4):
            # [switcher, main, sec, _drink]

            #то, что будет использовано для составления рациона
            buffer = daylee(main_food, sec_food, drink_day, dinosh, switcher, porrige.sort, f)

            #циклическая смена блюд по очереди
            if dinosh:
                if isinstance(main_food, Porrige):
                    porrige.sort = porrige.list_porrige[(porrige.list_porrige.index(porrige.sort)+1) % len(porrige.list_porrige)]
                main_food = list_main[(list_main.index(buffer[1]) + 1) % len(list_main)]
            else:
                sec_food = list_sec[(list_sec.index(buffer[2]) + 1) % len(list_sec)]

            drink_day = list_dr[(list_dr.index(buffer[3]) + 1) % len(list_dr)]

            dinosh = not dinosh
            switcher = buffer[0]

        newdayfood = editing(dayfood)
        dfprint(newdayfood)
        print(' ')
        dayfood.clear()
        day += 1
        fruit_day = list_fr[(list_fr.index(fruit_day)+1)%len(list_fr)]
        f.write('\n')

if __name__ == '__main__':
    list_main = [omlette, dumplings, porrige, potato, pasta, veg_mix]

    list_sec = [sandwich, muesli, salad, curd]

    list_fr = [banana, apple]

    list_dr = [soda, cofee, milk, cacao, juice, tea, alc]

    f = open('schedule.txt', 'w')

    schedule(list_main, list_sec, list_fr, list_dr, f)

    print("Расписание загружено в .txt файл, который находится в папке проекта")
    f.close()
    # вывод
