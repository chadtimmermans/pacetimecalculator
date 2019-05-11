"""
logging.py, gui for the logging

Pace & Time Calculator
Created by Chad Timmermans (www.github.com/chadtimmermans)
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QPlainTextEdit, QVBoxLayout

from ptwidgets import PTButton, PTTitle


class Logging(QVBoxLayout):
    """GUI logging of any calculations."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.log_data = []

        # Initialize the top which contains the title and info.
        self.top = PTTitle(title='Log',
                           info='Summary of previous calculations.')

        # Initialize the button widgets for clearing log contents.
        self.button_clear_all = PTButton('Clear All')
        self.button_clear_all.setToolTip('Clear all log entries.')
        self.button_clear_latest = PTButton('Clear Latest')
        self.button_clear_latest.setToolTip('Clear the most recent log entry.')

        # Horizontal box to hold the buttons.
        hbox_buttons = QHBoxLayout()
        hbox_buttons.setAlignment(Qt.AlignCenter)
        hbox_buttons.addWidget(self.button_clear_all)
        hbox_buttons.addWidget(self.button_clear_latest)

        # Initialize the log output.
        self.log_output = QPlainTextEdit()
        self.log_output.setStyleSheet('font: bold 12px; color: white; background: navy; border: 4px outset black;')
        self.log_output.setFixedSize(450, 175)
        self.log_output.setReadOnly(True)

        # Set the layout.
        self.setAlignment(Qt.AlignCenter)
        self.addLayout(self.top)
        self.addLayout(hbox_buttons)
        self.addWidget(self.log_output)

    def add_to_log(self, title, first, second, output):
        """Add an entry to the log based on title."""
        if 'Pace' in title:
            #  output = pace, first = time, second = distance
            self.log_data.insert(0, f'{output}  Pace   where   T={first}   &   D={second}')
        elif 'Time' in title:
            # output = time, first = pace, second = distance
            self.log_data.insert(0, f'{output}  Time   where   P={first}   &   D={second}')
        elif 'Distance' in title:
            # output = distance, first = time, second = pace
            self.log_data.insert(0, f'{output}  Distance   where   T={first}   &   P={second}')
        elif '+' in title:
            # output = left + right, first = left, second = right
            self.log_data.insert(0, f'{output}  =  {first}  +  {second}')
        elif '-' in title:
            # output = left - right, first = left, second = right
            self.log_data.insert(0, f'{output}  =  {first}  -  {second}')
        self.log_output.setPlainText('\n'.join(self.log_data))

    def clear_latest(self):
        """Clear most recent entry from log."""
        if len(self.log_data) == 0:  # log is already empty
            return
        else:
            del self.log_data[0]
            self.log_output.setPlainText('\n'.join(self.log_data))

    def clear_all(self):
        """Clear all contents of the log."""
        self.log_data = []
        self.log_output.clear()
