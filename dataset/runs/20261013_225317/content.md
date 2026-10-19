
# **Product Specification 10km 100G eCWDM4 QSFP28 Optical Transceiver Module (4WDM-10)** 

## **FTLC1157RGPLA** 

## **PRODUCT FEATURES** 

- Hot-pluggable QSFP28 form factor 

- Supports 103.1Gb/s aggregate bit rate 

- Power dissipation < 3.5W 

- RoHS-6 compliant 

- Commercial case temperature range of 0°C to +70°C 


- Single 3.3V power supply 

- Maximum link length of 10km on Single Mode Fiber (SMF) [with KR4 FEC] 

- 4x25Gb/s CWDM transmitter 

## **APPLICATIONS** 

   - 100G 4WDM applications with FEC 

- 4x25G retimed electrical interface 

- Duplex LC receptacles 

- I2C management interface 

Finisar’s FTLC1157RGPLA QSFP28 transceiver modules are designed for use in 100 Gigabit Ethernet links on up to 10 km of single mode fiber, based on the CWDM4 wavelength grid.  Designed for data center applications, the transceivers are compliant with the QSFP28 MSA[1] , CWDM4 MSA[2] , 4WDM MSA[3] , and portions of IEEE P802.3bm CAUI-4[4] .  Digital diagnostic functions are available via the I2C interface, as specified by the QSFP28 MSA and Finisar Application Notes AN-2153[5] and AN-2154[6] . The transceiver is RoHS-6 compliant and lead-free per Directive 2011/65/EC[7] and Finisar Application Note AN-2038[8] . 

## **PRODUCT SELECTION** 

## **FTLC1157RGPLA** 

R: Ethernet maximum bit rate (103.1 Gb/s) G: 4x25G CWDM optical architecture P: Pull-tab release L: LC straight receptacles A: Extended reach (10 km) 

© Finisar Corporation – 07-Jan-2020 

Rev. B1 

Page 1 

FTLC1157RGPLA Product Specification – Jan 2020 


## **I. Pin Descriptions** 



**Figure 1 – QSFP28-compliant 38-pin connector (per SFF-8679)** 

|**Pin**|**Symbol**|**Name/Description**|**Notes**|
|---|---|---|---|
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
|28|IntL|Interrupt||
|29|Vcc Tx|+3.3 V Power supply transmitter||



© Finisar Corporation – 07-Jan-2020 

Rev. B1 

Page 2 

FTLC1157RGPLA Product Specification – Jan 2020 


|30|Vcc1|+3.3 V Power Supply||
|---|---|---|---|
|31|LPMode|Low Power Mode||
|32|GND|Ground|1|
|33|Tx3p|Transmitter Non-Inverted Data Input||
|34|Tx3n|Transmitter Inverted Data Input||
|35|GND|Ground|1|
|36|Tx1p|Transmitter Non-Inverted Data Input||
|37|Tx1n|Transmitter Inverted Data Input||
|38|GND|Ground|1|



## Notes 

1. Circuit ground is internally isolated from chassis ground. 

## **II. Absolute Maximum Ratings** 

Module performance is not guaranteed beyond the operating range (see Section VI). Exceeding the limits below may damage the transceiver module permanently. 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Ref.**|
|---|---|---|---|---|---|---|
|Maximum Supply Voltage|Vcc|-0.5||3.6|V||
|Storage Temperature|TS|-40||+85|C||
|Case OperatingTemperature|TOP|0||+70|C||
|Relative Humidity|RH|15||85|%|1|
|Receiver Damage Threshold, per Lane|PRdmg|5.5|||dBm||



## Notes: 

1. Non-condensing. Do not operate in a condensing environment. 

## **III. Electrical Characteristics (EOL, TOP = 0 to +70**  **C, VCC = 3.135 to 3.465 Volts)** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Ref.**|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.135||3.465|V||
|Supply Current|Icc|||1.12|A||
|Module total power|P|||3.5|W|1|
|**Transmitter**|||||||
|Signaling rate per lane||25.78125 ± 100 ppm|||GBd||
|Differential data input swing per lane|Vin,pp|||900|mV||
|Differential input return loss (min)|RLd(f)|9.5 – 0.37f,   0.01≤f<8<br>4.75–7.4log10(f/14),  8 ≤f<19|||dB||
|Differential to common mode input<br>return loss (min)|RLdc(f)|22-20(f/25.78), 0.01≤f<12.89<br>15-6(f/25.78), 12.89≤f<19|||dB||
|Differential termination mismatch||||10|%||
|Stressed input parameters|||||||
|Eye width|||0.46||UI||
|Applied pk-pk sinusoidal jitter||Per IEEE 802.3bm Table 88-13|||||
|Eye height|||95||mV||
|DC common mode voltage||-350||2850|mV||
|**Receiver**|||||||
|Signaling rate per lane||25.78125 ± 100||ppm|GBd||
|Differential data output swing|Vout,pp|100||400|mVpp|2|
|||300||600|||
|||400||800|||
|||600||1200|||
|Eye width||0.57|||UI||
|Vertical eye closure||||5.5|dB||



© Finisar Corporation – 07-Jan-2020 

Rev. B1 

Page 3 

FTLC1157RGPLA Product Specification – Jan 2020 


|Differential output return loss (min)|RLd(f)|9.5 – 0.37f,   0.01≤f<8<br>4.75 – 7.4log10(f/14),8≤f<19|9.5 – 0.37f,   0.01≤f<8<br>4.75 – 7.4log10(f/14),8≤f<19|9.5 – 0.37f,   0.01≤f<8<br>4.75 – 7.4log10(f/14),8≤f<19|dB||
|---|---|---|---|---|---|---|
|Common to differential mode<br>conversion return loss (min)|RLdc(f)|22-20(f/25.78), 0.01≤f<12.89<br>15-6(f/25.78), 12.89≤f<19|||dB||
|Differential termination mismatch||||10|%||
|Transition time, 20% to 80%|trtf|12|||ps||



Notes: 

1. Maximum total power value is specified across the full temperature and voltage range. 

2. Output voltage is settable in 4 discrete ranges via I2C.  Default range is Range 2 (400 – 800 mV). 

## **IV. Optical Characteristics (EOL, TOP = 0 to +70**  **C, VCC = 3.135 to 3.465 Volts)** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Ref.**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
|Signaling Speed per Lane||25.78125 ± 100 ppm|||GBd|1|
|Lane center wavelengths (range)||1264.5 – 1277.5<br>1284.5 – 1297.5<br>1304.5 – 1317.5<br>1324.5–1337.5|||nm||
|Transmit OMA per Lane|TxOMA1|-4||2.5|dBm||
|Transmit OMA per Lane @TDP max|TxOMA2|-2|||dBm|2|
|Transmit Average Power per Lane||||2.5|dBm|8|
|Optical Extinction Ratio|ER|3.5|||dB||
|Transmitter and Dispersion Penalty<br>per Lane|TDP|||3|dB|3|
|Launch Power (OMA-TDP)|OMA-<br>TDP|-5|||dBm||
|Sidemode Suppression ratio|SSRmin|30|||dB||
|Average launch power of OFF<br>transmitter, per lane||||-30|dBm||
|Transmitter Reflectance||||-12|dB||
|Transmitter eye mask definition {X1,<br>X2, X3, Y1, Y2, Y3}||Expected to follow CWDM4<br>MSA||||4|
|**Receiver**|||||||
|Signaling Speed per Lane||25.78125 ± 100 ppm|||GBd|5|
|Lane center wavelengths (range)||1264.5 – 1277.5<br>1284.5 – 1297.5<br>1304.5 – 1317.5<br>1324.5–1337.5|||nm||
|Receive Saturation  (OMA) per Lane|Rmax|2.5|||dBm||
|Damage threshold per Lane||3.5|||dBm||
|Unstressed Receiver Sensitivity<br>(OMA) per Lane|Rxsens|||-11.3|dBm|6|
|Stressed Receiver Sensitivity (OMA)<br>per Lane|SRS|||-8.9|dBm|7|
|Conditions of stressed receiver sensitivity test:|||||||
|Vertical Eye Closure Penalty|VECP|Expected to follow<br>MSA||CWDM4|dB||
|Stressed J2 Jitter|J2||||UI||
|Stressed J4 Jitter|J4||||UI||
|SRS eye mask definition {X1, X2,<br>X3, Y1, Y2, Y3}||Expected to follow<br>MSA||CWDM4|||
|LOS De-Assert|LOSD|||-12.8|dBm||
|LOS Assert|LOSA|-24||-14|dBm||
|LOS Hysteresis|||1.5||dB||



UNotesU: 

© Finisar Corporation – 07-Jan-2020 

Rev. B1 

Page 4 

FTLC1157RGPLA Product Specification – Jan 2020 


1. Transmitter consists of 4 lasers operating at 25.78Gb/s each. 

2. At maximum TDP. 

3. TDP value does not include MPI penalty. 

4. Hit ratio of 5x10[-5] , per IEEE. 

5. Receiver consists of 4 photodetectors operating at 25.78Gb/s each. 

6. Sensitivity is specified at 5x10[-5] BER. 

7. Measured with 4WDM MSA[3] conformance test signal at TP3 for 5x10[-5] BER. 

8. Power value and power accuracy are with all channels on. 

## **V. General Specifications** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Ref.**|
|---|---|---|---|---|---|---|
|Bit Rate(all wavelengths combined)|BR|||103.1|Gb/s||
|Bit Error Ratio @25.78Gb/s|BER|||5x10-5||1|
|**Maximum Supported Reach **|||||||
|Fiber Type|||||||
|SMF per G.652|LossBdgt|||6.5|dB|2|



Notes: 

1. Tested with a 2[31] – 1 PRBS. 

2. The maximum informative link length is 10km. The option to bypass RS-FEC is not supported. Loss budget may include up to 1dB MPI loss penalty with worse case Transmitter and worst case connector MPI. 

## **VI. Environmental Specifications** 

Finisar FTLC1157RGPLA QSFP28 transceivers have an operating case temperature range of 0°C to +70°C. 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Ref.**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Top|0||+70|°C||
|Storage Temperature|Tsto|-40||+85|°C||



## **VII.  Regulatory Compliance** 

Finisar FTLC1157RGPLA QSFP28 transceivers are Class 1 Laser Products. They are certified per the following standards: 

|**Agency**|**Standard**|
|---|---|
|FDA/CDRH|CDRH 21 CFR 1040 and Laser Notice 50|
|CSA|IEC60825-2:2004+A1+A2|
|TüV|EN60825-1:2014 & EN60825-2:2006+A1+A2|
|CSA|IEC60950-1:2005+A1+A2|
|TüV|EN60950-1:2006+A11+A1+A12+A2|
|UL/CSA|CLASS 3862.13 & CLASS 3862.93|



Copies of the referenced certificates are available at Finisar Corporation upon request. 

Page 5 

© Finisar Corporation – 07-Jan-2020 

Rev. B1 

FTLC1157RGPLA Product Specification – Jan 2020 


## **VIII.  Digital Diagnostics Functions** 

FTLC1157RGPLA QSFP28 transceivers support the I2C-based diagnostics interface specified by the SFF Commitee[1] . See also Finisar Application Note AN-2153[5] . 

## **IX. Memory Contents** 

Per SFF-8665 Specification[1] . See Finisar Application Note AN-2153[5] . 

## **XI. Mechanical Specifications** 

Finisar FTLC1157RGPLA transceivers are compatible with the QSFP28 Specification for pluggable form factor modules. 


**Figure 2.  FTLC1157RGPLA Mechanical Dimensions.** 


**Figure 3.  Product Label (Not to Scale)** 

Page 6 

© Finisar Corporation – 07-Jan-2020 

Rev. B1 

FTLC1157RGPLA Product Specification – Jan 2020 


## **XII. References** 

1. SFF-8665: “QSFP+ 28Gb/s 4X Pluggable Transceiver Solution (QSFP28)”, Rev 1.9, June 29, 2015 and associated SFF documents referenced therein: 

   - i. SFF-8661 

   - ii. SFF-8679 

   - iii. SFF-8636 

   - iv. SFF-8662 

   - v. SFF-8663 

   - vi. SFF-8672 

   - vii. SFF-8683 

2. “100G CWDM4 MSA Technical Specifications: 2km Optical Specifications”, Rev. 1.1, November 23, 2015. 

3. “100G 4WDM-10 MSA Technical Specifications: 10km Optical Specifications,” Rev 1.0, March 10, 2017. 

4. IEEE P802.3bm, CAUI-4 Interface. 

5. Application Note AN-2153: Initialization, Finisar Corporation. 

6. Application Note AN-2154: EEPROM Map, Finisar Corporation. 

7. Directive 2011/65/EU of the European Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment,” Certain products may use one or more exemptions as allowed by the Directive.  July 1, 2011. 

8. Application Note AN-2038: Finisar Implementation Of RoHS Compliant 

## **For More Information:** 

Finisar Corporation 1389 Moffett Park Drive Sunnyvale, CA  94089-1133 Tel. 1-408-548-1000 Fax 1-408-541-6138 sales@finisar.com www.finisar.com 

© Finisar Corporation – 07-Jan-2020 

Rev. B1 

Page 7 

