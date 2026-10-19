Optical Transceivers 

## FTLC1154RDPLC 

## **100G 20km eLR4 QSFP28 Optical Transceiver Module (WDM-20)** 

FTLC1154RDPLC QSFP28 transceiver modules are designed for use in 100 Gigabit Ethernet links on up to 20km of single mode fiber, based on the LAN-WDM wavelength grid. Designed for outside plant applications with an extended temperature range (-20°C to +85°C), they are compliant with the QSFP28 MSA[1] , IEEE 802.3ba 100GBASE-LR4[2] , 4WDM MSA[7] , portions of CWDM4 MSA[8] , and IEEE 802.3bm CAUI-4[6] . Digital diagnostic functions are available via the I2C interface, as specified by the QSFP28 MSA and Finisar Application Notes AN-21524and AN-21535. The optical transceiver is compliant per the RoHS-6 Directive 2011/65/EU[6] . See Finisar Application Note AN-2038[7] for more details. 


## FEATURES 

## APPLICATIONS 

- Hot-pluggable QSFP28 form factor 

- Supports 103.1Gb/s aggregate bit rate 

- Power dissipation < 4.5W 

   - 100G 4WDM applications with FEC 

   - Outside Plant 

   - Reduced Air Flow Central Office 

- RoHS-6 compliant 

- Extended temperature range of -20°C to 85°C 

- Single 3.3V power supply 

- Maximum link length of 20km on Single Mode Fiber (SMF) 

- 4x25Gb/s DFB-based LAN-WDM transmitter 

- 4x25G retimed electrical interface 

- Duplex LC receptacles 

- I2C management interface 

**FTLC1154RDPLC** 

## **Product Selection** 

## **FTLC1154RDPLC** 

- R: 100GE-LR4 maximum bit rate (103.1 Gb/s) D: 4x25G LAN-WDM optical architecture 

- P: Pull-tab release 

- L: LC straight receptacles C: Extended reach (20 km), extended temperature 

## **I. Pin Descriptions** 


Figure 1 – QSFP28-compliant 38-pin connector (per SFF-8679) 

2 

**FTLC1154RDPLC** 


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
|10|Vcc Rx|+3.3 V Power supply receiver||
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
|28|IntL|Interrupt|2|
|29|Vcc Tx|+3.3 V Power supply transmitter||
|30|Vcc1|+3.3 V Power Supply||
|31|LPMode|Low Power Mode|2|
|32|GND|Ground|1|
|33|Tx3p|Transmitter Non-Inverted Data Input||
|34|Tx3n|Transmitter Inverted Data Input||
|35|GND|Ground|1|
|36|Tx1p|Transmitter Non-Inverted Data Input||
|37|Tx1n|Transmitter Inverted Data Input||
|38|GND|Ground|1|



Notes 

1. Circuit ground is internally isolated from chassis ground. 

2. The IntL pin (“Interrupt Low”, pin 28) can be configured to act as an Rx_LOS output; The LPMode pin (“Low Power Mode”, pin 31) can be configured to act as an input for Tx_Disable; These changes require customization. See Finisar Application Note AN-21748 for more details. 

3 

**FTLC1154RDPLC** 

## **II. Absolute Maximum Ratings** 

Module performance is not guaranteed beyond the operating range (see Section VI). Exceeding the limits below may damage the transceiver module permanently. 

|Parameter|Symbol|Symbol|Min|Min|Typ|Typ|Max|Max|Unit|Unit|Ref.|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Maximum SupplyVoltage|Vcc||-0.5||||3.6||V|||
|Storage Temperature|TS||-40||||+85||°C|||
|Case OperatingTemperature|TOP||-40||||+85||°C|||
|Relative Humidity|RH||15||||85||%||1|
|Receiver Damage Threshold,per Lane|PRdmg||5.5||||||dBm|||
|~~Notes:~~<br>Non-condensing.<br>**III. Electrical Characteristics  (EOL, TOP = -20 to +85 °C, VCC = 3.135 to 3.465 Volts)**||||||||||||
|Parameter||Symbol||Min||Typ||Max||Unit|Ref.|
|Supply Voltage||Vcc||3.135||||3.465||V||
|Supply Current||Icc||||||1.6||A||
|Module total power||P||||||4.5||W|1|
|Transmitter||||||||||||
|Signaling rate per lane||||25.78125 ±||100 ppm||||Gb/s||
|Diferential data input swing per lane||Vin,pp||||||900||mV||
|Diferential input return loss (min) at LR4||RLd(f)||9.5 – 0.37f, 0.01≤f<8<br>4.75 – 7.4log10(f/14), 8 ≤f<19||||||dB||
|Diferential to common mode input return loss<br>(min) at LR4||RLdc(f)||22-20(f/25.78), 0.01≤f<12.89<br>15-6(f/25.78), 12.89≤f<19||||||dB||
|Diferential termination mismatch||||||||10||%||
|Stressed input parameters||||||||||||
|Eye width||||||0.46||||UI||
|Applied pk-pk sinusoidal jitter||||Per IEEE 802.3bm Table 88-13||||||||
|Eye height||||||95||||mV||
|DC common mode voltage||||-350||||2850||mV||



4 

**FTLC1154RDPLC** 


**----- Start of picture text -----**<br>
Receiver<br>**----- End of picture text -----**<br>


|Receiver|||||||
|---|---|---|---|---|---|---|
||||||||
|Signaling rate per lane||25.78125 ± 100 ppm|||GBd||
|Diferential data output swing|Vout,pp|100||400|mVpp|3|
|||300||600|||
|||400||800|||
|||600||1200|||
|Eye width|EW15|0.57|||UI|4|
|Vertical eye closure||||5.5|dB||
|Diferential output return loss (min)|RLd(f)|9.5 – 0.37f, 0.01≤f<8<br>4.75 – 7.4log10(f/14), 8 ≤f<19|||dB||
|Common to diferential mode conversion return<br>loss (min)|RLdc(f)|22-20(f/25.78), 0.01≤f<12.89<br>15-6(f/25.78), 12.89≤f<19|||dB||
|Diferential termination mismatch||||10|%||
|Transition time, 20% to 80%|tr tf|12|||ps||



Notes: 

1. Maximum total power value is specified across the full temperature and voltage range. Power consumption ≤ 4.5W when stabilized (both Tx and Rx CDR locked), but may be ≤ 5W during locking acquisition. 

2. Output voltage is settable in 4 discrete ranges via I2C. Default range is 400 – 800 mV. 

5 

**FTLC1154RDPLC** 

## **IV. Optical Characteristics (EOL, TOP = -20 to 85 °C, VCC = 3.315 to 3.465 Volts)** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transmitter|||||||
|Signaling Speed per Channel||25.78125 ± 100 ppm|||Gb/s|1|
|Channel center wavelengths (range)||1294.53 – 1296.59<br>1299.02 – 1301.09<br>1303.54 – 1305.63<br>1308.09 – 1310.19|||nm||
|Total Average Launch Power|POUT|||10.5|dBm||
|Transmit OMA per Lane|TxOM A|-1.3||4.5|dBm||
|Average Launch Power per Channel|TXPx|-4.3||4.5|dBm|5|
|Optical Channel Extinction Ratio|ER|4.0||6.5|dB||
|Sidemode Suppression ratio|SSRmin|30|||dB||
|Average launch power of OFF transmitter, per<br>lane||||-30|dBm||
|Relative Intensity Noise|RIN|||-130|dB/Hz||
|Optical Return Loss Tolerance||||20|dB||
|Transmitter Refectance||||-12|dB||
|Transmitter eye mask defnition {X1,<br>X2, X3, Y1, Y2, Y3}||{0.25, 0.4, 0.45, 0.25, 0.28, 0.4}||||2|
|Receiver|||||||
|Signaling Speed per Channel||25.78125 ± 100 ppm|||GBd|3|
|Channel center wavelengths (range)||1294.53 – 1296.59<br>1299.02 – 1301.09<br>1303.54 – 1305.63<br>1308.09 – 1310.19|||nm||
|Receive Power (OMA) per Lane|RxOMA|||4.5|dBm||
|Average Receive Power per Lane|RXPx|-14.5||4.5|dBm|5,7|
|Unstressed Receiver Sensitivity (OMA) per<br>Lane|Rxsens|||-12.5|dBm||
|Return Loss|RL|-26|||dB||
|Stressed Receiver Sensitivity (OMA) per Lane|SRS|||-10|dBm||
|Receive electrical 3 dB upper cutof frequency,<br>per lane||||31|GHz||
|LOS De-Assert|LOSD|||-13.5|dBm||
|LOS Assert|LOSA|-24||-14|dBm||
|LOS Hysteresis|||1.5||dB||



Notes: 

1. Transmitter consists of 4 lasers operating at 25.78Gb/s each. 

2. Minimum value is informative. 

3. Hit ratio 5x10-5. 

4. Receiver consists of 4 photodetectors operating at 25.78Gb/s each. 

5. Minimum value is informative, equals min TxOMA with infinite ER and max channel insertion loss. 

6. SRS is measured with vertical eye closure penalty of 1.8 dB max, J2 of 0.30 UI, and J9 of 0.47 UI. 

7. Power value and power accuracy are with all channels on. Sensitivity is specified at 5x10-5 BER. 

8. Measured with 4WDM MSA[7] conformance test signal at TP3 for 5x10[-5] BER. 

6 

**FTLC1154RDPLC** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Typ Max Units Ref.<br>**----- End of picture text -----**<br>


|Parameter|Parameter|Symbol||Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|---|
|||||||||
|Bit Rate (all wavelengths combined)||BR|||103.1|Gb/s||
|Bit Error Ratio @25.78Gb/s||BER|||5x10-5||1|
|Maximum Supported Distances||||||||
|Fiber Type||||||||
|SMF per G.652||Lmax|||20|km||



Notes: 

1. Tested with a 231 – 1 PRBS. 

## **VI. Environmental Specifications** 

Finisar FTLC1154RDPLC QSFP28 transceivers have an operating case temperature range of -20°C to +85°C. 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-20||+85|°C||
|Storage Temperature|Tsto|-40||+85|°C||



## **VIII. Regulatory Compliance** 

Finisar FTLC1154RDPLC QSFP28 transceivers are Class 1 Laser Products. They are certified per the following standards: 


**----- Start of picture text -----**<br>
Feature Agency Standard<br>**----- End of picture text -----**<br>


|Feature|Agency|Standard|
|---|---|---|
||||
|Laser Eye Safety|FDA/CDRH|CDRH 21 CFR 1040 and Laser Notice 50|
||CSA|IEC60825-2:2004+A1+A2|
||TüV|EN60825-1:2014 & EN60825-2:2006+A1+A2|
|Electrical Safety|CSA|IEC60950-1:2005+A1+A2|
||TüV|EN60950-1:2006+A11+A1+A12+A2|
||UL/CSA|CLASS 3862.13 & CLASS 3862.93|



Copies of the referenced certificates are available at Finisar Corporation upon request. 

## **VIII. Digital Diagnostics Functions** 

FTLC1154RDPLC QSFP28 transceivers support the I2C-based diagnostics interface specified by the SFF Commitee1. See also Finisar Application Notes AN-21524 and AN- 2153[5] . 

## **IX. Memory Contents** 

Per SFF-8665 Specification[1] . See Finisar Application Note AN-2152[4] . For CFP replacement applications, the transceiver module can be customized to enable Tx_Disable and Rx_LOS functions as alternate functions on LPMode and IntL pins. See Finisar Application Note AN-2174[8] for more details. 

7 

**FTLC1154RDPLC** 

## **XI. Mechanical Specifications** 

Finisar FTLC1154RDPLC transceivers are compatible with the QSFP28 Specification for pluggable form factor modules. 


Figure 2. FTLC1154RDPLC Mechanical Dimensions. 


Figure 3. Product Label (Not to Scale) 

8 

**FTLC1154RDPLC** 

## **X. References** 

1. SFF-8665: “QSFP+ 28Gb/s 4X Pluggable Transceiver Solution (QSFP28)”, Rev 1.9, June 29, 2015 (and associated SFF documents) 

   - i. SFF-8661 

   - ii. SFF-8679 

   - iii. SFF-8636 

   - iv. SFF-8662 

   - v. SFF-8663 

   - vi. SFF-8672 vii. SFF-8683 

2. IEEE 802.3ba, PMD Type 100GBASE-LR4. 

3. IEEE 802.3bm, Annex 83E, CAUI-4 Interface. 

4. Application Note AN-2152: EEPROM Map, Finisar Corporation. 

5. Application Note AN-2153: Initialization, Finisar Corporation. 

6. Directive 2011/65/EU of the European Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment,” July 1, 2011. 

7. Application Note AN-2038: Finisar Implementation Of RoHS Compliant Transceivers, Finisar Corporation. 

8. Application Note AN-2174: QSFP28 LR4 and QSFP28 CWDM4 – Tx_Disable and Rx_LOS Capability, Finisar Corporation. 

© 2023 Coherent Corp. photonics.sales@coherent.com Legal notices : coherent.com/legal www.coherent.com 

