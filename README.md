# Новостной парсер

Скрипт забирает материалы с ленты [«Новый День»](https://newdaynews.ru/today/) и складывает их в PostgreSQL. В контейнере запускается `main.py`: раз в 30 минут он вызывает `job()` из `pars_news.py`.

`job()` скачивает страницу ленты, находит ссылки новостей и из текста ссылки читает дату, время и заголовок. Затем открывает каждую новость, забирает текст и убирает из него служебные подписи сайта. Новая ссылка пишется в `links`, сама новость — в `news`.

## Схема

- `links`: `id`, уникальная `link`.
- `news`: `id`, `link_id` (внешний ключ на `links.id`, уникальный), уникальный `news_id`, `date`, `time`, `title`, `text`.

Таблицы создаются при импорте `database.py`. Строка подключения берётся из `DATABASE_URL`. Если её нет, адрес собирается из `POSTGRES_PASSWORD` (и при необходимости `POSTGRES_USER`, `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`). Пароль в коде не хранится.

## Запуск

```bash
cp .env.example .env
```

Заполните `.env`. `DATABASE_URL` можно оставить пустым.

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=choose-a-password
POSTGRES_DB=ParsNewsDB
DATABASE_URL=
```

Дальше:

```bash
docker compose up --build
```

Compose подставляет `${POSTGRES_PASSWORD}` в сервис Postgres и передаёт те же переменные в приложение. Хост базы внутри сети compose — `db`, порт `5432`, имя базы по умолчанию — `ParsNewsDB`.
