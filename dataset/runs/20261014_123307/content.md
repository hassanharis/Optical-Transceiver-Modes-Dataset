DATASHEET 

5.1 

## **SO-SFP-1000BASE-BX-MMD-35 & -53** 

SFP BiDi, 1.063/1.25Gbps, 1310/1550nm, MM, DDM, 11dB, 1km, C-temp & I-temp 

## OVERVIEW 

The SO-SFP-1000BASE-BX-MMD is a bi-directional transceiver solution operating directly on a single-fiber without the need for a separate optical filter. This is achieved by having two transceivers that inject different wavelengths into the same single-fiber. The solution thus consists of two transceivers; SO-SFP-1000BASE-BX-MMD-35 and SO-SFP-1000BASE-BX-MMD-53, operating at 1310nm and 1550nm respectively on a MultiMode (MM) fiber. Using a single-fiber solution provides a cost-efficient solution for interconnect and it simplifies the patching since no separate transmit/receive direction has to be taken into account. 

The transceiver pair supports 1Gbps Fiberchannel (1G FC), 1Gbps Ethernet (GbE) and the mobile fronthaul CPRI option 1 services. The optical performance of the transceiver pair provides a bridgeable distance of up to 1000m. 

The transceiver solution is available in two temperature range options, one being the Industrial temperature range (I-temp) of -40°C to +85°C (-40°F to +185°F). The transceivers provide digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

## TECHNICAL DATA 

|**Parameter**|**Value**|
|---|---|
|Technology|BiDi SFP|
|Transmission media|MM (1x LC)|
|Typical reach|500m@62.5/125um (500MHz*km`）`|
||1000m@50/125um (800MHz*km)|
|Nominal wavelengths|1310nm1)/ 1550nm2)|
|Bit rate range<br>Protocol support|1.0625 / 1.25Gbps|
||GbE|
||1G FC|
||CPRI Opt 2 (1.2288 Gbps)|
|Power budget|0 – 11.5 dB4)/ 0 – 12.5 dB5)|
|Power consumption|< 1 W|
|Operating temperature|0°C to +70°C|
||-40°C to +85°C (-I)|
|Storage temperature|-40°C to +85°C|



|**Parameter**|**Value**|
|---|---|
|**Transmitter data:**||
|Output power|Min: -9.5dBm3)|
||Max: -3.0dBm3)|
|Transmit wavelength|1260 - 1360nm1)|
||1500 - 1580nm2)|
|**Receiver data:**||
|Minimum input power|-21dBm3) 4)|
||-22dBm3) 5)|
|Overload (max power)|-3dBm3)|
|Wavelength range|1500 – 1580nm1)|
||1260 - 1360nm2)|
|LOS Assert|Min -35dBm|
|LOS De-assert|Max -23dBm|
|LOS Hysteresis|Min 0.5dB|
|DDM|Yes|
|MSA compliance|SFP MSA, SFF 8472|



- 1) SO-SFP-1000BASE-BX-MMD-35 

- 2) SO-SFP-1000BASE-BX-MMD-53 

- 3) Average power 

4) @ GbE, PRBS 27-1, BER <1E-12 5) @ FE, PRBS 27-1, BER <1E-12 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.1 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-SFP-1000Base-BX-MMD-35|SFP, BiDi, 1G Ethernet, 1G FC, TX/RX=1310/1550nm, MM, 1km, 11dB, LC|
|SO-SFP-1000Base-BX-MMD-53|SFP, BiDi, 1G Ethernet, 1G FC, TX/RX=1550/1310nm, MM, 1km, 11dB, LC|
|SO-SFP-1000Base-BX-MMD-35-I|SFP, BiDi, 1G Ethernet, 1G FC, TX/RX=1310/1550nm, MM, 1km, 11dB, I-temp, LC|
|SO-SFP-1000Base-BX-MMD-53-I|SFP, BiDi, 1G Ethernet, 1G FC, TX/RX=1550/1310nm, MM, 1km, 11dB, I-temp, LC|



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

