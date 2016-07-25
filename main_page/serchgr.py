import vk

# строка запроса кода для получения аксесс токена. 396952789cd7cd8f07

# strreq = r"https://oauth.vk.com/authorize?client_id=5561499&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos ,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=code&v=5.53"

# строка запроса токена

# dfd = r"https://oauth.vk.com/access_token?client_id=5561499&client_secret=67mgnwNNHZFY2WvSf7dD&redirect_uri=https://oauth.vk.com/blank.html&code=a0dc8e06aede67017b"

## тут надо вернуть акссеесс токен
api = vk.API(session)
# api.wall.post(message=r'http://aaxbut.pythonanywhere.com')
href_ids = 'https://vk.com/id'
# поиск начальников
# ls_serch = api.users.search(sex=2, count="1000", age_from=30, position="начальник")
#for_iter = ls_serch[1:]
#for x in for_iter:
#    print(x)
ts1 = api.groups.search(q='C', city_id='74')
t = 1
for x in ts1[1:]:
    xc = api.groups.getById(group_ids=x['screen_name'], fields='can_post')
    print(xc)

