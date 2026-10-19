DATASHEET 

5.0 

## **SO-SFP28-32GFC-LR10-Cxx** 

SFP28, 32Gbps FC/25GbE/10GbE, CWDM, DDM, 9.4dB, 10km, 1270nm-1330nm (4ch) 

## OVERVIEW 

The SO-SFP28-32GFC-LR10-Cxx is a CWDM SFP28 transceiver for 32G Fiber Channel (FC) services, also supporting 25Gbps and 10Gbps Ethernet. The transceiver can also be used for transport of single lane 25G Ethernet and 10GbE services. The optical performance provides a bridgeable distance of up to 10 km for 32G FC. 

The transceiver has a Rate_Select function compliant with SFF-8472 Rev12.2 where a switch between 32G FC, 25GbE and 10GbE is done. The transceiver is available in 4 CWDM wavelength versions, spanning from 1270nm to 1330nm in accordance with the G.694.2 standard. 

As stipulated by the 32G FC and 25G Ethernet standards, Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The optical parameters below will provide a bit error ratio (BER) of 1 x 10[-6 ] for 32G FC. FEC will provide the required quality for secure service. 

This transceiver provides digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|CWDM SFP28||**Transmitter data:**||
|Transmission media|SM (2x LC)||Output power  32G FC|Min: -3.0dBm1)|
|Typical reach|10km|||Max: +2.0dBm1)|
|Nominal wavelength|1271 – 1331nm (4ch)||Transmit wavelength|1271 – 1331nm (ITU G.694.2)|
|Bit rate support|28.05Gbps / 25.78Gbps||**Receiver data:**||
||10.31Gbps / 9.95Gbps||Minimum input power 32G FC|<br>-12.4dBm1) 2)|
|Protocol support|32G FC / 25GE||Overload (max power)|+2.0dBm1) 2)|
||10GbE-WAN / 10GbE-LAN||Wavelength range|1260nm – 1350nm|
|Power budget|0 – 9.4dB for 32G FC||LOS Assert|Min -30dBm|
|Dispersion penalty|Max 4.5dB||LOS De-assert|Max -17dBm|
|Power consumption|< 1.2W||LOS Hysteresis|Min 0.5dB|
|Operating temperature|-0°C to +70°C||DDM|Yes|
|Storage temperature|-40°C to +85°C||MSA compliance|SFF-8402, -8472|
||||1)Average power.||
||||2)@ BER 1x10-6, PRBS 231-1,|back-to-back.|
|**Safety/regulatory compliance:**|||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||||
|RoHS compliance|||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.0 

## RATE_SELECT OPERATION 

The SO-SFP28-32GFC-LR10-Cxx supports high data rates 25.78Gbps/28.05Gbps (25GbE /32GFC) and Low data rates 9.95Gbps/10.31Gbps(10GbE-LW/LR). Rate_Select is compliant with SFF-8472 Rev12.2. 

|**Logic OR of RS0 pin**<br>**and bit 110.3 of A2H**|**Logic OR of RS1 pin**<br>**and bit 118.3 of A2H**|**RX Data Rate**|**TX Data Rate**|
|---|---|---|---|
|High|High|25.78 / 28.05Gbps (25GE/32G FC)|25.78 / 28.05Gbps (25GE/32G FC)|
|Low|Low|9.95 / 10.31Gbps (10GbE-LW/-LR)|9.95 / 10.31Gbps (10GbE-LW/-LR)|



## ORDERING INFORMATION 

|**Ordering code**|**Description**|
|---|---|
|SO-SFP28-32GFC-LR10-C27|SFP28, 32G FC, 25G/10G Ethernet, CWDM, 10km, 9.4dB, LC, 1270nm|
|SO-SFP28-32GFC-LR10-C29|SFP28, 32G FC, 25G/10G Ethernet, CWDM, 10km, 9.4dB, LC, 12790nm|
|SO-SFP28-32GFC-LR10-C31|SFP28, 32G FC, 25G/10G Ethernet, CWDM, 10km, 9.4dB, LC, 1310nm|
|SO-SFP28-32GFC-LR10-C33|SFP28, 32G FC, 25G/10G Ethernet, CWDM, 10km, 9.4dB, LC, 1330nm|



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

