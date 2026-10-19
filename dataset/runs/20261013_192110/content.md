DATASHEET 

5.2 

## **32G-IR-DxxS-BR** 

SFP28, 32/16/8G FC, Secure Optics DWDM 100GHz grid, 192.00 - 196.00THz (41ch), 10km, 7dB, LC, D200-D600 


## OVERVIEW 

The 32G-IR-DxxS-BR is a versatile DWDM transceiver in SFP28 form-factor supporting a wide range of Fiber Channel (FC) services (8G to 32G). The transceiver is provided in versions covering all C-band channels in the 100GHz DWDM grid as specified in the ITU-T G.694.1 standard. The transceiver is approved by Brocade as “Secure Optics” and supports the authentication protocol required for the Gen7 system platforms. 

- The transceiver has an inbuilt 3-mode CDR (Clock Data Recovery) function; - High data rate mode for 32G FC - Low data rate mode for 16G FC 

- Bypass mode for 8 GFC 

The optical performance provides a bridgeable distance of up to 10km (without dispersion compensation) for 32G FC. This transceiver provides digital diagnostic functions via a 2-wire serial interface as defined by the SFF-8472 specification. 

The transceiver module is compliant to RoHS-6/6. 

## TECHNICAL DATA 

|Parameter|Value||Parameter|Value||
|---|---|---|---|---|---|
|Technology|DWDM 100GHz SFP28||**Transmitter data:**|||
|Transmission media|SM (2x LC)||Output power|Min: -3.0dBm2)||
|Typical reach|10km|||Max: +2.0dBm2)||
|Nominal wavelengths|192.00 - 196.00THz||Transmit wavelengths|192.00 - 196.00THz||
|Bit rate support|28.05Gbps|||100GHz (ITU-T G.694.1)||
||14.025Gbps||**Receiver data:**|||
||8.500Gbps||Minimum input power|-10.0dBm1) 2)||
|Protocol support|32GFC||Overload (max power)|+2.0dBm1) 2)||
||16GFC||Wavelength range|1480 - 1580nm||
||8GFC||LOS De.Assert (@ 32G FC)|Max -17dBm||
|Power budget|0 – 7.0dB||LOS Assert (@ 32G FC)|Min -30dBm||
|Dispersion tolerance|-170 to +170ps/nm||LOS Hysteresis|Min 0.5dBm||
|Power consumption|< 2.0W||DDM|Yes||
|Operating temperature|0°C to +70°C||MSA compliance|SFP28 MSA||
|Storage temperature|-40°C to +85°C|||SFF-8402||
|1)@ 28.05 Gbps (32G FC) and BER < 10-6using PRBS 231-1||||||
|2)Average power||||||
|Safety/regulatory compliance:||||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)||||||
|RoHS compliance||||||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.2 

## ORDERING INFORMATION 

|Ordering number|Frequency THz|Wavelength nm|<br>Ordering number|Frequency THz|Wavelength nm|
|---|---|---|---|---|---|
|32G-IR-D20S-BR|192.00|1561.42|32G-IR-D41S-BR|194.10|1544.53|
|32G-IR-D21S-BR|192.10|1560.61|32G-IR-D42S-BR|194.20|1543.73|
|32G-IR-D22S-BR|192.20|1559.79|32G-IR-D43S-BR|194.30|1542.94|
|32G-IR-D23S-BR|192.30|1558.98|32G-IR-D44S-BR|194.40|1542.14|
|32G-IR-D24S-BR|192.40|1558.17|32G-IR-D45S-BR|194.50|1541.35|
|32G-IR-D25S-BR|192.50|1557.36|32G-IR-D46S-BR|194.60|1540.56|
|32G-IR-D26S-BR|192.60|1556.55|32G-IR-D47S-BR|194.70|1539.77|
|32G-IR-D27S-BR|192.70|1555.75|32G-IR-D48S-BR|194.80|1538.98|
|32G-IR-D28S-BR|192.80|1554.94|32G-IR-D49S-BR|194.90|1538.19|
|32G-IR-D29S-BR|192.90|1554.13|32G-IR-D50S-BR|195.00|1537.40|
|32G-IR-D30S-BR|193.00|1553.33|32G-IR-D51S-BR|195.10|1536.61|
|32G-IR-D31S-BR|193.10|1552.52|32G-IR-D52S-BR|195.20|1535.82|
|32G-IR-D32S-BR|193.20|1551.72|32G-IR-D53S-BR|195.30|1535.04|
|32G-IR-D33S-BR|193.30|1550.92|32G-IR-D54S-BR|195.40|1534.25|
|32G-IR-D34S-BR|193.40|1550.12|32G-IR-D55S-BR|195.50|1533.47|
|32G-IR-D35S-BR|193.50|1549.32|32G-IR-D56S-BR|195.60|1532.68|
|32G-IR-D36S-BR|193.60|1548.51|32G-IR-D57S-BR|195.70|1531.90|
|32G-IR-D37S-BR|193.70|1547.72|32G-IR-D58S-BR|195.80|1531.12|
|32G-IR-D38S-BR|193.80|1546.92|32G-IR-D59S-BR|195.90|1530.33|
|32G-IR-D39S-BR|193.90|1546.12|32G-IR-D60S-BR|196.00|1529.55|
|32G-IR-D40S-BR|194.00|1545.32||||



## RATE SELECT OPERATION 

The 32G-IR-DxxS--BR supports high data rates 25.78G/28.05G with CDR engaged and Low data rate 14.025G with CDR half-rate engaged, 8.5G with CDR bypassed. 

|RS0|RS1|Rx data rate|Tx data rate||
|---|---|---|---|---|
|High/1|High/1|28.05Gbps|28.05Gbps||
|Low/0|Low/0|14.025/8.5Gbps|14.025/8.5Gbps||



## LOOPBACK CONFIGURATION 

E-wrap Loopback: User can configure e-wrap loopback by writing 0x01 to byte 111 of A2H. The default value of byte 111 of A2H is 0x00. Please note that the changed value will not be saved at power-off. 

O-wrap Loopback: User can configure e-wrap loopback by writing 0x04 to byte 111 of A2H. The default value of byte 111 of A2H is 0x00. Please note that the changed value will not be saved at power-off. 


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

