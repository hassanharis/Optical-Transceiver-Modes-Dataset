Optical Transceivers 

## FTLF1323F2XTR 

## **OC-3 SR-1/STM I-1 or OC-3 IR-1/STM S-1.1 2x5 SFF Transceiver** 

FTLF1323S2xTR Small Form Factor (SFF) transceivers are compatible with the Small Form Factor Multi-Sourcing Agreement (MSA)[1] . They comply with SONET OC-3 SR-1/IR-1 (SDH STM I-1/S-1.1) standards[2] . The transceivers are RoHS compliant and lead-free per Directive 2002/95/EC[5] and Finisar Application Note AN-2038[6] 


## FEATURES 

## APPLICATIONS 

- Up to OC-3/STM-1 bi-directional data links 

- Standard 2x5 pin SFF footprint (MSA compliant) 

   - SONET OC-3 SR-1 / SDH STM I-1 

   - SONET OC-3 IR-1 / SDH STM S-1.1 

- Analog diagnostics functions 

- Uncooled 1310nm FP laser transmitter 

- Duplex LC connector 

- Very low jitter 

- Metal enclosure, for lower EMI 

- Single 3.3V power supply 

- Low power dissipation <700 mW typical 

- Extended operating temperature range: -40°C to 85°C 

**FTLF1323F2xTR** 

## **Product Selection** 

## **FTLF1323F2xTR** 

E: 40GBASE-SR4 compliant optical interface 1: First generation product C: Commercial temperature rate 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|MS|MS|Mounting Studs are for mechanical attachment and are<br>connected to chassis ground. Chassis ground is inter-<br>nally isolated from circuit grounds. Connection to user’s<br>ground plane is recommended.|NA|
|1|VEER|Receiver Ground (Common with Transmitter Ground)|NA|
|2|VCCR|Receiver Power Supply|NA|
|3|SD|Signal Detect. Logic 1 indicates normal operation.|LVTTL|
|4|RD-|Receiver Inverted DATA out. AC Coupled|See Rx spec.|
|5|RD+|Receiver Non-inverted DATA out. AC Coupled|See Rx spec.|
|6|VCCT|Transmitter Power Supply|NA|
|7|VEET|Transmitter Ground (Common with Receiver Ground)|NA|
|8|TDIS|Transmitter Disable|LVTTL|
|9|TD+|Transmitter Non-Inverted DATA in. AC Coupled.|See Tx spec.|
|10|TD-|Transmitter Inverted DATA in. AC Coupled|See Tx spec.|




2 

**FTLF1323F2xTR** 

## **II. Absolute Maximum Ratings** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum Supply Voltage|Vcc|0.5||4.5|V||
|Storage Temperature|TS|-40||100|°C||
|Case Operating Temperature|TA|-40||85|°C||
|Relative Humidity|RH|0||85|%|1|
|Lead Soldering Temperature/Time||||260/10|°C/s||



Notes: 

Non-condensing. 

## **III. Electrical Characteristics (TOP = -40 to 85 °C, VCC = 3.0 to 3.6 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.00||3.60|V||
|Supply Current|Icc||190|300|mA||
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|2|
|Single ended data input swing|Vin,pp|250||1200|mV||
|Transmit Disable Voltage|VD|Vcc – 1.3||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V|3|
|Transmit Disable Assert Time||||10|us||
|Receiver|||||||
|Single ended data output swing|Vout,pp|300|400|800|mV|4|
|Data output rise/fall time|tf|||1250|ps|5|
|SD Assert|VSD assert|2.4||Vcc|V|6|
|SD De-Assert|VSD deassert|Vee||0.5|V|6|
|Power Supply Rejection|PSR|100|||mVpp|7|
|Total Generated Receiver Jitter<br>(peak to peak)|JRXp-p|||0.07|UI||
|Total Generated Receiver Jitter<br>(rms)|JRXrms|||0.007|UI||



Notes: 

1. Non condensing. 

2. AC coupled. 

3. Or open circuit. 

4. Into 100 ohm differential termination. 

5. 20 – 80 % 

6. Signal Detect is LVTTL. Logic 1 indicates normal operation; logic 0 indicates no signal detected. 

7. All transceiver specifications are compliant with a power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specified value applied through the power supply filtering network shown on page 23 of the Small Form-factor Pluggable (SFP) Transceiver MultiSource Agreement (MSA), September 14, 2000. 

3 

**FTLF1323F2xTR** 

## **Optical Characteristics (TOP = -40 to 85°C, VCC = 3.0 to 3.6 Volts)** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ 7BMax Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|7BMax|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transmitter|||||||
|Output Opt. Pwr: 9/125 SMF|POUT|-15||-8|dBm|1|
|Optical Wavelength|λ|1261||1360|nm|2|
|Spectral Width|δ|||7.7|nm|2|
|Optical Extinction Ratio|ER|8.2|||dB||
|Optical Rise/Fall Time|tr/ tf|||1250|ps|3|
|Relative Intensity Noise|RIN|||-120|dB/Hz||
|Total Generated Transmitter Jitter<br>(peak to peak)|JTXp-p|||0.07|UI||
|Total Generated Transmitter Jitter (rms)|JTXrms|||0.007|UI||
|Receiver|||||||
|Rx Sensitivity @ OC-3|RSENS1|-28||-8|dBm|4|
|Rx Sensitivity @ 125Mb/s|RSENS2|-28||-8|dBm|4|
|Optical Center (Input) Wavelength|λC|1260||1600|nm||
|SD Assert|SDA|||-34|dBm||
|SD De-Assert|SDD|-45|||dBm||
|SD Hysteresis||0.5||5|dB||



Notes: 

1. Class 1 Laser Safety per FDA/CDRH and EN (IEC) 60825 regulations. 

2. Also specified to meet curves in FC-PI 13.0 Figures 18 and 19, which allow trade-off between wavelength, spectral width and OMA. 

3. Unfiltered, 20 – 80% 

4. With worst-case extinction ratio. Measured with a PRBS 2[23] -1 test pattern. 

4 

**FTLF1323F2xTR** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol  Min  Typ Max  Units  Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Data Rate|BR|125||156|Mb/sec|1|
|Bit Error Rate|BER|||10-10||2|
|Max. Supported Link Length on<br>9/125μm SMF @ OC-3|LMAX5||15||km|4|



Notes: 

1. SONET OC-3 SR/SDH STM I-1 and SONET OC-3 IR-1/SDH STM S-1.1 compliant. Compatible with Ethernet,. 

2. Tested with a PRBS 2[31] -1 test pattern. 

3. Attenuation of 0.55 dB/km is used for the link length calculations (per GR-253 CORE). Distances are indicative only. Please refer to the Optical Specifications in Table IV to calculate a more accurate link budget based on specific conditions in your application. 

## **VI. Environmental Specifications** 

Finisar 1310nm SFP transceivers have an extended operating temperature range from –40°C to +85°C case temperature. 

|Parameter|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-40||85|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements of EN (IEC) 60825 and the electrical safety requirements of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

## **VIII. Mechanical Specifications** 

Finisar’s OC-3/STM-1 Small Form Factor (SFF) transceivers comply with the standard dimensions defined by the Small Form Factor Multi-Sourcing Agreement (MSA). 

5 

**FTLF1323F2xTR** 


FTLF1323F2GTR – 2 pin version 


FTLF1323F2MTR– 6 pin version 

6 

**FTLF1323F2xTR** 


FTLF1323F2HTR – 6 pin version (Long EMI Shield) 

6 

**FTLF1323F2xTR** 

## **Ix. PCB Layout and Bezel Recommendations** 


Minimum Recommended Pitch is 0.600” 

7 

**FTLF1323F2xTR** 

## **x. References** 

1. Small Form Factor (SFF) Transceiver Multisource Agreement (MSA). January 1998. 

2. Bellcore GR-253 and ITU-T G.957 Specifications (Transmitter Optical Output Power complies with SONET OC-48 requirements only). 

3. IEEE Std 802.3, 2002 Edition, Clause 38, PMD Type 1000BASE-LX. 

IEEE Standards Department, 2002. (Transmit Optical Output has a minimum Extinction Ratio of 8.2 dB only). 

4. Directive 2002/95/EC of the European Council Parliament and of the Council. “On the restriction of the use of certain hazardous substances in electrical and electronic equipment”. January 27, 2003. 

5. “Application Note AN-2038: Finisar Implementation of RoHS Compliant Transceivers: Finisar Corporation, January 21, 2005. 

6. “Fibre Channel Draft Physical Interface Specification (FC-PI 13.0)”. American National Standard for Information Systems. (*) 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

