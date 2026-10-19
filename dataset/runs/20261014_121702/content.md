DATASHEET 

5.0 

## **SO-QSFP28-ER4-OTU4** 

QSFP28, 100G Ethernet ER4, OTU4, SM  1296/1300/1305/1309nm, 40km, 18dB, LC 

## OVERVIEW 

The SO-QSFP28-ER4 is a QSFP28 form-factor transceiver for 100Gbps Ethernet and OTN (OT4) applications. It is intended for use in inter- and intra-connect applications within and between data centers between switches, routers, storage equipment etc. The optical performance is in accordance with the 100G 4WDM-40 MSA standard, i.e. for optical distances up to 40km over a SingleMode (SM) fiber. 

SO-QSFP28-ER4 uses four LANWDM channels/lanes @ 25.78Gbps and 27.95Gbps to transport an Ethernet and OTN signal respectively. 

Forward Error Correction (FEC) is required in the host equipment in order to ensure reliable system operation at the specified distance. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The below optical parameters will provide a bit error ratio (BER) of 5 x 10[-5] . FEC will render in the required BER of better than 1 x 10[-12] . 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**||
|---|---|---|---|---|---|
|Technology|Grey QSFP28||**Transmitter data:**|||
|Transmission media|SM (2x LC)||Output power, total|Max +12.5dBm3)(100GbE)||
|Typical reach|40km|||Max +11.1dBm3)(OTU4)||
|Nominal wavelength|Lane 1: 1295.56nm||Output power, per lane 100GbE|Min: -0.3dBm3)||
||Lane 2: 1300.05nm|||Max: +6.5dBm3)||
||Lane 3: 1304.58nm||Output power, per lane OTU4|Min: 0.6dBm3)||
||Lane 4: 1309.14nm|||Max: +5.1dBm3)||
|Interface standards|100G 4WDM-40||Transmit wavelength|1294.53 – 1296.59nm||
|Bit rate support|103.12 / 111.81 Gbps1)|||1299.02 – 1301.09nm||
||25.78 / 27.95 Gbps2)|||1303.54 – 1305.63nm||
|Protocol support|100GbE, OTU4|||1308.09 – 1310.19nm||
|Power budget|10 – 18dB (100GbE)||**Receiver data:**|||
||10 – 19.5dB (100GbE)||Minimum input power, per lane|-18.3dBm3) 4)(100GbE)||
|Optical path penalty|3dB (100GbE), 1.5dB (OTU4)|||-18.9dBm3) 5)(OTU4)||
|Power consumption|< 5W||Overload (max power), per lane|-3.5dBm3) 4)(100GbE)||
|Operating temperature|0°C to +70°C|||-4.9dBm3) 5)(OTU4)||
|Storage temperature|-40°C to +85°C||Wavelength range|1294.53 – 1296.59nm||
|1)Aggregated line rate 100GbE / OTU4||||1299.02 – 1301.09nm||
|2)Per lane||||1303.54 – 1305.63nm||
|3)Average power||||1308.09 – 1310.19nm||
|4)Specified at pre-FEC BER|5x10-5||LOS Assert, min|-32dBm||
|5)Specified at pre-FEC BER|1x10-6||LOS De-assert, max|-22dBm||
||||LOS Hysteresis|0.5||
|**Safety/regulatory compliance:**|||DDM|Yes||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||MSA compliance|QSFP28 MSA, SFF-8636,||
|RoHS compliance||||100G 4WDM-40||




Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

5.0 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-QSFP28-ER4-OTU4|QSFP28 100GE ER4 OTU4 1310nm SM 40km|



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

