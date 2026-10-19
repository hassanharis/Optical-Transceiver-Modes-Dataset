DATASHEET 

5.1 

## **SO-QSFP-DD-2C-10 / -4** 

QSFP-DD 2x 100G Ethernet, 1295.56nm/1300.05nm/1304.58nm/1309.14nm, 10km, 7.3dB, Dual CS 

## OVERVIEW 

The SO-QSFP-DD-2C-10 is a QSFP-DD form-factor transceiver for 2x 100Gbps Ethernet applications. It is intended for use in data center interconnect between switches, routers, storage equipment etc. for optical distances up to 10km over a SingleMode (SM) fiber cable. 

The transceiver has a dual CS connector interface which means that there are two singlemode fiber pairs connected to the transceiver, each transporting a 100Gbps signal. The SO-QSFP-DD-2C-10 is thus intended for 200G to 2x 100G breakout configurations using two 100G QSFP-28 transceivers on the 100G Ethernet side. The SO-QSFP28-LR4-10L has matching optical performance and is a recommended option for this. 

The electrical interface consists of eight 25.78G NRZ signals (SFF-8679) that are converted to eight channels/lanes (four per fiberpair) to transport the Ethernet signal. 

Digital diagnostics functions are available via an I[2] C interface, as specified by the QSFP-DD MSA.The transceiver is provided in two versions, compliant with Common Management Interface Specification CMIS3.0 and CMIS4.0. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey QSFP-DD||**Transmitter data:**||
|Transmission media|SM (Dual CS)||Output power, per lane|Min: -0.7dBm3)|
|Typical reach|10km|||Max: +4.5dBm3)|
|Nominal wavelengths|1295.56nm||Transmit wavelengths|1294.53 - 1296.59nm|
||1300.05nm|||1299.02 - 1301.09nm|
||1304.58nm|||1303.54 - 1305.63nm|
||1309.14nm|||1308.09 - 1310.19nm|
|Interface standards|100GBASE-LR4||**Receiver data:**||
|Bit rate support|2x 103.12Gbps1)||Minimum input power, per lane|-8.0dBm3) 4)|
||25.78Gbps2)||Overload (max power), per lane|+4.5dBm3) 4)|
|Protocol support|2x 100GbE||Wavelength range|1294.53 - 1296.59nm|
|Power budget|0 – 7.3dB|||1299.02 - 1301.09nm|
|Power consumption|< 8W|||1303.54 - 1305.63nm|
|Operating temperature|0°C to +70°C|||1308.09 - 1310.19nm|
|Storage temperature|-40°C to +85°C||DDM|Yes|
|1)Aggregated line rate 200GbE|||MSA compliance|QSFP-DD MSA|
|2)Line rate per lane||||CMIS3.0 / CMIS4.0|
|3)Average power, per lane|||||
|4)Specified at BER 1x10-12|||Dual CS interface||
|**Safety/regulatory compliance:**|||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||||
|RoHS compliance|||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.1 

## APPLICATION CODE LIST 

|**CMIS Application Code**|**Host format**|**Electrical interface**|**Payload**|**FEC**|**MSA**|
|---|---|---|---|---|---|
|1|2x100GBASE-R|2x CAUI-4 (4x 25G)|200G|No FEC|100GBASE-LR4 (Clause 88)|



## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-QSFP-DD-2C-10|QSFP-DD 2x100G Ethernet 10km 7.3dB CMIS3 Dual CS|
|SO-QSFP-DD-2C-10-4|QSFP-DD 2x100G Ethernet 10km 7.3dB CMIS4 Dual CS|



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

