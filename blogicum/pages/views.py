from django.shortcuts import render

# Create your views here.
rules_list = [
    '''<b>Cамовыражение.</b> У наших пользователей должна
    быть возможность создать что-то своё, выразить себя,
    свои мысли и чувства.''',

    '''<b>Многообразие.</b> Мы уважаем и приветствуем разные
    мнения и культуры. Блогикум — это место, объединяющее
    самых разных людей. Поделитесь своим уникальным взглядом на мир.''',

    '''<b>Творчество.</b> Не важно, в какой области вы творите,
    это может быть литература, дизайн, программирование.
    Наши инструменты помогут вам раскрыть талант максимально
    просто и комфортно. ''',

    '''<b>Личность.</b> Мы сохраним ваши сокровенные мысли в тайне.
    Делитесь своей информацией только с теми, кого выбрали.
    Как и насколько засекречивать вашу личную информацию —
    определяете вы и только вы.''',
]

about_list = [
    '''Блогикум — это дом для творческих людей.
    Это — сообщество людей, для которых
    нет грани между ведением блога и дружбой в социальных сетях.''',

    '''Дружба и рассказы о новых, неизведанных впечатлениях — вот
    что вы найдете на нашем ресурсе.  Миллионы блогов по различным темам.
    Путешествия, политики, развлечения, мода, мода, литература, дизайн и все
    другие сферы человеческой деятельности.''',

    '''Творчество, разнообразие и свобода взглядов и самовыражения —
    основные черты наших пользователей.''',
]


def about(request):
    template = 'pages/about.html'
    context = {'about_list': about_list}
    return render(request, template, context)


def rules(request):
    context = {'rules_list': rules_list}
    template = 'pages/rules.html'
    return render(request, template, context)
