# Логика игры

# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define c = Character('Шарлотта', color="#3c296d")
define mar = Character('Мама', color="#5f1919", image='marianna')
define n = Character(None, kind=nvl)
define g = Character('Девушка', color="#1c660c", image='martha')
define mt = Character('Марта', color="#1c660c", image='martha')
define u = Character('Дядя Марты', color="#0e425d", image='uncle')
define gel = Character('Девушка', color="#a47000", image="eleonora")
define el = Character('Элеонора', color="#a47000", image="eleonora")

define config.mouse={"default" : [("gui/cursors/Cursor 003_Green.png", 0,0)]}
#Аудио
define audio.knock = "audio/knock.ogg"
define audio.writing = "audio/writing-pencil.ogg"
define audio.grass = "audio/grass-steps.ogg"
define audio.birds = "audio/birds-singing.ogg"
define nature.horse = "audio/horse_steps.ogg"
define nature.fireplace = "audio/fireplace.ogg"
#Музыка
define music.peace = "music/New-Endings.ogg"
define music.wbird = "music/Waterbird.ogg"
define music.tgp = "music/The-Golden-Peas.ogg"
define music.soul = "music/Soul.ogg"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
 

init:
    $ left_2 = Position(xpos=0.3, ypos=1.1)
    $ right_2 = Position(xpos=0.7, ypos=1.1)
    $ center_2 = Position(xpos=0.5, ypos=1.1)

init:
    python:
        onn = ImageDissolve("eye.png", 2.0, 20, reverse=False)
        off = ImageDissolve("eye.png", 2.0, 20, reverse=True)

        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # центральная позиция
                self.dist = dist    # максимальное расстояние, в пикселях, от начальной точки
                self.child = child
                
            def __call__(self, t, sizes):
                # Число с плавающей точкой в целое число... превращает числа с плавающей точкой
                # в целые.      
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)

init:
    $ sshake = Shake((0,0,0,0), 1.0, dist = 15)
    
init:
    python:
        NotebookCount = 0

        allAchievements = {
            "1-2-3-4-5! Я иду искать" : "achievements/book.png",
            "Вокруг света за 7 дней" : "achievements/earth.png",
            "Хранительница очага" : "achievements/village_girl.png",
            "Психолог" : "achievements/roses.png",
            "Спокойная ночь" : "achievements/bear.png",
            "Обед раздели с другом" : "achievements/bag.png",
            "Вместе веселей" : "achievements/doll.png"
        }

        imageAchieve = None

        persistent.AddAchieve = []

        def AddAchieve(achieve, message):
            if not achieve in persistent.AddAchieve:
                persistent.AddAchieve.append(achieve)
                imageAchieve = allAchievements[achieve]
                renpy.show_screen("notifyAchieve", message, achieve, imageAchieve)
            
