Optical Transceivers 

## FTLF1323P1XTR 

## **OC-3 IR-1/STM S-1.1 RoHS Compliant Pluggable SFP Transceiver** 

FTLF1323P1xTR Small Form Factor Pluggable (SFP) transceivers are compatible with the Small Form Factor Pluggable Multi-Sourcing Agreement (MSA)[1] . They comply with SONET and SDH standards[2] at OC-3 IR-1/STM S-1.1 and OC-3 SR/ STM I-1, and are suitable for Fast Ethernet applications. Digital diagnostics functions are available via the 2-wire serial bus specified in the SFP MSA. The optical transceiver is compliant per the RoHS Directive 2011/65/EU[3] . See Finisar Application Note AN-2038 for more details[4] . 


## FEATURES 

## APPLICATIONS 

- Up to 155 Mb/s bi-directionaldata links 

- Hot-pluggable SFP footprint 

- Built-in digital diagnostic functions 

   - SONET OC-3 IR-1 / SDH STM S-1.1 

   - SONET OC-3 SR / SDH STM I-1 

   - Suitable for Fast Ethernet 

- Uncooled Fabry-Perot 1310nm laser transmitter 

- Duplex LC connector 

- RoHS compliant and lead-free 

- Metal enclosure, for lower EMI 

- Single 3.3V power supply 

- Low power dissipation <700mW typical 

- Industrial operating temperature range: -40°C to 85°C 

**FTLF1323P1XTR** 

## **Product Selection** 

## **FTLF1323P1xTR** 

x W Wide Extraction Bail B Narrow Extraction Bail 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLF1323P1XTR** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.||
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|2|
|4|MOD_DEF(2)|Module Defnition 2. Data line for Serial ID.|3|
|5|MOD_DEF(1)|Module Defnition 1. Clock line for Serial ID.|3|
|6|MOD_DEF(0)|Module Defnition 0. Grounded within the module.|3|
|7|Rate Select|No connection required|4|
|8|LOS|Loss of Signal indication. Logic 0 indicates normal operation.|5|
|9|VEER|Receiver Ground (Common with Transmitter Ground)|1|
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

2. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

3. Should be pulled up with 4.7k - 10kohms on host board to a voltage between 2.0V and 3.5V. MOD_DEF(0) pulls line low to indicate module is plugged in. 

4. Finisar FTLF1322xxxxx transceivers operate without active control. 

5. LOS is open collector output. Should be pulled up with 4.7k - 10kohms on host board to a voltage between 2.0V and 3.5V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

## **II. Absolute Maximum Ratings** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Maximum Supply Voltage|Vcc|-0.5||4.5|V||
|Storage Temperature|TS|-40||100|°C||
|Case Operating Temperature|TOP|-40||85|°C||
|Relative Humidity|RH|0||85|%|1|



3 

**FTLF1323P1XTR** 

## **III. Electrical Characteristics (TOP = -40 to 85 °C,  VCC = 3.10 to 3.50 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.10||3.50|V||
|Supply Current|Icc||165|300|mA||
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|2|
|Single ended data input swing|Vin,pp|250||1200|mV||
|Transmit Disable Voltage|VD|Vcc – 1.3||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V|3|
|Transmit Disable Assert Time||||10|us||
|Receiver|||||||
|Single ended data output swing|Vout,pp|300|400|800|mV|4|
|Data rise/fall time|tr||250|500|ps|5|
|LOS Fault|VLOS fault|Vcc – 0.5||VccHOST|V|6|
|LOS Normal|VLOS norm|Vee||Vee+0.5|V|6|
|Power Supply Rejection|PSR|100|||mVpp|7|



Notes: 

1. Non condensing. 

2. AC coupled. 

3. Or open circuit. 

4. Into 100 ohm differential termination. 

5. 20 – 80 % 

6. Loss Of Signal is LVTTL. Logic 0 indicates normal operation; logic 1 indicates no signal detected. 

7. All transceiver specifications are compliant with a power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specified value applied through the power supply filtering network shown on page 23 of the Small Form-factor Pluggable (SFP) Transceiver MultiSource Agreement (MSA), September 14, 2000. Valid on receive side for input powers within receive sensitivity. 

4 

**FTLF1323P1XTR** 

## **IV. Optical Characteristics (TOP = -40 to 85 °C , VCC = 3.10 to 3.50 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Output Opt. Pwr: 9/125 SMF|POUT|-15||-8|dBm|1|
|Optical Wavelength|λ|1261||1360|nm||
|Spectral Width|δ|||7.7|nm||
|Optical Extinction Ratio|ER|10|||dB||
|Optical Rise/Fall Time|tr/ tf|||500|ps|2|
|Relative Intensity Noise|RIN|||-120|dB/Hz||
|Generated Jitter (peak to peak)|JTXp-p|||0.07|UI|3|
|Generated Jitter (rms)|JTXrms|||0.007|UI|3|
|Mask Margin|||20%||||
|Receiver|||||||
|Average Rx Sensitivity @ OC-3|RSENS1|-28||-8|dBm|4|
|Average Rx Sensitivity @ 125 Mb/s|RSENS2|-28||-8|dBm|4|
|Optical Center Wavelength|λC|1260||1600|nm||
|LOS De-Assert|LOSD|||-28|dBm||
|LOS Assert|LOSA|-45|||dBm||
|LOS Hysteresis||0.5|||dB||



Notes: 

1. Class 1 Laser Safety per FDA/CDRH and EN (IEC) 60825 regulations. 

2. Unfiltered, 20-80% 

3. Jitter measurements taken using Agilent OMNIBERT 718 in accordance with GR-253. 

4. With worst-case extinction ratio. Measured with a PRBS 2[23] -1 test pattern. 

5 

**FTLF1323P1XTR** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Data Rate|BR|125||155|Mb/sec|1|
|Bit Error Rate|BER|||10-12||2|
|Max. Supported Link<br>Length on 9/125µm SMF<br>@ OC-3|LMAX5||15||km|4|



Notes: 

5. Compliant with SONET and SDH at the following rates: OC-3 IR-1/STM S-1.1 and OC-3 SR/STM I-1. 

6. Tested with a PRBS 2[23] -1 test pattern. 

7. Attenuation of 0.55 dB/km is used for the link length calculations (per GR-253 CORE). Distances are indicative only. Please refer to the Optical Specifications in Table IV to calculate a more accurate link budget based on specific conditions in your application. 

## **VI. Environmental Specifications** 

Finisar 1310nm SFP transceivers have an industrial operating temperature range from –40°C to +85°C case temperature. 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-40||85|°C||
|Storage Temperature|Tsto|-40||100|°C||



## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements of EN (IEC) 60825 and the electrical safety requirements of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

6 

**FTLF1323P1XTR** 

## **VIII. Digital Diagnostic Functions** 

Finisar FTLF1323P1xTR SFP transceivers support the 2-wire serial communication protocol as defined in the SFP MSA[1] . It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar SFP transceivers provide a unique enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory-set normal range. 

The SFP MSA defines a 256-byte memory map in E[2] PROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN-2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFP MSA documentation1 or Finisar Application Note AN-2030. 

Digital diagnostics for the FTLF1323P1xTL are externally calibrated by default. 

Please note that evaluation board FDB-1018 is available with Finisar ModDEMO software that allows simple to use communication over the 2-wire serial interface. 

7 

**FTLF1323P1XTR** 

## **IX. Mechanical Specifications** 

Finisar’s Small Form Factor Pluggable (SFP) transceivers are compatible with the dimensions defined by the SFP Multi-Sourcing Agreement (MSA)[3] . 


FTLF1323P1BTR 


FTLF1323P1WTR 

8 

**FTLF1323P1XTR** 

## **X. PCB Layout and Bezel Recommendations** 


9 

**FTLF1323P1XTR** 



10 

**FTLF1323P1XTR** 

## **XII. References** 

1. Small Form Factor Pluggable (SFP) Transceiver Multi-Source Agreement (MSA), September 2000. Documentation is currently available at Finisar upon request. 

2. Bellcore GR-253 and ITU-T G.957 Specifications. 

3. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. Certain products may use one or more exemptions as allowed by the Directive. 

4. “Application Note AN-2038: Finisar Implementation of RoHS Compliant Transceivers” 

© 2023 Coherent Corp. photonics.sales@coherent.com Legal notices : coherent.com/legal www.coherent.com 

