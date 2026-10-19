Optical Transceivers 

## FTLF1432P3BCE 

## **32GFC RoHS Compliant Long Wavelength SFP+ Transceiver** 

FTLF1432P3BCE SFP+ transceivers are designed for use in Fibre Channel links up to 28.05 Gb/s data rate and up to 25km link length. They are compliant with SFF-8472 Rev 12.1c, and compatible with SFF-8432band applicable portions of SFF_ x005F_xFFFE_8431 Rev. 4.1d. The optical transceiver is compliant per RoHS Directive 2011/65/EUe.See Finisar Application Note AN-2038 for more details. 


## FEATURES 

## APPLICATIONS 

- Up to 28.05 Gb/s bi-directionaldata links 

   - Tri-Rate 8.5/14.025/28.05 Gb/sFibre Channel 

- Hot-pluggable SFP+ footprint 

- Built-in digital diagnostic functions 

- 1310nm DFB laser transmitter 

- Duplex LC connector 

- RoHS compliant 

- Up to 25 km on 9/125μm SMF 

- Metal enclosure, for lower EMI 

- 1.5W maximum power consumptionwith established link 

- Single 3.3V power supply 

- Operating temperature range:0°C to 70°C 

**FTLF1432P3BCE** 

## **Product Selection** 

## **FTLF1432P3BCE** 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLF1432P3BCE** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line (MOD-DEF2)|4|
|5|SCA|2-wire Serial Interface Clock (MOD-DEF1)|4|
|6|MOD_ABS|Module Absent, connected to VEETor VEER|4|
|7|RS0|Rx Rate Select:<br>Open or Low =<br>8.5 or 14.025 Gb/s Fibre Channel (Low Bandwidth)<br>High =<br>28.05 Gb/s Fibre Channel (High Bandwidth)|5|
|8|LOS|Loss of Signal indication. Logic 0 indicates normal operation.|6|
|9|RS1|Tx Rate Select:<br>Open or Low =<br>8.5 or 14.025 Gb/s Fibre Channel (Low Bandwidth)<br>High =<br>28.05 Gb/s Fibre Channel (High Bandwidth)|5|
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

2. TFAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V. A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. MOD_ABS pulls line low to indicate module is plugged in. 5. Rate select can also be set through the 2-wire bus in accordance with SFF-8472 v. 10.2. Rx Rate Select is set at Bit 3, Byte 110, Address A2h. Tx Rate Select is set at Bit 3, Byte 118, Address A2h. Note: writing a “1” selects maximum bandwidth operation. Rate select is the logic OR of the input state of Rate Select Pin and 2-wire bus. 

6. LOS is open collector output. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

3 

**FTLF1432P3BCE** 

## **II. Absolute Maximum Ratings** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Case Operating Temperature|TOP|-40||85|°C||
|Relative Humidity (Non-condensing)|RH|0||85|%|1|



Notes: 

1. Non Condensing 

## **III. Electrical Characteristics (TA ,  VCC = 3.15 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.15||3.46|V||
|Supply Current|Icc|||440|mA|1|
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|2|
|Single-ended data input swing<br>28.05Gb/s<br>14.025Gb/s & 8.5Gb/s|Vin,pp|250<br>180||900<br>700|mV|2|
|Inner Eye Height|EH6|50|||mV|3|
|Transmit Disable Voltage|VD|2||Vcc|V|4|
|Transmit Enable Voltage|VEN|Vee||Vee+0.8|V||
|Receiver|||||||
|Single ended data output swing|Vout,pp|185||425|mV|5|
|LOS Fault|VLOS fault|2||VccHOST|V|6|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|6|
|Power Supply Rejection|PSR|100|||mVpp|7|



Notes: 

1. With established link, the total power dissipation shall not exceed 1.3W. 

2. Connected directly to TX data input pins. AC coupling from pins into CDR, BER contour 10[-6] , per FC-PI 6 and FC-MSQS-2. 

3. Inner eye height (EH6) for high loss case 

4. Or open circuit. 

5. Into 100 ohms differential termination. 

6. LOS is an open collector output. Should be pulled up with 4.7k – 10kohms on the host board. Normal operation is logic 0; loss of signal is logic 1. Maximum pull-up voltage is 5.5V. 

7. Receiver sensitivity is compliant with power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specified value applied through the recommended power supply filtering network. 

4 

**FTLF1432P3BCE** 

## **IV. Optical Characteristics (TA , VCC = 3.15 to 3.46 Volts)** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>Transmitter<br>Average Output Power POUT +2.5 +7.0 dBm 1, 2<br>Optical Wavelength λ 1295 1310 nm 3<br>Spectral Width (-20dB) δ 1 nm 4<br>Side Mode Suppression Ratio 30 dB<br>Optical Modulation Amplitude OMA 3 7 dBm 5<br>Transmitter Dispersion Penalty @ TDP<br>8.5 Gb/s 3.2 dB<br>14.025Gb/s 4.4<br>28.05Gb/s 2.7<br>Extinction Ratio ER 4 dB<br>Relative Intensity Noise RIN -130 dB/Hz<br>Receiver<br>Unstressed Receiver OMA Sensitivity RxSENS dBm 3<br>8.5 Gb/s -14.1<br>14.025Gb/s -13.1<br>28.05Gb/s -12.9<br>Receiver Optical Modulation Amplitude RxMAX 2 dBm 4<br>Stress Receiver Sensitivity -9.5 dBm<br>Optical Return Loss dB<br>8.5Gb/s & 14.025Gb/s 12<br>28.05Gb/s 26<br>LOS De-Assert LOSD -17 dBm<br>LOS Assert LOSA -30 dBm<br>LOS Hysteresis 0.5 dB<br>Link Parameters<br>Channel IL 5 13.2 dB<br>Allocation of Penalties 2.7 dB<br>Total Power Budget (Maximum TDP) 15.9 dB<br>**----- End of picture text -----**<br>


Notes: 

1. Class 1 Laser Safety limit per FDA/CDRH, and EN (IEC) 60825 laser safety standards. 

2. 3200-SM-LC-L OMA in dBm shall also exceed -5.0 TDP. 

3. For 32GFC with FEC, receiver sensitivity is defined at 10-6 BER level, not 10-12 BER level. 

4. This transceiver is targeted for long reach application with high power transmitter. Thus, for optical loopback testing please ensure ~6dB optical attenuator is included. 

5 

**FTLF1432P3BCE** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Data Rate|BR||8.5<br>14.025<br>28.05||Gb/sec|1|
|Bit Error Rate|BER|||10-12<br>10-6||2<br>3|
|Fiber Length|L|||25|km|2|



Notes: 

1. 8x, 16x and 32x Fibre Channel compatible, per FC-PI-5[a] ., FC-PI-6[a] respectively 

2. PRBS 2[7] -1 for 8GFC. PRBS 2[31] -1 for 16GFC 

3. FEC for 32GFC 

## **VI. Environmental Specifications** 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|0||70|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements of  EN  (IEC)  60825  and  the  electrical  safety  requirements  of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

6 

**FTLF1432P3BCE** 

## **VIII. Digital Diagnostic Functions** 

Finisar FTLF1432P3BCE SFP+ transceivers support the 2-wire serial communication protocol as defined in the SFP MSA[f] . It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar SFP transceivers provide a enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in E[2] PROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN-2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFP MSA documentationc,f and Finisar Application Note AN- 2030. 

7 

**FTLF1432P3BCE** 

## **IX. Digital Diagnostic Specifications** 

FTLF1432P3BCE transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Units Min Max Accuracy Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Units|Min|Max|Accuracy|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transceiver temperature|DDDTemp|ºC|0|+70|±5ºC||
|Transceiver supply voltage|DDDVoltage|V|3.14|3.45|±3%||
|Transmitter bias current|DDDBias|mA|0|72|±10%|1|
|Transmitter output power|DDDTx-Power|dBm|2|+7|±3dB||
|Receiver average optical input power|DDDRx-Power|dBm|-12|2|±3dB||



Notes: 

1. Accuracy of Measured Tx Bias Current is 10% of the actual Bias Current from the laser driver to the laser. 

8 

**FTLF1432P3BCE** 

## **X. Mechanical Specifications** 

Finisar’s FTLF1432P3BCE SFP+ transceivers are compatible with the SFF-8432[b] specification for improved pluggable form factor. 



**----- Start of picture text -----**<br>
FTLF1432P3BCE<br>**----- End of picture text -----**<br>


9 

**FTLF1432P3BCE** 

## **XI. PCB Layout and Bezel Recommendations** 


10 

**FTLF1432P3BCE** 



11 

**FTLF1432P3BCE** 

## **XII. References** 

1. “Fibre Channel – Physical Interfaces -5, INCITS 479-2011 (Defines 8GFC and 16GFC) Fibre Channel – Physical Interfaces -6, INCITS 512-2014 (Defines 32GFC)” 

2. “Improved Pluggable Form Factor”, SFF Document Number SFF-8432, Revision 5.0, July 16, 2007. 

3. “Digital Monitoring Interface for Optical Transceivers”, SFF Document Number SFF-8472, Revision 12.1. 

4. “Enhanced Small Form Factor Pluggable Module ‘SFP+ ‘”, SFF Document Number SFF-8431, Revision 4.1, July 6, 2009; Addendum Jun 21, 2013. 

5. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. 08-June 2011, which supercedes the previous ROHS Directive 2002/95/EC. 

6. Small Form Factor Pluggable (SFP) Transceiver Multi-source Agreement (MSA), September 14, 2000 which is available as SFF Document Number INF-8074, Revision 1.0 May 12, 2001 

7. “0.8mm Card Edge Connector for 16Gb/s Applications”, SFF Document Number SFF-8081, Revision 0.2, December 21, 2009. 

8. SFF-8402, Revision 0.2 

© 2023 Coherent Corp. photonics.sales@coherent.com Legal notices : coherent.com/legal www.coherent.com 

