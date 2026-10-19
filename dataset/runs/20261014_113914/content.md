DATASHEET 

5.5 

## **SO-QSFP-DD-4C-DR4-M / -DR4-4-M** 

QSFP-DD 400G-DR4 Ethernet, 4x100G-DR PAM4, 4x 1311nm, 500m, 3dB, MPO12/APC 

## OVERVIEW 

The SO-QSFP-DD-4C-DR4-M is a QSFP-DD form-factor transceiver for 400Gbps Ethernet applications. It is intended for use in data center interconnect between switches, routers, storage equipment etc. for optical distances up to 500m over a SingleMode (SM) ribbon fiber cable. 

The electrical interface consists of eight 53.125G signals (400GAUI-8) that are converted to eight PAM4-modulated channels/lanes to transport the Ethernet signal. The transceiver can also be set in 4x100GAUI-2 mode (application code 2) to enable 400G to 4x 100G break-out configurations. Digital diagnostics functions are available via an I[2] C interface, as specified by the QSFP-DD MSA. 

The optical interface to the transceiver is an MPO12 Angled Polished Connector (APC). 

Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 2.4 x 10[-4] . 

The transceiver is provided in two versions, compliant with Common Management Interface Specification CMIS3.0 and CMIS4.0. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey QSFP-DD||**Transmitter data:**||
|Transmission media|SM (1x MPO12)||Output power, per lane|Min: -2.9dBm3)|
|Typical reach|500m|||Max: +4.0dBm3)|
|Nominal wavelengths|4x 1311nm||Transmit wavelength|1304.5 – 1317.5nm|
|Interface standards|400GBASE-DR4||**Receiver data:**||
|Electrical interfaces|400GAUI-8 or 4x100GAUI-2||Minimum input power, per lane|-5.9dBm3) 4)|
|Bit rate support|425Gbps1)||Overload (max power), per lane|+4.0dBm3) 4)|
||53.125Gbd2)||Wavelength range|1304.5 – 1317.5nm|
|Protocol support|400GbE||LOS Assert|Min -15dBm|
|Power budget|0 – 3.0dB||LOS De-assert|Max -10dBm|
|Power consumption|< 10W||LOS Hysteresis|Min 0.5dB|
|Operating temperature|0°C to +70°C||DDM|Yes|
|Storage temperature|-40°C to +85°C||MSA compliance|QSFP-DD MSA|
|1)Aggregated line rate 400GbE||||CMIS3.0 / CMIS4.0|
|2)Line baud rate per lane|||||
|3)Average power, per lane|||||
|4)Specified at BER 2.4x10-4|||||
|**Safety/regulatory compliance:**|||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||||
|RoHS compliance|||||




Subject to change without notice. 


For more information visit smartoptics.com. 

DATASHEET 

5.5 

## APPLICATION CODE LIST 

||**CMIS Application Code**|**Host format**|**Electrical interface**|**Payload**|**FEC**|**MSA**||
|---|---|---|---|---|---|---|---|
||1|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|RS-FEC|400GBASE-DR4 DR4 (Clause 124)||
||2|4 x 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|RS-FEC|100GBASE-DR (Clause 140)||
||ORDERING INFORMATION|||||||
||**Ordering number**|**Description**||||||
||SO-QSFP-DD-4C-DR4-M|QSFP-DD|400G-DR4 Ethernet, 4x100G-DR PAM4 CMIS3.0, 4x 1311nm 500m 3dB MPO12/APC|||||
||SO-QSFP-DD-4C-DR4-4-M|<br>QSFP-DD|400G-DR4 Ethernet, 4x100G-DR PAM4 CMIS4.0, 4x 1311nm 500m 3dB MPO12/APC|||||



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

