This project is mainly to train usage of Qt GUI. 

Software for Desctops.

To be also useful, it implements the monitoring of Device CO2-Ampel
which is composed of Raspberry Pi(including WiFi Stick), DHT-22 sensor, K-30 Sensor.
The Raspberry is configured to provide WiFi Hotspot with ssid 'gl' with password 'aaaaaaaa'
The raspberry provides DHCP server and has IP 192.168.12.1
The Data of Sensors are available via e.g. 192.168.12.1/sqlwraper.php?len=10
Since it will not work without according hardware, I put here just a video (or screenshot), 
how it works(or how it looks like).

There should run according software on "server" (raspberry). It is published in
according git repository RHTCO2: https://github.com/paulau/RHTCO2.git 

src/  - Python sources of the guteluftGUI project, including ui project of QT Designer, text descriptions and some training versions.
WindowsPyQT4/  - some materials, to get project working on Windows 


Pavel Paulau
