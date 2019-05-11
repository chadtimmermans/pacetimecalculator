"""
ptwidgets.py, customized widgets for pace & time calculator

Pace & Time Calculator
Created by Chad Timmermans (www.github.com/chadtimmermans)
"""
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout


class PTButton(QPushButton):
    """Custom button for PaceTimeCalcualtor."""
    def __init__(self, text='Calculate', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('font: bold; color: blue; background: #799ad3;')
        self.setText(text)


class PTTitle(QVBoxLayout):
    """Custom QVBoxLayout with title and information labels."""
    def __init__(self, title, info, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Label for the title.
        title = QLabel(title)
        title.setStyleSheet('font: bold 20px; padding: 5px; background: navy; color: white; border: 6px outset black;')
        title.setAlignment(Qt.AlignCenter)

        # Label for the information header.
        info = QLabel(info)
        info.setStyleSheet('font: bold 14px; color: black;')
        info.setAlignment(Qt.AlignCenter)

        # Configure the main layout.
        self.setAlignment(Qt.AlignCenter)
        self.addWidget(title)
        self.addWidget(info)


class PTBox(QVBoxLayout):
    """Custom QVBoxLayout for either a pace, time, or distance box."""
    def __init__(self, title, first, second, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # The title widget.
        title = QLabel(title)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('font: bold 16px; padding: 3px; color: white; background: navy; border: 4px outset black;')

        # Widgets for first input.
        first_header = QLabel(first)
        first_header.setAlignment(Qt.AlignCenter)
        first_header.setStyleSheet('font: bold;')
        self.first_field = PTField(field=first)
        self.first_field.setAlignment(Qt.AlignCenter)

        # Widgets for second input.
        second_header = QLabel(second)
        second_header.setAlignment(Qt.AlignCenter)
        second_header.setStyleSheet('font: bold;')
        self.second_field = PTField(field=second)
        self.second_field.setAlignment(Qt.AlignCenter)

        # Button to submit user input.
        self.calculate_button = PTButton()

        # Determine default output based on title.
        if title == 'Distance':
            self.output = PTOutput(text='0.0')
        else:
            self.output = PTOutput(text='00:00:00')

        # Configure the main layout.
        self.addWidget(title)
        self.addWidget(first_header)
        self.addWidget(self.first_field)
        self.addWidget(second_header)
        self.addWidget(self.second_field)
        self.addWidget(self.calculate_button)
        self.addWidget(self.output)
        self.setAlignment(Qt.AlignCenter)


class PTField(QLineEdit):
    """Custom QLineEdit for output with either distance or time."""
    def __init__(self, field, *args, **kwargs):
        super().__init__(*args, **kwargs)

        regex_pattern = QRegExp()

        # Set the help information and the regular expression pattern based on the input field type.
        if field == 'Time' or field == 'Pace':
            self.setToolTip('Input hour:minute:second, minute:second, or just seconds.')
            self.setPlaceholderText('00:00:00')
            regex_pattern = QRegExp('^[^\\D][\\d]*:?[\\d]*:?[\\d]+')
        elif field == 'Distance':
            self.setToolTip('Decimal usage is optional.')
            self.setPlaceholderText('0.0')
            regex_pattern = QRegExp('^[\\d]*[.]?[\\d]*')

        # Use the regular expression pattern on the input field.
        validator = QRegExpValidator(regex_pattern, self)
        self.setValidator(validator)
        self.setStyleSheet('background: gray;')
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(90, 35)

    def focusInEvent(self, event):
        """Change background when focused."""
        self.setStyleSheet('background: white;')

    def focusOutEvent(self, event):
        """Change background when out of focus."""
        self.setStyleSheet('background: gray;')


class PTOutput(QLabel):
    """Custom QLabel for output with either distance or time."""
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the output label to defaults.
        self.text = text
        self.reset_widget()
        self.setAlignment(Qt.AlignCenter)

    def set_valid(self):
        """Change font color when user input is valid."""
        self.setStyleSheet('font: bold; color: blue;')

    def set_invalid(self, error_message):
        """Change font color when user input is invalid."""
        self.setStyleSheet('font: bold; color: red;')
        self.setText(error_message)

    def reset_widget(self):
        """Reset the widget back to default."""
        self.setText(self.text)
        self.setStyleSheet('color: black;')
