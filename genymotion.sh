#!/bin/bash

instance1=$(gmsaas instances start 8f373fa1-97fa-4652-84c8-a006459d50a0  device_SamGa8)

# sprawdzamy czy utworzyla sie instancja
gmsaas instances list

# zestawiamy polaczenie z instancji1 z portem lokalnym 9999
gmsaas instances adbconnect $instance1 --adb-serial-port=9999

# sprawdzamy czy sie polaczyl
adb devices 

# uruchamiamy testy (pytest)
pytest testCaseGenyMotion.py

# konczymy 
gmsaas instances stop 8f373fa1-97fa-4652-84c8-a006459d50a0  
