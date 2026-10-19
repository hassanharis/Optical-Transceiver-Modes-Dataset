Finisar Transceiver 


**Product S ecification p 400G-FR4 OSFP Finisar Transceiver FTCD4315E1PCL** 

## **PRODUCT FEATURES** 

- Hot-pluggable OSFP form factor 

- Supports 425Gb/s aggregate bit rate 

- Power dissipation <12W 

- RoHS-6 compliant 

- Case temperature range of 0°C to +70°C (C-temp) 

- Single 3.3V power supply 


- Aligned with IEEE P802.3cu 

- 4x100Gb/s PAM4 serial lanes 

- 8x50G PAM4 retimed 400GAUI-8 electrical interface 

## **APPLICATIONS** 

   - 400G FR4 applications with FEC 

- LC duplex receptacle 

- I2C management interface 

FTCD4315E1PCL 400G FR4 OSFP transceiver modules are designed for use in 400 Gigabit Ethernet links on up to 2km of single mode fiber. They are compliant with the OSFP[1] MSA, IEEE P802.3cu[4] and portions of P802.3bs[5] . Digital diagnostic functions are available via the I2C interface, as specified by the OSFP MSA.  The transceiver is RoHS-6 compliant per Directive 2011/65/EU[2] and Finisar Application Note AN-2038[3] . 

## **PRODUCT SELECTION** 

3B 

## **FTCD4315E1PCL** 

E: Ethernet protocol P: Pull-tab type release C: Commercial temperature range L: LC duplex receptacle 

© Coherent Corp.  Jul. 2025  Rev B2 – Coherent Corp. Confidential 

Page 1 

Finisar Transceiver 

FTCD4315E1PCL Product Specification 

## **I. Pin Descriptions** 

The electrical pinout of the OSFP module is shown in Figure 1 below 


**Figure 1 – OSFP compliant connector (per OSFP MSA)** 

© Coherent Corp.  Jul. 2025  Rev B2 – Coherent Corp. Confidential 

Page 2 

Finisar Transceiver 

FTCD4315E1PCL Product Specification 


© Coherent Corp.  Jul. 2025  Rev B2 – Coherent Corp. Confidential 

Page 3 

Finisar Transceiver 

FTCD4315E1PCL Product Specification 


## **II.** 0B **General Product Characteristics** 

|**Parameter**|**Value**|**Unit**|**Notes**|
|---|---|---|---|
|Module Form Factor|OSFP|||
|Maximum Aggregate Data Rate|425|Gb/s||
|Protocols Supported|400G Ethernet|||
|Maximum Power Consumption per End|12|Watts|1|
|Management Interface|Serial, I2C-based, 1 MHz maximum frequency|||



|**Data Rate Specifications**|**Symbol **|**Min**|**Typ **|**Max **|**Units **|**Notes**|
|---|---|---|---|---|---|---|
|BitError Ratio|BER|||2.4E-4||2|
|**Maximum Supported Distances**|||||||
|Fiber Type|||||||
|SMFperG.652|Lmax1|0.002||2|km||



## UNotesU: 

1. Maximum total power value is specified across the full temperature and voltage range. 2. As defined by IEEE P802.3cu. 

© Coherent Corp.  Jul. 2025  Rev B2 – Coherent Corp. Confidential 

Page 4 

Finisar Transceiver 

FTCD4315E1PCL Product Specification 

## **III.** 11B **Absolute Maximum Ratings** 

Module performance is not guaranteed beyond the operating range (see Section VII). Exceeding the limits below may damage the transceiver module permanently. 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Maximum Supply Voltage|Vcc|-0.3||4.0|V||
|Storage Temperature|TS|-40||+85|C||
|Case OperatingTemperature|TOP|0||+70|C|C-temp|
|Relative Humidity|RH|15||85|%|1|
|Receiver Damage Threshold, per Lane|PRdmg|4.5|||dBm||



## UNotesU: 

## 1. Non-condensing. 

##  **IV.** 1B **Electrical Characteristics (EOL, TOP = 0 to +70 C, VCC = 3.135 to 3.465 Volts)** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.135|3.3|3.465|V||
|SupplyCurrent|Icc|||3.828|A||
|Module total power|P|||12|W|1|
|**Transmitter**|||||||
|Signaling rate per lane||26.5625±100 ppm.|||Gbd||
|Differential data input voltage per lane|Vin,pp,diff|900|||mV|2|
|Differential input return loss||Per equation (83E–5)<br>IEEE802.3bm|||dB||
|Differential to common mode input<br>return loss||Per equation (83E–6)<br>IEEE802.3bm|||dB||
|Differential termination mismatch||||10|%||
|Module stress input test||Per 120E.3.4.1<br>IEEE802.3bs||||3|
|Single-ended voltage tolerance range||-0.4||3.3|V||
|DC common mode voltage||-350||2850|mV|4|
|**Receiver**|||||||
|Signaling rate per lane||26.5625±100 ppm.|||Gbd||
|AC common-mode output voltage<br>(RMS)||||17.5|mV||
|Differential output voltage||||900|mV||
|Near-end ESMW (Eye symmetry<br>mask width)||0.265|||UI||
|Near-end Eye height, differential<br>(min)||70|||mV||
|Far-end ESMW (Eye symmetry mask<br>width)||0.2|||UI||
|Far-end Eye height, differential (min)||30|||mV||
|Far-end pre-cursor ISI ratio||-4.5||2.5|dB||
|Differential output return loss||Per equation 83E-2<br>IEEE802.3bm|||||
|Common to differential mode<br>conversion return loss||Per equation 83E-3<br>IEEE802.3bm|||||
|Differential termination mismatch||||10|%||
|Transition time (min, 20% to 80%)||9.5|||ps||
|DC common mode voltage (min)||-350||2850|mV|4|



© Coherent Corp.  Jul. 2025  Rev B2 – Coherent Corp. Confidential 

Page 5 

Finisar Transceiver 

FTCD4315E1PCL Product Specification 

## Notes: 

1. Maximum total power value is specified across the full temperature and voltage range. 

2. With the exception to 120E.3.1.2 that the pattern is PRBS31Q or scrambled idle. 

3. Meets specified BER 

4. DC common mode voltage generated by the host. Specification includes effects of ground offset voltage. 

##  **V.** 2B **Optical Characteristics (EOL, TOP = 0 to +70 C, VCC = 3.135 to 3.465 Volts)** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
|Signalingrate(each lane(range)||53.125 ± 100ppm|||GBd||
|Modulation format|||PAM4||||
|Lane wavelength (range)||1264.5<br>1284.5<br>1304.5<br>1324.5|1271<br>1291<br>1311<br>1331|1277.5<br>1297.5<br>1317.5<br>1337.5|nm||
|Side-mode suppression ratio (SMSR)||30|||dB||
|Total average launch power||||10.4|dBm||
|Average launch power, each lane||||4.4|dBm||
|Average launch power, each lane||-3.2|||dBm|1|
|Difference in launch power between<br>any two lanes (OMAouter) max||||3.9|dB||
|Outer Optical Modulation Amplitude<br>(OMAouter), each lane min<br>for TDECQ1.4 dB<br>for 1.4 dBTDECQ3.4 dB||-0.2<br>-1.6 + TDECQ||3.7|dBm<br>dBm||
|Transmitter and dispersion eye closure<br>for PAM4 (TDECQ), each lane||||3.4|dB||
|Transmitter eye closure for PAM4<br>(TECQ), each lane||||3.4|dB||
|TDECQ–TECQ||||2.5|dB||
|Average launch power of OFF<br>transmitter, each lane||||-16|dBm||
|Extinction ratio||3.5|||dB||
|Transmitter transition time||||17|pS||
|Transmitter over/under-shoot||||22|%||
|Transmitter power excursion||||1.8|dBm||
|RIN17.1OMA||||-136|dB/Hz||
|Optical return loss tolerance||||17.1|dB||
|Transmitter reflectance||||-26|dB|2|



## Notes: 

1. Average launch power, each lane (min) is informative and not the principal indicator of signal strength. A transmitter with launch power below this value cannot be compliant; however, a value above this does not ensure compliance. 

2. Transmitter reflectance is defined looking into the transmitter 

© Coherent Corp.  Jul. 2025  Rev B2 – Coherent Corp. Confidential 

Page 6 

Finisar Transceiver 

FTCD4315E1PCL Product Specification 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|**Receiver**|||||||
|Signalingrate(each lane(range)||53.125 ± 100ppm|||GBd||
|Modulation format||PAM4|||||
|Lane wavelength (range)||1264.5<br>1284.5<br>1304.5<br>1324.5|1271<br>1291<br>1311<br>1331|1277.5<br>1297.5<br>1317.5<br>1337.5|nm||
|Damage threshold, each lane||5.4|||dBm|1|
|Average receive power, each lane||||4.4|dBm||
|Average receive power, each lane||-7.2|||dBm|2|
|Receive power (OMAouter), each lane||||3.7|dBm||
|Difference in receive power between<br>any two lanes (OMAouter)||||4.1|dB||
|Receiver reflectance||||-26|dB||
|Receiver sensitivity (OMAouter), each lane<br>(max) for SECQ < 1.4 dB<br>for 1.4 dBSECQ 3.4 dB||||-4.6<br>-6 + SECQ|dBm<br>dBm||
|Receiver sensitivity (OMAouter),<br>each lane||||-2.6||3|
|Conditions of stressed receiver sensitivity test:4|||||||
|Stressed eye closure for PAM4<br>(SECQ), lane under test||3.4|||dB|4|
|OMAouter of each aggressor lane||1.5|||dBm||



## Notes: 

1. The receiver shall be able to tolerate, without damage, continuous exposure to an optical input signal having this average power level. 

2. Average receive power, each lane (min) is informative and not the principal indicator of signal strength. A received power below this value cannot be compliant; however, a value above this does not ensure compliance. 

3. Measured with conformance test signal at TP3 (see 151.8.13) for the BER specified in 151.1.1. 

4. These test conditions are for measuring stressed receiver sensitivity. They are not characteristics of the receiver. 

## **VI.** 12B **Memory Map and Control Registers** 

Per CMIS4.0. See Finisar Application Note AN-21xx (TBD).. 

## **VII.** 13B **Environmental Specifications** 

Finisar FTCD4315E1PCL FR4 OSFP transceivers have a max. operating case temperature range of 0°C to +70°C. 

|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Ref.**|
|---|---|---|---|---|---|
|Top|0||+70|°C|C-temp|
|Tsto|-40||+85|°C||



© Coherent Corp.  Jul. 2025  Rev B2 – Coherent Corp. Confidential 

Page 7 

Finisar Transceiver 

FTCD4315E1PCL Product Specification 

## **VIII.** 4B **Regulatory Compliance** 

Finisar FTCD4315E1PCL FR4 OSFP transceivers are Class 1 Laser Products. They are certified per the following standards: 

|**Feature**|**Agency**|**Standard**|
|---|---|---|
|Laser Eye<br>Safety|FDA/CDRH|CDRH 21 CFR 1040.10 and Laser<br>Notice 56|
|Laser Eye<br>Safety|UL/CSA/TÜV|IEC/EN 60825-1:2014<br>IEC/EN 60825-2: 2004+A1+A2|
|Electrical<br>Safety|UL/CSA/TÜV|IEC/UL/CSA/EN 62368-1:2014|



CAUTION: Use of controls or adjustments or performance of procedures other than those specified herein may result in hazardous radiation exposure. 

## **IX.** 5B **Mechanical Specifications** 

Finisar FTCD4315E1PCL FR4 OSFP transceivers are compatible with the OSFP Specification for pluggable form factor modules. 


© Coherent Corp.  Jul. 2025  Rev B2 – Coherent Corp. Confidential 

Page 8 

Finisar Transceiver 

FTCD4315E1PCL Product Specification 

**Figure 2.  FTCD4315E1PCL Mechanical Dimensions.** 


**Figure 3.  Product Label (Not to Scale) “Made in Malaysia” version also available under PN “FTCD4315E1PCL-1Y”** 

## **X.** 14B **References** 

1. OSFP Specification for OSFP Octal small form factor pluggable module 

2. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment” as well as Commission Delegated Directive (EU) 2015/863 amending Annex II to Directive 2011/65/EU. Certain products may use one or more exemptions as allowed by the Directive. 

3. Application Note AN-2038: “II-VI Implementation of RoHS Compliant Transceivers”. 

4. IEEE P802.3cu 400GBASE-FR4. 

5. IEEE P802.3bs, 400GAUI-8 Interface. 

## **XI.** 15B **For More Information** 

Coherent Corp. 375 Saxonburg Boulevard Saxonburg, PA  16056 sales@coherent.com Hwww.coherent.comU 

© Coherent Corp.  Jul. 2025  Rev B2 – Coherent Corp. Confidential 

Page 9 

