#RESTful-сервис на Django,
который
позволит пользователю произвести следующую последовательность действий (в формате
JSON):
1. Отправляем на endpoint `/tags/` POST-запрос, содержащий URL-адрес любой страницы
в интернете. В ответе приходит идентификатор задания на выполнение.
2. По GET-запросу к endpoint `/tags/<идентификатор_задания>` получаем количество
каждого типа HTML-тэгов (например, `{"html": 1, "head": 1, "body": 1, "p": 10,
"img": 2}`) на веб-странице или ошибку, если URL оказался чем-то отличным от HTMLстраницы, либо статус, что задание еще выполняется (формат произвольный).




Как запустить данный проект:

0. На машине должен быть установленный redis(проект настроен на локальный redis, в случае отличий изменить в settings.py).
1. Из коренной папки проекта активировать виртуальную среду: `source test/bin/activate.`
Все дальнейшие действия выполнять в виртуальной среде.
2. Запустить Redis: `redis-server.` 
3. Запустить воркер Celery из папки testwork: `celery worker -A testwork --concurrency=<макс.число задач>.`
4. Запустить сервер nginx: `python3 manage.py runserver.`
