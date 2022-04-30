# Контрольная работа #7
Напишите сайт для библиотеки. В библиотеке есть книги, авторы, жанры. Каждая книга может относиться к нескольким жанрам, и считается написанной одним автором.
## Этап 1
Создайте модель книги. У книги есть название, год издания, автор (на этом этапе - строчное поле), описание - текстовое поле. Все поля, кроме описания - обязательные.

**Создайте для книги следующие страницы CRUD:**
Список книг - выводите здесь название книги и имя автора, добавьте пагинацию.
Просмотр книги - выводите здесь все поля книги
Добавление книги
Редактирование книги
Удаление книги (с подтверждением).

Отсортируйте книги по алфавиту.

**Дополнительно (+2 балла):**
Выведите строку из ссылок с буквами от А до Я. Каждая ссылка фильтрует книги, у которых название или имя автора начинается с этой буквы. Для выбора поля, по которому фильтровать, выведите переключатель: "По книге" или "По автору" (тоже ссылки). При переключении типа фильтра выбранная буква должна сохраняться. При переключении буквы выбранный тип фильтра должен сохраняться.
## Этап 2
Создайте модель автора. У автора есть имя, даты жизни (могут быть пустыми), биография (описание). Даты жизни могут быть пустыми, остальные поля - обязательные.

Замените поле автора в книге на внешний ключ к модели автора.

**Создайте для автора следующие страницы CRUD:**
Список авторов - выводите здесь имя автора, добавьте пагинацию.
Просмотр автора - выводите здесь все поля автора и список его книг в виде названий книг и ссылок на них. Отсортируйте книги по году издания.

Обновите форму книги и страницы книги:
Создание книги
Редактирование книги
Просмотр книги / списка книг.

При создании книги вместо имени автора в форме передавайте код автора в url, и подставляйте его автоматически. Сделайте ссылку на эту страницу со страницы просмотра автора.

Там, где ранее выводилось имя автора из поля в книге, теперь выводите имя автора из связанного объекта модели "Автор".

При редактировании книги показывайте форму, где автор выбирается из выпадающего списка (виджет для поля типа ForeignKey по умолчанию).

Также оставьте ссылку на добавление книги с главной страницы, которая будет показывать форму для книги с выпадающим списком для выбора автора (другая форма).

**Дополнительно (+2 балла):**
Выведите список книг автора с пагинацией на его странице, аналогичный списку книг на главной странице. Используйте здесь включаемый шаблон с переменной.
## Этап 3
Создайте модель жанра. У жанра есть название. Добавьте в книгу поле для связи с жанром. У книги может быть несколько жанров, а в один жанр может входить множество книг.

Сделайте следующие страницы:
Создание жанра
Список жанров
Удаление жанра (без подтверждения)

В списке жанров выводите название жанра, ссылку на список книг в этом жанре, и ссылку на удаление жанра.

Для книг добавьте страницу поиска по названию, автору и жанру, и страницу результатов поиска. Ссылка из списка жанров ведёт сюда.

Добавьте поле выбора жанра в форму книги. Просто включите его название в список полей формы, оставьте стандартный виджет (мульти-селект).

**Дополнительно (+1 балл):**
Поменяйте виджет выбора жанров для книги на список чекбоксов (найдите подходящий класс в модуле django.forms).
Требования к шаблонам
Стилизуйте все страницы самостоятельно или с помощью Bootstrap.
Используйте контейнер. 
Элементы на страницах не должны слипаться.
Используйте любой шрифт или цветовую схему.
Создайте базовый шаблон и меню навигации.
Используйте включаемые шаблоны для повторяющихся блоков разметки.
Общие указания
Делайте регулярные коммиты (не меньше 15 коммитов).
Создайте дамп с тестовыми данными и сдайте его вместе с работой (загрузите в репозиторий).
Все страницы должны быть связаны ссылками.

