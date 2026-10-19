DATASHEET 

6.0 

## **OSFP RHS 400G DR4, CMIS5.0** 

OSFP112 RHS, 400G-DR4 Ethernet, 4x100G-DR, PAM4 CMIS5.0, 4x 1311nm 500m 3dB MPO12 

## TOS001-S31C-SO 

The TOS001-S31-SO is a OSFP112 Riding Heatsink (RHS) form-factor transceiver for 400Gbps Ethernet and 400G NDR InfiniBand applications. It is intended for use in data center interconnect between switches, routers, storage equipment etc. for optical distances up to 500m over a SingleMode (SM) ribbon fiber cable. 

The electrical interface consists of eight 106.25G signals (400GAUI-4) that are converted to eight PAM4-modulated channels/lanes to transport the optical signal. The transceiver can also be set in 4x100GAUI-1 mode to enable 400G to 4x 100G break-out configurations. Digital diagnostics functions are available via an I[2] C interface, as specified by the OSFP MSA. 

The optical interface to the transceiver is an MPO12 Angled Polished Connector (APC). 

Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 2.4 x 10[-4] . FEC on the module is Bypassed. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey, OSFP RHS||**Transmitter data:**||
|Transmission media|SM (1x MPO12)||Output power, Average, per lane|Min: -2.9dBm|
|Typical reach|500m|||Max: +4.0dBm|
|Nominal wavelengths|4x 1311nm||Output power, OMA, per lane|Min: -0.8dBm|
|Interface standards|400GBASE-DR4|||Max: +4.2dBm|
|Electrical interfaces|400GAUI-4 or 4x100GAUI-1||Transmit wavelength|1304.5 – 1317.5nm|
|Bit rate support|425Gbps1)||**Receiver data:**||
||53.125Gbd2)||Output power, Average, per lane|Min: -5.9dBm|
|Protocol support|400GbE|||Max: +4.0dBm|
|Power budget|0 – 3.6dB||Minimum input power, OMA per lane|-4.4dBm3)|
|Power consumption|< 9W||Overload (max power), OMA, per lane|+4.2dBm3)|
|Operating temperature|0°C to +70°C||Wavelength range|1304.5 – 1317.5nm|
|Storage temperature|-40°C to +85°C||LOS Assert|Min -15dBm|
|1)Aggregated line rate 400GbE|||LOS De-assert|Max -10dBm|
|2)Line baud rate per lane|||LOS Hysteresis|Min 0.5dB|
||||DDM|Yes|
||||MSA compliance|OSFP RHS MSA|
|||||CMIS5.0|
|**Safety/regulatory compliance:**|||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||||
|RoHS compliance|||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.0 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|TOS001-S31C-SO|OSFP112 RHS 400G-DR4 SM 500m MPO|



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

