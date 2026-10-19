**REV:5.0** 


## **10Gb/s 850nm Multi-mode SFP+ Transceiver** 

## **PRODUCT FEATURES** 

- Up to 11.1Gbps Data Links 

- Maximum link length of 300m links on OM3 multimode fiber or 400m links on OM4 multimode fiber 


- Power dissipation < 1W 

- VSCEL laser and PIN receiver 

- Metal enclosure, for lower EMI 

- 2-wire interface with integrated Digital Diagnostic monitoring 

- Hot-pluggable SFP+ footprint 

- Specifications compliant with SFF 8472 

- Compliant with SFP+ MSA with LC connector 

- Single 3.3V power supply 

- Case operating temperature range: Commercial: 0°C to +70°C 

Industrial: -40°C to +85°C 

## **APPLICATIONS** 

- 10GBASE-SR/SW & 10G Ethernet 

- 2.457 Gb/s CPRI 

- 3.072 Gb/s CPRI 

## **STANDARD** 

   - Compliant to SFP+ SFF-8431 

   - Compliant to 802.3ae 10GBASE-SR. 

   - RoHS Compliant. 

- 4.915 Gb/s CPRI 

- 6.144Gb/s CPRI 

- 9.8304 Gb/s CPRI 

- 10.1376 Gb/s CPRI 

**www.xgiga.cn                                           Page 1** 

**REV:5.0** 


## **Ordering information** 

|**Product part**<br>**Number**|**Data Rate**<br>**(Gbps)**||**Wavelength**<br>**(nm)**|**Transmission**<br>**Distance-Om3(m)**|**Temperature Range**<br>（**Tcase**）（℃）|**Temperature Range**<br>（**Tcase**）（℃）|
|---|---|---|---|---|---|---|
|||**Media**|||||
||||||||
|XGXP-8596-02D|10.3125|Multi-mode<br>fiber|850|300|0~70|commercial|
|XGXP-8596-02DA|10.3125|Multi-mode<br>fiber|850|300|-40~85|Industrial|



**Note:** XGXP-8596-02D(A) also supports data rates of 9.8304Gb/s,6.144Gb/s,4.915Gb/s,3.072Gb/s and 2.457Gb/s for CPRI. 

## **I. Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature|Ts|-40|-|85|ºC||
|Relative Humidity|RH|5|-|95|%||
|Power SupplyVoltage|VCC|-0.3|-|4|V||
|Signal Input Voltage||Vcc-0.3|-|Vcc+0.3|V||



## **II. Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Tcase|0|-|70|ºC|commercial|
|||-40|-|85|ºC|Industrial|
|Power Supply Voltage|VCC|3.14|3.3|3.47|V||
|Power Supply Current|ICC|-||300|mA||
|Data Rate|BR||10.3125||Gbps|1|
|Transmission Distance|TD||-|300|m|OM3|
|Coupled fiber||Multi mode fiber||||50/125um MMF|



## **Notes:** 

1. Compatible with data rates lower than 10.3125Gbps. 

## **III. Optical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Ref.**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
|Output Opt. Pwr|POUT|-6||-1|dBm|1|
|Optical Wavelength|λ|840|850|860|nm||
|Optical Extinction Ratio|ER|3.0|||dB||
|RIN|RIN|||-128|dB/Hz||
|Output Eye Mask||Compliant with IEEE 802.3ae|||||



**www.xgiga.cn                                           Page 2** 

**REV:5.0** 


|**Receiver**|||||||
|---|---|---|---|---|---|---|
|Rx Sensitivity|RSENS|||-10|dBm|2|
|Input Saturation Power(Overload)|Psat|0.5|||dBm||
|Wavelength Range|λC|840|850|860|nm||
|LOS De -Assert|LOSD|||-12|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|||dB||



## **Notes:** 

1. Class 1 Laser Safety per FDA/CDRH and IEC-825-1 regulations. 

- 31 -12 

- 2. Measured with a PRBS 2 -1 test pattern, @10.325Gb/s, BER<10 . 

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
|7|RS0|NO connection required||
|8|LOS|Loss of Signal indication.  Logic 0 indicates normal operation.|5|
|9|RS1|No connection required||
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

5. LOS is open collector output. It should be pulled up with 4.7kΩ – 10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

## **VI. Digital Diagnostic Functions** 

XGIGA XGXP-8596-02D(A) transceivers support the 2-wire serial communication protocol as defined in the SFP+ MSA. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, XGIGA SFP+ transceivers provide a unique enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP+ MSA defines a 256-byte memory map in EEPROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver 

**www.xgiga.cn                                           Page 5** 

**REV:5.0** 


into those segments of the E2PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

## **VII. Host - Transceiver Interface Block Diagram** 


**www.xgiga.cn                                           Page 6** 

**REV:5.0** 


## **VIII. Outline Dimensions** 

## **IX. Regulatory Compliance** 

||||
|---|---|---|
|**Feature**|**Reference**|**Performance**|
||||
|Electrostatic discharge（ESD）|IEC/EN 61000-4-2|Compatible with standards|
|Electromagnetic Interference (EMI)|FCC Part 15 Class B EN 55022 Class B<br>(CISPR 22A)|Compatible with standards|
|Laser Eye Safety|FDA 21CFR 1040.10, 1040.11 IEC/EN<br>60825-1,2|Class 1 laser product|
|Component Recognition|IEC/EN 60950, UL|Compatible with standards|
|ROHS|2011/65/EU and 2015/863/EU|Compatible with standards|
|EMC|EN61000-3|Compatible with standards|



## **Appendix A. Document Revision** 

|**Version No.**|**Date**|**Description**|
|---|---|---|
|1.0|2011-09-01|Preliminary datasheet|
|2.0|2011-09-10|Update format and company’s logo|
|3.0|2015-03-27|Add industrial type|
|4.0|2020-10-12|Add CPRI data rates.|
|5.0|2023-06-08|Update receiver wavelength min from 770nm to 840nm<br>Update ROHS compliance|



**www.xgiga.cn                                           Page 7** 

