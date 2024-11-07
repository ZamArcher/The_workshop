# Lesson 4_7 task 3
# mobile_devices = {
#     'cucuPhone': 2010,
#     'cucuBlet': 2013,
#     'cucuClock': 2015,
#     'cucuEar': 2018,
#     'cuCube': 2015,
# }

# home_devices = {
#     'cucuLot': 2011,
#     'cucuBlock': 2010,
#     'cucuWall': 2010,
#     'cucuMonitor': 2020,
#     'cucuLamp': 2015,
#     'cucuTable': 2016,
#     'cucuTV': 2017,
# }

# not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}

# result_catalog = {}


# # Допишите функцию выборки поддерживаемого девайса из словаря
# def get_supported_catalog(dict_devices, device):
#     supported_catalog = {}
#     if device in dict_devices:
#         supported_catalog[device] = dict_devices[device]
#     return supported_catalog


# all_devices = set(mobile_devices.keys()) | set(home_devices.keys())
# supported_devices = all_devices.difference(not_supported_devices)

# for device in supported_devices:
#     supported_mob_dev = get_supported_catalog(mobile_devices, device)
#     # Добавьте значение в словарь result_catalog
#     result_catalog.update(supported_mob_dev)
#     supported_home_dev = get_supported_catalog(home_devices, device)
#     # Добавьте значение в словарь result_catalog
#     result_catalog.update(supported_home_dev)


# print('Каталог поддерживаемых девайсов: ')
# print(result_catalog)
# ---------------------------------------
# def get_sum(a, b) -> int:
#     return a ** 2 + b ** 2


# print(f'Что же это было? {get_sum(5, 7)}') # test
# ------------------------------------------
from decimal import Decimal
import datetime as dt


DATE_FORMAT = "%Y-%m-%d"

# goods = {
#     'Пельмени Универсальные': [
#         # Первая партия продукта 'Пельмени Универсальные':
#         {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
#         # Вторая партия продукта 'Пельмени Универсальные':
#         {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
#     ],
#     'Вода': [
#         {'amount': Decimal('1.5'), 'expiration_date': None}
#     ],
# }

# goods for add()
# goods = {}

# goods for find()
# goods = {
#     'Яйца': [{'amount': Decimal('1'), 'expiration_date': datetime.date(2023, 6, 24)}],
#     'Яйца гусиные': [{'amount': Decimal('4'), 'expiration_date': datetime.date(2023, 7, 15)}],
#     'Морковь': [{'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 6)}]
# }

# goods for amound()
# goods = {
#     'Яйца': [{'amount': Decimal('1'), 'expiration_date': None}],
#     'Морковь': [
#         {'amount': Decimal('2'), 'expiration_date': dt.date(2023, 8, 1)},
#         {'amount': Decimal('3'), 'expiration_date': dt.date(2023, 8, 6)}
#     ],
#     'Вода': [{'amount': Decimal('2.5'), 'expiration_date': None}]
# }

# goods for expire()
goods = {
    "Хлеб": [
        {"amount": Decimal("1"), "expiration_date": None},
        {"amount": Decimal("1"), "expiration_date": dt.date(2023, 12, 9)},
    ],
    "Яйца": [
        {"amount": Decimal("2"), "expiration_date": dt.date(2023, 12, 12)},
        {"amount": Decimal("3"), "expiration_date": dt.date(2023, 12, 11)},
    ],
    "Вода": [{"amount": Decimal("100"), "expiration_date": None}],
}


def add(items, title, amount, expiration_date=None):
    """Добавляет продукт в словарь goods."""
    if title not in items:
        items[title] = []
    expiration_date = (
        dt.datetime.strptime(expiration_date, DATE_FORMAT).date()
        if expiration_date
        else expiration_date
    )
    list.append(items[title], {"amount": amount, "expiration_date": expiration_date})


# add(goods, "Яйца", Decimal("10"), "2023-9-30")
# print(goods)

# add(goods, 'Яйца', Decimal('3'), '2023-10-15')
# print(goods)

# add(goods, 'Вода', Decimal('2.5'))
# print(goods)


def add_by_note(items, note):
    """Добавляет продукт в словарь goods,
    преобразуя текстовое описание в структурированные данные."""
    parts = str.split(note, " ")
    # print(parts)
    if len(str.split(parts[-1], "-")) == 3:
        expiration_date = parts[-1]
        good_amount = Decimal(parts[-2])
        title = str.join(" ", parts[0:-2])
    else:
        expiration_date = None
        good_amount = Decimal(parts[-1])
        title = str.join(" ", parts[0:-1])
    add(items, title, good_amount, expiration_date)


# add_by_note(goods, 'Яйца Фабрики №1 4 2023-07-15')
# print(goods)


def find(items, needle):
    """Ищет в словаре goods заданное слово или строку
    и возвращает список продуктов, в названии которых есть это слово."""
    suitable_products = []
    for el in items.keys():
        if needle.lower() in el.lower():
            suitable_products.append(el)
    return suitable_products


# print(find(goods, 'йц'))


def amount(items, needle):
    """Возвращает количество запрошенного продукта."""
    product_list = find(items, needle)
    count = Decimal("0")
    for product in product_list:
        for el in items[product]:
            count += el["amount"]
    return count


# amount(goods, 'яйца')
# print(amount(goods, 'пельмени'))
# # Вывод: 1
# print(amount(goods, 'морковь'))
# # Вывод: 5


def expire(items, in_advance_days=0):
    """Возвращает список кортежей просроченных продуктов."""
    # dt_today = dt.date.today() - dt.timedelta(days=333)
    dt_today = dt.date.today()
    dt_today += dt.timedelta(days=in_advance_days)
    expired_products = {}

    for product in items:
        for el in items[product]:
            if el["expiration_date"] and el["expiration_date"] <= dt_today:
                if product in expired_products:
                    expired_products[product] += el["amount"]
                else:
                    expired_products[product] = el["amount"]

    return list(expired_products.items())
    # print(tuple_list)


# expire(goods, 2)
# Если функция вызвана 10 декабря 2023 года
print(expire(goods))
# Вывод: [('Хлеб', Decimal('1'))]
print(expire(goods, 1))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('3'))]
print(expire(goods, 2))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('5'))]
