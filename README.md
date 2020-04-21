# Django Q Starter

本專案基於[YihaoSu/DjangoProjectStarter](https://github.com/YihaoSu/DjangoProjectStarter)專案，可當作具有Django Q排程功能的範例及專案起始樣板，目錄結構請見DjangoProjectStarter專案的README說明。

## 使用方式 - 建立本地端的開發環境
1.  下載此專案，並將DjangoQStarter/及django_q_starter/目錄更名為符合你的專案的名稱，並修改config/settings/
/base.py檔案中的[APPS_DIR變數的值](https://github.com/YihaoSu/DjangoQStarter/blob/master/config/settings/base.py#L8)(將django_q_starter更名)。 
```shell
git clone https://github.com/YihaoSu/DjangoQStarter.git
```

2. 安裝PostgreSQL (11.5以上的版本)、建立本地端用的資料庫，並以下面指令安裝所需Ubuntu packages
```shell
sudo apt install python3-dev libpq-dev
```

3. 依據你的開發環境(資料庫的帳密及資料庫名、DJANGO_SECRET_KEY等等)，修改dot_env_file_template檔中的設定值，並將檔名改為.env(如要使用django_q_starter/email_example app中的寄信功能，請在.env檔中設定好EMAIL相關值)

4. 利用[virtualenv](https://virtualenv.pypa.io/en/latest/)或[Conda](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)建立獨立的開發環境 (Python 版本: 依你的專案所需)

5. 啟動進入該開發環境後，輸入以下指令以便安裝專案所需的Python套件 (Django 版本: requirements檔是2.2 LTS, 依你的專案所需做變更)
```shell
cd 專案名稱
pip install -r requirements/local.txt
```

6. 在更名後的django_q_starter/目錄中，開發你專案所需的Django apps ，並擴充config/目錄中的設定檔及requirements/目錄中的套件需求檔。如要開發Django Q tasks排程功能，請參考範例[django_q_starter/email_example/tasks.py](https://github.com/YihaoSu/DjangoQStarter/blob/master/django_q_starter/email_example/tasks.py)及[Django Q的說明文件](https://django-q.readthedocs.io/en/latest/)

7. 執行完以下指令後，在瀏覽器輸入 http://127.0.0.1:8000 或是 http://localhost:8000 即可在本地端瀏覽此Django專案所建立的網頁
```shell
# 執行manage.py時會預設載入 config/settings/local.py 本地端設定檔
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic # 有使用[static files](https://docs.djangoproject.com/en/2.2/howto/static-files/)才需要，會在專案根目錄中建立名為staticfiles的資料夾，並將各APP所屬static files彙集到此資料夾中
python manage.py qcluster & python manage.py runserver
```

## 伺服器環境注意事項
請在伺服器中加入 /etc/systemd/system/qcluster.service 並啟用該服務

```text
[Unit]
Description=Django-Q Cluster for Myproject
After=network.target
Wants=gunicorn.service

[Service]
User=user name
Group=group name
WorkingDirectory=project directory
ExecStart=python路徑 manage.py qcluster --settings=config.settings.production
Restart=always

[Install]
WantedBy=multi-user.target
```