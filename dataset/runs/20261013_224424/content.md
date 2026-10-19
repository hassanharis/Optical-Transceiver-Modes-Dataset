Optical Transceivers 

## FTL4E1QE1C 

## **40GBASE QSFP+ Optical Transceiver Module – 40km** 

FTL4E1QE1C QSFP+ transceiver modules are designed for use in 40 Gigabit Ethernet links over single mode fiber. They are compliant with the QSFP+ MSA[1] and IEEE 802.3bm 40GBASE-ER42. Digital diagnostics functions are available via an I2C interface, as specified by the QSFP+ MSA. The optical transceiver is compliant per the RoHS Directive 2011/65/EU[5] . See Finisar Application Note AN-2038 for more details[4] . 


## FEATURES 

## APPLICATIONS 

- Hot-pluggable QSFP+ form factor 

   - 40GBASE-ER4 40G Ethernet 

- Supports 41.3 Gb/s aggregate bit rate 

- Power dissipation < 3.5W 

- 18.5 dB link insertion loss budget 

- RoHS-6 compliant 

- Commercial case temperature range 0°C to 70°C 

- Single 3.3V power supply 

- Maximum link length of 40km on Single Mode Fiber (SMF) 

- Uncooled 4x10Gb/s CWDM transmitter 

- XLPPI electrical interface 

- Duplex LC receptacles 

- Built-in digital diagnostic functions, including Tx/Rx power monitoring1 

**FTL4E1QE1C** 

## **Product Selection** 

## **FTL4E1QE1C** 

- E: Ethernet support 1: First generation product C: Commercial temperature range 

## **I. Pin Descriptions** 


Figure 1 – QSFP+ MSA-compliant 38-pin connector 

2 

**FTL4E1QE1C** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|GND|Ground|1|
|2|Tx2n|Transmitter Inverted Data Input||
|3|Tx2p|Transmitter Non-Inverted Data Input||
|4|GND|Ground|1|
|5|Tx4n|Transmitter Inverted Data Input||
|6|Tx4p|Transmitter Non-Inverted Data Input||
|7|GND|Ground|1|
|8|ModSelL|Module Select||
|9|ResetL|Module Reset||
|10|Vcc Rx|+3.3 V Power supplyreceiver||
|11|SCL|2-wire serial interface clock||
|12|SDA|2-wire serial interface data||
|13|GND|Ground|1|
|14|Rx3p|Receiver Non-Inverted Data Output||
|15|Rx3n|Receiver Inverted Data Output||
|16|GND|Ground|1|
|17|Rx1p|Receiver Non-Inverted Data Output||
|18|Rx1n|Receiver Inverted Data Output||
|19|GND|Ground|1|
|20|GND|Ground|1|
|21|Rx2n|Receiver Inverted Data Output||
|22|Rx2p|Receiver Non-Inverted Data Output||
|23|GND|Ground|1|
|24|Rx4n|Receiver Inverted Data Output||
|25|Rx4p|Receiver Non-Inverted Data Output||
|26|GND|Ground|1|
|27|ModPrsL|Module Present||
|28|IntL|Interrupt||
|29|Vcc Tx|+3.3 V Power supplytransmitter||
|30|Vcc1|+3.3 V Power Supply||
|31|LPMode|Low Power Mode||
|32|GND|Ground|1|
|33|Tx3p|Transmitter Non-Inverted Data Input||
|34|Tx3n|Transmitter Inverted Data Input||
|35|GND|Ground|1|
|36|Tx1p|Transmitter Non-Inverted Data Input||
|37|Tx1n|Transmitter Inverted Data Input||
|38|GND|Ground|1|



Notes 

1. Circuit ground is internally isolated from chassis ground. 

3 

**FTL4E1QE1C** 

## **II. General Product Characteristics** 


**----- Start of picture text -----**<br>
Parameter Value Unit Notes<br>**----- End of picture text -----**<br>


|Parameter|Value|Unit|Notes|
|---|---|---|---|
|||||
|Module Form Factor|QSFP+|||
|Maximum Aggregate Data<br>Rate|41.2500|Gb/s||
|Maximum Data Rateper Lane|10.3125|Gb/s||
|Protocols Supported|40G Ethernet|||
|Electrical Interface and Pin-out|38-pin edge connector|||
|Maximum Power Consump-<br>tion|38-pin edge connector||Pin-out as defned by the QSFP+ MSA|
|Management Interface|3.5|Watts||
|Management Interface|Serial, I2C-based, 400 kHz<br>maximum frequency||As defned by the QSFP+ MSA|




**----- Start of picture text -----**<br>
Data Rate Specifications Symbol  Min  Typ Max  Units  Ref.<br>**----- End of picture text -----**<br>


|Data Rate Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Bit Rate per Lane|BR||10.3125||Mb/sec|1|
|Bit Error Ratio|BER|||10-12||2|
|Link distance on SMF-28|d|0.002||300|meters|3|



Notes: 

1. ± 100 ppm , compliant with 40GBASE-ER4 and XLPPI per IEEE 802.3bm. 

2. Tested with a PRBS 2[31] -1 test pattern. 

3. Per 40GBASE-ER4, IEEE 802.3bm. Links longer than 30km are considered to be engineered links, with losses less than the worst case specified for the fiber type. 

## **III. Absolute Maximum Ratings** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Maximum Supply Voltage|Vcc1, VccTx,<br>VccRx|-0.5||3.6|V||
|Storage Temperature|TS|-40||85|°C||
|Case OperatingTemperature|TOP|0||70|°C||
|Relative Humidity|RH|0||85|%|1|
|Damage Threshold,per Lane|DT|3.8|||dBm||



Notes: Non-condensing. 

4 

**FTL4E1QE1C** 

## **IV. Electrical Characteristics  (TOP = 0 to 70°C, VCC = 3.1 to 3.47 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc1, VccTx,<br>VccRx|3.1||3.47|V||
|SupplyCurrent|Icc|||1.13|A||
|Link turn-on time|||||||
|Transmit turn-on time||||2000|ms|1|
|Transmitter (per Lane)|||||||
|Single ended input voltage tolerance|VinT|-0.3||4.0|V||
|Diferential data input swing|Vin,pp|120||1200|mVpp|3|
|Diferential input threshold|||50||mV||
|AC common mode input voltage toler-<br>ance (RMS)||15|||mV||
|Diferential input return loss||Per IEEE P802.3ba, Section 86A.4.1.1|||dB|4|
|J2 Jitter Tolerance|Jt2|0.17|||UI||
|J9 Jitter Tolerance|Jt9|0.29|||UI||
|Data Dependent Pulse Width Shrinkage|DDPWS|0.07|||UI||
|Eye mask coordinates {X1, X2<br>Y1, Y2}||0.11, 0.31<br>95, 350|||UI<br>mV|5|
|Receiver (per Lane)|||||||
|Single-ended output voltage||-0.3||4.0|V||
|Diferential data output swing|Vout,pp|0||800|mVpp|6|
|AC common mode output voltage<br>(RMS)||||7.5|mV||
|Termination mismatch at 1 MHx||||5|%||
|Diferential output return loss||Per IEEE P802.3ba, Section 86A.4.2.1|||dB|4|
|Common mode output return loss||Per IEEE P802.3ba, Section 86A.4.2.2|||dB|4|
|Output transition time, 20% to 80%||28|||ps||
|J2 Jitter output|Jo2|||0.42|UI||
|J9 Jitter output|Jo9|||0.65|UI||
|Eye mask coordinates  #1 {X1, X2<br>Y1, Y2}||0.29, 0.5<br>150, 425|||UI<br>mV|5|
|Power SupplyRipple Tolerance|PSR|50|||mVpp||



Notes: 

1. Maximum total power value is specified across the full temperature and voltage range. 

2. From power-on and end of any fault conditions. 

3. After internal AC coupling. Self-biasing 100Ω differential input. 

4. 10 MHz to 11.1 GHz range. 

5. Hit ratio = 5 x 10E-5. 

6. AC coupled with 100Ω differential output impedance. 

5 

**FTL4E1QE1C** 

## **V. Optical Characteristics (TOP = 0 to 70°C, VCC = 3.1 to 3.47 Volts)** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transmitter|||||||
|Signaling Speed per Lane|||10.3125||GBd||
|Lane center wavelengths (range)||1264.5 – 1277.5<br>1284.5 – 1297.5<br>1304.5 – 1317.5<br>1324.5 – 1337.5|||nm||
|Total Average Launch Power|POUT|||10.5|dBm||
|Transmit OMA per Lane|TxOMA|0.3||5.0|dBm||
|Average Launch Power per Lane|TXPx|-2.7||4.5|dBm|2|
|Diference in launch power between any two<br>lanes (OMA)|TxOMA|||3.0|dBm|2|
|Peak Power per Lane|PPx|||4.0|dBm||
|Transmitter Dispersion Penalty|TDP|||2.6|dB||
|Launch power (OMA) minus TDP per<br>lane||-0.5|||dBm||
|Optical Extinction Ratio|ER|5.5|||dB||
|Sidemode Suppression ratio|SSRmin|30|||dB||
|Average launch power of OFF transmitter, per lane||||-30|dBm||
|Relative Intensity Noise|RIN|||-128|dB/Hz|3|
|Optical Return Loss Tolerance||||20|dB||
|Transmitter Refectance||||-12|dB||
|Transmitter eye mask defnition {X1, X2, X3,<br>Y1, Y2, Y3}||{0.25, 0.4, 0.45, 0.25, 0.28, 0.4}|||||



6 

**FTL4E1QE1C** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Receiver per Lane|||||||
|Signaling Speed per Lane|||10.3125||GBd|4|
|Lane center wavelengths (range)||1264.5 – 1277.5<br>1284.5 – 1297.5<br>1304.5 – 1317.5<br>1324.5 – 1337.5|||nm||
|Receive Power (OMA) per Lane|RxOMA|||-4.0|dBm||
|Average Receive Power per Lane|RXPx|-21.2||-4.5|dBm|5, 6|
|Receiver Sensitivity (OMA) per Lane|Rxsens|||-19|dBm||
|Stressed Receiver Sensitivity (OMA)<br>per Lane|SRS|||-16.8|dBm||
|Damage Threshold per Lane|PMAX|||3.8|dBm||
|Return Loss|RL|||-26|dB||
|Vertical eye closure penalty, per lane||||2.2|dB||
|Receive electrical 3 dB upper cutof<br>frequency, per lane||||12.3|GHz||
|LOS De-Assert|LOSD|||-19|dBm||
|LOS Assert|LOSA|-35|||dBm||
|LOS Hysteresis|||1||dBm||



Notes: 

1. Transmitter consists of 4 lasers operating at up to 10.3 Gb/s each, ± 100ppm 

2. Minimum value is informative. 

3. RIN is scaled by 10*log(10/4) to maintain SNR outside of transmitter. 

4. Receiver consists of 4 photodetectors operating at up to 10.3125 Gb/s each, ± 100ppm 

5. Minimum value is informative, equals min TxOMA with infinite ER and max channel insertion loss. 

6. Maximum value is based on a min. of 9dB loss. Additional attenuation may be required when connected in loopback or short fiber link. 

## **VI. Memory Map and Control Registers** 

Compatible with SFF-8636 (QSFP+ MSA)[1] . Please see Finisar Application Note AN-2104[5] . 

## **VII. Environmental Specifications** 

Finisar FTL4E1Q transceivers have an operating temperature range from 0°C to +70°C case temperature. 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|0||70|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VIII. Regulatory Compliance** 

Finisar FTL4E1Q transceivers are RoHS-6 Compliant. Copies of certificates are available at Finisar Corporation upon request. 

FTL4E1Q transceiver modules are Class 1 laser eye safety compliant per IEC 60825-1. 

7 

**FTL4E1QE1C** 

## **IX. Mechanical Specifications** 

The FTL4E1QE1C mechanical specifications are compliant to the QSFP+ MSA transceiver module specifications. 


Figure 2 – FTL4E1QE1C mechanical drawing 


Figure 3 – FTL4E1QE1C label 

## **X. References** 

1. SFF-8636 – Specification for Common Management Interface, Rev 2.4, November 2014. 

2. IEEE P802.3bm, Draft 3.0, May 2014 – PMD Type 40GBASE-ER4. 

3. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. Certain products may use one or more exemptions as allowed by the Directive. 

4. “Application Note AN-2038: Finisar Implementation of RoHS Compliant Transceivers”. 

5. “Application Note AN-2104: QSFP+ 40G LR4 Transceiver EEPROM Mapping,” Rev. A, Finisar Corporation, June, 2013. 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

