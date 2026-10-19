Optical Transceivers 

## FTLC9555REPM3 

## **100m Parallel MMF 100G QSFP28 Optical Transceiver** 

FTLC9555REPM3 100G QSFP28 transceiver modules are designed for use in 100 Gigabit Ethernet links over multimode fiber with extended case temperature range of 0°C to 85°C. They are compliant with the QSFP28 MSA[1] and IEEE 802.3bm100GBASE-SR4[2] and CAUI-4[2] . Digital diagnostics functions are available via the I2Cinterface, as specified by the QSFP28 MSA[1] and Finisar Application Note AN-2141[3] . The transceiver is RoHS-6 compliant per Directive 2011/65/EU[4] and Finisar Application Note AN-2038[5] . 


## FEATURES 

## APPLICATIONS 

- Hot-pluggable QSFP28 form factor 

   - 100GBASE-SR4 100G Ethernet 

- Supports 103.1Gb/s aggregate bit rate 

- Power dissipation < 2.5W 

- RoHS-6 compliant 

- Extended case temperature range of 0°C to 85°C 

- Single 3.3V power supply 

- Maximum link length of 100m on OM4 Multimode Fiber (MMF) 

- 4x25Gb/s 850mm VCSEL-based transmitter 

- 4x25G electrical interface 

- Single MPO12 receptacle 

- I2C management interface 

**FTLC9555REPM3** 

## **Product Selection** 

## **FTLC9555REPM3** 

- R: 100G Ethernet maximum bit rate (103.1Gb/s) E: 4x25G parallel optics 

- P: Pull tab release M: MPO receptacle 

- 3: Extended temperature range 

## **I. Pin Descriptions** 


Figure 1 – QSFP28-compliant 38-pin connector (per SFF-8679) 

2 

**FTLC9555REPM3** 


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
|28|IntL|Interrupt||
|29|Vcc Tx|+3.3 V Power supply transmitter||
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

**FTLC9555REPM3** 

## **II. Absolute Maximum Ratings** 

Module performance is not guaranteed beyond the operating range (see Section VI). Exceeding the limits below may damage the transceiver module permanently. 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum SupplyVoltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Case OperatingTemperature|TOP|0||85|°C||
|Relative Humidity|RH|15||85|%|1|
|Receiver Damage Threshold,per Lane|PRdmg|3.4|||dBm||



~~Notes:~~ 

Non-condensing. 

## **III. Electrical Characteristics  (EOL, TOP = 0 to 85 °C, VCC = 3.135 to 3.465 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.135||3.465|V||
|Supply Current|Icc|||1.5|A||
|Module total power|P|||2.5|W|1|
|Transmitter|||||||
|Signaling rate per lane||25.78125 ±|100ppm||Gb/s||
|Diferential data input swing per lane|Vin,pp,dif|||900|mV||
|Stressed input parameters|Vin,pp|-0.35||+3.3|V||
|Module stress input test||Per Section 83E.3.4.1, IEEE 802.3bm|||||
|Receiver|||||||
|Signaling rate per lane||25.78125 ±|100ppm||Gb/s||
|Diferential data output swing|Vout,pp|100||400|mVpp|2|
|||300||600|||
|||400|600|800|||
|||600||1200|||
|Eye width||0.57|||UI||
|Eye height, diferential||228|||mV||
|Vertical eye closure|VEC|5.5|||dB||
|Transition time (20% to 80%)|tr, tf|12|||ps||



## Notes: 

1. Maximum total power value is specified across the full operational temperature and voltage range when CDRs are locked or a lack of input signal results in squelch being activated. If incorrect frequencies cause the CDRs to continuously attempt to lock, maximum power dissipation may reach 3.5 W. 

2. Output voltage is settable in 4 discrete ranges via I2C. Default range is Range 2 (400 – 800 mV). 

4 

**FTLC9555REPM3** 

## **IV. Optical Characteristics (EOL, TOP = 0 to 85 °C, VCC = 3.315 to 3.465 Volts)** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transmitter|||||||
|Signaling Speed per Lane||25.78125 ± 100ppm|||Gb/s|1|
|Center wavelength||840||860|nm||
|RMS Spectral Width|SW|||0.6|nm||
|Average Launch Power per Lane|TXPx|-8.4||2.4|dBm||
|Transmit OMA per Lane|TxOMA|-6.4||3|dBm||
|Launch Power [OMA] minus TDEC per Lane|P-TDEC|-7.3|||||
|TDEC per Lane|TDEC|||4.3|dBm||
|Optical Extinction Ratio|ER|2|||dBm||
|Optical Return Loss Tolerance|ORL|||12|dB||
|Encircled Flux|FLX|>86% at 19 um, <30% at 4.5 um|||dB||
|Average Launch Power of OFF Transmitter,<br>per Lane||||-30|dBm||
|Transmitter Eye mask defnition {X1, X2, X3,<br>Y1, Y2, Y3}||{0.3,0.38,0.45,0.35,0.41,0.5}||||2|
|Receiver|||||||
|Signaling Speed per Lane||25.78125 ± 100ppm|||GBd|3|
|Center wavelength||840||860|nm||
|Damage Threshold|DT|3.4|||dBm||
|Average Receive Power per Lane|RXPx|-10.3||2.4|dBm|4|
|Receive Power (OMA) per Lane|RxOMA|||3|dBm||
|Receiver Refectance|Rf|||-12|dB||
|Stressed Receiver Sensitivity (OMA) per Lane|SRS|||-5.2|dBm||
|Stressed Conditions:|||||||
|Stressed Eye Closure|SEC|4.3|||dB||
|Stressed Eye J2 Jitter|J2|0.39|||UI||
|Stressed Eye J4 Jitter|J4|0.53|||UI||
|OMA of each aggressor lane||3|||dBm||
|Stressed Receiver Eye Mask<br>Defnition {X1, X2, X3, Y1, Y2, Y3}||{0.28,0.5,0.5,0.33,0.33,0.4}|||dBm|5|
|LOS De-Assert|LOSD|||-13|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|2||dB||



Notes: 

1. Transmitter consists of 4 lasers operating at a maximum speed of 25.78125Gb/s ±100ppm each. 

2. Hit Ratio 1.5 x 10[-3] hits/sample. 

3. Receiver consists of 4 photodetectors operating at a maximum speed of 25.78125Gb/s ±100ppm each. 

4. Minimum value is informative only and not the principal indicator of signal strength. 

5. Hit Ratio 5 x 10[-5] hits/sample. 

5 

**FTLC9555REPM3** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Typ Max Units Ref.<br>**----- End of picture text -----**<br>


|Parameter|Parameter|Symbol||Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|---|
|||||||||
|Bit Rate (all wavelengths combined)||BR|||103.1|Gb/s|1|
|Bit Error Ratio (pre-FEC)||BER|||5x10-5||2|
|Maximum Supported Distances||||||||
|Fiber Type||||||||
|OM3 MMF||Lmax1|||70|m|3|
|OM4 MMF||Lmax2|||100|m|3|



Notes: 

1. Supports 100GBASE-SR4 per IEEE 802.3bm. 

2. Tested with a 2[31] – 1 PRBS. 

3. Requires FEC on the host to support maximum distance, per 100GBASE-SR4. 

## **VI. Environmental Specifications** 

Finisar FTLC9555REPM3 QSFP28 transceivers have a extended operating case temperature range of 0°C to +85°C. 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|0||85|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

Finisar FTLC9555 QSFP28 transceivers are Class 1 Laser Products. They are certified per the following standards: 


**----- Start of picture text -----**<br>
Feature Agency Standard<br>**----- End of picture text -----**<br>


|Feature|Agency|Standard|
|---|---|---|
||||
|Laser Eye Safety|FDA/CDRH|CDRH 21 CFR 1040 and Laser Notice 50|
||TÜV|EN 60825-1:2014<br>EN 60825-2:2004+A1+A2|
|Electrical Safety|TÜV|EN 60950-1:2006+A11+A1+A12+A2|
||UL/CSA|CAN/CSA-C22.2 No. 60950-1-07+A2:2014 ANSI/UL Std. No. 60950-1:2014|



Copies of the referenced certificates will be available at Finisar upon request. Complies with FDA performance standards for laser products except for deviations pursuant to Laser Notice No. 50, dated June 24, 2007. 

CAUTION – Use of Controls or adjustments or performance of procedures other than those specified herein may result in hazardous radiation exposure. 

6 

**FTLC9555REPM3** 

## **VIII. Digital Diagnostics Functions** 

FTLC9555REPM3 QSFP28 transceivers support the I2C-based diagnostics interface specified by the QSFP28 MSA[1] . See Finisar Application Note AN-2141[ 3] . 

**IX. Memory Contents** Per the QSFP28 MSA[1] . See Finisar Application Note AN-2141[3] . 

## **XI. Mechanical Specifications** 

Finisar FTLC9555REPM3 QSFP28 transceivers are compatible with the QSFP28 MSA specification[1] . 


Figure 2. FTLC9555REPM Mechanical Dimensions. 


Figure 3. Standard Product Label 

7 

**FTLC9555REPM3** 

## **X. References** 

1. SFF-8665: “QSFP+ 28Gb/s 4X Pluggable Transceiver Solution (QSFP28)”, Rev 1.9, June 29, 2015 (and associated SFF documents) 

   - i. SFF-8661 

   - ii. SFF-8679 iii. SFF-8636 

   - iv. SFF-8662 

   - v. SFF-8663 vi. SFF-8672 

   - vii. SFF-8683 

2. IEEE 802.3bm, PMD Type 100GBASE-SR4 and CAUI-4. 

3. Application Note AN-2141, “100G QSFP28 SR4 NVR Application Note”, Finisar Corporation. 

4. Directive 2011/65/EU of the European Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment,” July 1, 2011. 

5. “Application Note AN-2038: Finisar Implementation Of RoHS Compliant Transceivers”, Finisar Corporation, January 21, 2005. 

© 2023 Coherent Corp. photonics.sales@coherent.com Legal notices : coherent.com/legal www.coherent.com 

