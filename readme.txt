This project is mainly to train usage of Qt GUI. 

Software for Desctops.

To ba also useful, it implements the monitoring of Device CO2-Ampel
which is composed of Raspberry Pi(including WiFi Stick), DHT-22 sensor, K-30 Sensor.
The Raspberry is configured to provide WiFi Hotspot with ssid CO2-Ampel with password aaaaaaaa
The raspberry provides DHCP server and has IP 192.168.12.1
The Data of Sensors are available via e.g. 192.168.12.1/sqlwraper.php?len=10
Details of the Software for Raspberry will be published later. 

src/  - Python sources of the guteluftGUI project, including ui project of QT Designer, text descriptions and some training versions.
WindowsPyQT4/  - some materials, to get project working on Windows 

Pavel Paulau