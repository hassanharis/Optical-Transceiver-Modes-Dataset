Optical Transceivers 

## FTLX6871MNC, FTLX6872MNC 

## **10Gb/s DWDM 80km Multi-Rate Tunable SFP+ Transceiver E-temp versions** 

FTLX6871MNC andFTLX6872MNC transceivers are Enhanced Small Form Factor Pluggable Tunable SFP+ transceivers designed for use in 10-Gigabit multi-rate links up to 80km of G.652 single mode fiber. They are compliant with SFF-8431[1] , SFF-8432[2] , SFF-86908, and G.698.1 DS100S1-2Dz(C), and support SONET OC-192, SDH STM-64, 10G Ethernet ZR and 10G Fibre Channel over 80km fiber. Digital diagnostics functions are available via a 2-wire serial interface, as specified in SFF84723. The optical transceiver is compliant per the RoHS Directive 2011/65/EU[4] . See Finisar Application Note AN-2038[5] for more details. 


## FEATURES 

## APPLICATIONS 

- Hot-pluggable SFP+ footprint 

- Supports 8.5 and 9.95 to 11.3 Gb/s 

- Up to 80km link length 

- 50GHz ITU-based channel spacing(C-Band) with a wavelength locker 

- -5 /+85°C case temperature range 

- Single 3.3V power supply 

   - DWDM 80km point to point links: 

   - 8G Fibre Channel 

   - 10Gb/s SONET/SDH 

   - 10G Ethernet 

   - 10G Fibre Channel 

   - ITU-T G.698.1 DS100S1-2Dz(C) 

   - ITU-T G.709 

- Monolithic MZM Tunable TOSA 

- Linear or Limiting electrical interfacereceiver 

- Duplex LC connector 

- Built-in digital diagnostic functions 

- RoHS-6 compliant (lead-free) 

**FTLX6871MNC, FTLX6872MNC** 

## **Product Selection** 

## **FTLX6871MNC, FTLX6872MNC** 

Product Part Number RX Interface FTLX6871MNC Linear FTLX6872MNC Limiting 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLX6871MNC, FTLX6872MNC** 


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
|7|NA|Not Used||
|8|RX_LOS|Loss of Signal indication. Logic 0 indicates normal operation.|4|
|9|NA|No Used||
|10|VEER|Receiver Ground|1|
|11|VEER|Receiver Ground|1|
|12|RD-|Receiver Inverted DATA out. AC Coupled.||
|13|RD+|Receiver Non-inverted DATA out. AC Coupled.||
|14|VEER|Receiver Ground|1|
|15|VCCR|Receiver Power Supply|5|
|16|VCCT|Transmitter Power Supply|5|
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

3 

**FTLX6871MNC, FTLX6872MNC** 

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

## **III. Electrical Characteristics (TOP = -5 to 70 °C )** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>Supply Voltage Vcc 3.14 3.46<br>Supply Current Icc 800 mA 1<br>Module total power dissipation P 2.5 W 2<br>Transmitter<br>Input differential impedance Rin 80 100 120 Ω<br>Differential data input swing Vin,pp 200 850 mV 3<br>Transmit Disable Voltage VD Vcc-0.8 Vcc V<br>Transmit Enable Voltage VEN Vee Vee+ 0.8 V<br>Receiver<br>Output differential impedance Rout 80 100 120 Ω<br>Differential data output swing Vout,pp 150 850 mV 4<br>Output rise time and fall time Tr, Tf 28 ps 4,5<br>LOS asserted VLOS A Vcc-0.8 Vcc V<br>LOS de-asserted VLOS D Vee Vee+0.8 V<br>Power Supply Noise Tolerance VccT/VccR Per SFF-8431 Rev 4.1 mVpp<br>Power Consumption<br>Tx and Rx CDR’s ON Pdiss 1.8 1.9 W 5<br>Tx CDR OFF and Rx CDR ON 1.7 1.8 W 5<br>Tx & Rx CDR’s OFF and Ethernet spec. 1.6 1.7 W 5<br>**----- End of picture text -----**<br>


Notes: 

1. Internally AC coupled. Data pins connect directly to the CDR. 

2. 20 – 80%. Measured with Module Compliance Test Board and OMA test pattern. Use of four 1’s and four 0’s sequence in the PRBS 9 is an acceptable alternative. SFF-8431 Rev 4.1. 

3. LOS is an open collector output. Should be pulled up with 4.7kΩ – 10kΩ on the host board. Normal operation is logic 0; loss of signal is logic 1. 

4. See Section 2.8.3 of SFF-8431 Rev 4.1. 

5. Typical power consumption at 70ΩC case temperature, beginning of life and 3.3V supply voltage. 

4 

**FTLX6871MNC, FTLX6872MNC** 

## **IV. Optical Characteristics (TOP = -5 to 85 °C, VCC = 3.14 to 3.46 Volts))** 

|Parameter|Parameter|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|---|---|
|Transmitter (Tx)|||||||||
|Average Launch Power|||PAVE|-1||+3|dBm||
|Optical Wavelength|||λC|As per ITU-T 694.1, 50GHz spacing 1528.77<br>to 1563.86|||nm||
|Side-Mode Suppression Ratio|||SMSR|30|||dB||
|Optical Extinction Ratio|||ER|8.2|||dB||
|Average Launch power when Tx is OFF|||POFF|||-30|dBm||
|Tx Jitter 20kHz - 80MHz|||Txj1|||0.3|UI||
|Tx Jitter 4MHz - 80MHz|||Txj2|||0.1|UI||
|Relative Intensity Noise|||RIN|||-128|dB/Hz||
|Center Wavelength|Beginning of Life||λC BOL|z-1.5|z|z+1.5|Pm||
||End of Life||λC EOL|z-2.5|z|z+2.5|Pm||
|Receiver (Rx)|||||||||
|Bit rate||BER|||||||
|8.5, 9.95||<1E-12|RSENS1|||-24.0|dBm|1, 2|
|10.7 Gb/s||<1E-12|RSENS2|||-23.0|dBm|1, 2|
|11.1 Gb/s||<1E-4|RSENS3|||-27.0|dBm||
|11.3 Gb/s||<1E-4|RSENS4|||-27.0|dBm||
|Overload (Average Power)|||PAVE|||-7|dBm||
|Optical Center Wavelength|||λC|1260||1600|dBm||
|LOS De-Assert|||LOSD|||-25|dBm||
|LOS Assert|||LOSA|-34||-27|dB||
|LOS Hysteresis|||LOSH|0.5|||||
|Receiver Refectance|||Rrx|||-27|||



5 

**FTLX6871MNC, FTLX6872MNC** 

|||||||
|---|---|---|---|---|---|
|FTLX6871/72MNC||||||
|Receiver Sensitivity3||||||
|Data rate (Gb/s)|BER|Dispersion (ps/nm)|Sensitivity back-to-<br>back at OSNR>30dB<br>(dBm)|Dispersion Penalty at<br>OSNR>30dB (dB)|Threshold Adjust<br>Required|
|9.95|1e-12|-300 to 1450|-24|2|No5|
|10.3|1e-12|-300 to 1450|-23|2.5|No5|
|10.7|1e-4|-300 to 1300|-27|3|Yes6|
|11.1|1e-4|-300 to 1300|-27|3|Yes6|
|11.3|1e-4|-300 to 1300|-27|3.5|Yes6|
|OSNR Performance4||||||
|Data rate (Gb/s)|BER|Dispersion (ps/nm)|Min OSNR Back- to-<br>back at Power:<br>-18dBm to -7dBm (dB)|Max OSNR<br>Penalty at Power:<br>-18 to -7dBm (dB)|Threshold Adjust<br>Required|
|9.95|1e-12|-300 to 1450|24|4|Yes6|
|10.3|1e-12|-300 to 1450|24|4|Yes6|
|10.7|1e-4|-300 to 1300|16|4|Yes6|
|11.1|1e-4|-300 to 1300|16|4|Yes6|
|11.3|1e-4|-300 to 1300|17|4|Yes6|



Notes: 

1. Measured with worst ER=8.2dB; BER<10[-12] ; 2[31] – 1 PRBS. 

2. For 10GEthernet application, -24dBm is equivalent to an OMA of -22.09dBm for an ER = 8.2 dB. 

3. Measured at 1528-1600nm with worst ER; PRBS31. 

4. All OSNR measurements are performed with 0.1nm resolution. 

5. Linecard SerDes input threshold adjustment required (set to 50%) at 9.95 and 10.3Gb for AGC ROSA only 

6. Linecard SerDes input threshold adjustment required for AGC ROSA. RxDTV control required for Limiting ROSA 

6 

**FTLX6871MNC, FTLX6872MNC** 

## **V. General Specifications** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Bit Rate|BR|8.5||11.3168|Gb/s|1|
|Max. Supported Link Length|LMAX|||80|km|2|



Notes: 

1. Tested with a 2[31] – 1 PRBS pattern at the BER defined in Table IV. 

2. Over G.652 single mode fiber. 

## **Timing Parameters** 

|Parameter|Symbol|Min|Max|Unit|Ref.|
|---|---|---|---|---|---|
|Time to initialize cooled module|t_start_up_cooled||90|s||



## **VI. Environmental Specifications** 

Finisar FTLX6871/72MNC transceivers have an operating temperature range from -5°C to +85°C case temperature. 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-5||85|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements  of  EN  (IEC)  60825  and  the  electrical  safety  requirements  of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

7 

**FTLX6871MNC, FTLX6872MNC** 

## **VIII. Digital Diagnostic Functions** 

Finisar FTLX6871/72MNC Tunable SFP+ transceivers support the 2-wire serial communication protocol as defined in the SFP MSA[1] . It is very closely related to the memory map defined in the GBIC standard, with the same electrical specifications. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar T-SFP+ transceivers provide a enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The  SFP  MSA  defines  a  256-byte  memory  map  that  is  accessible  over  a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

8 

**FTLX6871MNC, FTLX6872MNC** 

## **IX. Digital Diagnostic Specifications** 

FTLX6871/72MNC transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Min Max Accuracy Units Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Max|Accuracy|Units|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transceiver temperature|ΔDDDDTemp|-10|+90|±5ºC|ºC|1|
|Transceiver supply voltage|ΔDDDDVoltage|2.8|4.0|±3%|V||
|Transmitter bias current|ΔDDDDBias|0|127|±10%|mA|2|
|Transmitter output power|ΔDDDDTx-Power|-1|+5|±2dB|dBm||
|Receiver average optical input power|ΔDDDDRx-Power|-28|-5|±2dB|dBm||



Notes: 

1. Internally measured 

2. The accuracy of the Tx bias current is 10% of the actual current from the laser driver to the laser 

## **X. Start-Up Sequence** 

The FTLX6871/72MNC modules adhere to MSA SFF-8690 for wavelength / channel selection of these tunable modules. The module behavior is described in the flowchart below: 


9 

**FTLX6871MNC, FTLX6872MNC** 

## **Alarm and Warning Threshold Values (A2h)** 


**----- Start of picture text -----**<br>
Address Parameter Threshold Values UNITS<br>**----- End of picture text -----**<br>


|Address|Parameter|Threshold Values|UNITS|
|---|---|---|---|
|||||
|00-01|Temp High Alarm|90|C|
|02-03|Temp Low Alarm|‐15|C|
|04-05|Temp High Warning|88|C|
|06-07|Temp Low Warning|‐10|C|
|08-09|Voltage High Alarm|3.56|V|
|10-11|Voltage Low Alarm|3.04|V|
|12-13|Voltage High Warning|3.46|V|
|14-15|Voltage Low Warning|3.14|V|
|16-17|Bias High Alarm|130|mA|
|18-19|Bias Low Alarm|5|mA|
|20-21|Bias High Warning|120|mA|
|22-23|Bias Low Warning|10|mA|
|24-25|TX Power High Alarm|6.5|dBm|
|26-27|TX Power Low Alarm|‐3|dBm|
|28-29|TX Power High Warning|6|dBm|
|30-31|TX Power Low Warning|‐1.5|dBm|
|32-33|RX Power High Alarm|‐4|dBm|
|34-35|RX Power Low Alarm|‐31|dBm|
|36-37|RX Power High Warning|‐5|dBm|
|38-39|RX Power Low Warning|‐25|dBm|
|40-55|Reserved|||



## **XI. The FTLX6871/72MNC modules do not contain Internal CDRs.** 

## **XII. SFF-8431 Power-up Sequence** 

The typical power consumption of the FTLX6871/72MNC exceeds the limit of 1.5W specified in the SFF-8431 for the Power Level II device, for which the SFF-8431 recommends a power-up sequence. Per the SFF-8431, at the power-on a Power Level II transceiver can stay in Power Level I until the host enables the transceiver to complete its power-up sequence, reaching its operating power consumption into Power Level Mode II. Please, refer to SFF-8431 and Finisar Application Note AN-20767 for additional details. The FTLX6871/72MNC is factory set to power-up directly to its operating conditions in Power Level Mode II. Upon request, it can be factory set to follow the above power-up sequence at the power-on. In power level I, the FTLX6871/72MNC does not carry traffic, but the 2-wire serial communication is active. 

10 

**FTLX6871MNC, FTLX6872MNC** 

## **XIII. Mechanical Specifications** 

Finisar FTLX6871/72MNC SFP+ transceivers are compatible with the SFF-8432 specification for improved pluggable form factor, and shown here for reference purposes only. Bail color is green. 



Figure 2. Mechanical Dimensions Connector Recommendations 

## **Product Label and Box Label** 

These are “subject to change without notice” and being used as a guideline for the format. 



11 

**FTLX6871MNC, FTLX6872MNC** 

## **XIV. PCB Layout and Bezel Recommendations** 


Figure 3. PCB Layout and Bezel Recommendations, as per [9] 

12 

**FTLX6871MNC, FTLX6872MNC** 



Figure 4. 

13 

**FTLX6871MNC, FTLX6872MNC** 

## **XV. Host-Module Interface Diagram** 

To Be Provided in future release. Figure 5 

## **XVI. References** 

1. “Specifications for Enhanced 8.5 and 10 Gigabit Small Form Factor Pluggable Module ‘SFP+ ‘”, SFF Document Number SFF-8431, Revision 4.1 (or later). 

2. “Improved Pluggable Form factor”, SFF Document Number SFF-8432, Revision 4.2, April 18, 2007 (or later). 

3. “Digital Diagnostics Monitoring Interface for Optical Transceivers”. SFF Document Number SFF-8472, Revision 11.3, (or later). 

4. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment” 

5. “Application Note AN-2038: Finisar Implementation of RoHS Compliant Transceivers”, Finisar Corporation, January 21, 2005. 

6. Small Form-factor Pluggable (SFP) Transceiver Multi-Source Agreement (MSA) 

7. “Application Note AN-2076: SFP+ Level II Power Up Sequence”, Rev B 

8. Tunable SFP+ MSA; SFF-8690 

## **XVII. Revision History** 

|Revision|Date|Description|
|---|---|---|
|A00|8/18/2015|Initial Release|
|A01|12/08/2015|Change the product image on page 1.<br>Add product and box label samples on mechanical Specifcations section.|
|A02|March 2017|Corrected Max current to support 2.5W total power consumption of module.|
|A03|April 2017|Corrected RoHS statements to reference 2011 directive|



© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

