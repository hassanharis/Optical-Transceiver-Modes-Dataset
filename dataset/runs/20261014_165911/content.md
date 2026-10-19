**REV:3.0** 


## **XP-13B1-10D-5** 

## **32G FC 1310nm Single-mode SFP28 Transceiver** 

## **PRODUCT FEATURES** 

- ⚫ Up to 28.05Gb/s bit rates 

- ⚫ Up to 10km transmission on SMF 

- ⚫ DFB Laser and PIN receiver 

- ⚫ Metal enclosure, for lower EMI 


- ⚫ 2-wire interface with integrated Digital Diagnostic monitoring 

- ⚫ Specifications compliant with SFF 8472 

- ⚫ Compliant with SFP+ MSA with LC connector 

- ⚫ Single 3.3V power supply 

- ⚫ Power dissipation < 1.5 W 

- ⚫ Case operating temperature range: 0°C to 70°C 

## **APPLICATIONS** 

- ⚫ Tri-Rate 8.5/14.025/28.05Gb/s Fiber Channel. 

## **STANDARD** 

- ⚫ Compliant to SFF-8431 

- ⚫ Compliant to SFF 8472 

- ⚫ RoHS Compliant. 

**www.xgiga.cn                                           Page 1** 

**REV:3.0** 


## **I. Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature|Ts|-40|-|85|ºC||
|Relative Humidity|RH|5|-|95|%||
|Power SupplyVoltage|VCC|-0.5|-|4.0|V||
|Signal Input Voltage||Vcc-0.3|-|Vcc+0.3|V||



## **II. Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Tcase|0|-|70|ºC||
|Power SupplyVoltage|VCC|3.14|3.30|3.47|V||
|Power SupplyCurrent|ICC|-||360|mA||
|Data Rate|BR||8.5<br>14.025<br>28.05||Gbps|1|
|Bit Error Rate|BER|||10^-12<br>10^-6|Gbps|2<br>3|
|Transmission Distance|TD||-|10|km||
|Coupled fiber|Single mode fiber||||||



## **Notes:** 

1. 8x, Fibre Channel compatible, per FC-PI-41. 

2. PRBS 27-1 for 8GFC. PRBS 231-1 for 16GFC 

3. FEC for 32GFC 

## **III. Optical Characteristics** 

|**III. Optical Characteristics **|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Ref.**|
|**Transmitter**|||||||
|Average Output Power,28.05Gb/s & 14.025Bb/s|POUT|-5||+2.0|dBm|1,2|
|Average Output Power,8.5Gb/s|POUT|-8.4||+0.5|dBm|1|
|Optical Wavelength|λ|1295||1325|nm||
|Spectral Width(RMS)|σ|||1|nm||
|Optical Modulation Amplitude<br>8.5Gb/s<br>14.025Gb/s<br>28.05Gb/s|OMA|-5.4<br>-2.0<br>-2.0||+3|dBm||
|Transmitter Dispersion Penalty<br>8.5Gb/s<br>14.025Gb/s<br>28.05Gb/s|TDP|||3.2<br>4.4<br>2.7|dB||
|Optical Extinction Ratio<br>8.5Gb/s&14.025Gb/s<br>28.05Gb/s|ER|3.5<br>4.0|||dB||
|Relative Intensity Noise<br>8.5Gb/s<br>14.025Gb/s<br>28.05Gb/s|RIN|||-128<br>-130<br>-130|dB/Hz||
|**Receiver**|||||||



**www.xgiga.cn                                           Page 2** 

**REV:3.0** 


|Unstressed Receiver OMA Sensitivity<br>8.5Gb/s<br>14.025Gb/s<br>28.05Gb/s|RSENS|||-13.8<br>-12.0<br>-11.4|dBm|3|
|---|---|---|---|---|---|---|
|Average Receiver Power|RxMAX|||2|dBm||
|Optical Return Loss<br>8.5Gb/s&14.025Gb/s<br>28.05Gb/s||12<br>26|||dB||
|LOS De -Assert|LOSD|||-17|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|||dB||



## **Notes:** 

1. Class 1 Laser Safety limit per FDA/CDRH, and EN (IEC) 60825 laser safety standards. 

2. 3200-SM-LC-L OMA in dBm shall also exceed -5.0 TDP. 

3. For 32GFC with FEC, receiver sensitivity is defined at 10^-6 BER level, not 10^-12 BER level. 

## **IV. Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.14|3.3|3.46|V||
|Supply Current|Icc|||400|mA|1|
|**Transmitter**|||||||
|Input differential impedance|Rin||100||Ω|2|
|Differential data input eye height|Vin,pp|250||900|mV|2|
|Transmit Disable Voltage|VD|Vcc–1.3||Vcc|V|3|
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V||
|**Receiver**|||||||
|Differential data output swing|Vout,pp|300||1000|mV|4|
|LOS Fault|VLOS fault|Vcc–1.3||VccHOST|V|5|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|5|



## **Notes:** 

1. With established link, the total power dissipation shall not exceed 1.3W. 

2. Connected directly to TX data input pins. AC coupling from pins into CDR, BER contour 10-6. 

3. Or open circuit. 

4. Into 100 ohms differential termination. 

5. LOS is an open collector output. Should be pulled up with 4.7k – 10kohms on the host board. Normal operation is logic 0; loss of signal is logic 1. Maximum pull-up voltage is 5.5V. 

**www.xgiga.cn                                           Page 3** 

**REV:3.0** 


## **V. Pin Descriptions** 


## **Pin out of Connector Block on Host Board** 

|**Pin**|**Symbol**|**Name/Description**|**NOTE**|
|---|---|---|---|
|1|VEET|Transmitter Ground  (Common with Receiver Ground)|1|
|2|Tx_Fault|Transmitter Fault.|2|
|3|Tx_Disable|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line (MOD-DEF2)|4|
|5|SCL|2-wire Serial Interface Clock (MOD-DEF1)|4|
|6|MOD_ABS|Module Absent, connected to VEETor VEER|4|
|7|RS0|Rx Rate Select:<br>Open or Low = 8.5 or 14.025 Gb/s Fibre Channel (Low Bandwidth)<br>High = 28.05 Gb/s Fibre Channel(High Bandwidth)|5|
|8|Rx_LOS|Loss of Signal indication.  Logic 0 indicates normal operation.|6|
|9|RS1|Tx Rate Select:<br>Open or Low = 8.5 or 14.025 Gb/s Fibre Channel (Low Bandwidth)<br>High = 28.05 Gb/s Fibre Channel(High Bandwidth)|5|
|10|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|11|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|12|RD-|Receiver Inverted DATA out.||
|13|RD+|Receiver Non-inverted DATA out.||
|14|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|15|VCCR|Receiver Power Supply||
|16|VCCT|Transmitter Power Supply||



**www.xgiga.cn                                           Page 4** 

**REV:3.0** 


|17|VEET|Transmitter Ground  (Common with Receiver Ground)|1|
|---|---|---|---|
|18|TD+|Transmitter Non-Inverted DATA in.||
|19|TD-|Transmitter Inverted DATA in.||
|20|VEET|Transmitter Ground  (Common with Receiver Ground)|1|



## **Notes:** 

1. Circuit ground is internally isolated from chassis ground. 

2. TFAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V. A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. MOD_ABS pulls line low to indicate module is plugged in. 

5. Rate select can also be set through the 2-wire bus in accordance with SFF-8472 v. 12.1c. Rx Rate Select is set at Bit 3, Byte 110, Address A2h. Tx Rate Select is set at Bit 3, Byte 118, Address A2h. Note: writing a “1” selects maximum bandwidth operation. Rate select is the logic OR of the input state of Rate Select Pin and 2-wire bus. 

6. LOS is open collector output. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

## **VI. Digital Diagnostic Functions** 

XGIGA XP-13B1-10D-5 transceivers support the 2-wire serial communication protocol as defined in the SFP+ MSA. The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, XGIGA SFP+ transceivers provide a unique enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in EEPROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h).The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E2PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with 

**www.xgiga.cn                                           Page 5** 

**REV:3.0** 


SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

## **VII. Host - Transceiver Interface Block Diagram** 


**www.xgiga.cn                                           Page 6** 

**REV:3.0** 


## **VIII. Outline Dimensions** 

## **IX. Regulatory Compliance** 

|**Feature**|**Reference**|**Performance**|
|---|---|---|
|Electrostatic discharge（ESD）|IEC/EN 61000-4-2|Compatible with standards|
|Electromagnetic Interference (EMI|)<br>FCC Part 15 Class B EN 55022 Class B<br>(CISPR 22A)|Compatible with standards|
|Laser Eye Safety|FDA 21CFR 1040.10, 1040.11 IEC/EN<br>60825-1,2|Class 1 laser product|
|Component Recognition|IEC/EN 60950, UL|Compatible with standards|
|ROHS|2011/65/EU and (EU)2015/863|Compatible with standards|
|EMC|EN61000-3|Compatible with standards|



## **Appendix A. Document Revision** 

|**Version No.**|**Date**|**Description**|
|---|---|---|
|1.0|2020-06-03|<br>Preliminary datasheet|
|2.0|2021-08-19|<br>Add specifications for Tri-Rate 8.5/14.025Gbps Fiber Channel.|
|3.0|2021-11-19|<br>Update product picture.|



**www.xgiga.cn                                           Page 7** 

