from gui.sensor_formats import hundredths_format, thousands_format, int_format
from re import search
from PyQt5 import QtGui, QtCore, QtWidgets
from numpy import ndarray
from collections import OrderedDict
from datetime import datetime
from gui.start_stop_clear import clear_gui


# [Command, repeat interval, class]
COMMANDS = [
    ['GTM', 1, 'TimeUpdate'],
    ['STS', 1, 'StatusUpdate'],
    ['get_sensor_readings', 1, 'SensorUpdate'],
    ['logger_info', 10, 'DeploymentUpdate'],
    ['FSZ', 5, 'FileSizeUpdate'],
    ['CTS', 10, 'FileSizeUpdate'],
    ['CFS', 10, 'FileSizeUpdate'],
    ['GSN', 10, 'SerialNumberUpdate'],
    ['GFV', 10, 'SimpleUpdate']
]

FILE_SIZE = {
    'FSZ': ('File size {:0.2f} MB', 'label_file_size'),
    'CTS': (' of {:0.2f} GB available', 'label_sd_total_space'),
    'CFS': ('SD card free space: {:0.2f}','label_sd_free_space')
}

SIMPLE_FIELD = {
    'GTM': ('Logger Time: {}', 'label_logger_time'),
    'GFV': ('Firmware Version: {}', 'label_firmware')
}

SENSORS = OrderedDict(
    [('ax', thousands_format),
     ('ay', thousands_format),
     ('az', thousands_format),
     ('mx', int_format),
     ('my', int_format),
     ('mz', int_format),
     ('temp', thousands_format),
     ('batt', hundredths_format)]
)

LOGGER_INFO = {
    'DP': ('Deployment Number: {}', 'label_deployment'),
    'MN': ('Model Number: {}', 'label_model')
}

ERROR_CODES = [
    (2, 'Delayed start'),
    (4, 'SD card error'),
    (8, 'MAT.cfg error'),
    (16, 'Safe shutdown'),
    (32, 'SD retry error'),
    (64, 'ADXL data error'),
    (128, 'Stack Overflow')
]


class Commands:
    def __init__(self, gui):
        self.gui = gui
        self.command_schedule = []
        self.command_handlers = {}
        self.make_commands()

    def make_commands(self):
        self.command_handlers = {}
        for command, _, klass in COMMANDS:
            handler_obj = globals()[klass]
            self.command_handlers[command] = handler_obj(self.gui)

    def get_schedule(self):
        command_schedule = []
        for command, repeat, _ in COMMANDS:
            command_schedule.append([command, repeat, 0])
        return command_schedule

    def command_handler(self, query_results):
        query_command, data = query_results
        handler = self.command_handlers.get(query_command)
        if handler:
            handler.update(query_results)


class Update:
    def __init__(self, gui):
        self.gui = gui

    def update(self, query_results):
        raise NotImplementedError


class SimpleUpdate(Update):
    def __init__(self, gui):
        super().__init__(gui)
        self.widget = None

    def update(self, query_results):
        command, data = query_results
        format_, widget_name = SIMPLE_FIELD[command]
        self.widget = getattr(self.gui, widget_name)
        self.widget.setText(format_.format(data))


class TimeUpdate(SimpleUpdate):
    def update(self, query_results):
        super().update(query_results)
        _, data = query_results
        logger_time = datetime.strptime(data, '%Y/%m/%d %H:%M:%S')
        computer_time = datetime.now()
        diff = abs(logger_time - computer_time).total_seconds()
        if diff > 60:
            style = 'background-color: rgb(255, 255, 0);'
        else:
            style = ''
        self.widget.setStyleSheet(style)


class SerialNumberUpdate(Update):
    def update(self, query_results):
        command, data = query_results
        self.gui.label_serial.setText('Serial Number: {}'.format(data))
        self.gui.statusbar_serial_number.setText(
            '  Connected to {}  '.format(data))


class FileSizeUpdate(Update):
    def update(self, query_results):
        command, data = query_results
        format_, widget_name = FILE_SIZE[command]
        self.widget = getattr(self.gui, widget_name)
        numeric_data = search('[0-9]+', data).group()
        numeric_data = float(numeric_data) / 1024**2
        self.widget.setText(format_.format(numeric_data))


class StatusUpdate(Update):
    def __init__(self, gui):
        super().__init__(gui)
        self.gui = gui
        self.rabbit_icon = QtGui.QIcon()
        self.rabbit_icon.addPixmap(
            QtGui.QPixmap(':/icons/icons/icons8-running-rabbit-48.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopped_icon = QtGui.QIcon()
        self.stopped_icon.addPixmap(
            QtGui.QPixmap(':/icons/icons/icons8-private-48.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def update(self, query_results):
        command, data = query_results
        status_code = int(data, 16)
        self._show_running(self._running(status_code))
        self.gui.label_status.setText(self.description(status_code))

    def _running(self, status_code):
        return False if status_code & 1 else True

    def description(self, status_code):
        running = 'running' if self._running(status_code) else 'halted'
        status_str = 'Device is {}'.format(running)
        for value, string in ERROR_CODES:
            if status_code & value:
                status_str += ' - {}'.format(string)
        return status_str

    def _show_running(self, state):
        self.gui.pushButton_start.setEnabled(not state)
        self.gui.pushButton_stop.setEnabled(state)
        self.gui.pushButton_sync_clock.setEnabled(not state)
        icon = self.rabbit_icon if state is True else self.stopped_icon
        self.gui.pushButton_status.setIcon(icon)
        self.gui.pushButton_status.setIconSize(QtCore.QSize(36, 36))
        status = '  Device Running  ' if state else '  Halted  '
        self.gui.statusbar_logging_status.setText(status)


class SensorUpdate(Update):
    def update(self, query_results):
        command, data = query_results
        for index, sensor in enumerate(SENSORS.keys()):
            self._set_item_text(index, 1, self.enabled_string(sensor, data))
            self._set_item_text(index, 2, self.value_string(sensor, data))

    def _set_item_text(self, row, col, value):
        item = QtWidgets.QTableWidgetItem(value)
        self.gui.tableWidget.setItem(row, col, item)

    def enabled_string(self, sensor, readings):
        if readings and sensor in readings:
            return 'Yes'
        return 'No'

    def value_string(self, sensor, readings):
        if not readings:
            return ''
        reading = readings.get(sensor, '')
        if isinstance(reading, ndarray):
            return self._format_sensor_value(sensor, reading[0])
        return self._format_sensor_value(sensor, reading)

    def _format_sensor_value(self, sensor, value):
        return SENSORS[sensor](value)


class DeploymentUpdate(Update):
    def update(self, query_results):
        command, data = query_results
        for tag in LOGGER_INFO:
            if tag in data:
                format_, widget_name = LOGGER_INFO[tag]
                widget = getattr(self.gui, widget_name)
                widget.setText(format_.format(data[tag]))


class ConnectionStatus:
    def __init__(self, gui):
        self.gui = gui
        self.connected_icon = QtGui.QIcon()
        self.connected_icon.addPixmap(
            QtGui.QPixmap(':/icons/icons/icons8-usb-connected-48.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.not_connected_icon = QtGui.QIcon()
        self.not_connected_icon.addPixmap(
            QtGui.QPixmap(':/icons/icons/icons8-usb-disconnected-48.png'),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def update(self, state):
        if state is False:
            clear_gui(self.gui)
            self.gui.pushButton_connected.setIcon(self.not_connected_icon)
        else:
            self.gui.pushButton_connected.setIcon(self.connected_icon)
            self.gui.label_connected.setText('Connected on USB')
