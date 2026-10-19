Optical Transceivers 

## FTLF1318P3BTL 

## **Industrial Temperature 1.25 Gb/s RoHS Compliant  LongWavelength Pluggable SFP Transceiver** 

FTLF1318P3BTL Small Form Factor Pluggable (SFP) transceivers are compatible with the Small Form Factor Pluggable Multi-Sourcing Agreement (MSA)[4] . They simultaneously comply with Gigabit Ethernet as specified in IEEE Std 802.31 and 1x Fibre Channel as defined in FC-PI-4 Rev. 8.003. The optical transceivers are compliant per the RoHS Directive 2011/65/ EU. See Finisar Application Note AN-2038 for more details. Digital diagnostics functions are available via the 2-wire serial bus specified in the SFP MSA. 


## FEATURES 

## APPLICATIONS 

- Up to 1.25Gb/s bi-directional data links 

- Hot-pluggable SFP footprint 

   - 1.25Gb/s 1000Base-LX Ethernet 

   - 1.06 Gb/s Fibre Channel 

- Built-in digital diagnostic functions 

- 1310nm Fabry-Perot laser transmitter 

- Duplex LC connector 

- RoHS compliant and Lead Free 

- Up to 10 km on 9/125μm SMF 

- Metal enclosure for lower EMI 

- Single 3.3V power supply 

- Low power dissipation <600mW typical 

- Industrial operating temperature range: -40°C to 85°C 

**FTLF1318P3BTL** 

## **Product Selection** 

## **FTLF1318P3BTL** 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Pinout of Connector Block on Host Board 

2 

**FTLF1318P3BTL** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|MOD_DEF(2)|Module Defnition 2. Data line for Serial ID.|4|
|5|MOD_DEF(1)|Module Defnition 1. Clock line for Serial ID.|4|
|6|MOD_DEF(0)|Module Defnition 0. Grounded within the module.|4|
|7|Rate Select|No connection required|5|
|8|LOS|Loss of Signal indication. Logic 0 indicates normal operation.|6|
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

2. TFAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V. A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Should be pulled up with 4.7k - 10 kohms on host board to a voltage between 2.0V and 3.6V. MOD_DEF(0) pulls line low to indicate module is plugged in. 

5. Finisar FTLF1318xxxxx transceivers operate at 1x Fibre Channel and Gigabit Ethernet data rates and respective protocols without active control. 

6. LOS is open collector output. Should be pulled up with 4.7k – 10 kohms on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

## **II. Absolute Maximum Ratings** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Maximum SupplyVoltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||100|°C||
|Case OperatingTemperature|TA|-40||85|°C||
|Relative Humidity|RH|0||85|%|1|



3 

**FTLF1318P3BTL** 

## **III. Electrical Characteristics (TA = -40 to 85 °C, VCC = 3.0 to 3.6 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.0||3.6|V||
|Supply Current|Icc|||300|mA||
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|2|
|Single ended data input swing|Vin,pp|250||1200|mV||
|Transmit Disable Voltage|VD|2||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V|3|
|Transmit Disable Assert Time||||10|us||
|Receiver|||||||
|Single ended data output swing|Vout,pp|250|450|800|mV|4|
|Data output rise time|tr|0.6||300|ps|5|
|Data output fall time|tf|0.6||300|ps|5|
|LOS Fault|VLOS fault|2||VccHOST|V|6|
|LOS Normal|VLOS norm|Vee||Vee+0.5|V|6|
|Power Supply Rejection|PSR|100|||mVpp|7|
|Deterministic Jitter Contribution|RX Δ DJ|||80|ps|8|
|Total Jitter Contribution|RX Δ TJ|||122.4|ps||



Notes: 

1. Non-condensing. 

2. AC coupled. 

3. Or open circuit. 

4. Into 100 ohm differential termination. 

5. 20 – 80 % 

6. LOS is LVTTL. Logic 0 indicates normal operation; logic 1 indicates no signal detected. 

7. All transceiver specifications are compliant with a power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specified value applied through the power supply filtering network shown on page 23 of the Small Form-factor Pluggable (SFP) Transceiver MultiSource Agreement (MSA), September 14, 2000. 

8. Measured with DJ-free data input signal. In actual application, output DJ will be the sum of input DJ and Δ DJ. 

4 

**FTLF1318P3BTL** 

## **IV. Optical Characteristics (Top =-40 to 85°C, VCC = 3.00 to 3.60 Volts)** 

|Parameter|Symbol|Min|Typ|7BMax|Unit|Ref.|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Output Opt. Power|POUT|-9.5||-3|dBm|1|
|Optical Wavelength|λ|1270||1355|nm|2|
|Spectral Width|δ|||3|nm|2|
|Optical Modulation Amplitude|OMA|174|||ns|2,3|
|Optical Rise/Fall Time|tr/ tf||150|260|ns|4|
|RIN||||-120|dB/Hz||
|Deterministic Jitter Contribution|TX Δ DJ||20|56.5|ns|5|
|Total Jitter Contribution|TX Δ TJ||50|119|ns||
|Optical Extinction Ratio|ER|9|||dB||
|Receiver|||||||
|Average Rx Sensitivity @ 1.25 Gb/s (Gigabit<br>Ethernet)|RSENS2|||-19|dBm|6, 7|
|Average Rx Sensitivity @ 1.06 Gb/s (1X Fibre<br>Channel)|RSENS1|||-21|dBm|6, 7|
|Stressed RX sens. = 1.25 Gb/s||||-14.5|dBm||
|Average Received Power|RxMAX|||0|dBm||
|Receiver Elec. 3 dB cutof freq.||||1500|MHz||
|Optical Center Wavelength|λC|1265||1600|nm||
|Return Loss||12|||dB||
|LOS De-Assert|LOSD|||-19|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|||dB||



Notes: 

1. Class 1 Laser Safety per FDA/CDRH and EN (IEC) 60825 regulations. 

2. Also specified to meet curves in FC-PI-4 Rev. 8.00 Figure 21, which allow trade-off between wavelength, spectral width and OMA. 

3. Equivalent extinction ratio specification for Fibre Channel. Allows smaller ER at higher average power. 

4. Unfiltered, 20-80%. Complies with IEEE 802.3 (Gig. E) and FC 1x eye masks when filtered. 

5. Measured with DJ-free data input signal. In actual application, output DJ will be the sum of input DJ and Δ DJ. 

6. Measured with conformance signals defined in FC-PI-4 Rev. 8.00 specifications. 

7. Measured with PRBS 2[7] -1 at 10[-12] BER 

5 

**FTLF1318P3BTL** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Data Rate|BR|1062||1250|Mb/sec|1|
|Bit Error Rate|BER|||10-12||2|
|Max. Supported Link Length on 9/125 μm<br>SMF @ 1X Fibre Channel|LMAX1||10||km|3, 4|
|Max. Supported Link Length on 9/125 μm<br>SMF @ Gigabit Ethernet|LMAX2||10||km|3, 4|



Notes: 

1. Gigabit Ethernet and 1x Fibre Channel compliant. 

2. Tested with a PRBS 27-1 test pattern. 

3. Dispersion limited per FC-PI-4 Rev. 8.00 

4. Attenuation of 0.55 dB/km is used for the link length calculations. Distances are indicative only. Please refer to the Optical Specifications in Table IV to calculate a more accurate link budget based on specific conditions in your application. 

## **VI. Environmental Specifications** 

Finisar 1310nm Industrial Temperature SFP transceivers have an operating temperature range from -40°C to +85°C case temperature. 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-40||85|°C||
|Storage Temperature|Tsto|-40||100|°C||



## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements of EN (IEC) 60825 and the electrical safety requirements of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

6 

**FTLF1318P3BTL** 

## **VIII. Digital Diagnostic Functions** 

Finisar FTLF8519P3xyL SFP transceivers support the 2-wire serial communication protocol as defined in the SFP MSA[1] . It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar SFP transceivers provide a unique enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in E[2] PROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN- 2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFP MSA documentation[1,5] or Finisar Application Note AN-2030. 

Please note that evaluation board FDB-1018 is available with Finisar ModDEMO software that allows simple to use communication over the 2-wire serial interface. 

7 

**FTLF1318P3BTL** 

## **IX. Digital Diagnostic Specifications** 

FTLF8519P2xyL transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Units Min Typ Max Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Units|Min|Typ|Max|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transceiver temperature|DDDTemp|ºC|-40|+85|±5ºC||
|Transceiver supply voltage|DDDVoltage|V|3.14|3.45|±3%||
|Transmitter bias current|DDDBias|mA|0|60|±10%|1|
|Transmitter output power|DDDTx-Power|dBm|-11.5|-1|±3dB||
|Receiver average optical input power|DDDRx-Power|dBm|-23|+2|±3dB||



## Notes: 

1. Accuracy of Measured Tx Bias Current is 10% of the actual Bias Current from the laser driver to the laser. 

8 

**FTLF1318P3BTL** 

## **X. Mechanical Specifications** 

Finisar’s Small Form Factor Pluggable (SFP) transceivers are compatible with the dimensions defined by the SFP Multi-Sourcing Agreement (MSA)[ 3] . 


FTLF1318P3BTL 

9 

**FTLF1318P3BTL** 

## **XI. PCB Layout and Bezel Recommendations** 


10 

**FTLF1318P3BTL** 



11 

**FTLF1318P3BTL** 

## **XII. References** 

1. IEEE Std 802.3, 2002 Edition, Clause 38, PMD Type 1000BASE-LX. 

IEEE Standards Department, 2002. 

2. “Fibre Channel Physical and Signaling Interface (FC-PH, FC-PH2, FC-PH3)”. American National Standard for Information Systems. 

3. “Fibre Channel Physical Interface-4 Specification (FC-PI-4 Rev. 8.00)”. American National Standard for Information Technology, May 21, 2008. 

4. Small Form-factor Pluggable (SFP) Transceiver Multi-source Agreement (MSA), September 14, 2000. 

5. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. Certain products may use one or more exemptions as allowed by the Directive. 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

