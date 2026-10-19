DATASHEET 

5.1 

## **SO-SFP-155M-O-Cxx-E** SFP, OSC/OTDR, 155Mbps, CWDM, SM, 100km, LC, E-temp 

## OVERVIEW 

The SO-SFP-155M-O-Cxx-E is an SFP form-factor transceiver for OSC (Optical Supervisory Channel) and OTDR (Optical Time Domain Reflectometer) applications. The transceiver operates as a OSC transceiver at 100Mbps Ethernet and STM1/OC3 rates up to 100km distances. Upon disruption of the data link, or failure to connect, the transmitter section of the SFP switches into OTDR mode. 

The SFPs measures the optical fiber link optical return loss during the OTDR start-up “handshaking” routine of the SFPs, before the data link is made. The receiver also measures the signal received. 

The SO-SFP-155M-O-Cxx-E is provided in three different wavelength versions according to the CWDM wavelength grid plus one at 1625nm. The transceiver is intended to be used together with the Smartoptics Open Line System products. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**||**Value**|
|---|---|---|---|---|---|
|Technology|CWDM SFP||**Transmitter data:**|||
|Transmission media|SM (2x LC)||Output power||Min: -2dBm1)|
|Typical reach|100km||||Max: +1dBm1)|
|Nominal wavelengths|1491nm3)||Transmit wavelengths||1484.5 – 1497.5nm3)|
||1511nm4)||||1504.5 – 1517.5nm4)|
||1611nm5)||||1604.5 – 1617.5nm5)|
||1625nm6)||||1618.5 – 1631.5nm6)|
|Bit rate support|125Mbps / 155Mbps||**Receiver data:**|||
|Protocol support|100M Ethernet / STM1/OC3||Minimum input power||-36dBm1) 2)|
|Power budget|0 – 34dB7)||Overload (max power)||+1dBm1) 2)|
|Power consumption|< 0.9W||Wavelength range||1260 – 1635nm|
|Operating temperature|-20°C to +70°C||DDM||Yes|
|Storage temperature|-40°C to +85°C||LOS Assert||Typ: -25dBm7)|
||||LOS De-Assert||Typ: -24dBm7)|
|**OTDR data:**|||LOS Hysteresis||Min: 1dB|
|Dynamic range|Typ: 65dB||MSA compliance||SFP MSA|
|Dead zone|Max 30m|||||
|Resolution|Max 10m||1)Average power|||
|Accuracy|Max 50m||2)at 125Mbps PRBS7 and BER|1x10-12||
|3)SO-SFP-155M-O-C49-E|5)SO-SFP-155M-O-C61-E||7)The transceiver DDM reports Rx power reliably down to -25dBm.<br>Beyond -25dBm the transceiver will report unreliably and assert|||
|4)SO-SFP-155M-O-C51-E|6)SO-SFP-155M-O-C62-E||Rx_LOS. Even if the Rx_LOS is asserted, the Rx sensitivity is still valid<br>down to -36dBm.|||
|**Safety/regulatory compliance:**||||||
|TUV/UL/FDA (contact Smartoptics for latest certification information).||||||
|RoHS compliance||||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.1 

## **Pull tab colors:** 

1491nm: Blue 1511nm: White 1611nm: Brown 1625nm: Magenta 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-SFP-155M-O-C49-E|SFP FE/155M 34dB, OTDR 65dB, E-temp, LC, 1490nm|
|SO-SFP-155M-O-C51-E|SFP FE/155M 34dB, OTDR 65dB, E-temp, LC, 1510nm|
|SO-SFP-155M-O-C61-E|SFP FE/155M 34dB, OTDR 65dB, E-temp, LC, 1610nm|
|SO-SFP-155M-O-C62-E|SFP FE/155M 34dB, OTDR 65dB, E-temp, LC, 1625nm|



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

