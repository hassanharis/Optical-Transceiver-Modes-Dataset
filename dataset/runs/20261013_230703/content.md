Optical Transceivers 

## FTLF8536P5XYZ 

## **25GBASE-SR 100m SFP28 Finisar® Transceiver** 

FTLF8536P5xyz SFP28 transceiver modules are designed for use in 25 Gigabit per second links over multimode fiber. They are compliant to IEEE802.3by, SFF-8472 Rev 12.2band SFF-8402g, and compatible with SFF-8432aand applicable portions of SFF-8431 Rev. 4.1c. The transceiver is RoHS compliant as described in Application Note AN-2038. 


## FEATURES 

## APPLICATIONS 

- Up to 25.78 Gb/s bi-directional data links 

- Hot-pluggable SFP+ footprint 

- Built-in digital diagnostic functions 

   - 25GE SR and 10GE SR Lite 

   - 100G SR4 fan out to 4x25GE SR 

   - eCPRI 

- 850nm Oxide VCSEL laser transmitter 

- Duplex LC connector 

- Bail latch or pull tab 

- RoHS compliant 

- 100m over M5F MMF (50/125 um OM4) 

- 70m over M5E MMF (50/125um OM3) 

- Metal enclosure, for lower EMI 

- 1W maximum power consumption 

- Single 3.3V power supply 

- Single rate and dual rate 

- Operating temperature range: C-temp: 0°C to 70°C E-temp: 0°C to 85°C 

**FTLF8536P5Xyz** 

## **Product Selection** 

## **FTLF8536P5xyz** 

x=B: Bail latch x=P: Pull tab y=C: C-temp y=N: E-temp z=L: Single rate (25GbE only) z=V: Dual rate (25GbE and 10GbE) 

## **I. Pin Descriptions** 


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLF8536P5Xyz** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line (MOD-DEF2)|4|
|5|SCL|2-wire Serial Interface Clock (MOD-DEF1)|4|
|6|MOD_ABS|Module Absent, connected to VEETor VEER|4|
|7|RS0|Rx Rate Select<br>Single rate (FTLF8536P5xyL): Not Connected (NC)<br>Dual rate (FTLF8536P5xyV):<br>Open or Low = 10.3 Gb/s Ethernet (Low Bandwidth)<br>High = 25.78 Gb/s Ethernet (High Bandwidth)|5|
|8|RX_LOS|Loss of Signal indication. Logic 0 indicates normal operation.|6|
|9|RS1|Tx Rate Select<br>Single rate (FTLF8536P5xyL): Not Connected (NC)<br>Dual rate (FTLF8536P5xyV):<br>Open or Low = 10.3 Gb/s Ethernet (Low Bandwidth)<br>High = 25.78 Gb/s Ethernet (High Bandwidth)|5|
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

4. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. MOD_ABS pulls line low to indicate module is plugged in. 5. Rate select can also be set through the 2-wire bus in accordance with SFF-8472 v. 12.1c. Rx Rate Select is set at Bit 3, Byte 110, Address A2h. Tx Rate Select is set at Bit 3, Byte 118, Address A2h. Note: writing a “1” selects maximum bandwidth operation. Rate select is the logic OR of the input state of Rate Select Pin and 2-wire bus. 

6. LOS is open collector output. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

3 

**FTLF8536P5Xyz** 

## **II. Absolute Maximum Ratings** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Case Operating Temperature|TC|0<br>0||70<br>85|°C||
|Relative Humidity (Non-condensing)|RH|0||85|%|1|



Notes: 

1. Non-condensing. 

## **III. Electrical Characteristics (TA, VCC = 3.15 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.15||3.46|V||
|Supply Current|Icc|||290|mA|1|
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|2|
|Single-ended data input swing|Vin,pp|125||450|mV|3|
|Inner Eye Height (@ 25.78Gb/s)|EH6|95|||mV||
|Transmit Disable Voltage|VD|2||Vcc|V|4|
|Transmit Enable Voltage|VEN|Vee||Vee+0.8|V||
|Receiver|||||||
|Single ended data output swing|Vout,pp|185||425|mV|5|
|LOS Fault|VLOS fault|2||VccHOST|V|6|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|6|
|Power Supply Rejection|PSR|100|||mVpp|7|



Notes: 

1. With established link. The total power dissipation could exceed 1W when the module is trying to establish link at operating case temperature below 25oC 

2. Connected directly to TX data input pins. AC coupling from pins into laser driver IC. 

3. The minimum value represents the minimum outer eye amplitude. 

4. Or open circuit. 

5. Into 100 ohms differential termination. 

6. LOS is an open collector output. Should be pulled up with 4.7k – 10kohms on the host board. Normal operation is logic 0; loss of signal is logic 1. Maximum pull-up voltage is 5.5V. 

7. Receiver sensitivity is compliant with power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specified value applied through the recommended power supply filtering network. 

4 

**FTLF8536P5Xyz** 

## **IV. Optical Characteristics (TAVCC3 = 3.15 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Average Output Power|POUT|-8.4||2.4|dBm|1|
|Optical Wavelength|λ|840||860|nm||
|Spectral Width (RMS)|σ|||0.60|nm||
|Optical Modulation Amplitude<br>25.78Gb/s (Single and Dual Rate) 10.3Gb/s (Dual<br>Rate only)|OMA|-6.4<br>-5.2||3|dBm||
|Launch power in OMA minus TDEC||-7.3|||dBm||
|Transmitter Dispersion Penalty @ 10.3Gb/s|TDP|||3.9|dB||
|Transmitter and Dispersion Eye Closure @ 25.7Gb/s|TDEC|||4.3|dB||
|Average Launch Power of OFF transmitter|POFF|||-30|dBm||
|Optical Return Loss Tolerance|ORLT|||12|dB||
|Extinction Ratio @ 25.78Gb/s|ER|2|||dB||
|Receiver|||||||
|Damage Threshold|RxDamage|3.4|||dBm|2|
|Stressed Receiver OMA Sensitivity<br>25.78Gb/s (Single and Dual Rate) 10.3Gb/s<br>(Dual Rate only)|RxSENS|||-5.2<br>-7.5|dBm|3|
|Unstressed Receiver OMA<br>Sensitivity @ 10.3Gb/s|RxSENS|||-11.1|dBm|4|
|Average Receiver Power @ 25.78Gb/s|RxMAX|-10.3||2.4|dBm|5|
|Optical Center Wavelength|λC|840||860|||
|Optical Return Loss||12|||||
|LOS De-Assert|LOSD|||-13|||
|LOS Assert|LOSA|-30|||||
|LOS Hysteresis||0.5|||||



## Notes: 

1. Class 1 Laser Safety limit per FDA/CDRH, and EN (IEC) 60825 laser safety standards. 

2. The receiver shall be able to tolerate, without damage, continuous exposure to an optical input signal having this average power level. The receiver does not have to operate correctly at this input power. 

3. Measured with conformance test signal at TP3 (see IEEE P802.3bm 95.8.8) for BER 5E-5. 

4. Unstressed receiver OMA sensitivity is informative. 

5. Average receive power (min) is informative and not the principal indicator of signal strength. A received power below this value cannot be compliant; however, a value above this does not ensure compliance. 

5 

**FTLF8536P5Xyz** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Data Rate<br>Dual Rate<br>Single Rate|BR||25.78 and 10.3<br>25.78||Gb/sec||
|Bit Error Rate|BER|5E-5<br>1E-12||||1, 2|
|Fiber Length on 50/125µm high- band-<br>width (OM3/M5E) MMF|L|||70|m||
|Fiber Length on 50/125µm high- band-<br>width (OM4/M5F) MMF|L|||100|m||



Notes: 

1. At 25.78Gb/s Ethernet data rate (IEEE 802.3by) 

2. At 10.3Gb/s Ethernet data rate (Dual Rate only) 

## **VII. Environmental Specifications** 


**----- Start of picture text -----**<br>
Environmental Specifications Symbol  Min  Typ  Max  Units  Ref.<br>**----- End of picture text -----**<br>


|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Case Operating Temperature<br>C-temp (FTLF8536P5xCz)<br>E-temp (FTLF8536P5xNz)|Top|0<br>0||70<br>85|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

The FTLF8536P5xyz transceivers are RoHS compliant. Copies of certificates are available from II-VI Incorporated upon request. 

FTLF8536P5xyz transceiver modules are Class 1 laser eye safety compliant per IEC 60825-1. 

CAUTION: Use of controls or adjustments or performance of procedures other than those specified herein may result in hazardous radiation exposure. 

6 

**FTLF8536P5Xyz** 

## **VIII. Digital Diagnostic Functions** 

Finisar® FTLF8536P5xyz SFP28 transceivers support the 2-wire serial communication protocol as defined in the SFP MSAf. It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar® SFP transceivers provide a enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in E[2] PROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN-2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFP MSA documentation[c,f ] and Finisar Application Note AN-2030. 

## **TX Equalization Control @ 25G** 

Tx input equalization control can be accessed through 2-wire serial interface at byte address 114 (A2h). Tx input equalization control for 25GE is located at the upper 4 bits of byte 114 (A2h) while the lower 4 bits are reserved for rate low in the case of dual rate application. 

## **RX Emphasis Control @ 25G** 

Rx output emphasis control can be accessed through 2-wire serial interface at byte address 115 (A2h). Rx output emphasis control for 25GE is located at the upper 4 bits of byte 115 (A2h) while the lower 4 bits are reserved for rate low in the case of dual rate application. 

## **IX. Digital Diagnostic Specifications** 

FTLF8536P5xyz transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Units Min Max Accuracy Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Units|Min|Max|Accuracy|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transceiver Temperature<br>C-temp (FTLF8532P5xCz)<br>E-temp (FTLF8532P5xNz)|DDDTemp|ºC|0<br>0|+70<br>+85|±5ºC||
|Transceiver supply voltage|DDDVoltage|V|3.14|3.45|±3%||
|Transmitter bias current|DDDBias|mA|0|20|±10%|1|
|Transmitter output power|DDDTx-Power|dBm|-9|+2.4|±3dB||
|Receiver average optical input power|DDDRx-Power|dBm|-11|+2.4|±3dB||



Notes: 

1. Accuracy of Measured Tx Bias Current is 10% of the actual Bias Current from the laser driver to the laser. 

7 

**FTLF8536P5Xyz** 

## **X. Mechanical Specifications** 

Finisar® FTLF8536P5xyz SFP28 transceivers are compatible with the SFF-8432b specification for improved pluggable form factor. 



**----- Start of picture text -----**<br>
  FTLF8536P5Byz (Bail latch)<br>**----- End of picture text -----**<br>



FTLF8536P5Pyz (Pull tab) 

8 

**FTLF8536P5Xyz** 

## **XI. PCB Layout and Bezel Recommendations** 


9 

**FTLF8536P5Xyz** 



10 

**FTLF8536P5Xyz** 

## **XII. Ordering Information** 


**----- Start of picture text -----**<br>
Part Number Unlocking Mechanism Operating Temp Range Data Rate<br>**----- End of picture text -----**<br>


|Part Number|Unlocking Mechanism|Operating Temp Range|Data Rate|
|---|---|---|---|
|||||
|FTLF8536P5BCL|Bail latch|0°C to 70°C|25GbE only|
|FTLF8536P5BCV|Bail latch|0°C to 70°C|25GbE and 10GbE|
|FTLF8536P5BNL|Bail latch|0°C to 85°C|25GbE only|
|FTLF8536P5BNV|Bail latch|0°C to 85°C|25GbE and 10GbE|
|FTLF8536P5PCL|Pull tab|0°C to 70°C|25GbE only|
|FTLF8536P5PCV|Pull tab|0°C to 70°C|25GbE and 10GbE|
|FTLF8536P5PNL|Pull tab|0°C to 85°C|25GbE only|
|FTLF8536P5PNV|Pull tab|0°C to 85°C|25GbE and 10GbE|



## **XII. References** 

a. “Improved Pluggable Form Factor”, SFF Document Number SFF-8432, Revision 5.0, July 16, 2007. 

b. “Digital Monitoring Interface for Optical Transceivers”, SFF Document Number SFF-8472, Revision 12.2. 

c. “Enhanced Small Form Factor Pluggable Module ‘SFP+’ ”, SFF Document Number SFF-8431, Revision 4.1, July 6, 2009; Addendum Jun 21, 2013. 

d. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. 08-June 2011, which supercedes the previous ROHS Directive 2002/95/EC. 

e. Small Form Factor Pluggable (SFP) Transceiver Multi-source Agreement (MSA), September 14, 2000 which is available as SFF Document Number INF-8074, 

Revision 1.0 May 12, 2001 

f. “0.8mm Card Edge Connector for 16Gb/s Applications”, SFF Document Number SFF-8081, Revision 0.2, December 21, 2009. 

g. SFF-8402, Revision 0.2 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

