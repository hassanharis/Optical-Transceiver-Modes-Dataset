DATASHEET 

5.3 

## **SO-QSFP28-100G-LRx** 

QSFP28, 100G Ethernet LR, SM, CWDM, PAM4, 10km, 6.3dB, LC 

## OVERVIEW 

The SO-QSFP28-100G-LRx is a QSFP28 form-factor transceiver for 100 Gbps Ethernet applications. It is intended for use in intraand interconnect applications within and between data centers between switches, routers, storage equipment etc. 

SO-QSFP28-100G-LRx is a single-lambda 100G transceiver provided in four different CWDM wavelength versions that match the wavelengths of the 400G Transceiver SO-QSFP-DD-4C-LR4 to support a 400G to 4x 100G break-out configuration. 

SO-QSFP28-100G-LRx has an optical performance enabling distances of up to 10km over a SingleMode (SM) G.652 fiber-pair cable. The module includes FEC coding Forward Error Correction (KP4 FEC) to ensure reliable system operation. The host system shall thus not have FEC activated. The optical parameters will provide a bit error ratio (BER) of 2.4 x 10[-4] . FEC will render in the required BER of better than 1 x 10[-12] . 

SO-QSFP28-100G-LRx uses a single CWDM channel/lane @ 50Gbaud using PAM4 modulation to transport the Ethernet signal. The electrical interface is 4x 25.78Gbps and compliant with OIF CEI-28G-VSR.  Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey QSFP28||**Transmitter data:**||
|Transmission media|SM (2x LC)||Output power, per lane|Min: -1.4dBm3)|
|Typical reach|10km|||Max: +4.5dBm3)|
|Nominal wavelengths|1271nm (SO-QSFP28-100G-LRA)||Transmit wavelengths|1264.5 - 1277.5nm|
||1291nm (SO-QSFP28-100G-LRB)|||1284.5 - 1297.5nm|
||1311nm (SO-QSFP28-100G-LRC)|||1304.5 - 1317.5nm|
||1331nm (SO-QSFP28-100G-LRD)|||1324.5 - 1337.5nm|
|Interface standards|100GBASE-LR||**Receiver data:**||
|Bit rate support|103.12Gbps1)||Minimum input power|-7.7dBm3) 4)|
||53.125Gbd2)||Overload (max power)|+4.5dBm3) 4)|
|Protocol support|100GbE||Wavelength range|1260 - 1355nm|
|Power budget|0 – 6.3dB||LOS Assert|Min -15dBm|
|Power consumption|< 4.5W||LOS De-assert|Max -12dBm|
|Operating temperature|0°C to +70°C||LOS Hysteresis|Min 0.5dB|
|Storage temperature|-40°C to +85°C||DDM|Yes|
|1)Aggregated line rate 100GbE|||MSA compliance|QSFP28 MSA, SFF-8636|
|2)Line baud rate|||||
|3)Average power, per lane|||||
|4)Specified at BER 2.4x10-4|||||
|**Safety/regulatory compliance:**|||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||||
|RoHS compliance|||||




Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

5.3 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-QSFP28-100G-LRA|QSFP28, 100G Ethernet FR, SM, 1x 1271nm, PAM4, 10km, 6.3dB, LC|
|SO-QSFP28-100G-LRB|QSFP28, 100G Ethernet FR, SM, 1x 1291nm, PAM4, 10km, 6.3dB, LC|
|SO-QSFP28-100G-LRC|QSFP28, 100G Ethernet FR, SM, 1x 1311nm, PAM4, 10km, 6.3dB, LC|
|SO-QSFP28-100G-LRD|QSFP28, 100G Ethernet FR, SM, 1x 1331nm, PAM4, 10km, 6.3dB, LC|



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

