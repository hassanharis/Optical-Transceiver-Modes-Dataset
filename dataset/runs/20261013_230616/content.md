Optical Transceivers 

## FTLF8532P4BNV 

## **32GFC RoHS Compliant Short Wavelength SFP+ Transceiver** 

FTLF8532P4BNV SFP+ transceivers are designed for use in Fibre Channel links up to 28.05 Gb/s data rate over multimode fiber. They are compliant with FC-PI-6a, SFF-8472 Rev 12.2c, and compatible with SFF-8432b and applicable portions of SFF_x005F_xFFFE_8431 Rev. 4.1d. The transceiver is RoHS compliant and per Directive 2011/65/EUe . See Finisar Application Note AN-2038 for more details. 


## FEATURES 

## APPLICATIONS 

- Up to 28.05 Gb/s bi-directional data links 

   - Tri-Rate 8.5/14.025/28.05 Gb/s Fibre Channel 

- Hot-pluggable SFP+ footprint 

- Built-in digital diagnostic functions 

- 850nm Oxide VCSEL laser transmitter 

- Duplex LC connector 

- RoHS compliant 

- 100m over M5F MMF (50/125 um OM4) 

- 70m over M5E MMF (50/125um OM3) 

- 20m on 50μm (OM2) MMF 

- Metal enclosure, for lower EMI 

- Single 3.3V power supply 

- Operating temperature range: 0°C to 85°C 

**FTLF8532P4BNV** 

## **Product Selection** 

## **FTLF8532P4BNV** 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLF8532P4BNV** 


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

**FTLF8532P4BNV** 

## **II. Absolute Maximum Ratings** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Case Operating Temperature|TOP|0||70|°C||
|Relative Humidity (Non-condensing)|RH|0||85|%|1|



Notes: 

1. Non Condensing 

## **III. Electrical Characteristics (TA ,  VCC = 3.15 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.15||3.46|V||
|Supply Current|Icc|||290|mA|1|
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|2|
|Single-ended data input swing<br>28.05Gb/s<br>14.025Gb/s & 8.5Gb/s|Vin,pp|50<br>180||900<br>700|mV|2|
|Transmit Disable Voltage|VD|2||Vcc|V|3|
|Transmit Enable Voltage|VEN|Vee||Vee+0.8|V||
|Receiver|||||||
|Single ended data output swing|Vout,pp|185||425|mV|4|
|LOS Fault|VLOS fault|2||VccHOST|V|5|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|5|
|Power Supply Rejection|PSR|100|||mVpp|6|



Notes: 

1. With established link. The total power dissipation could exceed 1W when the module is trying to establish link at operating case temperature below 25oC 

2. Connected directly to TX data input pins. AC coupling from pins into CDR, Inner eye height (EH6) for high loss case , BER contour 10[-6] , per FC-PI 6 and FC-MSQS-2. 

3. Or open circuit. 

4. Into 100 ohms differential termination. 

5. LOS is an open collector output. Should be pulled up with 4.7k – 10kohms on the host board. Normal operation is logic 0; loss of signal is logic 1. Maximum pull-up voltage is 5.5V. 

6. Receiver sensitivity is compliant with power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specified value applied through the recommended power supply filtering network. 

4 

**FTLF8532P4BNV** 

## **IV. Optical Characteristics (TA , VCC = 3.15 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Avergare Output Power: 50 or 62.5 MMF<br>8.5Gb/s<br>14.025Gb/s<br>28.05Gb/s|POUT|-8.2<br>-7.8<br>-6.7|||dBm|1|
|Optical Wavelength|λ|840||860|nm||
|Spectral Width (RMS), 28.05Gb/s|δ|||0.57|nm||
|Optical Modulation Amplitude<br>8.5 Gb/s<br>14.025Gb/s<br>28.05Gb/s|OMA|302 (-5.2)<br>331 (-4.8)<br>479 (-3.2)|||µW(dBm)||
|Transmitter Waveform and Dispersion Penalty,<br>8.5 Gb/s|TWDP|||4.3|dB|2|
|Vertical Eye Closure Penalty<br>14.025 Gb/s<br>28.05 Gb/s|CEVPQ|||2.56<br>3.13|dB|3,4|
|Relative Intensity Noise<br>28.05Gb/s<br>14.025Gb/s & 8.5Gb/s|RIN|||-129<br>-128|dB/Hz||
|Receiver|||||||
|Unstressed Receiver OMA Sensitivity<br>8.5 Gb/s<br>14.025Gb/s<br>28.05Gb/s|RxSENS|||76(-11.2)<br>89(-10.5)<br>95(-10.2)|µW(dBm)|5, 6|
|Receiver Optical Modulation Amplitude|RxMAX|||2|dBm||
|Stress Receiver Sensitivity|λC|770||860|nm||
|Optical Return Loss||12|||dB||
|LOS De-Assert|LOSD|||-13|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|||dB||



Notes: 

1. Class 1 Laser Safety limit per FDA/CDRH, and EN (IEC) 60825 laser safety standards. 

2. TWDP is calculated with a 1,0 equalizer and a 9.84 GHz Gaussian filter for the fiber simulation. Jitter values at γ T and γ R are controlled by TWDP and stress receiver sensitivity. 

3. For 16GFC, VECPQ is calculated with a 16.6 GHz Gaussian filter for fiber simulation 

4. For 32GC, VECPQ is calculated with a 24.7GHz Gaussian filter for fiber simulation 

5. Unstressed Rx sensitivity 

6. For 32GFC with FEC, receiver sensitivity is defined at 10[-6] BER level, not 10[-12] BER level. 

5 

**FTLF8532P4BNV** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Data Rate|BR||8.5<br>14.025<br>28.05||Gb/sec|1|
|Bit Error Rate|BER|||10-12<br>10-6||2<br>3|
|Fiber Length on 50/125 µm<br>(OM2/M5) MMF|L|||50<br>35<br>20|m|4<br>5<br>6|
|Fiber Length on 50/125µm high-<br>bandwidth (OM3/M5E) MMF|L|||150<br>100<br>70|m|4<br>5<br>6|
|Fiber Length on 50/125 µm high-<br>bandwidth (OM4/M5F) MMF|L|||190<br>125<br>100|m|4<br>5<br>6|



Notes: 

1. 8x Fibre Channel compatible, per FC-PI-4[1] . 

2. PRBS 2[7] -1 for 8GFC. PRBS 2[31] -1 for 16GFC 

3. FEC for 32GFC 

4. At 8.5 Gb/s Fibre Channel data rate. 

5. At 14.025 Gb/s Fibre Channel data rate. 

6. At 28.05Gb/s Fibre Channel data rate 

## **VI. Environmental Specifications** 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|0||70|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements of  EN  (IEC)  60825  and  the  electrical  safety  requirements  of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

6 

**FTLF8532P4BNV** 

## **VIII. Digital Diagnostic Functions** 

Finisar FTLF8532P4BNV SFP+ transceivers support the 2-wire serial communication protocol as defined in the SFP MSA[f] . It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar SFP transceivers provide a enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in E[2] PROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN-2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFP MSA documentation[c,f] and Finisar Application Note AN- 2030. 

7 

**FTLF8532P4BNV** 

## **IX. Digital Diagnostic Specifications** 

FTLF8532P4BCV transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Units Min Max Accuracy Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Units|Min|Max|Accuracy|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transceiver temperature|DDDTemp|ºC|0|+70|±5ºC||
|Transceiver supply voltage|DDDVoltage|V|3.14|3.45|±3%||
|Transmitter bias current|DDDBias|mA|0|50|±10%|1|
|Transmitter output power|DDDTx-Power|dBm|-9|+2|±3dB||
|Receiver average optical input power|DDDRx-Power|dBm|-12|2|±3dB||



Notes: 

1. Accuracy of Measured Tx Bias Current is 10% of the actual Bias Current from the laser driver to the laser. 

8 

**FTLF8532P4BNV** 

## **X. Mechanical Specifications** 

Finisar’s FTLF8532P4BNV SFP+ transceivers are compatible with the SFF-8432[b] specification for improved pluggable form factor. 


FTLF8532P4BNV 

9 

**FTLF8532P4BNV** 

## **XI. PCB Layout and Bezel Recommendations** 


10 

**FTLF8532P4BNV** 



11 

**FTLF8532P4BNV** 

## **XII. References** 

1. “Fibre Channel – Physical Interfaces -5, INCITS 479-2011 (Defines 8GFC and 16GFC) Fibre Channel – Physical Interfaces -6, INCITS 512-2014 (Defines 32GFC)” 

2. “Improved Pluggable Form Factor”, SFF Document Number SFF-8432, Revision 5.0, July 16, 2007. 

3. “Digital Monitoring Interface for Optical Transceivers”, SFF Document Number SFF-8472, Revision 12.2. 

4. “Enhanced Small Form Factor Pluggable Module ‘SFP+ ‘”, SFF Document Number SFF-8431, Revision 4.1, July 6, 2009; Addendum Jun 21, 2013. 

5. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. 08-June 2011, which supercedes the previous ROHS Directive 2002/95/EC. 

6. Small Form Factor Pluggable (SFP) Transceiver Multi-source Agreement (MSA), September 14, 2000 which is available as SFF Document Number INF-8074, Revision 1.0 May 12, 2001 

7. “0.8mm Card Edge Connector for 16Gb/s Applications”, SFF Document Number SFF-8081, Revision 0.2, December 21, 2009. 

8. SFF-8402, Revision 0.2 

© 2023 Coherent Corp. photonics.sales@coherent.com Legal notices : coherent.com/legal www.coherent.com 

