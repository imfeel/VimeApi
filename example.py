""" 
Пример работы с библиотекой vimeapi
"""
import vimeapi, os
api = vimeapi.VimeApi("token")
class program(): 
    def moders(): 
        moders = []
        for i in range(len(api.online_staff()[0])): 
            try: 
                moders.append(api.online_staff()[i]["username"])
            except IndexError: 
                break
        return (f'Всего модеров онлайн: {len(api.online_staff()[0])}' + '\nМодераторы онлайн: ' + ', '.join(map(str,moders)))
    def userstats(usernick): 
        username = api.user_name(usernick)[0]["username"]
        """
Поясняю для школоты, которая будет писать мне о том, что имя пользователя можно взять и из usernick (параметр)
обращения - при обращении к userstats можно ввести и xtraFRANCYz, а не xtrafrancyz, и API VimeWorld обработает
запрос, хоть ты и написал имя капсом, но выдавать такое имя нету смысла. Api само определит капс, и выведет
в "username" правильный ник.
        """
        guild = api.user_name(usernick)[0]["guild"]["name"]
        rank = api.user_name(usernick)[0]["rank"]
        level = api.user_name(usernick)[0]["level"]
        if guild == None: 
            return(f'Имя игрока: {username}\nИгрок не состоит в гильдии\nРанк игрока: {rank}\n Уровень игрока: {level}')
        elif guild == 'interdefected': 
            return(f'Имя игрока: {username}\nИгрок состоит в лучшей гильдии на VimeWorld\nРанк игрока: {rank}\n Уровень игрока: {level}')
        else: 
            return(f'Имя игрока: {username}\nИгрок состоит в гильдии {guild}\nРанк игрока: {rank}\nУровень игрока: {level}')
if __name__ == '__main__': 
    print(program.moders())
    try: 
        print(program.userstats(input('Введите ник пользователя, информациую которого хотите увидеть: ')))
        os.system("Pause")
    except: 
        print('Ошибка при обращении к Api')
    
