DATASHEET 

5.8 

## **SO-QSFP28-ZR4** 

## QSFP28, 100G Ethernet ZR4, SM 1296/1300/1305/1309nm, 80km, 31dB, LC 

## OVERVIEW 

The SO-QSFP28-ZR4 is a QSFP28 form-factor transceiver for 100 Gbps Ethernet applications. It is intended for use in interconnect applications between data centers between switches, routers, storage equipment etc. 

SO-QSFP28-ZR4 has an optical performance enabling distances of up to 80km over a SingleMode (SM) G.652 fiber-pair cable. Forward Error Correction (FEC) is required to be implemented by the host in order to ensure reliable system operation. The FEC type shall be as defined in IEEE802.3bj, i.e. Reed Solomon RS(528,514). The optical parameters will provide a bit error ratio (BER) of 5 x 10[-5] . FEC will render in the required BER of better than 1 x 10[-12] . 

SO-QSFP28-ZR4 uses four LANWDM channels/lanes @ 25.78 Gbps to transport the Ethernet signal. Digital diagnostics functions (DDM) are available via an I2C interface, as specified by the QSFP28 MSA. 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey QSFP28||**Transmitter data:**||
|Transmission media|SM (2x LC)||Output power, total|Max: +13.0dBm|
|Typical reach|80km||Diff in power betw lanes|Max: 3.6dB|
|Nominal wavelengths|1295.56nm||Output power, per lane|Min: +2.0dBm3)|
||1300.05nm|||Max: +7.0dBm3)|
||1304.58nm||Transmit wavelengths|1294.53 - 1296.59nm|
||1309.14nm|||1299.02 - 1301.09nm|
|Interface standards|100GBASE-ZR4|||1303.54 - 1305.63nm|
|Bit rate support|103.12Gbps1)|||1308.09 - 1310.19nm|
||25.78Gbps2)||**Receiver data:**||
|Protocol support|100GbE||Minimum input power, per lane|-29.0dBm3) 4)|
|Power budget|12.0 – 31.0dB||Overload (max power), per lane|-5.0dBm3) 4)|
|Dispersion penalty|1.0dB||Wavelength range|1294.53 - 1296.59nm|
|Power consumption|Max < 5.0W5)|||1299.02 - 1301.09nm|
|Operating temperature|0°C to +70°C|||1303.54 - 1305.63nm|
|Storage temperature|-40°C to +85°C|||1308.09 - 1310.19nm|
||||LOS Assert|Min -40dBm|
|1)Aggregated line rate 100GbE|||LOS De-assert|Max -31.5dBm|
|2)Line rate per 25.78Gbps lane|||LOS Hysteresis|Min 0.5dB|
|3)Average power|||DDM|Yes|
|4)Per 25.78Gbps lane. Measured with PRBS31 (231-1) @ BER 5E-5|||MSA compliance|QSFP28 MSA, SFF-8636|
|5)Max is worst case at high temp limit|||||
|**Safety/regulatory compliance:**|||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||||
|RoHS compliance|||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.8 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-QSFP28-ZR4|QSFP28, 100G Ethernet ZR4, SM 1296/1300/1305/1309nm, 80km, 31dB, LC|



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
||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

