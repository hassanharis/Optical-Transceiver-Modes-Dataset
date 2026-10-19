**REV:5.0** 


## **28Gb/s 850nm Multi-mode SFP28 Transceiver** 

## **PRODUCT FEATURES** 

- Up to 28Gbps Data Links 

- Maximum link length of 70m links on OM3 or 

100m links on OM4 multimode fiber 


- Power dissipation < 1W 

- VSCEL laser and PIN receiver 

- Metal enclosure, for lower EMI 

- 2-wire interface with integrated Digital Diagnostic monitoring 

- Hot-pluggable SFP+ footprint 

- Specifications compliant with SFF 8472 

- Compliant with SFP+ MSA with LC connector 

- Single 3.3V power supply 

- Case operating temperature range: Commercial: 0°C to +70°C 

Extensional: 0°C to +85°C 

## **APPLICATIONS** 

- 25G Ethernet 

- Data center and Fiber channel 

## **STANDARD** 

- Compliant to SFF-8431 

- Compliant to SFF 8472 

- RoHS Compliant. 

**www.xgiga.cn                                           Page 1** 

**REV:5.0** 


##  **Ordering information** 

|**Product part**<br>**Number**|**Data Rate**<br>**(Gbps)**||**Wavelength**<br>**(nm)**|**Transmission**<br>**Distance(km)**|**Temperature Range**<br>（**Tcase**）（℃）|**Temperature Range**<br>（**Tcase**）（℃）|
|---|---|---|---|---|---|---|
|||**Media**|||||
||||||||
|XP-85B1-02D|25.78G|Multi mode<br>fiber|850|10|0~70|Commercial|
|XP-85B1-02DE|25.78G|Multi mode<br>fiber|850|10|0~85|Extensional|



## **I. Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature|Ts|-40|-|85|ºC||
|Relative Humidity|RH|5|-|95|%||
|Power Supply Voltage|VCC|-0.3|-|4|V||
|Signal Input Voltage||Vcc-0.3|-|Vcc+0.3|V||



## **II. Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Tcase|0|-|70|ºC|Commercial|
|||0|-|85|ºC|Extensional|
|Power Supply Voltage|VCC|3.14|3.3|3.47|V||
|Power Supply Current|ICC|-||300|mA||
|Data Rate|BR||25.78||Gbps||
|Transmission Distance|TD||-|100|m|OM4 or 70m OM3|
|Coupled fiber||Multi mode fiber|||||



## **III. Optical Characteristics** 

||**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Ref.**||
|---|---|---|---|---|---|---|---|---|
||**Transmitter**||||||||
||Output Opt. Pwr|POUT|-8.4||2.4|dBm|1||
||Optical Wavelength|λ|840|850|860|nm|||
||Spectral Width(RMS)|σ|||0.6|nm|||
||Optical Extinction Ratio|ER|2.0|||dB|||
||RIN|RIN|||-128|dB/Hz|||
||**Receiver**||||||||
||Average Receiver Power @25.78Gb/s|RxMAX|-10.3||3|dBm|2||
||Input Saturation Power(Overload)|Psat|2.4|||dBm|||
||Wavelength Range|λC|770|850|860|nm|||
||LOS De -Assert|LOSD|||-12|dBm|||
||LOS Assert|LOSA|-30|||dBm|||
||LOS Hysteresis||0.5|||dB|||



**www.xgiga.cn                                           Page 2** 

**REV:5.0** 


## **Notes:** 

1. Class 1 Laser Safety per FDA/CDRH and IEC-825-1 regulations. 31 

2. Measured with a PRBS 2 -1 test pattern, @25.78Gb/s, BER<10-5 . 

## **IV. Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.14|3.3|3.46|V||
|Supply Current|Icc|||300|mA||
||||||||
|**Transmitter**|||||||
||||||||
|Input differential impedance|Rin||100||Ω|1|
|Single ended data input swing|Vin,pp|180||700|mV||
|Transmit Disable Voltage|VD|Vcc–1.3||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V|2|
||||||||
|**Receiver**|||||||
||||||||
|Differential data output swing|Vout,pp|300||850|mV|3|
|LOS Fault|VLOS fault|Vcc–1.3||VccHOST|V|4|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|4|



## **Notes:** 

1. Connected directly to TX data input pins. AC coupled thereafter. 

2. Or open circuit. 

3. Into 100 ohms differential termination. 

4. Loss Of Signal is LVTTL. Logic 0 indicates normal operation; logic 1 indicates no signal detected. 

**www.xgiga.cn                                           Page 3** 

**REV:5.0** 


## **V. Pin Descriptions** 


**Pin out of Connector Block on Host Board** 

|**Pin**|**Symbol**|**Name/Description**|**NOTE**|
|---|---|---|---|
|1|VEET|Transmitter Ground  (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line|4|
|5|SCL|2-wire Serial Interface Clock Line|4|
|6|MOD_ABS|Module Absent. Grounded within the module|4|
|7|RS0|Rate Select 0|5|
|8|LOS|Loss of Signal indication.  Logic 0 indicates normal operation.|6|
|9|RS1|No connection required|1|
|10|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|11|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|12|RD-|Receiver Inverted DATA out.  AC Coupled||
|13|RD+|Receiver Non-inverted DATA out.  AC Coupled||
|14|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|15|VCCR|Receiver Power Supply||
|16|VCCT|Transmitter Power Supply||



**www.xgiga.cn                                           Page 4** 

**REV:5.0** 


|17|VEET|Transmitter Ground  (Common with Receiver Ground)|1|
|---|---|---|---|
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in.  AC Coupled.||
|20|VEET|Transmitter Ground  (Common with Receiver Ground)|1|



**Notes:** 

1. Circuit ground is internally isolated from chassis ground. 

2. TFAULT is an open collector/drain output, which should be pulled up with a 4.7kΩ– 10 kΩ resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V.A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Should be pulled up with 4.7kΩ- 10kΩ on host board to a voltage between 2.0V and 3.6V. MOD_ABS pulls line low to indicate module is plugged in. 

5. Internally pulled down per SFF-8431 Rev 4.1. 

6. LOS is open collector output. It should be pulled up with 4.7kΩ – 10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

## **VI. Digital Diagnostic Functions** 

XGIGA XP-85B1-02D(E) transceivers support the 2-wire serial communication protocol as defined in the SFP+ MSA. The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, XGIGA SFP+ transceivers provide a unique enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP+ MSA defines a 256-byte memory map in EEPROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E2PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. 

**www.xgiga.cn                                           Page 5** 

**REV:5.0** 


The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

## **VII. Host - Transceiver Interface Block Diagram** 


**www.xgiga.cn                                           Page 6** 

**REV:5.0** 


## **VIII. Outline Dimensions** 


**----- Start of picture text -----**<br>
LC connector<br>**----- End of picture text -----**<br>


## **IX. Regulatory Compliance** 

||||
|---|---|---|
|**Feature**|**Reference**|**Performance**|
||||
|Electrostatic discharge（ESD）|IEC/EN 61000-4-2|Compatible with standards|
|Electromagnetic Interference (EMI)|<br>FCC Part 15 Class B EN 55022 Class B<br>(CISPR 22A)|<br>Compatible with standards|
|Laser Eye Safety|FDA 21CFR 1040.10, 1040.11 IEC/EN<br>60825-1,2|<br>Class 1 laser product|
|Component Recognition|IEC/EN 60950, UL|Compatible with standards|
|ROHS|2002/95/EC|Compatible with standards|
|EMC|EN61000-3|Compatible with standards|



**www.xgiga.cn                                           Page 7** 

**REV:5.0** 


## **Appendix A. Document Revision** 

|**Version No.**|**Date**|**Description**|
|---|---|---|
|1.0|2018-07-18|Preliminary datasheet|
|2.0|2020-04-28|Update LOS De –Assert to -12|
|3.0|2020-12-18|Add PN XP-85B1-02D-4, support 10/25Gb/s|
|4.0|2021-03-01|Add PN XP-85B1-02DE, support temperature range:0~85°C|
|5.0|2021-05-12|Delete PN XP-85B1-02D-4<br>Change receiver sensitivity toAverage Receiver Power @25.78Gb/s from<br>-10.3~+3dBm|



**www.xgiga.cn                                           Page 8** 

