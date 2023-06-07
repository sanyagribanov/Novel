label prolog:
    scene table with fade
    play music "music/Waterbird.ogg"

    n "Эта история случилась солнечным летом 1898 года"
    n "Ближе к концу очередного учебного года объявили конкурс. Я бы и не обратила на него внимания, если бы не его условия."
    n "А именно, нужно было за две недели проявить свои писательские способности и написать роман на тему путешествия."
    n "Кстати, забыла представиться, мое имя Шарлотта, семнадцати лет от роду."
    n "Я с детства увлекаюсь писательством, и этот конкурс поможет раскрыться моему таланту. И мама в свое время 
    помогла мне определиться с будущим призванием. "
    n "Но получиться ли у меня всех удивить?"

    "Но в последнее время как-то не до удивлений толпы читателей"
    "От того, что ничего не можешь сделать долгое время, со злости можно начать говорить в пустоту"
    "Это мало помогает, но тишина давит на черепную коробку еще сильнее самого громкого и ужасного шума"
    c "Мысли вообще в голову не лезут, хоть целыми днями за столом сиди!"
    "За все время сколько занимаюсь писательством, это впервые"
    c "Никакого вдохновения, хоть тресни!"
    "Из-за повысившейся в этот момент тональности мой голос, словно грозовая туча, пронесся над стеллажами книг"

    play nature "audio/knock.ogg"
    "Кто-то стучится в дверь. Наверное мама"
    stop nature
    mar "Шарлотта, я войду?"
    "Услышав ее голос, я наполовину выдохнула, чтобы говорить более спокойнее"
    c "Конечно, мам, заходи"

    scene library with fade
    show marianna normal
    "В библиотеку вошла мама. На ее лице читалось некое недоумение"
    mar "Опять разговариваешь сама с собой?"
    "Я промолчала и отвела взгляд в сторону"
    show marianna happy
    mar "Ладно, можешь не отвечать"
    c "Тогда зачем приходила?"
    show marianna vhappy
    mar "Что, уже и родную дочь проверить нельзя? Гляди, уже со своим писательством с ума сойдешь"
    c "Так ты меня этому и научила..."
    "Мама не ответила, но заметила на моем столе пустой лист бумаги"
    show marianna sadsmile
    mar "Шарлотта, тебе бы отдохнуть. Сколько к тебе не загляну, все сидишь над пустым листом"
    c "Тут отдохнешь. Конкурс закончится через неделю. Смысл тогда от моего участия, если я ничего не могу выдавить из своего мозга..."
    "Руки совсем опустились. И вправду, никакого развития за последнее время"
    "Мама села рядом и положила мне руку на плечо. Она всегда понимала меня и старалась хоть немного подбодрить меня в случае каких-либо неудач"
    mar "Ты себя не бережешь. Безусловно, мне приятно видеть твои старания, но не нужно трудиться через силу"
    c "Да, наверное..."
    "Но мне в голову пришла одна интересная мысль, которой тут же захотелось поделиться с мамой"
    c "Мам, я тут подумала кое о чем. Мне хочется на эту неделю уехать из дома, чтобы написать книгу к конкурсу
    Возможно, на новых местах и вдохновение появится"
    c "Да и написать роман про путешествие, переживая то же самое, что и лирический герой. Мне уже нравится данная мысль. А тебе, мам?"
    show marianna surprised
    mar "Уехать? Одной?"
    c "Да, а что такого? Я уже давно не ребенок, так что почему бы и нет"
    mar "Просто я как мать за тебя волнуюсь. Не сказала бы, что готова так взять и отпустить тебя одну..."
    show marianna closed
    mar "Да и расходы в последнее время сильно увеличились. На путешествие тебе я вряд ли смогу дать хоть немного денег."
    c "Я не говорила про это. Можно путешествовать и без денег."
    show marianna happy
    mar "Ты своей горячей головой напоминаешь своего отца в молодости."
    show marianna vhappy
    mar "И когда собираешься ехать?"
    c "Почему бы не поехать прямо сейчас"
    c "Время вроде еще есть, да и собраться я вполне себе успею"
    hide marianna with dissolve
    stop music fadeout 1
    "Я взяла измученный моим творческим кризисом листок, после чего спешно покинула библиотеку"
    scene bedroom_1 with fade
    "Войдя в комнату, нужно понять, какие вещи стоит взять в дорогу"
    "Надо бы сначала найти три тетради. Одна из них служит черновиком, в других пишется чистовой роман"
    "Интересно, где я их видела в последний раз?"
    jump bedroom
    return

#меню первое
label bedroom:
    menu optional_name:
        "На кровати":
            jump bed
        "В шкафу":
            jump wardrobe
        "На тумбе":
            jump tumb
            

#выбор1
label bed:
    scene bedroom_1 with fade
    "Странно, но тетрадей на кровати нет. Возможно, они где-то еще."
    jump bedroom
    return

#выбор2
label tumb:
    scene book_hands with fade
    "Я взяла лежащую на тумбе тетрадь. Когда-то я записывала туда старые наработки романа"
    "Но в последствии отложила ее, многое, написанное там, совершенно мне не нравилось"
    "Однако, некоторые мелочи все же были обведены, тем самым помечены как важные"
    "Иногда старые записи неплохо помогают, хоть раннее они же считались ненужными"
    "Перелистнув на конец тетради, я вложила туда листок из библиотеки"

    scene bedroom_1 with fade
    "Вуаля, и тетрадь легким движением руки отправилась прямиком в сумку"
    $ NotebookCount += 1
    $ renpy.notify (f"Собрано тетрадей: {NotebookCount}/3")
    if NotebookCount == 3:
        scene bedroom_1 with fade
        "Я решила не задерживать мать и быстро спустилась вниз."
        jump garden
    else:
        scene bedroom_1 with fade
        "Собраны не все тетради! Нужно вернуться обратно"
        jump bedroom

#выбор3
label wardrobe:
    scene bedroom_1 with fade
    "На самом верху я увидела две тонкие тетради"
    "Встав на рядом стоящий стул, я взяла их и сложила их в сумку."
    "Брать чернила в дорогу смысла я не видела, поэтому взяла пару карандашей и нож для писем, чтобы их заточить."
    "Чтобы нож не повредил сумку, пришлось обмотать лезвие листом бумаги"
    "Напоследок я решила взять вторую рубашку. Помимо ее основной функции как запасной одежды, на ней можно будет спать как на подушке"
    "Перед тем, как покинуть комнату, я выглянула в окно. Снаружи меня ждала мама, желая проводить"

    $ NotebookCount += 2
    $ renpy.notify (f"Собрано тетрадей: {NotebookCount}/3")
    #чуть позже надо добавить ачивку
    if NotebookCount == 3:
        scene bedroom_1 with fade
        "Я решила не задерживать мать и быстро спустилась вниз."
        jump garden
    else:
        scene bedroom_1 with fade
        "Собраны не все тетради! Нужно вернуться обратно"
        jump bedroom
    return

# сад
label garden:
    scene garden with fade
    show marianna normal
    play nature birds
    "Мама стояла у дверей дома, держа в руках какой-то сверток"
    mar "Уже собираешься уходить?" 
    c "Наверное. Пока солнце не зашло за горизонт, нужно выдвигаться"
    mar "Хорошо. Тогда я дам тебе одну вещь"
    c "Этот сверток?"
    "Я показала на него рукой"
    show marianna vhappy
    mar "Немного не угадала. Это моя дорожная накидка. Тебе она будет впору, да и ночью не замерзнешь"
    "Я взяла накидку из рук мамы и примерила ее. Она оказалась довольно просторной, а еще в ней было довольно уютно"
    c "Большое спасибо, мам"
    mar "Пожалуйста, моя дорогая"
    c "Ладно, думаю, мне пора. Надеюсь, что спустя неделю у меня все будет готово"
    show marianna vhappy
    mar "С богом, Шарлотта"
    "Мама обняла меня напоследок. Внутри меня на мгновение возникло ощущение, что мне не хочется ее покидать"
    "Но видимо придется..."
    hide marianna with dissolve
    "Собравшись с чувствами, я покинула родной дом, видя, как мама машет мне рукой вслед"
    "Так начался первый день моего путешествия..."
    # и тут надо добавить ачивку
    stop nature fadeout 1
    jump day_1
    return