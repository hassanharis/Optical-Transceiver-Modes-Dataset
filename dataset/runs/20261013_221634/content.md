DATASHEET 

6.1 

## **SFP28 ER 40km** 

## SFP28, 25G Ethernet ER, 1310nm, SM, 40km, 19dB, LC 

## TS2013-S31C-SO 

The TS2013-S31C-SO is an SFP+ form-factor transceiver for 25Gbps Ethernet and CPRI Option 10 applications. It is intended for use in interconnect applications between data centers with switches, routers, storage equipment etc. The optical performance supports distances up to 40km over a SingleMode (SM) fiber. 

TS2013-S31C-SO uses a single 1310nm channel to transport a 25G Ethernet or CPRI signal. As stipulated by the 25G Ethernet standards, Forward Error Correction (FEC) is required to be implemented by the host equipment in order to ensure reliable system operation. The optical parameters below will provide a bit error ratio (BER) of 5 x 10[-5 ] for 25G Ethernet. FEC will provide the required quality for secure service. 

TS2013-S31C-SO supports C-temp operating case temperature 0°C to +70°C. For I-temp version (0 to +85°C), see part number _SO-SFP28-ER-I_ 

Digital diagnostics functions are available via an I2C interface, as specified by the MSA. 

## TECHNICAL DATA 

|**Parameter**|**Value**||
|---|---|---|
|Technology|Grey SFP28||
|Transmission media|SM (2x LC)||
|Typical reach|40km||
|Nominal wavelength|1x 1310nm||
|Bit rate support|24.33 / 25.78Gbps||
|Protocol support|CPRI opt 10 / 25GE||
|Power budget|10 – 19dB||
|Dispersion penalty|< 2.7dB||
|Power consumption|< 1.5W||
|Operating temperature|0°C to +70°C||
|Storage temperature|-40°C to +85°C||



1) Average power 2) at 25.78Gbps (25GE) and BER 5E-5 **Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 

|**Parameter**|**Value**|
|---|---|
|**Transmitter data:**||
|Output power|Min: -3.0dBm1)|
||Max: +6.0dBm1)|
|Output power, OMA|Min: 0dBm|
||Max: 6.0dBm|
|Transmit wavelength|1295 – 1325nm|
|**Receiver data:**||
|Minimum input power|-21.0dBm1)|
|Minimum input power, OMA|-19.0dBm2)|
|Overload (max power)|-4.0dBm1) 2)|
|Wavelength range|1295 – 1325nm|
|LOS De-assert|Max -23dBm|
|LOS Assert|Min -35dBm|
|LOS Hysteresis|Min 0.5dB|
|DDM|Yes|
|MSA compliance|SFF-8402, 25GBASE-ER|



Note: The 25GbE specification states that a 25GbE interface can operate with or without FEC. The optical data above is defined at a BER of 5x10[-5] , implying that FEC shall be enabled on the host equipment to provide required quality at specified distance. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.1 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TS2013-S31C-SO|SFP28, 25G ER, 1310nm, SM, 40km, 18dB, LC|



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
||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

