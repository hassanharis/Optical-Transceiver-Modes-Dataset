DATASHEET 

5.0 

## **SO-QSFP56-2C-2** 

QSFP56 200G-FR4 Ethernet, 1271nm/1311nm/1311nm/1331nm, 2km, 4.8dB, LC 

## OVERVIEW 

The SO-QSFP56-2C-2 is a QSFP56 form-factor transceiver for 200Gbps Ethernet applications. It is intended for use in data center interconnect between switches, routers, storage equipment etc. for optical distances up to 2km over a SingleMode (SM) fiber cable. 

The module has 4 independent electrical input/output channels operating at 26.5625GBd per channel. This transceiver uses four PAM4 modulated lanes operating at the ITU G.694.2 CWDM grid. The transceiver requires that the host system uses Forward Error Correction (FEC). 

The electrical interface is compliant with the 200GAUI-4 interface as defined by IEEE 802.3bs. 

Digital diagnostics functions are available via an I[2] C interface, as specified by the QSFP56 MSA using CMIS4.0. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**||
|---|---|---|---|---|---|
|Technology|Grey QSFP56||**Transmitter data:**|||
|Transmission media|SM (2x LC)||Total output power|Max: +10.7dBm||
|Typical reach|2km||Output power, per lane|Min: 0dBm||
|Nominal wavelengths|1271nm|||Max: +4.7dBm||
||1291nm||Transmit wavelengths|1264.5 – 1277.5nm||
||1311nm|||1284.5 – 1297.5nm||
||1331nm|||1304.5 – 1317.5nm||
|Interface standards|IEEE 200GBASE-FR4|||1324.5 - 1317.5nm||
|Bit rate support|212.5Gbps1)||**Receiver data:**|||
||26.5625Gbd (PAM4)2)||Minimum input power per lane|-4.8dBm3)||
|Protocol support|200GbE||Overload (max power) per lane|+4.7dBm3)||
|Power budget|0 –4.8dB||Wavelength range|1264.5 – 1277.5nm||
|Power consumption|< 5.5W (typical <4.5W)|||1284.5 – 1297.5nm||
|Operating temperature|0°C to +70°C|||1304.5 – 1317.5nm||
|Storage temperature|-40°C to +85°C|||1324.5 - 1317.5nm||
||||LOS Assert|Min 17dBm||
||||LOS De-Assert|Max -12dBm||
|1)Aggregated line rate 200GbE|||LOS Hysteresis|Min 0.5dBm||
|2)Line rate per lane|||DDM|Yes||
|3)Specified at BER 2x10-4|||MSA compliance|QSFP56 MSA, SFF8636||
|**Safety/regulatory compliance:**||||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)||||||
|RoHS compliance||||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.0 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-QSFP56-2C-2|QSFP56 200G-FR4 Ethernet, 1271nm/1311nm/1311nm/1331nm, 2km, 4.8dB, CMIS4.0, LC|



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

