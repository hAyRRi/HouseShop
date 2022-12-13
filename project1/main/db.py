
owns = [
    {
        'street': 'Ривер стрит 31Б',
        'city': 'Бермингем',
        'img': 'https://pngimg.com/uploads/house/house_PNG74.png',
        'price': 80000 ,
        'raiting': 7,
        'about': 'Отличный дом для крепкой семьи!',
        'type': 'Home',
        'broker': 'kostya'
    },
    {
        'street': 'Голливуд 266А',
        'city': 'Лос-Анджелес',
        'img': 'https://primamediamts.servicecdn.ru/f/big/2765/2764023.png?f95dcf0a93aecb4119203c3858c7e8fc',
        'price': 120100 ,
        'raiting': 10,
        'about': 'Дом в самом центре Голливуда!',
        'type': 'Home',
        'broker': 'kostya'
    },
    {
        'street': 'Океан стрит 23А',
        'city': 'Канары',
        'img': 'https://dom.com.cy/upload/iblock/929/929f4891e41fa1039e7ae74dac1ce67f.jpg',
        'price': 100300 ,
        'raiting': 8,
        'about': 'Пентхаус на берегу океана!',
        'type': 'Pentauses',
        'broker': 'zheka'
    },
    {
        'street': 'Бейкер - стрит 221Б',
        'city': 'Лондон',
        'img': 'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__hero_banner__hb_image__1880bp/public/hero_banner/sherlock-holmes.jpg',
        'price': 60000 ,
        'raiting': 10,
        'about': 'Дом известного детектива',
        'type': 'Apartaments',
        'broker': 'zheka'
    },
    {
        'street': 'Хрещатик 120',
        'city': 'Киев',
        'img': 'https://mfair.ua/user/realty/53091/53091-penthaus-pechersk-terrasa-new-york-centr-kiev-61.jpg',
        'price': 45000 ,
        'raiting': 6,
        'about': 'Пентхаус в самом центре Киева',
        'type': 'Pentauses',
        'broker': 'zheka'
    },
]

currentType = 'All'

types = [
    'All',
    'Home',
    'Apartaments',
    'Pentauses'
]

isLogin = False
isAdmin = False

user = None

users = [
    {
        'login': 'lera',
        'password': 'val228',
        'img': 'https://www.meme-arsenal.com/memes/0a2f97e29a2a95c781d322ff3dc50d6b.jpg',
        'isAdmin': False
    },
    {
        'login': 'zheka',
        'password': 'zkh',
        'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrxguXcGMjtKPsxXlShapGw7X3f-mgSUH-xodjs7krz60rWOwV3brX3po60gUnnI09hL0&usqp=CAU',
        'isAdmin': False
    },
    {
        'login': 'admin',
        'password': 'aaaddd',
        'img': 'https://koshka.top/uploads/posts/2021-12/1639030708_1-koshka-top-p-koshki-rzhut-1.jpg',
        'isAdmin': True
    }
]

def GetHouseByStreet(street: str):
    for own in owns:
        if(own['street'] == street):
            return own
    return None
