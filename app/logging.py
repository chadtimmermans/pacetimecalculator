"""
logging.py, gui for the logging

Pace & Time Calculator
Created by Chad Timmermans (www.github.com/chadtimmermans)
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPlainTextEdit, QVBoxLayout

from ptwidgets import PTButton, PTTitle


class Logging(QFrame):
    """GUI logging of any calculations. Can be disabled with menu bar option."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.log_data = []

        # init widgets
        self.top = PTTitle(title='Log',
                           info='Summary of previous calculations.')

        self.hbox_buttons = self.create_hbox_for_buttons()
        self.hbox_buttons.setAlignment(Qt.AlignCenter)

        self.log_output = QPlainTextEdit()
        self.log_output.setStyleSheet('font: bold 12px; color: white; background: navy; border: 4px outset black;')
        self.log_output.setFixedSize(450, 175)
        self.log_output.setReadOnly(True)

        # init main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(self.top)
        main_layout.addLayout(self.hbox_buttons)
        main_layout.addWidget(self.log_output)
        self.setLayout(main_layout)

    def create_hbox_for_buttons(self):
        self.button_clear_all = PTButton('Clear All')
        self.button_clear_all.setToolTip('Clear all log entries.')
        self.button_clear_latest = PTButton('Clear Latest')
        self.button_clear_latest.setToolTip('Clear the most recent log entry.')

        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(self.button_clear_all)
        hbox_buttons.addWidget(self.button_clear_latest)
        return hbox_buttons

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
        try:
            del self.log_data[0]
            self.log_output.setPlainText('\n'.join(self.log_data))
        except IndexError:
            pass

    def clear_all(self):
        """Clear all contents of the log."""
        self.log_data = []
        self.log_output.clear()
