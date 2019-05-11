#!/usr/bin/env python3
"""
mainwindow.py, main application

Pace & Time Calculator
Created by Chad Timmermans (www.github.com/chadtimmermans)
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget

from calculatormethods import CalculatorException
from calculators import PaceCalculator, TimeCalculator
from logging import Logging
from ptwidgets import PTButton


DEBUGGING = False  # Set to true for error output to terminal.


class PaceTimeCalculator(QMainWindow):
    """Main Window for PaceTimeCalculator application."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configure the main window.
        self.setWindowTitle('Pace & Time Calculator')
        self.setStyleSheet('background: white;')
        self.move(100, 100)

        # Initialize and set the central widget.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Initialize GUI layouts for the calculators.
        self.logging = Logging()
        self.time_calculator = TimeCalculator()
        self.pace_calculator = PaceCalculator()

        # Initialize the reset button.
        self.reset_button = PTButton('Reset Application')

        # Connect calculator layout buttons.
        self.time_calculator.calculate_button.clicked.connect(self.time_calculator_button_clicked)
        self.pace_calculator.pace.calculate_button.clicked.connect(self.pace_button_clicked)
        self.pace_calculator.time.calculate_button.clicked.connect(self.time_button_clicked)
        self.pace_calculator.distance.calculate_button.clicked.connect(self.distance_button_clicked)
        self.logging.button_clear_all.clicked.connect(self.logging.clear_all)
        self.logging.button_clear_latest.clicked.connect(self.logging.clear_latest)

        # Connect the reset button.
        self.reset_button.clicked.connect(self.reset_application_button_clicked)

        # Initialize and configure the main layout.
        main_layout = QGridLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(self.time_calculator, 0, 0, Qt.AlignCenter)
        main_layout.addLayout(self.pace_calculator, 1, 0, Qt.AlignCenter)
        main_layout.addLayout(self.logging, 2, 0, Qt.AlignCenter)
        main_layout.addWidget(self.reset_button, 3, 0, Qt.AlignCenter)

        # Attach the main layout to the central widget.
        central_widget.setLayout(main_layout)
        self.setFixedSize(500, 825)

    def time_calculator_button_clicked(self):
        """Calculate button for TimeCalculator."""
        try:
            operator, left_time, right_time, time = self.time_calculator.button_clicked()
            self.logging.add_to_log(operator, left_time, right_time, time)
        except CalculatorException as ce:
            self.time_calculator.output.set_invalid(str(ce))
            if DEBUGGING:
                raise

    def pace_button_clicked(self):
        """"Convert timestamp and use with distance to calculate a pace."""
        try:
            time, distance, output = self.pace_calculator.pace_clicked()
            self.logging.add_to_log('Pace', time, distance, output)
        except CalculatorException as ce:
            self.pace_calculator.pace.output.set_invalid(str(ce))
            if DEBUGGING:
                raise

    def time_button_clicked(self):
        """Convert timestamp and use with distance to calculate overall time.."""
        try:
            pace, distance, output = self.pace_calculator.time_clicked()
            self.logging.add_to_log('Time', pace, distance, output)
        except CalculatorException as ce:
            self.pace_calculator.time.output.set_invalid(str(ce))
            if DEBUGGING:
                raise

    def distance_button_clicked(self):
        """Convert timestamps and calculate distance."""
        try:
            time, pace, output = self.pace_calculator.distance_clicked()
            self.logging.add_to_log('Distance', time, pace, output)
        except CalculatorException as ce:
            self.pace_calculator.distance.output.set_invalid(str(ce))
            if DEBUGGING:
                raise

    def reset_application_button_clicked(self):
        """Reset the application and all gui components."""
        self.time_calculator.reset_widgets()
        self.pace_calculator.reset_widgets()
        self.logging.clear_all()


def main():
    """PaceTimeCalculator application entry point."""
    app = QApplication(sys.argv)
    win = PaceTimeCalculator()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
