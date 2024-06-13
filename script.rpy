label start:
    $ endings = []
    python:
        def add_ending(text, is_good):
            ending = (text, is_good)
            if ending not in endings:
                endings.append(ending)
                return 'Поздравляем вы достигли новой концовки'
    python:
        name = renpy.input("Как вас зовут?")

        ggname = name.strip().capitalize() or "Анон"
    define gg = Character('[ggname]', color="#c8ffc8")

    jump location1

label location1:
    scene bg cave1
    show gg idle1

    'Ища заветный вырванный листок, [ggname] попадает в глубокую заросшую мхом нору.'
    'На терпком сероватом грунте лежат камни и разные безделушки... однако, взгляд приковывает свежая собачья тушка в дальнем узком углу.'
    show dog justdied
    'Не дышит, но еще теплая.'

    menu:
        "Остаться с собакой":
            "[ggname] погиб от удушения во время секса. (Плохая концовка) "
            "[add_ending(text='[ggname] погиб от удушения во время секса.', is_good=False)]"
            return
        "Идти дальше":
            'Анон пинает мертвое животное и издает звуки умирающей чайки.'
            ' Идет дальше и не решается отступать, какой бы не была дорога.'
            jump location2
            
label location2:
    scene bg dark_corridors
    'Путь наедине с собственными мыслями прерывает звук на развилке, отдаленно напоминающий стон.'
    ' Скорее предсмертные возгласы и оханье, которые беспощадно искажает эхо. Оно внушает животный страх, кровь пульсирует в ушах.' 
    menu:
        'Стоит ли идти на звук?'
        'Проявить смелость':
            pass
        'Бежать со всех ног в другую сторону':
            pass
        

    
