Optical Transceivers 

## FTLF8538P5BCZ 

## **25GBASE-SR Low Latency SFP+ Transceiver** 

FTLF8538P5BCz SFP+ transceivers are designed for use in 25Gb/s data rate over multimode fiber. They are compliant to IEEE802.3by, SFF-8472 Rev 12.2band SFF-8402g, and compatible with SFF-8432aand applicable portions of SFF-8431 Rev. 4.1c. The transceiver is RoHS compliant as described in Application Note AN-2038. 


## FEATURES 

## APPLICATIONS 

- Up to 25.78 Gb/s bi-directional data links 

- Hot-pluggable SFP+ footprint 

- Built-in digital diagnostic functions 

   - 25GE SR 

   - 100G SR4 fan out to 4x25GE SR 

   - eCPRI 

- 850nm Oxide VCSEL laser transmitter 

- Duplex LC connector 

- RoHS compliant 

- 100m over M5F MMF (50/125 um OM4) 

- 70m over M5E MMF (50/125um OM3) 

- 1E-12 BER over 30m OM3 / 40m OM4 MMF 

- Metal enclosure, for lower EMI 

- 1.0W maximum power consumption 

- Single 3.3V power supply 

- Operating temperature range: 0°C to 70°C 

**FTLF8538P5BCz** 

## **Product Selection** 

## **FTLF8538P5BCz** 

z=L: Single rate (25GbE only) z=V: Dual rate (25GbE and 10GbE) 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLF8538P5BCz** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line (MOD-DEF2)|4|
|5|SCL|2-wire Serial Interface Clock (MOD-DEF1)|4|
|6|MOD_ABS|Module Absent, connected to VEET or VEER|4|
|7|RS0|Rx Rate Select<br>Single Rate (FTLF8538P5BCL): No Connection (NC)<br>Dual Rate (FTLF8538P5BCV)<br>Open or Low = 10.3 Gb/s Ethernet (Low Bandwidth)<br>High = 25.78 Gb/s Ethernet (High Bandwidth)|5|
|8|RX_LOS|Loss of Signal indication. Logic 0 indicates normal operation.|6|
|9|RS1|Tx Rate Select<br>Single Rate (FTLF8538P5BCL): No Connection (NC)<br>Dual Rate (FTLF8538P5BCV)<br>Open or Low = 10.3 Gb/s Ethernet (Low Bandwidth)<br>High = 25.78 Gb/s Ethernet (High Bandwidth)|5|
|10|VEER|Receiver Ground (Common with Transmitter Ground)|1|
|11|VEER|Receiver Ground (Common with Transmitter Ground)|1|
|12|RD-|Receiver Inverted DATA out. AC Coupled||
|13|RD+|Receiver Non-inverted DATA out. AC Coupled||
|14|VEER|Receiver Ground (Common with Transmitter Ground)|1|
|15|VCCR|Receiver Power Supply||
|16|VCCT|Transmitter Power Supply||
|17|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in. AC Coupled.||
|20|VEET|Transmitter Ground (Common with Receiver Ground)|1|



Notes 

1. Circuit ground is internally isolated from chassis ground. 

2. T FAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V. A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. MOD_ABS pulls line low to indicate module is plugged in. 5. Rate select can also be set through the 2-wire bus in accordance with SFF-8472 v. 12.1c. Rx Rate Select is set at Bit 3, Byte 110, Address A2h. Tx Rate Select is set at Bit 3, Byte 118, Address A2h. Note: writing a “1” selects maximum bandwidth operation. Rate select is the logic OR of the input state of Rate Select Pin and 2-wire bus. 

6. LOS is open collector output. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal 

3 

**FTLF8538P5BCz** 

## **II. Absolute Maximum Ratings** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Case Operating Temperature|TC|0||70|°C||
|Relative Humidity (Non-condensing)|RH|0||85|%|1|



Notes: 

1. Non Condensing 

## **III. Electrical Characteristics (TA , VCC = 3.15 to 3.46 Volts )** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.15||3.46|V||
|Supply Current|Icc|||290|mA|1|
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|2|
|Diferential data input swing|Vin,pp|125||450|mV|3|
|Inner Eye Height|EH6|95|||mV||
|Transmit Disable Voltage|VD|2||Vcc|V|4|
|Transmit Enable Voltage|VEN|Vee||Vee + 0.8|V||
|Receiver|||||||
|Single ended data output swing|Vout,pp|185||425|mV|5|
|LOS Fault|VLOS fault|2||VccHOST|V|6|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|6|
|Power Supply Rejection|PSR|100|||mVpp|7|



Notes: 

1. With established link. The total power dissipation could exceed 1W when the module is trying to establish link at operating case temperature below 25oC 

2. Connected directly to TX data input pins. AC coupling from pins into laser driver IC. 

3. The minimum value represents the minimum outer eye amplitude. 

4. Or open circuit. 

5. Into 100 ohms differential termination. 

6. LOS is an open collector output. Should be pulled up with 4.7k – 10kohms on the host board. Normal operation is logic 0; loss of signal is logic 1. Maximum pull-up voltage is 5.5V. 

7. Receiver sensitivity is compliant with power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specified value applied through the recommended power supply filtering network. 

4 

**FTLF8538P5BCz** 

## **IV. Optical Characteristics (TA , VCC = 3.15 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Average Output Power|POUT|-8.4||2.4|dBm|1|
|Optical Wavelength|λC|840||860|nm||
|Spectral Width (RMS)|σ|||0.60|nm||
|Optical Modulation Amplitude<br>25.78Gb/s (Single rate and dual rate)<br>10.3Gb/s (Dual rate only)|OMA|-6.4<br>-5.2||3|dBm||
|Transmitter and Dispersion Eye Closure @<br>25.7Gb/s|TDEC|||4.3|dB||
|Relative Intensity Noise|RIN|||-128|dB/Hz||
|Extinction Ratio @ 25.78Gb/s|ER|2|||||
|Receiver|||||||
|Unstressed Receiver OMA Sensitivity<br>25.78Gb/s (Single rate and dual rate)<br>10.3Gb/s (Dual rate only)|RxSENS|||-5.2<br>-7.5|dBm||
|Unstressed Receiver OMA Sensitivity<br>@ 10.3Gb/s (Dual rate only)|RxSENS|||-10.1|dBm||
|Average Receiver Power @25.78Gb/s|RxMAX|-10.3||3|dBm|2|
|Optical Center Wavelength|λC|840||860|nm||
|Optical Return Loss||12|||dB||
|LOS De-Assert|LOSD|||-13|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|||dB||



Notes: 

1. Class 1 Laser Safety limit per FDA/CDRH, and EN (IEC) 60825 laser safety standards. 

2. Informative Only 

5 

**FTLF8538P5BCz** 

## **V. General Specifications** 

|Fiber Type<br>Data Rate|OM3|OM3|OM3|OM4|OM4|OM4|
|---|---|---|---|---|---|---|
||70m|50m|30m|100m|70m|40m|
|10.3Gb/s|1E-12<br>Note 3|1E-12<br>Note 3|1E-12<br>Note 3|1E-12<br>Note 3|1E-12<br>Note 3|1E-12<br>Note 3|
|25.78Gb/s|5E-5<br>Note 1|5E-8<br>Note 2|5E-12<br>Note 3|5E-5<br>Note 1|5E-8<br>Note 2|5E-12<br>Note 3|



Notes: 

1. RS FEC 

2. Firecode FEC 

3. FEC Free 

## **VII. Environmental Specifications** 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Top|0||70|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

The FTLF8538P5BCz transceivers are RoHS compliant. Copies of certificates are available from II-VI Incorporated upon request. 

FTLF8538P5BCz transceiver modules are Class 1 laser eye safety compliant per IEC 60825-1. 

CAUTION: Use of controls or adjustments or performance of procedures other than those specified herein may result in hazardous radiation exposure. 

6 

**FTLF8538P5BCz** 

## **VIII. Digital Diagnostic Functions** 

Finisar® FTLF8538P5BCz SFP+ transceivers support the 2-wire serial communication protocol as defined in the SFP MSA[f] . It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar SFP transceivers provide a enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in E[2] PROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN-2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFP MSA documentation[c,f] and Finisar Application Note AN-2030. 

## **TX Equalization Control** 

Tx input equalization control can be accessed through 2-wire serial interface at byte address 114 (A2h). Tx input equalization control for 25GE is located at the upper 4 bits of byte 114 (A2h) while the lower 4 bits are reserved for rate low in the case of dual rate application. 

## **RX Emphasis Control** 

Rx output emphasis control can be accessed through 2-wire serial interface at byte address 115 (A2h). Rx output emphasis control for 25GE is located at the upper 4 bits of byte 115 (A2h) while the lower 4 bits are reserved for rate low in the case of dual rate application. 

7 

**FTLF8538P5BCz** 

## **IX. Digital Diagnostic Specifications** 

FTLF8538P4BCz transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Units Min Max Accuracy Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Units|Min|Max|Accuracy|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transceiver temperature|DDDTemp|ºC|0|+70|±5ºC||
|Transceiver supply voltage|DDDVoltage|V|3.14|3.45|±3%||
|Transmitter bias current|DDDBias|mA|0|20|±10%|1|
|Transmitter output power|DDDTx-Power|dBm|-9|+2.4|±3dB||
|Receiver average optical input power|DDDRx-Power|dBm|-11|+2.4|±3dB||



Notes: 

1. Accuracy of Measured Tx Bias Current is 10% of the actual Bias Current from the laser driver to the laser. 

8 

**FTLF8538P5BCz** 

## **X. Mechanical Specifications** 

Finisar® FTLF8538P5BCz SFP+ transceivers are compatible with the SFF-8432b specification for improved pluggable form factor. 


FTLF8538P5BCz 

9 

**FTLF8538P5BCz** 

## **XI. PCB Layout and Bezel Recommendations** 


Figure 3. PCB Layout and Bezel Recommendations, as per [9] 

10 

**FTLF8538P5BCz** 



Figure 4. 

11 

**FTLF8538P5BCz** 

## **XII. Ordering Information** 

|Part Number|Data Rate|
|---|---|
|FTLF8538P5BCL|Single Rate (25GbE only)|
|FTLF8538P5BCV|Dual Rate (25GbE and 10GbE)|



## **XIII. References** 

a. “Improved Pluggable Form Factor”, SFF Document Number SFF-8432, Revision 5.0, July 16, 2007. 

b. “Digital Monitoring Interface for Optical Transceivers”, SFF Document Number SFF-8472, Revision 12.2. 

c. “Enhanced Small Form Factor Pluggable Module ‘SFP+ ‘”, SFF Document Number SFF-8431, Revision 4.1, July 6, 2009; Addendum Jun 21, 2013. 

d. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. 08-June 2011, which supercedes the previous ROHS Directive 2002/95/EC. 

e. Small Form Factor Pluggable (SFP) Transceiver Multi-source Agreement (MSA), September 14, 2000 which is available as SFF Document Number INF-8074, 

Revision 1.0 May 12, 2001 

f. “0.8mm Card Edge Connector for 16Gb/s Applications”, SFF Document Number SFF-8081, Revision 0.2, December 21, 2009. 

g. SFF-8402, Revision 0.2 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

