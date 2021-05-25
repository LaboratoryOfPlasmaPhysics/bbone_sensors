import configparser, os
from appdirs import user_config_dir


def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


_CONFIG_FNAME = str(user_config_dir(appname="bbone sensors", appauthor="LPP")) + "/config.ini"
mkdir(os.path.dirname(_CONFIG_FNAME))
_config = configparser.ConfigParser()
_config.read(_CONFIG_FNAME)


class ConfigEntry:
    def __init__(self, key1, key2, default=""):
        self.key1 = key1
        self.key2 = key2
        self.default = default

    def get(self):
        if self.key1 in _config and self.key2 in _config[self.key1]:
            return _config[self.key1][self.key2]
        else:
            return self.default

    def set(self, value):
        if self.key1 not in _config:
            _config.add_section(self.key1)
        _config[self.key1][self.key2] = value
        with open(_CONFIG_FNAME, 'w') as f:
            _config.write(f)


firmware_version_url = ConfigEntry("Teamcity", "latest_build_number",
                                   "https://hephaistos.lpp.polytechnique.fr/teamcity/guestAuth/app/rest/buildTypes/BBoneSensors_BBoneSensorsCapeFw_Build/builds/status:success/number")

firmware_url = ConfigEntry("Teamcity", "latest_firmware",
                           "https://hephaistos.lpp.polytechnique.fr/teamcity/guestAuth/repository/download/BBoneSensors_BBoneSensorsCapeFw_Build/.lastSuccessful/BBoneSensors_DS18B20.ino.STMicroelectronics.stm32.BBoneSensors.bin")

current_firmware_version = ConfigEntry("Firmware", "current_version", "0")

serial_port_name = ConfigEntry("serial", "port_name", "/dev/ttyO1")
serial_port_speed = ConfigEntry("serial", "baud", "115200")

graphite_hostname = ConfigEntry("graphite", "hostname", "129.104.6.165")
graphite_pickle_port = ConfigEntry("graphite", "pickle_port", "12004")
