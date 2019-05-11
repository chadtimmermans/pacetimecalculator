"""
calculatormethods.py, contains calculation stuff for the buttons

Pace & Time Calculator
Created by Chad Timmermans (www.github.com/chadtimmermans)
"""


class CalculatorException(Exception):
    """Exception handling for when a calculation can not be made."""
    def __init__(self, msg='INVALID'):
        self.msg = msg
        super().__init__(self.msg)


def add_time(t1, t2):
    """Convert two timestamps into seconds and then add them together."""
    t1 = convert_to_seconds(t1)
    t2 = convert_to_seconds(t2)
    seconds = convert_to_timestamp(t1 + t2)
    return seconds


def subtract_time(t1, t2):
    """Convert two timestamps into seconds and then perform subtraction on them."""
    t1 = convert_to_seconds(t1)
    t2 = convert_to_seconds(t2)
    if t1 < t2:
        raise CalculatorException(msg='Left < Right')
    else:
        seconds = convert_to_timestamp(t1 - t2)
        return seconds


def calculate_pace(time_in_seconds, distance):
    """Calculate a pace time using an overall time and the distance covered."""
    pace_in_seconds = time_in_seconds / distance
    pace_rounded = int(round(pace_in_seconds))
    return convert_to_timestamp(int(pace_rounded))


def calculate_time(pace_in_seconds, distance):
    """Calculate an overall time using a pace time and the distance covered."""
    time_in_seconds = distance * pace_in_seconds
    return convert_to_timestamp(int(time_in_seconds))


def calculate_distance(time_in_seconds, pace_in_seconds):
    """Calculate the distance covered using an overall time and a pace."""
    if time_in_seconds < pace_in_seconds:
        raise CalculatorException(msg='Time < Pace')
    else:
        distance = time_in_seconds / pace_in_seconds
        return f'{distance:.2f}'  # truncate to 2 decimal positions


def convert_to_seconds(timestamp):
    """Convert a timestamp (HH:MM:SS) into seconds."""
    try:
        if timestamp.count(':'):
            colons = timestamp.count(':')
            position = timestamp.split(':')
            if colons == 2:
                hours = int(position[0]) * 3600
                minutes = int(position[1]) * 60
                seconds = int(position[2])
                return hours + minutes + seconds
            elif colons == 1:
                minutes = int(position[0]) * 60
                seconds = int(position[1])
                return minutes + seconds
        return int(timestamp)  # no colon, interpret as seconds
    except:
        raise CalculatorException


def convert_to_timestamp(seconds):
    """Convert seconds into a timestamp (HH:MM:SS)."""
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time = f'{hours}:{minutes}:{seconds}'
    return time
