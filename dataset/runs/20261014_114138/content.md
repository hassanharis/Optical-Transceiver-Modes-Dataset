DATASHEET 

5.6 

## **SO-QSFP-DD-4C-FR4-4** 

QSFP-DD 400G-FR4 Ethernet, PAM4 CMIS4.0, 1271nm/1291nm/1311nm/1331nm 2km 4dB LC 

## OVERVIEW 

The SO-QSFP-DD-4C-FR4 is a QSFP-DD form-factor transceiver for 400Gbps Ethernet applications. It is intended for use in data center interconnect between switches, routers, storage equipment etc. for optical distances up to 2km over a SingleMode (SM) fiber cable. 

The electrical interface consists of eight 53.125G signals (400GAUI-8) that are converted to eight PAM4-modulated channels/lanes to transport the Ethernet signal. The transceiver can also be set in 4x100GAUI-2 mode (application code 2) to enable 400G to 4x 100G break-out configurations. Digital diagnostics functions are available via an I[2] C interface, as specified by the QSFP-DD MSA. 

Forward Error Correction (FEC) is required to be implemented by the host to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 2.4 x 10[-4] . 

The optical interface to the transceiver is 2x LC connectors. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**||
|---|---|---|---|---|---|
|Technology|Grey QSFP-DD||**Transmitter data:**|||
|Transmission media|SM (2x LC)||Output power, per lane|Min: -3.3dBm3)||
|Typical reach|2km|||Max: +3.5dBm3)||
|Nominal wavelengths|1271nm||Transmit wavelengths|1264.5 - 1277.5nm||
||1291nm|||1284.5 - 1297.5nm||
||1311nm|||1304.5 - 1317.5nm||
||1331nm|||1324.5 - 1337.5nm||
|Interface standards|400GBASE-FR4||**Receiver data:**|||
|Electrical interfaces|400GAUI-8 or 4x100GAUI-2||Minimum input power, per lane|-7.3dBm3) 4)||
|Bit rate support|425Gbps1)||Overload (max power), per lane|+3.5dBm3) 4)||
||53.125Gbd2)||Wavelength range|1264.5 - 1277.5nm||
|Protocol support|400GbE|||1284.5 - 1297.5nm||
|Power budget|0 – 4.0dB|||1304.5 - 1317.5nm||
|Power consumption|< 10W|||1324.5 - 1337.5nm||
|Operating temperature|0°C to +70°C||LOS Assert|Min -15dBm||
|Storage temperature|-40°C to +85°C||LOS De-assert|Max -9.5dBm||
|1)Aggregated line rate 400GbE|||LOS Hysteresis|Min 0.5dB||
|2)Line baud rate per lane|||DDM|Yes||
|3)Average power, per lane|||MSA compliance|QSFP-DD MSA / CMIS4.0||
|4)Specified at BER 2.4x10-4||||||
|**Safety/regulatory compliance:**||||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)||||||
|RoHS compliance||||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.6 

## APPLICATION CODE LIST 

|**CMIS Application Code**|**Host format**|**Electrical interface**|**Payload**|**FEC**|**MSA**||
|---|---|---|---|---|---|---|
|1|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|RS-FEC|400GBASE-FR4 (Clause 151)||
|2|4 x 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|RS-FEC|100GBASE-FR1 (Clause 140)||



## ORDERING INFORMATION 

|**Ordering number**|**Description**||
|---|---|---|
|SO-QSFP-DD-4C-FR4-4|QSFP-DD 400G-FR4 Ethernet, 4×100G-FR, PAM4 CMIS4.0, 1271nm/1291nm/1311nm/1331nm 2km 4dB LC||



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

