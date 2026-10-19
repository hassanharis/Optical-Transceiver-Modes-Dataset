DATASHEET 

6.0 

## **QSFP28 100G-PSM4 10KM** 

## QSFP28, 100GBASE-PSM4, 1310nm, SM, DDM, 8.6dB, 10km, MPO/APC 

## TQ2037-S31C-SO 

The TQ2037-S31C-SO is a QSFP28 form-factor transceiver for 100Gbps Ethernet applications. It is intended for use in inter- and intra-connect applications within and between data centers between switches, routers, storage equipment etc. The optical performance is based on the 100GBASE PSM4 industry standard but with an extended reach of 10km over a SingleMode (SM) 12fiber ribbon cable. 

TQ2037-S31C-SO has an optical performance enabling distances of up to 10km over a SingleMode (SM) ribbon fiber. Forward Error Correction (FEC) is required to be implemented by the host to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 5 x 10[-5] . FEC will render in the required BER of better than 1 x 10[-12] . 

TQ2037-S31C-SO uses four 1310nm channels/lanes @ 25.78 Gbps to transport the Ethernet signal. The transceiver enables aggregation with 4x25G asynchronous streams of 25GBASE-LR. The transceiver has a single 12 lane optical fiber MPO/MTPconnector interface. Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey QSFP28||**Transmitter data:**||
|Transmission media|SM (1x MPO/APC)||Output power, total|Max +8.0dBm3)|
|Typical reach|10km||Output power, per lane|Min: -4.0dBm3)|
|Nominal wavelength|4x 1310nm|||Max: +2.0dBm3)|
|Interface standards|100GBASE-PSM4||Transmit wavelength|1295 – 1325nm|
|Bit rate support|103.12Gbps1)||**Receiver data:**||
||25.78 Gbps2)||Minimum input power, per lane|-12.6dBm3) 4)|
|Protocol support|100GbE||Overload (max power), per lane|+2.0dBm3) 4)|
|Power budget|0 – 8.6dB||Wavelength range|1295 – 1325nm|
|Path penalty|2.9dB||LOS Assert|Min -24dBm|
|Power consumption|< 3.5W||LOS De-assert|Max -12.5dBm|
|Operating temperature|0°C to +70°C||LOS Hysteresis|Min 0.5dB|
|Storage temperature|-40°C to +85°C||DDM|Yes|
||||MSA compliance|QSFP28 MSA|
|1)Aggregated line rate 100GbE|||||
|2)Per lane|||||
|3)Average power|||||
|4)Specified at BER 5x10-5|||||



**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 

MPO (Multi-fiber Push On) is an optical connector for ribbon cables with four to twenty-four fibers. MTP is a specific brand of an MPO connector. 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

6.0 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TQ2037-S31C-SO|QSFP28, 100G Eth PSM4, SM 4x 1310nm, 10km, 8.6dB, MPO/APC|



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
|Temperature range|Standard temperature range (C-temp):  0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
||Industrial temperature range (I-temp):-40°C to +85°C (-40°F to +185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

