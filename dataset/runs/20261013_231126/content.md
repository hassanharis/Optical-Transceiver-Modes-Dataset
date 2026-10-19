Optical Transceivers 

## FTLX1672M3BCL 

## **10Gb/s, 40km Single Mode, Multi-Rate SFP+ Transceiver** 

FTLX1672M3BCL transceivers are Enhanced Small Form Factor Pluggable SFP+ transceivers designed for use in 10-Gigabit multi-rate links up to 40km of G.652 single mode fiber. They are compliant with SFF-8431[1] , SFF-8432[2] , SONET OC-192 IR_x005F_xFFFE_2R/3R, SDH STM-64.2b/3b, OTN P1S1-2D2b, 10GBASE-ER/EW and support 8.5G and 10G Fibre Channel. The transceivers use internal clock and data recovery (CDR) IC’s for the transmitter and the receiver. This guarantees compliance with the SONET/SDH jitter requirements and it can be used to set the electrical interface to be XFI-compliant. Digital diagnostics functions are available via a 2-wire serial interface, as specified in SFF-84723. The optical transceiver is compliant per the RoHS Directive 2011/65/EU[4] . See Finisar Application Note AN-2038 for more details[5] . 


## FEATURES 

## APPLICATIONS 

- Hot-pluggable SFP+ footprint 

- Supports 8.5 and 9.95 to 11.3 Gb/s 

- 40km link length (800ps/nm) 

- -5/70°C case temperature range 

- Internal transmitter/receiver CDR 

- low power consumption 

   - SONET OC-192 IR-2/-3 

   - SDH STM-64.2b/3b 

   - OTN G959.1 P1S1-2D2b 

   - OTN G.709 OTU1e/2/2e FEC bit rates 

   - 10GBASE-ER/EW 

   - 8.5/10G Fibre Channel 

- Cooled 1550nm EML laser 

- Limiting electrical interface receiver 

- Duplex LC connector 

- Built-in digital diagnostic functions 

- RoHS-6 compliant (lead-free) 

**FTLX1672M3BCL** 

## **Product Selection** 

## **FTLX1672M3BCL** 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLX1672M3BCL** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|VEET|Transmitter Ground|1|
|2|TFAULT|Transmitter Fault|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line|2|
|5|SCL|2-wire Serial Interface Clock Line|2|
|6|MOD_ABS|Module Absent. Grounded within the module|2|
|7|RS0|Rate Select 0.|4|
|8|RX_LOS|Loss of Signal indication. Logic 0 indicates normal operation.|5|
|9|RS1|Rate Select 1.|4|
|10|VEER|Receiver Ground|1|
|11|VEER|Receiver Ground|1|
|12|RD-|Receiver Inverted DATA out. AC Coupled.||
|13|RD+|Receiver Non-inverted DATA out. AC Coupled.||
|14|VEER|Receiver Ground|1|
|15|VCCR|Receiver Power Supply|6|
|16|VCCT|Transmitter Power Supply|6|
|17|VEET|Transmitter Ground|1|
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in. AC Coupled.||
|20|VEET|Transmitter Ground|1|



Notes 

1. Circuit ground is internally isolated from chassis ground. 

2. T FAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V. A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Internally pulled down per SFF-8431 Rev 4.1. 

5. LOS is open collector output. Should be pulled up with 4.7k – 10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

6. Internally connected 

## **II. Absolute Maximum Ratings** 

Exceeding the limits below may damage the transceiver module permanently. 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Relative Humidity|RH|0||85|°C|1|
|Receiver Optical Damage Threshold|RxDamage|5|||dBm||



Notes: 

1. Non Condensing 

3 

**FTLX1672M3BCL** 

## **III. Electrical Characteristics (TOP = -5 to 70 °C )** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>Supply Voltage Vcc 3.14 3.30 3.46 V<br>Transmitter<br>Input differential impedance Rin 80 100 120 Ω<br>Differential data input swing Vin,pp 120 850 mV 1<br>Transmit Disable Voltage VD Vcc-0.8 Vcc V<br>Transmit Enable Voltage VEN 0 0.8 V<br>Receiver<br>Output differential impedance Rout 80 100 120 Ω<br>Differential data output swing Vout,pp 300 850 mV 1<br>Output rise time and fall time Tr, Tf 28 ps 2<br>LOS asserted VLOS A Vcc-0.8 Vcc V 3<br>LOS de-asserted VLOS D 0 0.8 V 3<br>Power Supply Noise Tolerance VccT/VccR Per SFF-8431 Rev 4.1 mVpp 4<br>Power Consumption<br>Tx and Rx CDRs ON Pdiss-C 1.6 1.7 W 5<br>Tx and Rx CDRs OFF and Ethernet spec. 1.4 1.5 W 5<br>**----- End of picture text -----**<br>


Notes: 

1. Internally AC coupled. Data pins connect directly to the CDR. 

2. 20 – 80%. Measured with Module Compliance Test Board and OMA test pattern. Use of four 1’s and four 0’s sequence in the PRBS 9 is an acceptable alternative. SFF-8431 Rev 4.1. 

3. LOS is an open collector output. Should be pulled up with 4.7kΩ– 10kΩ on the host board. Normal operation is logic 0; loss of signal is logic 1. 

4. See Section 2.8.3 of SFF-8431 Rev 4.1. 

5. Typical power consumption values refer to 70ΩC, 3.3V and beginning of life. 

4 

**FTLX1672M3BCL** 

## **IV. Optical Characteristics (TOP = -5 to 70 °C, VCC = 3.14 to 3.46 Volts))** 

|Parameter|Parameter|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|---|---|
|Transmitter (Tx)|||||||||
|Output Power|||PAVE|-1||+2|dBm||
|Optical Wavelength|||λC|1530||1565|nm||
|Side-Mode Suppression Ratio|||SMSR|30|||dB||
|Optical Extinction Ratio|||ER|8.2|||dB||
|Average Launch power when Tx is OFF|||POFF|||-30|dBm||
|Jitter Generation 20kHz-80MHz, peak-peak|||Txjpk2pk1|||0.3|UI|1|
|Jitter Generation 4MHz-80MHz, peak-peak|||Txjpk2pj2|||0.1|UI|1|
|Relative Intensity Noise|||RIN|||-128|dB/Hz||
|Receiver (Rx)|||||||||
|Optical Center Wavelength|||λC|1260||1600|nm||
|Receiver Refectance|||Rrx|||-27|dB||
|Sensitivity|8.5, 9.95-10.7 Gb/s||RS_AVE1|||-16|dBm|2,3|
||11.1-11.3 Gb/s||RS_OMA|||-15|dBm|2,3|
|Stressed Sensitivity|10.3G|OMA|RSRS|-1|||dBm|2,3|
|Overload|||ROVL|||2|dB||
|Path Penalty|||PP|||-21|dBm||
|LOS De-Assert|||LOSD|-29|||dBm||
|LOS Assert|||LOSA|0.5|||dB||
|LOS Hysteresis|||LOSH|0.5|||dB||



Notes: 

1. SONET/SDH jitter performance is guaranteed with the internal CDRs enabled and locked 

2. PRBS 2[31] – 1at BER<10[-12] 

3. Measured with worst ER=8.2 dB 

## **V. General Specifications** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Bit Rate|BR|8.5||11.3168|Gb/s|1|
|Max. Supported Link Length|LMAX|||40|km|2|



Notes: 

1. Tested with a 2[31] – 1 PRBS pattern at the BER defined in Table IV. 

2. Over G.652 single mode fiber. 

## **VI. Timing Parameters** 

|Parameter|Symbol|Min|Max|Unit|Ref.|
|---|---|---|---|---|---|
|Time to initialize|t_start_up_cooled||10|s||



5 

**FTLX1672M3BCL** 

## **VII. Environmental Specifications** 

Finisar FTLX1672M3BCL transceivers have the following temperature specifications: 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-5||70|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements  of  EN  (IEC)  60825  and  the  electrical  safety requirements  of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

6 

**FTLX1672M3BCL** 

## **VIII. Digital Diagnostic Functions** 

Finisar FTLX1672M3BCL SFP+ transceivers support the 2-wire serial communication protocol as defined in the SFP MSA[1] . It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar SFP+ transceivers provide a enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in E[2] PROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN- 2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFP MSA documentation[3] and Finisar Application Note AN-20307. 

Please note that evaluation board FDB-1027 is available with Finisar ModDEMO software that allows simple to use communication over the 2-wire serial interface. 

7 

**FTLX1672M3BCL** 

## **IX. Digital Diagnostic Specifications** 

FTLX1672M3BCL transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Min Max Accuracy Units Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Max|Accuracy|Units|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transceiver temperature|ΔDDDDTemp|-5|+75|±5ºC|ºC|1|
|Transceiver supply voltage|ΔDDDDVoltage|2.8|4.0|±3%|V||
|Transmitter bias current|ΔDDDDBias|0|127|±10%|mA|2|
|Transmitter output power|ΔDDDDTx-Power|-2|+3|±2dB|dBm||
|Receiver average optical input power|ΔDDDDRx-Power|-20|+1|±2dB|dBm||



Notes: 

1. Internally measured 

2. The accuracy of the Tx bias current is 10% of the actual current from the laser driver to the laser 

## **X. Internal CDR’s Locking Modes** 

The FTLX1672M3BCL is equipped with internal CDR units on both the receiver and the transmitter sides. The host can set the CDR’s to lock at 8.5Gb/s, 10G (9.95-11.3Gb/s), or in by-pass mode, by setting the rate select pins or the soft bits (logic OR). The different locking modes are shown in the following logic table: 

|R/S 0|R/S 1|CDR’s Locking Mode|
|---|---|---|
|Logic OR of: pin 7 & bit 110.3|Logic OR of: pin 9 & bit 118.3||
|Low or 0|Low or 0|Both CDR’s lock at 8.5Gb/s|
|Low or 0|High or 1|Tx CDR is in bypass mode.<br>Rx CDR locks at 10G (9.95-11.3Gb/s)|
|High or 1|Low or 0|Tx & Rx CDR’s in bypass mode|
|High or 1|High or 1|Both CDR’s lock at 10G (9.95-11.3Gb/s)<br>The bits 110.3 and 118.3 are set to 1 by default at power-up|



The RS0 and RS1 pins are internally pulled-down to ground as per [1]. The soft bits 110.3 and 118.3 are both set to “1” at the transceiver power-up, to select the 10G locking mode by default. The host can change this configuration via the 2-wire communication as described in the SFP MSA [1]. Alternative configurations can be factory set upon request. Please refer to Finisar for additional details. 

## **XI. SFF-8431 Power-up Sequence** 

If either CDR is enabled, the typical power consumption of the FTLX1672M3BCL may exceed the limit of 1.5W specified for the Power Level II transceivers in [1], for which a power-up sequence is recommended. However, the FTLX1672M3BCL is factory set to power-up directly to its operating conditions. Upon request, it can be factory set to follow the power-up sequence specified for transceivers exceeding 1W, as per [1]. In power level I, the FTLX1672M3BCL does not carry traffic, but the 2-wire serial communication is active. 

Please refer to [1] and Finisar Application Note AN-2076 for additional details. 

8 

**FTLX1672M3BCL** 

## **XII. Mechanical Specifications** 

Finisar FTLX1672M3BCL SFP+ transceivers are compatible with the SFF-8432 specification for improved pluggable form factor, and shown here for reference purposes only. Bail color is red. 



Figure 2. Mechanical Dimensions 

Note: the option of the label on the top side of the transceiver is not recommended. 

9 

**FTLX1672M3BCL** 

## **XIII. Host Board SFP+ Connector Recommendations** 


Figure 3. PCB Layout and Bezel Recommendations, as per [9] 

10 

**FTLX1672M3BCL** 



Figure 4. 

11 

**FTLX1672M3BCL** 

## **XIV. Host-Module Interface Diagram** 



**----- Start of picture text -----**<br>
Figure 5<br>**----- End of picture text -----**<br>


12 

**FTLX1672M3BCL** 

## **XV. References** 

1. “Specifications for Enhanced 8.5 and 10 Gigabit Small Form Factor Pluggable Module ‘SFP+ ‘”, SFF Document Number SFF-8431, Revision 4.1, including SFF- 8431 Rev 4.1 Addendum. September 15, 2013. 

2.  “Improved Pluggable Form factor”, SFF Document Number SFF-8432, Revision 4.2, April 18, 2007. 

3. “Digital Diagnostics Monitoring Interface for Optical Transceivers”. SFF Document Number SFF-8472, Revision 10.1, March 1, 2007. 

4. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment” 

5. “Application Note AN-2038: Finisar Implementation of RoHS Compliant Transceivers” 

6. Small Form-factor Pluggable (SFP) Transceiver Multi-Source Agreement (MSA) 

7. “Application Note AN-2030: Digital Diagnostic Monitoring Interface for SFP Optical Transceivers” 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

