DATASHEET 

5.0 

**SO-SFP-MR25-BX40D-35 & -53 / -35-I & -53-I** SFP BiDi, 100Mbps-2.7Gbps, 1310/1550nm, SM, DDM, 19dB/13dB, 40km 

## OVERVIEW 

The SO-SFP-MR25-BX40D is a bi-directional transceiver solution operating directly on a single-fiber without the need for a separate optical filter. This is achieved by having two transceivers that inject different wavelengths into the same single-fiber. The solution thus consists of two transceivers; SO-SFP-MR25-BX40D-35 and SO-SFP-MR25-BX40D-35, operating at 1310nm and 1550nm respectively. Using a single-fiber solution provides a cost-efficient solution for interconnect and it simplifies the patching since no separate transmit/receive direction has to be taken into account. 

The transceiver pair supports the bit rate range from 100Mbps to 2.7Gbps covering a wide range of Ethernet, SAN, SDH/SONET and OTN services. The optical performance of the transceiver pair provides a bridgeable distance of up to 10km. 

The transceiver solution is available in two temperature range options, one being the Industrial temperature range (I-temp) of -40°C to +85°C (-40°F to +185°F). The transceivers provide digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**||**Value**|
|---|---|---|---|---|---|
|Technology|BiDi SFP||**Transmitter data:**|||
|Transmission media|SM (1x LC)||Output power|-BX40D-35|Min: +1dBm3)|
|Typical reach|40km||||Max: +5dBm3)|
|Nominal wavelength Tx/Rx|1310nm/1550nm & 1550nm/1310nm|||-BX40D-53|Min: -5dBm3)|
|Bit rate support|100Mbps – 2.670Gbps||||Max: 0dBm3)|
|Protocol support|FE, GbE||Transmit wavelength|-BX40D-35|1260 – 1360nm1)|
||STM1/OC3, STM4/OC12, STM16/OC48|||-BX40D-53|1530 – 1570nm2)|
||OTU1||**Receiver data:**|||
||1G FC, 2G FC||Minimum input power STM1/OC3||-18.0dBm3) 4)|
||CPRI Opt 1, 2, 3||Overload (max power)||-3.0dBm3) 4)|
||OBSAI 1x, 2x||Wavelength range|-BX40D-35|1530 – 1570nm1)|
|Power budget|8 – 19dB in 1310nm direction|||-BX40D-53|1260 – 1360nm2)|
||3 – 13dB in 1550nm direction||LOS Assert||Min -35dBm|
|Dispersion penalty|Max 1dB||LOS De-assert||Max -19dBm|
|Power consumption|< 1.0W||LOS Hysteresis||Min 0.5dB|
|Operating temperature|0°C to +70°C (-BxxC-)||DDM||Yes|
||-40°C to +85°C (-BxxI-)||MSA compliance||SFF-8431, -8432, -8472|
|Storage temperature|-40°C to +85°C|||||
||||1)SO-SFP-MR25-BX40D-35.|||
||||2)SO-SFP-MR25-BX40D-53.|||
||||3)Average power.|||
||||4)BER1x10-12, back-to-back.|||
|**Safety/regulatory compliance:**||||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)||||||
|RoHS compliance||||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.0 

## POWER BUDGET INFORMATION 


Note that the power budget differs in 1310nm vs 1550nm direction. This has to be taken into account for links with high attenuation. Note also that the fiber attenuation is ~0.4dB/km in the 1310nm region and ~0.25dB/km in the 1550nm region. 

## ORDERING INFORMATION 

|**Ordering code**|**Description**|
|---|---|
|SO-SFP-MR25-BX40D-35|SFP, BiDi, Multirate 100Mbps-2.7Gbps, TX/RX=1310/1550nm, SM, 40km, 19dB/13dB, LC|
|SO-SFP-MR25-BX40D-53|SFP, BiDi, Multirate 100Mbps-2.7Gbps, TX/RX=1550/1310nm, SM, 40km, 13dB/19dB, LC|
|SO-SFP-MR25-BX40D-35-I|SFP, BiDi, Multirate 100Mbps-2.7Gbps, TX/RX=1310/1550nm, SM, 40km, 19dB/13dB, I-temp, LC|
|SO-SFP-MR25-BX40D-53-I|SFP, BiDi, Multirate 100Mbps-2.7Gbps, TX/RX=1550/1310nm, SM, 40km, 13dB/19dB, I-temp, LC|



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


Subject to change without notice. 

For more information visit smartoptics.com. 

