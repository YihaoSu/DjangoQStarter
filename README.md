# Django Project Starter

## 專案目錄結構
本專案可當作Django專案的起始樣板，為了讓專案更為結構化且符合實務(區分測試及正式機等不同環境的設定及所需套件)， 此專案採用Django專案範本產生器[Cookiecutter Django](https://github.com/pydanny/cookiecutter-django)及[Two Scoops of Django 1.11](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11)一書所偏好的目錄結構， 而非Django project預設的目錄結構。 專案根目錄[DjangoProjectStarter/](https://github.com/YihaoSu/DjangoProjectStarter)包含以下子目錄及檔案:

* [config/](https://github.com/YihaoSu/DjangoProjectStarter/tree/master/config)目錄: 包含[settings/](https://github.com/YihaoSu/DjangoProjectStarter/tree/master/config/settings)目錄、[URL設定檔](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/config/urls.py)及[WSGI設定檔](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/config/wsgi.py)。 [settings/](https://github.com/YihaoSu/DjangoProjectStarter/tree/master/config/settings)目錄中又包含用以進行本地端開發 ([local.py](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/config/settings/local.py)) 及正式上線([production.py](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/config/settings/production.py))等不同狀況時的設定檔, 這兩個檔都繼承自基本設定檔[base.py](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/config/settings/base.py)。 

* [ starter/](https://github.com/YihaoSu/DjangoProjectStarter/tree/master/starter)目錄: 包含此專案中司職不同功能的[apps](https://docs.djangoproject.com/en/2.2/ref/applications/)及其所屬的[templates](https://docs.djangoproject.com/en/2.2/ref/templates/)和[static files](https://docs.djangoproject.com/en/2.2/howto/static-files/)。

* [requirements/](https://github.com/YihaoSu/DjangoProjectStarter/tree/master/requirements)目錄: 包含用以進行本地端開發 ([local.txt](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/requirements/local.txt)) 及正式上線([production.txt](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/requirements/production.txt))等不同狀況時的Python套件需求, 這三個檔都繼承自基本套件需求檔[base.txt](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/requirements/base.txt)。 

* [README.md](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/README.md): 此專案GitHub repository的主說明文件。

* [.gitignore](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/.gitignore): 包含git commit時不需要版本控制而要忽略的檔案列表及規則。

* [manage.py](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/manage.py):  [Django的命令列工具](https://docs.djangoproject.com/en/2.2/ref/django-admin/)。

* [dot_env_file_template](https://github.com/YihaoSu/DjangoProjectStarter/blob/master/dot_env_file_template): 環境變數.env檔模板，請依據你的開發環境修改、擴展檔案中的設定(資料庫帳密等等)，並更名為.env ，為了安全性請務必更改模板中的設定值，且不要將本地端/正式機中的.env檔上傳到GitHub，請參考[Django-environ的文件](https://django-environ.readthedocs.io/en/latest/)。


## 使用方式  - 建立本地端的開發環境
1.  下載此專案，並將DjangoProjectStarter/及starter/目錄更名為符合你的專案的名稱
```shell
git clone https://github.com/YihaoSu/DjangoProjectStarter.git
```

2. 利用[virtualenv](https://virtualenv.pypa.io/en/latest/)或[Conda](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)建立獨立的開發環境 (Python 版本: 依你的專案所需)

3. 啟動進入該開發環境後，輸入以下指令以便安裝專案所需的Python套件 (Django 版本: requirements檔是2.2 LTS, 依你的專案所需做變更)
```shell
cd 專案名稱
pip install -r requirements/local.txt
```

4. 依據你的專案所需，安裝並建立PostgreSQL或MySQL資料庫

5. 依據你的開發環境(資料庫的帳密及資料庫名、DJANGO_SECRET_KEY等等)，修改dot_env_file_template檔中的設定值，並將檔名改為.env

6. 在更名後的starter/目錄中，開發你專案所需的Django apps ，並擴充config/目錄中的設定檔及requirements/目錄中的套件需求檔

7. 執行完以下指令後，在瀏覽器輸入 http://127.0.0.1:8000 或是 http://localhost:8000 即可在本地端瀏覽此Django專案所建立的網頁
```shell
# 執行manage.py時會預設載入 config/settings/local.py 本地端設定檔
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # 有使用Django admin才需要
python manage.py collectstatic # 會在專案根目錄中建立名為staticfiles的資料夾，並將各APP所屬static files彙集到此資料夾中
python manage.py runserver
```