DATASHEET 

6.0 

## **SFP28 25G-LR, I-TEMP** SFP28, 25G/10G Ethernet LR, 1310nm, SM, 10km, 7.0dB, I-temp, LC 

## TS2009-S31I-SO 

The TS2009-S31I-SO is an SFP+ form-factor transceiver for 25 Gbps Ethernet applications. Since the transmission rate can reach up to 28Gbps, the engineering and industry name is SFP28. It is intended for use in interconnect applications between data centers with switches, routers, storage equipment etc. The optical performance supports distances up to 10km over a SingleMode (SM) fiber. TS2009-S31I-SO also supports the high data rate CPRI option 10 having a bit rate of 24.33024 Gbps. With the Clock and Data Recovery (CDR) functionality disabled, the transceiver can also be used for 10GbE-LAN and 10GbE-WAN services. 

TS2009-S31I-SO uses a single 1310nm channel @ 25.78 Gbps to transport a 25G Ethernet signal. As stipulated by the 25G Ethernet standards, Forward Error Correction (FEC) is required to be implemented by the host equipment to ensure reliable system operation. The optical parameters below will provide a bit error ratio (BER) of 5 x 10[-5 ] for 25G Ethernet. FEC will provide the required quality for secure service. 

Digital diagnostics functions are available via an I2C interface, as specified by the MSA. 

The transceiver operates in the Industrial temperature range (I-temp) -40°C to 85°C (-40°F to 185°F). 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey SFP28||**Transmitter data:**||
|Transmission media|SM (2x LC)||Output power|Min: -5.0dBm3)|
|Typical reach|10km|||Max: +2.0dBm3)|
|Nominal wavelength|1x 1310nm||Transmit wavelength|1295 – 1325nm|
|Bit rate support|24.33 / 25.78 Gbps1)||**Receiver data:**||
||9.953 / 10.312 Gbps2)||Minimum input power|-12.0dBm3) 4)|
|Protocol support|25GE1)||Overload (max power)|+2.0dBm3) 4)|
||10GE LAN/WAN2)||Wavelength range|1260 – 1325nm|
||CPRI opt 101)||LOS De-assert|Max -16dBm|
|Power budget|0 – 7.0dB||LOS Assert|Min -30dBm|
|Dispersion penalty|Max 2.7dB||LOS Hysteresis|Min 0.5dB|
|Power consumption|< 1.5W||DDM|Yes|
|Operating temperature|-40°C to +85°C||MSA compliance|SFF-8402|
|Storage temperature|-40°C to +85°C||||
|1)CDR engaged|||||
|2)CDR disengaged|||||
|3)Average power|||||
|4)at 25.78 Gbps (25GE) and|BER 5E-5||||
|**Safety/regulatory compliance:**|||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||||
|RoHS compliance|||||




Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.0 

Note: The 25GbE specification states that a 25GbE interface can operate with or without FEC. The optical data above is defined at a BER of 5x10[-5] , implying that FEC shall be enabled on the host equipment to provide required quality at specified distance. 

## ORDERING INFORMATION 

|**Ordering number**|**Ordering number**|**Description**||||
|---|---|---|---|---|---|
|TS2009-S31I-SO||SFP28, 25G/10G|Ethernet LR, 1310nm, SM,|10km, 7.0dB, I-temp, LC||
|CDR RATE SELECT LOGIC||||||
|**Logic OR of**|**Logic OR of**|||||
|**RS0 Pin and**|**RS1 Pin and**|**RX**|**TX**|**Status of**|**Status of**|
|**Bit 110.3 of**|**Bit 118.3 of**|**Data Rate**|**Data Rate**|**RX CDR**|**TX CDR**|
|**A2H**|**A2H**|||||
|High / 1|High / 1|24.33G/25.78G|<br>24.33G/25.78G|CDR Engaged|CDR Engaged|
|Low / 0|Low / 0|9.95G/10.31G|9.95G/10.31G|CDR Bypassed|CDR Bypassed|



## GENERAL DEFINITIONS 

|**Parameter**|**Description**||
|---|---|---|
||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
|Technology|DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
||AOC: Active Optical Cable. Optical cable with attached connectors.||
|Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
|Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.||
|Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
|Protocols|Protocols within supported bit rate range.||
|Nominal wavelength|Typical wavelength(s) from transmitter.||
|Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
|Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
|Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.||
||Max operating case temperature range.||
|Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
||Industrial temperature range (I-temp):-40°C to +85°C (-40°F to +185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.0 



Subject to change without notice. For more information visit smartoptics.com. 

