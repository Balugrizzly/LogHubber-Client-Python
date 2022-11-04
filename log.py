import requests
import json
import time

import logging


def log(
    token: str,
    level: str,
    timestamp: float,
    log: str,
    project: str = None,
    app: str = None,
    client: str = None,
    url: str = "http://127.0.0.1:3000/log",
):

    data = {
        "Token": token,
        "Level": level,
        "Timestamp": timestamp,
        "Log": log,
        "Project": project,
        "App": app,
        "Client": client,
    }

    response = requests.post(url, data)
    response.raise_for_status()


log(
    "aslkd-asls-203",
    level="DEBZG",
    timestamp=time.time(),
    log=logging.warning("Logger Warning "),
)


class LogLevel:
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
    FATAL = "FATAL"


class Log:
    """
    Log Model
    """

    level: str
    timestamp: int
    log: str
    project: str
    app: str
    client: str

    def __init__(
        self, level: str, timestamp: int, log: str, project: str, app: str, client: str
    ) -> None:

        self.level = level
        self.timestamp = timestamp
        self.log = log
        self.project = project
        self.app = app
        self.client = client


class LogHubber:
    """
    LogHubber Client

    """

    # TODO: revisite url setup
    base_url = "http://127.0.0.1:3000/"
    url = base_url + "log"

    def __init__(self, base_url):
        self.base_url = base_url

    def debug(self, log):
        timestamp = int(time.time())

        log = Log(
            LogLevel.DEBUG,
            timestamp,
            log,
        )
        response = requests.post(self.url, data={"Level": "INFO"})

    def info(self):
        print("hi")

    def warning(self):

        print("warning")

    def error(self):
        raise NotImplemented

    def critical(self):
        raise NotImplemented

    def fatal(self):
        raise NotImplemented

    def _set_timestamp(self):
        raise NotImplemented
