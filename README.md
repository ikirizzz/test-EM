# test-EM. -- Effective Mobile — Тестовое задание DevOps

## Используемые технологии
- **Backend**: (http.server) `python:3.12-slim`
- **Reverse Proxy**: `nginx:1.27-alpine`
- **Контейнеризация**: Docker `29.3` + Docker Compose `5.1.0`

## Как запустить
Убедитесь что у вас установлено и настроено окружение git, docker compose.
После командами, склонируйте репозитарий и запустите сборку и запуск контейнеров.
```bash
git clone https://github.com/ikirizzz/test-EM
cd test-EM
docker compose up -d
```

## Как проверить результат 
- **Windows (Docker desktop)**: Открыть адрес `http://localhost` через браузер
- **Linux**: Запустить команду `curl http://localhost` в терминале
- **Корректный ответ**: должен быть в виде `Hello from Effective Mobile!`

## Схема работы
- Сервис nginx (контейнер em-nginx) принимает все запросы на порт 80 и проксирует их на порт 8080 сервиса `backend` (em-backend) по имени контейнера внутри Docker-сети (em-network).
- По ТЗ: Backend недоступен снаружи, запуск от non-root + healthcheck + depends_on.

