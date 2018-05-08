class CyanRequest(object):
    link = 'https://www.cian.ru/cat.php'
    deal_type = ''
    metro = 0
    maxprice = 0
    minprice = 0
    offer_type = ''
    room1 = 0
    room2 = 0
    room3 = 0
    room4 = 0
    room9 = 0
    type = 0
    region = 1

    def __init__(self):
        self.deal_type = 'rent'
        self.offer_type = 'flat'
        self.type = 4
        self.region = 1


class DomofondRequest(object):
    link = 'https://www.domofond.ru/arenda-odnokomnatnyh-kvartir-akademicheskaya-m17'
    PropertyTypeDescription = ''
    PriceFrom = 0
    PriceTo = 0
    RentalRate = ''
    Rooms = ''

    def __init__(self):
        self.RentalRate = 'Month'
        self.PropertyTypeDescription = 'kvartiry'


class AvitoRequest(object):
    link = 'https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok'
    pmax = 0
    pmin = 0
    metro = 0
