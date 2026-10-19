DATASHEET 

5.4 

## **SO-QSFP28-LR4** QSFP28, 100GBASE-LR4, OTU4, 1310nm, SM, DDM, 7.3dB, 10km 

## OVERVIEW 

The SO-QSFP28-LR4 is a QSFP28 form-factor transceiver for 100 Gbps Ethernet (100GBASE-LR4) and OTN (OTU4) applications. It is intended for use in inter- and intra-connect applications within and between data centers between switches, routers, storage equipment etc. The optical performance is in accordance with the 100GBASE-LR4 standard, i.e. for optical distances up to 10km over a SingleMode (SM) fiber. The lasers are of EML type. 

SO-QSFP28-LR4 uses four LANWDM channels/lanes @ 25.78Gbps and 27.95Gbps to transport an Ethernet and OTN signal, respectively. Digital diagnostics functions are available via an I[2] C interface, as specified by the QSFP28 MSA. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey QSFP28||**Transmitter data:**||
|Transmission media|SM (2x LC)||Output power, total|Max +10.5dBm3)(100GbE)|
|Typical reach|10km|||Max +8.9dBm3)(OTU4)|
|Nominal wavelength|Lane 1: 1295.56nm||Output power, per lane 100GbE|Min: -1.7dBm3)|
||Lane 2: 1300.05nm|||Max: +4.5dBm3)|
||Lane 3: 1304.58nm||Output power, per lane 100GbE, OMA|Min: -1.3dBm3)|
||Lane 4: 1309.14nm|||Max: +4.5dBm3)|
|Interface standards|100GBASE-LR4||Output power, per lane OTU4|Min: -2.5dBm3)|
||OTU4 4I1-9D1F|||Max: +2.9dBm3)|
|Bit rate support|103.12 / 111.81 Gbps1)||Transmit wavelength|1294.53 – 1296.59nm|
||25.78 / 27.95 Gbps2)|||1299.02 – 1301.09nm|
|Protocol support|100GbE|||1303.54 – 1305.63nm|
||OTU4|||1308.09 – 1310.19nm|
|Power budget|0 – 7.3dB (100GbE) / 0 - 6.3dB (OTU4)||**Receiver data:**||
|Optical path penalty|2.2dB (100GbE)||Minimum input power, per lane|-8.0dBm3)(100GbE)|
||1.5dB (OTU4)|||-8.8dBm3) 5)(OTU4)|
|Power consumption|< 3.5W||Minimum input power, per lane (OMA)|-8.6dBm4)|
|Operating temperature|0°C to +70°C||Overload (max power), per lane|+4.5dBm3) 4)(100GbE)|
|Storage temperature|-40°C to +85°C|||+2.9dBm3) 5)(OTU4)|
|1)Aggregated line rate 100GbE / OTU4|||Wavelength range|1294.53 – 1296.59nm|
|2)Per lane||||1299.02 – 1301.09nm|
|3)Average power||||1303.54 – 1305.63nm|
|4)Specified at BER 1x10-12||||1308.09 – 1310.19nm|
|5)Specified at pre-FEC BER|1x10-6||LOS Assert|Min -25dBm|
||||LOS De-assert|Max -12dBm|
|**Safety/regulatory compliance:**|||LOS Hysteresis|Min 0.5dB|
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||DDM|Yes|
|RoHS compliance|||MSA compliance|QSFP28 MSA, SFF-8636|





Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.4 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-QSFP28-LR4|QSFP28, 100GBASE-LR4, OTU4, 1310nm, SM, DDM, 7.3dB, 10km|



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
|Optical modulation Amplitude,<br>OMA|Optical Modulation Amplitude is a parameter that, in certain standards, specifies the output power and receiver sensitivity. To<br>measure the OMA, a oscilloscope with a baud rate corresponding to the transceiver is required. Thus, this parameter cannot be<br>measured using an ordinary optical power meter.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

