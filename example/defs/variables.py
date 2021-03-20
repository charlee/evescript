from datetime import datetime


def currentTime():
    return datetime.now()


def lightSensor():
    return 25


VARIABLES = {
    '$currentTime': currentTime,
    '$lightSensor': lightSensor,
}
