# carbon-calculator

This app will automatically re-deploy to Elastic Beanstalk on every push to the main branch via the Github actions workflow in `.github/workflows/main.yml`.

Because Elastic Beanstalk expects the flask app to be named `application`, set the `FLASK_APP` environment variable to `application.py` before running Flask. To run in debug mode locally, set the environment variable instead of using the parameter in `application.run()` so that the production app is not in debug mode. For example, on Linux:
```
$ setenv FLASK_DEBUG=1
$ setenv FLASK_APP=application.py
$ flask run
```

All installation dependencies required in the deployed app must be included in `requirements.txt`. If you are using a virtual environment, you can install the requirements locally from `requirements.txt` with `pip3 install -r requirements.txt` or output the installed packages in your virtual environment into `requirements.txt` with `pip3 freeze > requirements.txt`
