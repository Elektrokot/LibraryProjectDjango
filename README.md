### 1. **Как запустить локально**
```markdown
## Запуск локально

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Elektrokot/LibraryProjectDjango.git
cd LibraryProjectDjango
```

2. Создайте `.env` на основе `.env.example`:
```bash
cp .env.example .env
```

3. Запустите с помощью Docker Compose:
```bash
docker compose up --build
```


---

### 2. **Как настроить GitHub Secrets**
```markdown
## Настройка GitHub Actions

Добавьте в `Settings > Secrets and variables > Actions` следующие переменные:

- `SSH_KEY_SERVER`: приватный SSH-ключ сервера
- `SSH_USER`: имя пользователя на сервере (например, `ubuntu`)
- `SERVER_IP`: IP-адрес сервера
- `DEPLOY_DIR`: директория на сервере (например, `/home/ubuntu/myapp`)
- `DOCKER_HUB_USERNAME`: имя пользователя Docker Hub
- `DOCKER_HUB_ACCESS_TOKEN`: токен доступа к Docker Hub
```

---

### 3. **Как запустить workflow**
```markdown
## Запуск CI/CD

Workflow запускается автоматически при каждом `push` в репозиторий.

Чтобы вручную запустить:
1. Перейдите во вкладку `Actions`
2. Выберите нужный workflow
3. Нажмите `Run workflow`
```

---
