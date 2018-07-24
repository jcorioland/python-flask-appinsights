import os
import logging
from logging import StreamHandler
from flask import Flask
from applicationinsights.flask.ext import AppInsights

# create Flask app
app = Flask(__name__)

# retrieve the application insights instrumentation key from OS environment variable named INSTRUMENTATION_KEY
INSTRUMENTATION_KEY = os.getenv('INSTRUMENTATION_KEY')
if INSTRUMENTATION_KEY is None:
    print('INSTRUMENTATION_KEY environment variable was not found.')
    exit()

app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = INSTRUMENTATION_KEY
appinsights = AppInsights(app)

# keep stdout/stderr logging using StreamHandler
streamHandler = StreamHandler()
app.logger.addHandler(streamHandler)
app.logger.setLevel(logging.DEBUG)

# apply format on all log handlers
for logHandler in app.logger.handlers:
  logHandler.setFormatter(logging.Formatter('[FLASK-SAMPLE][%(levelname)s]%(message)s'))

# ensure that the telemetry gets sent
@app.after_request
def after_request(response):
  if INSTRUMENTATION_KEY is not None:
    appinsights.flush()
  return response

@app.route("/")
def hello():
    app.logger.debug('This is a debug log message')
    app.logger.info('This is an information log message')
    app.logger.warn('This is a warning log message')
    app.logger.error('This is an error message')
    app.logger.critical('This is a critical message')
    return "Hello World!"

@app.route("/error")
def hello_error():
  a = 42
  b = 0
  c = a/b
  return "a / b = {c}".format(c=c)