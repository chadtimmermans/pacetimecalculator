"""
calculators.py, gui stuff for the calculators

Pace & Time Calculator
Created by Chad Timmermans (www.github.com/chadtimmermans)
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QListWidget, QVBoxLayout

import calculatormethods
from ptwidgets import PTBox, PTButton, PTField, PTTitle, PTOutput


class PaceCalculator(QVBoxLayout):
    """GUI for the pace calculator."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize the widgets.
        top = PTTitle(title='Pace Calculator',
                      info='Calculate a pace, an overall time, or an overall distance.')
        self.pace = PTBox(title='Pace', first='Time', second='Distance')
        self.time = PTBox(title='Time', first='Pace', second='Distance')
        self.distance = PTBox(title='Distance', first='Time', second='Pace')

        # Horizontal box to hold all of the widgets except for the title.
        hbox = QHBoxLayout()
        hbox.addLayout(self.pace)
        hbox.addLayout(self.time)
        hbox.addLayout(self.distance)

        # Set the layout.
        self.addLayout(top)
        self.addLayout(hbox)
        self.setAlignment(Qt.AlignCenter)

    def pace_clicked(self):
        """Convert a timestamp and use it with the distance to calculate a pace."""
        time = self.pace.first_field.text()
        time_in_seconds = float(calculatormethods.convert_to_seconds(time))
        distance = float(self.pace.second_field.text())
        output = calculatormethods.calculate_pace(time_in_seconds, distance)

        # Update the GUI and return the input/output values.
        self.pace.output.setText(output)
        self.pace.output.set_valid()
        return time, distance, output

    def time_clicked(self):
        """Convert a timestamp and use it with the distance to calculate an overall time."""
        pace = self.time.first_field.text()
        pace_in_seconds = float(calculatormethods.convert_to_seconds(pace))
        distance = float(self.time.second_field.text())
        output = calculatormethods.calculate_time(pace_in_seconds, distance)

        # Update the GUI and return the input/output values.
        self.time.output.setText(output)
        self.time.output.set_valid()
        return pace, distance, output

    def distance_clicked(self):
        """Convert the time and pace timestamps and calculate the distance."""
        time = self.distance.first_field.text()
        time_in_seconds = float(calculatormethods.convert_to_seconds(time))
        pace = self.distance.second_field.text()
        pace_in_seconds = float(calculatormethods.convert_to_seconds(pace))
        output = calculatormethods.calculate_distance(time_in_seconds, pace_in_seconds)

        # Update the GUI and return the input/output values.
        self.distance.output.setText(output)
        self.distance.output.set_valid()
        return time, pace, output

    def reset_widgets(self):
        """Reset all the widgets."""
        # Reset the pace widgets.
        self.pace.first_field.clear()
        self.pace.second_field.clear()
        self.pace.output.reset_widget()

        # Reset the time widgets.
        self.time.first_field.clear()
        self.time.second_field.clear()
        self.time.output.reset_widget()

        # Reset the distance widgets.
        self.distance.first_field.clear()
        self.distance.second_field.clear()
        self.distance.output.reset_widget()


class TimeCalculator(QVBoxLayout):
    """GUI for the time calculator."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize the top layout.
        top = PTTitle(title='Time Calculator',
                      info='Add or subtract time.')

        # Initialize widgets for the middle layout.
        self.left_field = PTField(field='Time')
        self.right_field = PTField(field='Time')
        self.arithmetic_list = QListWidget()
        self.arithmetic_list.setStyleSheet('font: bold 13px')
        self.arithmetic_list.setFixedSize(45, 38)
        self.arithmetic_list.addItem('+')
        self.arithmetic_list.addItem('-')
        self.arithmetic_list.setCurrentRow(0)

        # Initialize middle layout and add the middle widgets.
        middle = QHBoxLayout()
        middle.addWidget(self.left_field)
        middle.addWidget(self.arithmetic_list)
        middle.addWidget(self.right_field)
        middle.setAlignment(Qt.AlignCenter)

        # Initialize widgets for the bottom layout.
        self.calculate_button = PTButton()
        self.output = PTOutput('00:00:00')

        # Initialize bottom layout and add the bottom widgets.
        bottom = QHBoxLayout()
        bottom.addWidget(self.calculate_button)
        bottom.addWidget(self.output)
        bottom.setAlignment(Qt.AlignCenter)

        # Configure the main layout.
        self.addLayout(top)
        self.addLayout(middle)
        self.addLayout(bottom)
        self.setAlignment(Qt.AlignCenter)

    def button_clicked(self):
        """Calculate button to either add or subtract time."""
        # Collect the input.
        left_time = self.left_field.text()
        right_time = self.right_field.text()
        operator = self.arithmetic_list.currentItem().text()
        time = ''

        # Add or subtract time.
        if operator == '+':
            time = calculatormethods.add_time(left_time, right_time)
        elif operator == '-':
            time = calculatormethods.subtract_time(left_time, right_time)

        # Update the GUI and return the input/output values.
        self.output.setText(time)
        self.output.set_valid()
        return operator, left_time, right_time, time

    def reset_widgets(self):
        """Reset all the time calculator widgets."""
        self.left_field.clear()
        self.right_field.clear()
        self.arithmetic_list.setCurrentRow(0)
        self.output.reset_widget()
