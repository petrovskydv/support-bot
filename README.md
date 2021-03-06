# Обучаемый бот для службы поддержки

Этот бот может отвечать на типовые вопросы пользователей. Если бот не понимает о чём речь, он просто молчит в ответ. 

Бот работает с [Telegram](https://telegram.org/) и [ВКонтакте](https://vk.com/).

Пример результата для [Telegram](https://telegram.org/):

![](docs/telegram_bot.gif)

Пример результата для [ВКонтакте](https://vk.com/):

![](docs/vk_bot.gif)

## Распознавание фраз
Для распознавания фраз используется [DialogFlow](https://cloud.google.com/dialogflow/es/docs).

Для этого необходимо создать:
* [аккаунт](https://cloud.google.com/dialogflow/es/docs/quick/setup)
* [агента](https://cloud.google.com/dialogflow/es/docs/quick/build-agent)
* [JSON-ключ](https://cloud.google.com/docs/authentication/getting-started)

При создании аккаунта вы получите идентификатор проекта, например такой:
```
moonlit-dynamo-211973
```

## Создание бота в [Telegram](https://telegram.org/)
Вы получите его API ключ. Выглядит он так:
```
95132391:wP3db3301vnrob33BZdb33KwP3db3F1I
```
Для этого нужно:
1. Написать [Отцу ботов](https://telegram.me/BotFather)
    * `/start`
    * `/newbot`

Отец ботов попросит ввести два имени. Первое — как он будет отображаться в списке контактов, можно написать на русском. Второе — имя, по которому бота можно будет найти в поиске. Должно быть английском и заканчиваться на bot (например, `notification_bot`)

## Как установить
Скачайте проект на свой компьютер.
В папке проекта необходимо создать файл `.env`. В этом файле нужно создать переменные, указанные в образце.

Образец файла:
```
TELEGRAM_TOKEN='<API-ключ бота>'
TELEGRAM_CHAT_ID='<ID чата для мониторинга>'
VK_TOKEN='<токен группы ВК>'
GOOGLE_APPLICATION_CREDENTIALS='<путь к JSON-ключу>'
GOOGLE_PROJECT_ID='<id проекта GOOGLE>'
TRAINING_PHRASES_FILEPATH='<путь к файлу с фразами>'
```
Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Как обучить бота
Необходимо подготовить `json` файл с тренировочными фразами. Пример файла:
```json
{
    "Устройство на работу": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Если вы хотите устроиться к нам, напишите на почту info@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
    },
    "Забыл пароль": {
        "questions": [
            "Не помню пароль",
            "Не могу войти",
            "Проблемы со входом",
            "Забыл пароль",
            "Забыл логин",
            "Восстановить пароль",
            "Как восстановить пароль",
            "Неправильный логин или пароль",
            "Ошибка входа",
            "Не могу войти в аккаунт"
        ],
        "answer": "Если вы не можете войти на сайт, воспользуйтесь кнопкой «Забыли пароль?» под формой входа. Вам на почту придёт письмо с дальнейшими инструкциями. Проверьте папку «Спам», иногда письма попадают в неё."
    }
}
```
В папке проекта лежит пример файла `questions.json`.
Путь к файлу с тренировочными фразами необходимо указать в файле `.env` в переменной `TRAINING_PHRASES_FILEPATH`.

Для обучения бота необходимо ввести в командной строке:
```
python bot_training.py
```

## Как запустить

Для запуска бота [Telegram](https://telegram.org/) на компьютере необходимо ввести в командной строке:
```
python telegram_bot.py
```
Для запуска бота [ВКонтакте](https://vk.com/) на компьютере необходимо ввести в командной строке:
```
python vk_bot.py
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

## Лицензия

Этот проект находится под лицензией MIT License - подробности см. в файле LICENSE.