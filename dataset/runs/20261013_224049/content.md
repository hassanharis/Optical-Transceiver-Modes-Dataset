Optical Transceivers 

## FTL410QD3C 

## **40BASE-SR4/10GBASE-SR 300m QSFP+ Gen3 Optical Transceiver Module** 

FTL410QD3C QSFP+ transceiver modules are designed for use in 40 Gigabit per second links over parallel multimode fiber, including breakout to four 10 Gigabit per second links. They are compliant with the QSFP+ MSA[1] ,[2] and IEEE 802.3ba 40GBASE-SR4[3 ] and compatible with IEEE 802.3ae 10GBASE-SR4. The optical transceiver is compliant per the RoHS Directive 2011/65/EU[5] . See Finisar Application Note AN-2038 for more details[6] . 


## FEATURES 

## APPLICATIONS 

- Four-channel full-duplex transceiver module 

- Hot Pluggable QSFP+ form factor 

- Maximum link length of 300m on OM3 Multimode Fiber (MMF) and 400m on OM4 MMF 

   - 40GBASE-SR4 40G Ethernet 

   - Breakout to 10GBASE-SR Ethernet 

   - Proprietary interconnections 

- Multirate capability: 1.06Gb/s to 10.5Gb/s per channel 

- Unretimed XLPPI electrical interface 

- Max power dissipation <1.2W 

- Reliable VCSEL array technology 

- Built-in digital diagnostic functions, including Tx and Rx power monitoring 

- Commercial operating case temperature range: 0ºC to 70ºC 

- Single 1x12 MPO receptacle 

- RoHS-6 Compliant 

**FTL410QD3C** 

## **Product Selection** 

## **FTL410QD3C** 

## **I. Pin Descriptions** 


Figure 1 – QSFP+ MSA-compliant 38-pin connector 

2 

**FTL410QD3C** 


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

**FTL410QD3C** 

## **II. General Product Characteristics** 


**----- Start of picture text -----**<br>
Parameter Value Unit Notes<br>**----- End of picture text -----**<br>


|Parameter|Value|Unit|Notes|
|---|---|---|---|
|||||
|Module Form Factor|QSFP+|||
|Number of Lanes|4 Tx and 4 Rx|||
|Maximum Aggregate Data<br>Rate|42.0|Gb/s||
|Maximum Data Rate per Lane|10.5|Gb/s|Higher bit rates may be supported.<br>Please contact Finisar.|
|Protocols Supported|Typical applications<br>include 40G Ethernet,<br>Infniband QDR, SATA/<br>SAS3|||
|Electrical Interface and Pin-out|38-pin edge connector||Pin-out as defned by the<br>QSFP+ MSA2|
|Maximum Power<br>Consumptionper End|1.2|Watts|Varies with output voltage swing and pre-em-<br>phasis settings|
|Management Interface|Serial, I2C-based, 400 kHz<br>maximum frequency||As defned by the QSFP+ MSA2|




**----- Start of picture text -----**<br>
Data Rate Specifications Symbol  Min  Typ Max  Units  Ref.<br>**----- End of picture text -----**<br>


|Data Rate Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Bit Rate per Lane|BR|1062||10500|Mb/sec|1|
|Bit Error Ratio|BER|||10-12||2|
|Link distance on OM3 MMF|d|||300|meters|3|
|Link distance on OM4 MMF|d|||400|meters|3|



Notes: 

1. Compliant with 40G and 10G* Ethernet. Compatible with 1 Gigabit Ethernet and 1/2/4/8/10G Fibre Channel. 

2. Tested with a PRBS 2[31] -1 test pattern. 

3. Per 40GBASE-SR4 and 10GBASE-SR IEEE 802.3ba 

* Max launch power exceeds 10G Ethernet specification by 1 dB, which is well within the guardband of receiver overload. 

## **III. Absolute Maximum Ratings** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Maximum Supply Voltage|Vcc1, VccTx,<br>VccRx|-0.5||3.6|V||
|Storage Temperature|TS|-40||85|°C||
|Case OperatingTemperature|TOP|0||70|°C||
|Relative Humidity|RH|0||85|%|1|
|Damage Threshold,per Lane|DT|3.4|||dBm||



Notes: Non-condensing. 

4 

**FTL410QD3C** 

## **IV. Electrical Characteristics  (TOP = 0 to 70°C, VCC = 3.1 to 3.45 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc1, VccTx,<br>VccRx|3.15||3.45|V||
|SupplyCurrent|Icc|||350|mA||
|Link turn-on time|||||||
|Transmit turn-on time||||2000|ms|2|
|Transmitter (per Lane)|||||||
|Single ended input voltage tolerance|VinT|-0.3||4.0|V||
|Diferential data input swing|Vin,pp|180||1200|mVpp|3|
|Diferential input threshold|||50||mV||
|AC common mode input voltage toler-<br>ance (RMS)||15|||mV||
|Diferential input return loss||Per IEEE P802.3ba, Section 86A.4.1.1|||dB|4|
|J2 Jitter Tolerance|Jt2|0.17|||UI||
|J9 Jitter Tolerance|Jt9|0.29|||UI||
|Data Dependent Pulse Width Shrinkage|DDPWS|0.07|||UI||
|Eye mask coordinates {X1, X2<br>Y1, Y2}||0.11, 0.31<br>95, 350|||UI<br>mV|5|
|Receiver (per Lane)|||||||
|Single-ended output voltage||-0.3||4.0|V||
|Diferential data output swing|Vout,pp|0||800|mVpp|7, 8|
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

4. 10 MHz to 11.1 GHz range 

5. Hit ratio = 5 x 10E-5. 

6. AC coupled with 100Ω differential output impedance. 

7. Settable in 4 discrete steps via the I2C interface. 

5 

**FTL410QD3C** 

## **V. Optical Characteristics (TOP = 0 to 70°C, VCC = 3.1 to 3.45 Volts)** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transmitter (per Lane)|||||||
|Signaling Speed per Lane||1.00|10.3125|10.5|GBd||
|Center wavelength||840||860|nm||
|RMS Spectral Width|SW|||0.40|nm||
|Average Launch Power per Lane|TXPx|-7.5||0|dBm|1|
|Transmit OMA per Lane|TxOMA|||3.0|dBm|2|
|Stressed Receiver Sensitivity (OMA) per Lane|DPx|||4.0|dB||
|Peak Power per Lane|PPx|||4.0|dBm||
|Launch Power [OMA] minus TDP per Lane|P-TDP|-6.5|||dBm||
|TDP per Lane|TDPSR4|||3.5|dB|3|
||TDPSR|||3.9||4|
|Optical Extinction Ratio|ER|3.0|||dB||
|Optical Return Loss Tolerance|ORL|||12|dB||
|Encircled Flux|FLX|> 86% at 19 um<br>< 30% at 4.5 um|||dBm||
|Average launch power of OFF transmitter, per<br>lane||||-30|dBm||
|Relative Intensity Noise|RIN|||-128|dB/Hz||
|Transmitter eye mask defnition {X1, X2, X3,<br>Y1, Y2, Y3}||0.23, 0.34, 0.43, 0.27, 0.35, 0.4|||||



6 

**FTL410QD3C** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Receiver per Lane|||||||
|Signaling Speed per Lane||1.00|10.3125|10.5|GBd|3|
|Center wavelength||840||860|nm||
|Damage Threshold|DT|3.4|||dBm||
|Average Receive Power per Lane|RXPx|-9.9||2.4|dBm||
|Receive Power (OMA) per Lane|RxOMA|||3.0|dBm||
|Unstressed Receiver Sensitivity<br>(OMA) per Lane|URS|-11.1|||dBm||
|Stressed Receiver Sensitivity (OMA)<br>per Lane|SRS|-7.5|||dBm||
|Peak Power, per lane|PPx|||4|dBm||
|Receiver Refectance|Rf|||-12|dB||
|Vertical eye closure penalty, per lane||||3.5|dB||
|Stressed eye J2 jitter, per Lane||||0.3|UI||
|Stressed eye J9 jitter, per Lane||||0.47|UI||
|OMA of each aggressor lane||||-0.4|dBm||
|Rx jitter tolerance: Jitter frequency and<br>p-p amplitude||(75, 5)|||kHz, UI||
|||(375, 1)|||kHz, UI||
|LOS De-Assert|LOSD|||-12|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|||dBm||



Notes: 

1. The maximum launch power of 0 dBm is well within the guardband of receiver overload specifications for commercially available 10GBASE-SR SFP+ transceivers from Finisar and other vendors. 

2. Even if TDP is <0.9dB, the OMA min must exceed the value given in the table below: 


**----- Start of picture text -----**<br>
Center   RMS Spectral width (nm)<br>Wavelength<br>Up to 0.05 0.05 to 0.1 0.1 to 0.15 0.15 to 0.2 0.2 to 0.25 0.25 to 0.3 0.3 to 0.35 0.35 to 0.4 0.4 to 0.45<br>(nm)<br>**----- End of picture text -----**<br>


|Center<br>Wavelength<br>(nm)|RMS Spectral width (nm)|RMS Spectral width (nm)|RMS Spectral width (nm)|RMS Spectral width (nm)|RMS Spectral width (nm)|RMS Spectral width (nm)|RMS Spectral width (nm)|RMS Spectral width (nm)|RMS Spectral width (nm)|
|---|---|---|---|---|---|---|---|---|---|
||Up to 0.05|0.05 to 0.1|0.1 to 0.15|0.15 to 0.2|0.2 to 0.25|0.25 to 0.3|0.3 to 0.35|0.35 to 0.4|0.4 to 0.45|
|||||||||||
|840 to 842|-4.2|-4.2|-4.2|-4.1|-3.9|-3.8|-3.5|-3.2|-2.8|
|842 to 844|-4.2|-4.2|-4.2|-4.1|-3.9|-3.8|-3.6|-3.3|-2.9|
|844 to 846|-4.2|-4.2|-4.2|-4.1|-4.0|-3.8|-3.6|-3.3|-2.9|
|846 to 848|-4.3|-4.2|-4.2|-4.1|-4.0|-3.8|-3.6|-3.3|-2.9|
|848 to 850|-4.3|-4.2|-4.2|-4.1|-4.0|-3.8|-3.6|-3.3|-3.0|
|850 to 852|-4.3|-4.2|-4.2|-4.1|-4.0|-3.8|-3.6|-3.4|-3.0|
|852 to 854|-4.3|-4.2|-4.2|-4.1|-4.0|-3.9|-3.7|-3.4|-3.1|
|854 to 856|-4.3|-4.3|-4.2|-4.1|-4.0|-3.9|-3.7|-3.4|-3.1|
|856 to 858|-4.3|-4.3|-4.2|-4.1|-4.0|-3.9|-3.7|-3.5|-3.1|
|858 to 860|-4.3|-4.3|-4.2|-4.2|-4.1|-3.9|-3.7|-3.5|-3.2|



1. This TDP is up to 100m on OM3 and 150m on OM4. 

2. This TDP is up to 300m on OM3 and 400m on OM4. 

7 

**FTL410QD3C** 

## **VI. Memory Map and Control Registers** 

Compatible with the SFF-8436 QSFP+ MSA[1] and the SFF-8636 Common Management Interface MSA.[2] See Finisar Application Note AN-2119[7] for a complete EEPROM memory map. 

## **VII. Environmental Specifications** 

Finisar FTL410QD3C transceivers have an operating temperature range from 0°C to +70°C case temperature. 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|0||70|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VIII. Regulatory Compliance** 

Finisar FTL410QD3C transceivers are RoHS-6 Compliant. Copies of certificates are available at Finisar Corporation upon request. 

FTL410QD3C transceiver modules are Class 1 laser eye safety compliant per IEC 60825-1. 

8 

**FTL410QD3C** 

## **IX. Mechanical Specifications** 

The FTL410QD3C mechanical specifications are compliant to the QSFP+ MSA[2] transceiver module specifications. 


Figure 2 – FTL410QD3C mechanical drawing 


Figure 3 – FTL410QD3C product label 

9 

**FTL410QD3C** 

The optical port is a male MPO connector receptacle, with fiber lane assignments as shown in Figure 4. 


**----- Start of picture text -----**<br>
Ch 0         Ch 1       Ch2          Ch3                                                                          Ch 3         Ch 2        Ch1        Ch0<br>**----- End of picture text -----**<br>


Figure 4 – FTL410QD3C optical lane assignment (front view of MPO receptacle) 

## **X. References** 

1. SFF-8436 – Specification for QSFP+ 10 Gbs 4x Pluggable Transceiver, Rev 4.8, October 2013. 

   - SFF-8636 – Specification for Common Management Interface, Rev 2.4, November 2014. 

2. 

3. IEEE 802.3ba – PMD Type 40GBASE-SR4. 

4. IEEE 802.3ae – PMD Type 10GBASE-SR. 

5. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. Certain products may use one or more exemptions as allowed by the Directive. 

6. “Application Note AN-2038: Finisar Implementation of RoHS Compliant Transceivers”. 

7. “Application Note AN-2119: QSFP+ 3rd Generation SR4 Transceiver – EEPROM Mapping”, Rev. B, Finisar Corporation, January, 2015. 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

