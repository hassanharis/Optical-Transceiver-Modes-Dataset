Optical Transceivers 

## FTLC1154SDPLD 

## **100G 20km eLR4 QSFP28 Optical Transceiver Module (WDM-20)** 

FTLC1154SDPLD QSFP28 transceiver modules are designed for use in 100 Gigabit Ethernet and 4x28G OTN client interface links on up to 20km of single mode fiber. Designed for outside plant applications with an industrial temperature range (-40°C to +85°C), they are compliant with the QSFP28 MSA[1] , IEEE 802.3ba 100GBASE-LR4[2] , IEEE 802.3bm CAUI-4[3] and OTU4 4I19D1F requirements specified in ITU-T Recommendations G.959.1/G.709 and Supplement 39 (G.sup39). Digital diagnostic functions are available via the I2C interface, as specified by the QSFP28 MSA and Finisar Application Notes AN-21524and AN-21535. The optical transceiver is compliant per the RoHS-6 Directive 2011/65/EU[6] . See Finisar Application Note AN2038[7] for more details. 


## FEATURES 

## APPLICATIONS 

- Hot-pluggable QSFP28 form factor 

- Supports 103.1Gb/s and 112Gb/s aggregate bit rates 

- Power dissipation < 4.5W 

- RoHS-6 compliant 

   - OTN OTU4 4I1-9D1F 

   - 100G 4WDM applications with FEC 

   - Outside plant 

   - Reduced air flow central office 

- Industrial case temperature range of -40°C to 85°C 

- Single 3.3V power supply 

- Maximum link length of 10km on Single Mode Fiber (SMF) 

- 4x28Gb/s DFB-based LAN-WDM transmitter 

- 4x28G retimed electrical interface 

- Duplex LC receptacles 

- I2C management interface 

**FTLC1154SDPLD** 

## **Product Selection** 

## **FTLC1154SDPLD** 

- 4: Gen 2 

- S: OTU4 maximum bit rate (112 Gb/s) D: 4x28G LAN-WDM optical architecture P: Pull-tab release 

- L: LC straight receptacles 

- 4: Industrial temperature range 

## **I. Pin Descriptions** 


Figure 1 – QSFP28-compliant 38-pin connector (per SFF-8679) 

2 

**FTLC1154SDPLD** 


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

2. The IntL pin (“Interrupt Low”, pin 28) can be configured to act as an Rx_LOS output; 

- The LPMode pin (“Low Power Mode”, pin 31) can be configured to act as an input for Tx_Disable; These changes require customization. See Finisar Application Note AN-21748 for more details. 

3 

**FTLC1154SDPLD** 

## **II. Absolute Maximum Ratings** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum SupplyVoltage|Vcc|-0.5||3.6|V||
|Storage Temperature|TS|-40||+85|°C||
|Case OperatingTemperature|TOP|-40||+85|°C||
|Relative Humidity|RH|15||85|%|1|
|Receiver Damage Threshold,per Lane|PRdmg|5.5|||dBm||



~~Notes:~~ 

Non-condensing. 

## **III. Electrical Characteristics  (EOL, TOP = -40 to +85 °C, VCC = 3.135 to 3.465 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.135||3.465|V||
|Supply Current|Icc|||1.6|A||
|Module total power|P|||4.5|W|1|
|Transmitter|||||||
|Signaling rate per lane||25.78||27.95|Gb/s||
|Diferential data input swing per lane|Vin,pp|||900|mV||
|Diferential input return loss (min) at LR4|RLd(f)|9.5 – 0.37f, 0.01≤f<8<br>4.75 – 7.4log10(f/14), 8 ≤f<19|||dB||
|Diferential to common mode input return loss<br>(min) at LR4|RLdc(f)|22-20(f/25.78), 0.01≤f<12.89<br>15-6(f/25.78), 12.89≤f<19|||dB||
|Diferential input return loss (min) at OTU4|SDD11|-11, 0.05<f<fb<br>-6.0+9.2log10(2f/fb), fb/7<f<fb|||dB||
|Diferent to common mode input return loss (min)<br>at OTU4|SDC11<br>SCD11|-22+14(f/fb), 0.05<f<fb/2<br>-18+6f/fb, fb/2<f<fb|||dB||
|Diferential termination mismatch||||10|%||
|Stressed input parameters|||||||
|Eye width|||0.46||UI||
|Applied pk-pk sinusoidal jitter||Per IEEE 802.3bm Table 88-13|||||
|Eye height|||95||mV||
|DC common mode voltage||-350||2850|mV||



4 

**FTLC1154SDPLD** 


**----- Start of picture text -----**<br>
Receiver<br>**----- End of picture text -----**<br>


|Receiver|||||||
|---|---|---|---|---|---|---|
||||||||
|Signaling rate per lane||25.78125||27.9525|GBd||
|Diferential data output swing|Vout,pp|100||400|mVpp|3|
|||300||600|||
|||400||800|||
|||600||1200|||
|Eye width|EW15|0.57|||UI|4|
|Eye height|EH15|228|||mV|4|
|Vertical eye closure||||5.5|dB||
|Diferential output return loss (min) at LR4|RLd(f)|9.5 – 0.37f, 0.01≤f<8<br>4.75 – 7.4log10(f/14), 8 ≤f<19|||dB||
|Common to diferential mode conversion return<br>loss (min) at LR4|RLdc(f)|22-20(f/25.78), 0.01≤f<12.89<br>15-6(f/25.78), 12.89≤f<19|||dB||
|Diferential output return loss (min) at OTU4|SDD22|-11, 0.05<f<fb<br>-6.0+9.2log10(2f/fb), fb/7<f<fb|||dB|2|
|Common to diferential mode conversion return<br>loss (min) at OTU4|SDC22 SCD22|-25+20(f/fb), 0.05<f<fb/2<br>-18+6f/fb, fb/2<f<fb|||dB|2|
|Common mode return loss at OTU4|SCC22|||-2|dB|5|
|Common mode noise, RMS||||17.5|mV||
|Diferential termination mismatch||||10|%||
|Transition time, 20% to 80% at LR4|tr tf|12|||ps||
|Transition time, 20% to 80% at OTU4|tr tf|9.5|||ps||



Notes: 

1. Maximum total power value is specified across the full temperature and voltage range. Power consumption ≤ 4.5W when stabilized (both Tx and Rx CDR locked), but may be ≤ 5W during locking acquisition. 

2. fb is the data rate per lane in Gb/s 

3. Output voltage is settable in 4 discrete ranges via I2C. Default range is 400 – 800 mV. 

4. Defined at 10-15 probability. 

5. From 250 MHz to 30 GHz. 

5 

**FTLC1154SDPLD** 

## **IV. Optical Characteristics (EOL, TOP = -40 to 85 °C, VCC = 3.315 to 3.465 Volts)** 

## **OTU4 4I1-9D1F Operation** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transmitter|||||||
|Signaling Speed per Channel||27.9525± 20 ppm|||Gb/s|1|
|Channel center wavelengths (range)||1294.53 – 1296.59<br>1299.02 – 1301.09<br>1303.54 – 1305.63<br>1308.09 – 1310.19|||nm||
|Total Average Launch Power|POUT|||10|dBm||
|Average Launch Power per Channel|TXPx|-0.6||4.0|dBm|5|
|Optical Channel Extinction Ratio|ER|4.0||6.5|dB||
|Channel Power Diference|∆POUT|||5|dB||
|Optical Return Loss|ORL|||20|dB||
|Transmitter eye mask defnition {X1,<br>X2, X3, Y1, Y2, Y3}||{0.25, 0.4, 0.45, 0.25, 0.28, 0.4}||||2|
|Receiver|||||||
|Signaling Speed per Channel||27.9525± 20 ppm|||GBd|3|
|Channel center wavelengths (range)||1294.53 – 1296.59<br>1299.02 – 1301.09<br>1303.54 – 1305.63<br>1308.09 – 1310.19|||nm||
|Average Input Power per Channel|RXPx|-6.9||4.0|dBm|4,5|
|Optical Path Penalty|OPP|||1.5|dB||
|Equivalent Sensitivity per Channel|Rxsens|||-8.4|dBm|4|
|Total Average Input Power|PIN|||10.0|dBm||
|Channel Power Diference|∆PIN|||5.5|dB||
|LOS De-Assert|LOSD|||-11.6|dBm||
|LOS Assert|LOSA|-24||-13.6|dBm||
|LOS Hysteresis|||1.5||dBm||



Notes: 

1. Transmitter consists of 4 lasers operating at 27.95Gb/s each. 

2. Hit ratio 5x10-5. 

3. Receiver consists of 4 photodetectors operating at 27.95Gb/s each. 

4. Specified at a BER of 10-6 (pre-FEC), per ITU-T G.sup39. 

5. Power value and power accuracy are with all channels on. 

6 

**FTLC1154SDPLD** 

## **100GBASE-LR4 Operation** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transmitter|||||||
|Signaling Speed per Channel||25.78125 ± 100 ppm|||Gb/s|1|
|Channel center wavelengths (range)||1294.53 – 1296.59<br>1299.02 – 1301.09<br>1303.54 – 1305.63<br>1308.09 – 1310.19|||nm||
|Total Average Launch Power|POUT|||10.5|dBm||
|Transmit OMA per Lane|TxOMA|-1.3||4.5|dBm||
|Average Launch Power per Lane|TXPx|-4.3||4.5|dBm|2,7|
|Optical Extinction Ratio|ER|4|||dB||
|Sidemode Suppression ratio|SSRmin|30|||dB||
|Average launch power of OFF<br>transmitter, per lane||||-30|||
|Relative Intensity Noise|RIN|||-130|||
|Optical Return Loss Tolerance||||20|||
|Transmitter Refectance||||-12|||
|Transmitter eye mask defnition {X1,<br>X2, X3, Y1, Y2, Y3}||{0.25, 0.4, 0.45, 0.25, 0.28, 0.4}||||3|
|Receiver|||||||
|Signaling Speed per Lane||25.78125 ± 100 ppm|||GBd|4|
|Channel center wavelengths (range)||1294.53 – 1296.59<br>1299.02 – 1301.09<br>1303.54 – 1305.63<br>1308.09 – 1310.19|||nm||
|Receive Power (OMA) per Lane|RxOMA|||4.5|dBm||
|Average Receive Power per Lane|RXPx|-14.5||4.5|dBm|5,7|
|Unstressed Receiver Sensitivity<br>(OMA) per Lane|Rxsens|||-12.5|dBm||
|Receiver Sensitivity (OMA) per Lane|Rxsens|||-8.6|dBm||
|Return Loss|RL|-26|||dB||
|Stressed Receiver Sensitivity (OMA) per Lane|SRS|||-10|dBm|6,8|
|Receive electrical 3 dB upper cutof frequency,<br>per lane||||31|GHz||
|LOS De-Assert|LOSD|||-13.5|dBm||
|LOS Assert|LOSA|-24||-14|dBm||
|LOS Hysteresis|||1.5||dBm||



Notes: 

1. Transmitter consists of 4 lasers operating at 25.78Gb/s each. 

2. Minimum value is informative. 

3. Hit ratio 5x10[-5] . 

4. Receiver consists of 4 photodetectors operating at 25.78Gb/s each. 

5. Minimum value is informative, equals min TxOMA with infinite ER and max channel insertion loss. 

6. SRS is measured with vertical eye closure penalty of 1.8 dB max, J2 of 0.30 UI, and J9 of 0.47 UI. 

7. Power value and power accuracy are with all channels on. 

8. Measured with 4WDM MSA[7] conformance test signal at TP3 for 5x10[-5 ] BER. 

7 

**FTLC1154SDPLD** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Units Ref.<br>**----- End of picture text -----**<br>


|Parameter|Parameter|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|---|
|||||||||
|Bit Rate (all wavelengths combined)||BR|103.1||112.0|Gb/s|1|
|Bit Error Ratio @25.78Gb/s||BER1|||10-12||2|
|Bit Error Ratio @27.95Gb/s||BER2|||10-6||3|
|Maximum Supported Distances||||||||
|Fiber Type||||||||
|SMF per G.652||Lmax1|||20|km||



Notes: 

1. Supports OTU4 4I1-9D1F per ITU-T G.959.1 and 100GBASE-LR4 per IEEE 802.3ba. 

2. Tested with a 231 – 1 PRBS. 

3. Tested with a 231 – 1 PRBS. Per ITU-T G.959.1 and G.sup39, the BER of 10-12 for the OTU4 (112 Gb/s) application code is required to be met only after forward error correction has been applied. ITU-T G.sup39 defines the pre-FEC BER to be met as 10-6. The values for receiver sensitivity and optical path penalty measured at the receiver output at a BER of 10-6 will normally be conservative estimates of the values for receiver sensitivity and path penalty at the BER of 10-12 after the FEC decoder. 

## **VI. Environmental Specifications** 

Finisar FTLC1154SDPLD QSFP28 transceivers have an operating case temperature range of -40°C to +85°C. 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-40||+85|°C||
|Storage Temperature|Tsto|-40||+85|°C||



## **VIII. Regulatory Compliance** 

Finisar FTLC1154SDPLD QSFP28 transceivers are Class 1 Laser Products. They are certified per the following standards: 


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

FTLC1154SDPLD QSFP28 transceivers support the I2C-based diagnostics interface specified by the SFF Commitee1. See also Finisar Application Notes AN-2152[4] and AN- 2153[5] . 

## **IX. Memory Contents** 

Per SFF-8665 Specification[1] . See Finisar Application Note AN-2152[4] . For CFP replacement applications, the transceiver module can be customized to enable Tx_Disable and Rx_LOS functions as alternate functions on LPMode and IntL pins. See Finisar Application Note AN-2174[8] for more details. 

8 

**FTLC1154SDPLD** 

## **XI. Mechanical Specifications** 

Finisar FTLC1154SDPLD transceivers are compatible with the QSFP28 Specification for pluggable form factor modules. 


Figure 2. FTLC1154SDPLD Mechanical Dimensions. 


Figure 3. Product Label (Not to Scale) 

9 

**FTLC1154SDPLD** 

## **X. References** 

## **1.** 

SFF-8665: “QSFP+ 28Gb/s 4X Pluggable Transceiver Solution (QSFP28)”, Rev 1.9, June 29, 2015 (and associated SFF documents) 

i. SFF-8661 

ii. SFF-8679 iii. SFF-8636 iv. SFF-8662 

v. SFF-8663 vi. SFF-8672 vii. SFF-8683 

2. IEEE 802.3ba, PMD Type 100GBASE-LR4. 

3. IEEE 802.3bm, Annex 83E, CAUI-4 Interface. 

4. Application Note AN-2152: EEPROM Map, Finisar Corporation. 

5. Application Note AN-2153: Initialization, Finisar Corporation. 

6. Directive 2011/65/EU of the European Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment,” July 1, 2011. 

7. Application Note AN-2038: Finisar Implementation Of RoHS Compliant Transceivers, Finisar Corporation. 

8. Application Note AN-2174: QSFP28 LR4 and QSFP28 CWDM4 – Tx_Disable and Rx_LOS Capability, Finisar Corporation. 

© 2023 Coherent Corp. photonics.sales@coherent.com Legal notices : coherent.com/legal www.coherent.com 

