DATASHEET 

5.2 

## **SO-QSFP28-LR4-20D** 

## QSFP28, 100G Ethernet 4WDM-20, OTU4, SM,1296/1300/1305/1309nm, 20km,10.2dB, LC 

## OVERVIEW 

The SO-QSFP28-LR4-20D is a QSFP28 form-factor transceiver for 100G Ethernet and OTU4 applications. It is intended for use in inter- and intra-connect applications within and between data centers between switches, routers, storage equipment etc. The optical performance supports optical distances up to 20km over a SingleMode (SM) fiber according to the 100G 4WDM-20 MSA. 

For Ethernet services, Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 5 x 10[-5] . FEC will render in the required BER of better than 1 x 10[-12] . 

SO-QSFP28-LR4-20D uses four optical channels/lanes @ 25.78Gbps to transport the Ethernet signal and 27.95Gbps for the OTU4 signal. Digital diagnostics functions are available via an I2C interface, as specified by the QSFP28 MSA. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**||
|---|---|---|---|---|---|
|Technology|Grey QSFP28||**Transmitter data:**|||
|Transmission media|SM (2x LC)||Output power, total|Max +10.5dBm3)(100GbE)||
|Typical reach|20km|||Max +10.5dBm3)(OTU4)||
|Nominal wavelength|Lane 1: 1295.56nm||Output power, per lane 100GbE|Min: -1.7dBm3)||
||Lane 2: 1300.05nm|||Max: +4.5dBm3)||
||Lane 3: 1304.58nm||Output power, per lane OTU4|Min: -2.5dBm3)||
||Lane 4: 1309.14nm|||Max: +4.5dBm3)||
|Interface standards|100G 4WDM-20 MSA||Transmit wavelength|1294.53 – 1296.59nm||
||OTU4 4I1-9D1F|||1299.02 – 1301.09nm||
|Bit rate support|103.12 / 111.81 Gbps1)|||1303.54 – 1305.63nm||
||25.78 / 27.95 Gbps2)|||1308.09 – 1310.19nm||
|Protocol support|100GbE||**Receiver data:**|||
||OTU4||Minimum input power, per lane|-11.9dBm3) 4)(100GbE)||
|Power budget|0 – 10.2dB (100GbE)|||-10.3dBm3) 5)(OTU4)||
||0 – 7.8dB (OTU4)||Overload (max power), per lane|+4.5dBm3) 4)(100GbE)||
|Optical path penalty|2.8dB (100GbE) / 1.5dB (OTU4)|||+4.5dBm3) 5)(OTU4)||
|Power consumption|< 4.5W||Wavelength range|1294.53 – 1296.59nm||
|Operating temperature|0°C to +70°C|||1299.02 – 1301.09nm||
|Storage temperature|-40°C to +85°C|||1303.54 – 1305.63nm||
|1)Aggregated line rate 100GbE / OTU4||||1308.09 – 1310.19nm||
|2)Per lane|3)Average power||LOS Assert|Min -25dBm||
|4)Specified at BER 5x10-5|||LOS De-assert|Max -13dBm||
|5)Specified at pre-FEC BER|1x10-6||LOS Hysteresis|Min 0.5dB||
||||DDM|Yes||
|**Safety/regulatory compliance:**|||MSA compliance|QSFP28 MSA, SFF-8636||
|TUV/UL/FDA (contact Smartoptics for latest certification information)||||||
|RoHS compliance||||||




Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

5.2 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-QSFP28-LR4-20D|QSFP28, 100G 4WDM-20, OTU4 4I1 9D1F, SM, 1296/1300/1305/1309nm, 20km, 10.2dB, LC|



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

