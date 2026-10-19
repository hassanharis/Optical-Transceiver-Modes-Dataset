DATASHEET 

5.2 

## **16G-ER-DxxS-BR2** 

SFP+, 16/8G/4G FC, Secure Optics DWDM 100GHz grid, 192.00 - 196.00THz (41ch), 40km, 14dB, LC, D200-D600 


## OVERVIEW 

The 16G-ER-DxxS-BR2 is a versatile DWDM transceiver in SFP+ form-factor supporting a wide range of Fiber Channel (FC) services (4G to 16G). The transceiver is provided in versions covering all C-band channels in the 100GHz DWDM grid as specified in the ITU-T G.694.1 standard. The transceiver is approved by Brocade and supports the authentication protocol required for the Gen7 system platforms. 

The optical performance provides a bridgeable distance of up to 40km (without dispersion compensation) for 16GFC. This transceiver provides digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

The transceiver module is compliant to RoHS-6/6. 

## TECHNICAL DATA 

|Parameter|Value||Parameter|Value||
|---|---|---|---|---|---|
|Technology|DWDM 100GHz SFP+||**Transmitter data:**|||
|Transmission media|SM (2x LC)||Output power|Min: 0dBm3)||
|Typical reach|40km|||Max: +4.0dBm3)||
|Nominal wavelengths|192.00 - 196.00THz||Transmit wavelengths|192.00 - 196.00THz||
|Bit rate support|14.025Gbps|||100GHz (ITU-T G.694.1)||
||8.500Gbps||**Receiver data:**|||
||4.250Gbps||Minimum input power|-14.0dBm2) 3)||
|Protocol support|16G FC||Overload (max power)|0dBm2) 3)||
||8G FC||Wavelength range|1260 - 1565nm||
||4G FC||LOS De-Assert|Max -16dBm||
|Power budget|4 – 14.0dB||LOS Assert|Min -26dBm||
|Dispersion tolerance|800ps/nm1)||DDM|Yes||
|Dispersion penalty|3.5dB||MSA compliance|SFF-8431||
|Power consumption|< 2.0W|||SFF-8432||
|Operating temperature|0°C to +70°C|||||
|Storage temperature|-40°C to +85°C|||||
|1)@ 14.025 Gbps (16G FC)||||||
|2)@ BER < 1E-6 using PRBS|231-1|||||
|3)Average power||||||
|Safety/regulatory compliance:||||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)||||||
|RoHS compliance||||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.2 

## ORDERING INFORMATION 

|Ordering number|Frequency THz|Wavelength nm|<br>Ordering number|Frequency THz|Wavelength nm|
|---|---|---|---|---|---|
|16G-ER-D20S--BR2|192.00|1561.42|16G-ER-D41S--BR2|194.10|1544.53|
|16G-ER-D21S--BR2|192.10|1560.61|16G-ER-D42S--BR2|194.20|1543.73|
|16G-ER-D22S--BR2|192.20|1559.79|16G-ER-D43S--BR2|194.30|1542.94|
|16G-ER-D23S--BR2|192.30|1558.98|16G-ER-D44S--BR2|194.40|1542.14|
|16G-ER-D24S--BR2|192.40|1558.17|16G-ER-D45S--BR2|194.50|1541.35|
|16G-ER-D25S--BR2|192.50|1557.36|16G-ER-D46S--BR2|194.60|1540.56|
|16G-ER-D26S--BR2|192.60|1556.55|16G-ER-D47S--BR2|194.70|1539.77|
|16G-ER-D27S--BR2|192.70|1555.75|16G-ER-D48S--BR2|194.80|1538.98|
|16G-ER-D28S--BR2|192.80|1554.94|16G-ER-D49S--BR2|194.90|1538.19|
|16G-ER-D29S--BR2|192.90|1554.13|16G-ER-D50S--BR2|195.00|1537.40|
|16G-ER-D30S--BR2|193.00|1553.33|16G-ER-D51S--BR2|195.10|1536.61|
|16G-ER-D31S--BR2|193.10|1552.52|16G-ER-D52S--BR2|195.20|1535.82|
|16G-ER-D32S--BR2|193.20|1551.72|16G-ER-D53S--BR2|195.30|1535.04|
|16G-ER-D33S--BR2|193.30|1550.92|16G-ER-D54S--BR2|195.40|1534.25|
|16G-ER-D34S--BR2|193.40|1550.12|16G-ER-D55S--BR2|195.50|1533.47|
|16G-ER-D35S--BR2|193.50|1549.32|16G-ER-D56S--BR2|195.60|1532.68|
|16G-ER-D36S--BR2|193.60|1548.51|16G-ER-D57S--BR2|195.70|1531.90|
|16G-ER-D37S--BR2|193.70|1547.72|16G-ER-D58S--BR2|195.80|1531.12|
|16G-ER-D38S--BR2|193.80|1546.92|16G-ER-D59S--BR2|195.90|1530.33|
|16G-ER-D39S--BR2|193.90|1546.12|16G-ER-D60S--BR2|196.00|1529.55|
|16G-ER-D40S--BR2|194.00|1545.32||||



## LOOPBACK CONFIGURATION 

Loopback can be configured on optical side (OWRAP) and electrical side (EWRAP), with and without forwarding. See definition in figure. 


Loopback is set in A2H, BYTE 111. 

|OWRAP+F<br>Bit 3|OWRAP<br>Bit 2|EWRAP+F<br>Bit 1|EWRAP<br>Bit 0|Write|Read|Mode||
|---|---|---|---|---|---|---|---|
|0|0|0|0|0x00|0x00|Normal mode||
|0|0|0|1|0x01|0x01|EWRAP||
|0|0|1|0|0x02|0x03|EWRAP with Forward||
|0|1|0|0|0x04|0x04|OWRAP||
|1|0|0|0|0x08|0x0C|OWRAP with Forward||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.2 

## GENERAL DEFINITIONS 

|Parameter|Description||
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

