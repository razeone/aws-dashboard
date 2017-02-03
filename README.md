# AWS-Dashboard

This is the repo for the AWS-Dashboard project.

### Quickstart

Create a file called `environ.rc` with the following data:

```
export APP_SETTINGS="develop"
export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"
export AWS_DEFAULT_REGION="SOME_DEFAULT_AWS_REGION"
```

Then you can run:

```
virtualenv -p python3.5 env
source env/bin/activate
pip install -r requirements/develop.txt
. environ.rc
python run.py
```
