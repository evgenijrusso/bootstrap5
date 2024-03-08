1. Подкаталог - `bootstrap`, тестовая версия каталога 'drafts'.
2. Сразу выбрал `poetry`, подключился питоновский интерпретатор, создал виртуальное окружение
и появился pyproject.toml. Виртуальное окружение bootstrap5-0Kr9FeLQ-py3.11
3. `poetry run django-admin startproject AdvPortal`
4. изменил имя рабочего каталога `work`
5. poetry install => poetry.lock
6. `pip install django django-bootstrap5` Устанавливаю django и django-bootstrap5
7. Настроил конфигурцию запуска проектв через порт 8020
8. Создал новое приложение `callboard` (`python manage.py startapp callboard`)
9. Активизация GIT: VSC -> Enable Version Control Integration, в выпадающем меню выбираем Git
10. * `cd advportal` => python manage.py migrate (initial migrations)б появился db.sqlite3
11. После создания модели, попытался сделать миграции  python manage.py `migrate`, появилась ошибка. 
Error: django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency callboard.0001_initial on database 'default'.
Решение: закомментировать временно:
- #'django.contrib.admin (INSTALLED_APPS)' 
- #path('admin/', admin.site.urls), (urlpatterns).
После изменений, миграция прошла. Убрал обратно комментарии.