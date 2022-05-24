# Basic open-domain QA system using BERT

## Instructions
1. Clone the repository into a local folder
```
$ git clone <repo url>
```

2. Download `train`, `dev` and `test` files containing subset of SQUAD data into a `/data` directory at the root level - [Link to data](https://drive.google.com/drive/folders/1K0gkypdXDnHUZ0c8qgrWbRjN2vJnG4Hj?usp=sharin")

3. Download the latest model checkpoint from this [folder](https://drive.google.com/drive/folders/1bGXP881qGySLorWQpMBHuuGWniByirU-?usp=sharing) and put it into a `ckpt` directory at the root level. 

4. Create a virtual environment and install dependencies
```
$ virtualenv venv
$ source venv/bin/activate
$ (venv) pip install -r requirements.txt
```
5. Navigate to the Django project directory `odqabert` and launch the Django development server

``` 
$ cd odqabert
$ (venv) opdqabert % python manage.py runserver
```
You should see the following output in your terminal:

```
INFO:bert_model.apps:2022-05-24 01:51:53.627196+00:00 - Loading QA BERT model from path /Users/juanavalanche/Desktop/open_domain_QA/ckpt
INFO:bert_model.apps:2022-05-24 01:51:59.352528+00:00 - QA BERT model loaded into memory
INFO:bert_model.apps:2022-05-24 01:52:01.230258+00:00 - Loading QA BERT model from path /Users/juanavalanche/Desktop/open_domain_QA/ckpt
INFO:bert_model.apps:2022-05-24 01:52:05.643590+00:00 - QA BERT model loaded into memory
Watching for file changes with StatReloader
INFO:django.utils.autoreload:Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 24, 2022 - 01:52:06
Django version 4.0.4, using settings 'odqabert.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
6. Click on http://127.0.0.1:8000/ to start interacting with the system
