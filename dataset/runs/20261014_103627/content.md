

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach TRS70xxFxCPA000-x 

www.lumentum.com 

Data Sheet 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

The Lumentum Tunable SFP+ module is a high performance tunable pluggable transceiver for use in the C-band window covering 1528 nm to 1566 nm. The module supports data rates from 9.95 Gbps to 11.3 Gbps and is provided in an SFP+, MSA-compliant package. 

The optical transmitter utilizes the Lumentum tunable ILMZ chip to provide a high performance, low cost 10 Gbps transceiver. Channel tuning is supported on the  ITU-T 50 GHz grid  across full C band with ±2.5 GHz stability. Wavelength and frequency tuning modes are supported in accordance with SFF-8690. 

The receive path comprises an APD receiver with limiting amplifier. 

Mechanical dimensions, connecters and footprint conform to SFP+ MSA. The module size is 56.5 mm L x 13.9 mm W x 11.85 mm H with 20-pin electrical connector. 

## Key Features 

- 1550 nm ITU-T C-band 50 GHz spacing tunable DWDM SFP+ transceiver 

- Data rate 9.95-1.3 Gbps 

- Supports 80 km link distances 

- Negative/zero chirp transmitter with ILMZ (integrated laser Mach Zehnder) TOSA 

- APD receiver with limiting amplifier 

- Positive power supply lines: 3.3 V 

- Operating case temperature range: up to industrial temperature 

- Compact size (56.5 mm L x 13.9 mm W x 11.85 mm H) 

## Compliance 

- SFF-8431 – Enhanced 8.5 and 10 Gigabit Small Form Factor Pluggable Module (SFP+) 

- SFF-8432 - Improved Pluggable Form factor 

- SFF-8690 - Tunable SFP+ Memory Map for ITU Frequencies 

- SFF-8472 - Diagnostic Monitoring Interface for Optical Xcvrs 

- INF-8074i - SFP (Small Form Factor) Transceiver 

- IEEE802.3ae CL 52 - IEEE 802.3 Standard (10Gigabit Ethernet Clause) 

- MIL-STD-883, Method 3015.4 

- IEC61000-4-2:Edition1 (Air Discharge) 

- Class 1 Laser Safety 

This document may contain technologies regulated by law [ECCN: 5E001.c.1, 5E001.c.2.d, 5E991 as of April 2005]. In the case of the export of product(s) and/or technologies described in this document, please take the appropriate procedure in conforming to all regulations related to the export. 

www.lumentum.com 

2 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

## Functional Description 

1 SFI Data Interface 


**----- Start of picture text -----**<br>
ASIC / Host SerDes SFP+ Module<br>DC block 50Ω<br>100Ω D C' C Amp / ROSA<br>DC block 50Ω<br>Connect or<br>50Ω DC block<br>A B' B 100Ω LD Driver / TOSA<br>50Ω DC block<br>**----- End of picture text -----**<br>


Figure 1 Interface to host 

Table 1: SFP+ Module Transmitter Electrical Characteristics at B'' 


**----- Start of picture text -----**<br>
Parameter @ B’’ Symbol Minimum Maximum Units<br>Eye mask X1 0.12 UI<br>Eye mask X2 0.33 UI<br>Eye mask Y1 95 mV<br>Eye mask Y2 350 mV<br>Y2<br>Y1<br>0<br>-Y1<br>-Y2<br>0.0   X1            X2   1-X2        1-X1   1.0<br>Normalized Time (UI)<br>**----- End of picture text -----**<br>


Figure 2 Eye mask at B’’ 

Table 2: SFP+ Module Receiver Electrical Characteristics at C’ 


**----- Start of picture text -----**<br>
Parameter @ C’ Symbol Minimum Maximum Units<br>Eye Mask X1 0.35 UI<br>Eye Mask Y1 150 mV<br>Eye Mask Y2 - 425 mV<br>Y2<br>Y1<br>0<br>-Y1<br>-Y2<br>0.0               X1         1-X1              1.0<br>Normalized Time (UI)<br>**----- End of picture text -----**<br>


Figure 3 SFP+ eye mask at C’ 

www.lumentum.com 

3 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

## 2 Low Speed Control Pins 

- TX_Fault 

- TX_Disable 

- Mod_ABS 

- RX_LOS 

## Table 3: Low Speed Control Pin Logic Levels 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Maximum Unit Conditions<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Minimum|Maximum|Unit|Conditions|
|---|---|---|---|---|---|
|||||||
|Host VCCRange|Host_VCC|3.14|3.47|V|with ± 5% variation|
|TX_Fault,<br>RX_LOS|VOL|0.0|0.40|V|Note 1|
||VOH|Host_VCC– 0.5|Host_VCC+ 0.3|V|Note 1|
|TX_Disable|VIL|-0.3|0.8|V|Pulled up with 10k ohms to VccT in<br>the module.|
||VIH|2.0|VCCT + 0.3|V||



Note: 

1. Rpullup (Rp) is the pull up resistor. Active bus termination may be used by the host in place of a pullup resistor. Pull ups can be connected to multiple power supplies, however the host board design shall ensure that no module pin has voltage exceeding module. Measured at the Host side of the connector. 

TX_Fault is a module output pin that when High, indicates that the module transmitter has detected a fault condition related to laser operation or safety. The TX_Fault output pin is an open drain/collector and must be pulled up to the Host_Vcc with 4.7k-10kΩ on the host board 

TX_Disable is a module input pin. When TX_Disable is asserted High or left open, the SFP+ module transmitter output must be turned off. The TX_Disable pin is pulled up to VccT with 10kΩ in the SFP+ module. The TX_Disable pin works for TX_fault_Reset as well. 

Mod_ABS is pulled up to Host_Vcc with 4.7k-10kΩ on the host board and connected to VeeT or VeeR in the SFP+ module. Mod_ABS is then asserted “High” when the SFP+ module is physically absent from a host slot. In the SFP MSA (INF8074i) this pin had the same function but is called MOD_DEF0. 

RX_LOS when high indicates an optical signal level below that specified in the relevant standard. The RX_LOS pin is an open drain/ collector output and must be pulled up to host Vcc with a 4.7k-10kΩ on the host board. RX_LOS assert min and de-assert max are defined in the relevant standard. 

www.lumentum.com 

4 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

## 3 2-Wire Interface I[2] C: SDA & SCL 

SCL is the 2-wire interface clock and SDA is the 2-wire interface data line. SCL and SDA are pulled up with a voltage in the range of 3.14 V to 3.47 V on the host. SFP+ low speed interface is based on 2-wire interface. SFP+ 2-wire interface is based on low voltage TTL (LVTTL) operating with a supply of 3.3 V ±5% and are given in Table 4. This specification ensures compatibility  between host masters and SFP+ SCL/SDA lines and compatibility with I2C. All voltages are referenced to VeeT. 

Note: After an interruption in protocol, power loss or system reset, the 2-wire part can be reset by following these steps: 

1. Clock up to 9 cycles. 

2. Look for SDA high in each cycle while SCL is high. 

3. Create a start condition. 

## Table 4: 2-Wire Interface Physical Interface 


**----- Start of picture text -----**<br>
Parameter Symbol Min. Max. Unit Conditions<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min.|Max.|Unit|Conditions|
|---|---|---|---|---|---|
|||||||
|Host VCCrange|Host_VCC|3.14|3.47|V||
|SCL and SDA|VOL|0.0|0.40|V|Rpullup1pulled to<br>Host_VCC.IOL(max) = 3 mA|
||VOH|Host_VCC– 0.5|Host_VCC+ 0.3|V|Rpullup1pulled to Host_VCC|
|SCL and SDA|VIL|-0.3|VCCT *0.3T|V||
||VIH|VCCT * 0.7|VCCT + 0.5|V||
|Input current on SCL and SDA pins|IL|-10|10|µA||
|Capacitance on SCL and SDA pins|Ci<br>2||14|pF||
|Total bus capacitance for SCL and<br>SDA|Cb<br>3||100|pF|At 400 kHz, Rp(max) = 3.0 kΩ<br>At 100 kHz, Rp(max) = 8.0 kΩ|
||||290|pF|At 400 kHz, Rp(max) = 1.1 kΩ<br>At 100 kHz, Rp(max) = 2.75 kΩ|



Note: 

1. Rpullup (Rmodule pin has voltage exceeding module. M easured at the Host side of the connector. VccT/R + 0.5 V nor requires the module to sink more than 3.0 mA current. p) is the pull up resistor. Active bus termination may be used by the host in place of a pullup resistor. Pull ups can be connected to multiple power supplies, however the host board design shall ensure  that no 

2. Ci is the capacitance looking into the module SCL and SDA pins 

3. Cb is the total bus cap acitance on the SCL or SDA bus 


**----- Start of picture text -----**<br>
Host SFP+ Module<br>Host_Vcc<br>Rp<br>SDA<br>Cb Ci<br>Host_Vcc<br>Rp<br>SCL<br>Cb Ci<br>**----- End of picture text -----**<br>


Figure 4 2-Wire interface physical interface 

www.lumentum.com 

5 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

Table 5: SFP+ 2-Wire Interface Timing Requirements 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Maximum Unit Conditions<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Minimum|Maximum|Unit|Conditions|
|---|---|---|---|---|---|
|||||||
|Clock frequency|fSCL|100|400|kHz||
|Clock pulse width low|tLOW|1.3||µs||
|Clock pulse width high|tHIGH|0.6||µs||
|Time bus free before new<br>transaction can start|tBUF|20||µs|Between STOP and START|
|START hold time|tHD,STA|0.6||µs||
|START set-up time|tSU,STA|0.6||µs||
|Data in hold time|tHD,DAT|0||µs||
|Data in set-up time|tSU,DAT|0.1||µs||
|Input rise time (100 kHz)|tR,100||1000|ns|Note 1|
|Input rise time (400 kHz)|tR,400||300|ns|Note 1|
|Input fall time (100 kHz)|tF,100||300|ns|Note 1|
|Input fall time (400 kHz)|tF,400||300|ns|Note 1|
|STOP set-ip time|tSU,ST O|0.6||µs||
|Serial interface clock holdoff “clock<br>stretching”|T_clock<br>_hold||500|µs|Maximum time the SFP+ may<br>hold the SCL line low before<br>continuing R or W operation|
|Complete single or sequential write|tWR||40|ms|Complete (up to) 8 Byte write|
|Endurance (write cycles)||10 k||Cycles|@ Max operating temperature|



Note: 

1. From (VIL, MAX – 0.15) to (VIH, MIN + 0.15) 


**----- Start of picture text -----**<br>
tHIGH tR tF<br>SCL tLow<br>tHD,STA<br>tSU,STA tHD,DAT tSU,DAT tSU,STO<br>tR<br>tF<br>SDA In<br>START ReSTART STOP<br>SDA Out<br>**----- End of picture text -----**<br>


Figure 5 SFP+ timing diagram 

www.lumentum.com 

6 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

## **4 SFP+ Module Timing** 

In the below figures are shown the required timing for TX_Fault and TX_Disable in various conditions. For more detail, please refer to SFF-8431. 

## Table 6: SFP+ Timing Requirements 


**----- Start of picture text -----**<br>
Parameter Symbol Min imum Maximum  Unit Conditions<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min imum|Maximum|Unit|Conditions|
|---|---|---|---|---|---|
|||||||
|TX_disable assert time|t_off||100|µs|Rising edge of TX_Disable to fall of output signal below 10% of<br>nominal.|
|TX_disable negate time|T_on||2|ms|Falling edge of TX_Disable to rise of output signal above 90% of<br>nominal. This only applies in normal operation, not during start up<br>or fault recovery.|
|Time to initialize 2-wire interface|t_2w_<br>start_up||300|ms|From power on or hot plug after the supply meeting Table 9.|
|Time to initialize cooled module and<br>time to power up a cooled module to<br>Power Level II|t_start_<br>up_c<br>ooled||90|sec|From power supplies meeting Table 9 or hot plug, or Tx disable<br>negated during power up or Tx_Fault recovery, until cooled power<br>level II part during fault recovery is fully operational. Also, from<br>stop bit low-to-high SDA transition enabling Power Level II until<br>cooled module is fully operational|
|Tx_fault assert for cooled module|Tx_fault_<br>on_cooled||1|ms|From occurence of fault to assertion of TX_Fault|
|Tx_fault_reset|t_reset|10||µs|Time TX_disable must be held high to reset TX_Fault.|
|RX_LOS assert delay|t_los_on||100|µs|From occurrence of loss of signal to assertion of RX_LOS.|
|RX_LOS negate delay|t_los_off||100|µs|From occurrence of presence of signal to negation of RX_LOS.|



## 5 Maximum Current Ramp on Power supply 

In the below figure and table are shown the required inrush current characteristics for the module power pins. 

## Table 7: Inrush Current 

|Parameter|Symbol|Minimum|Maximum|Unit|Remarks|
|---|---|---|---|---|---|
|Icc instantaneous peak current|||600|mA|Note 1, 2|
|Icc sustained peak current|||500|mA|Note 1, 2|



Note: 

1. The maximum currents are the allowed currents for each power supply VccT or VccR, therefore the total module peak currents can be twice this value. The instantaneous peak current is allowed to exceed the specified maximum current capacity of the connector contact for a short period. 

2. Not to exceed the sustained peak limit for more than 50 μs; may exceed this limit for shorter durations 

www.lumentum.com 

7 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

## PERFORMANCE SPECIFICATIONS 

## 6 Absolute Maximum Ratings 

Stresses in excess of the absolute maximum ratings can cause permanent damage to the transceiver. 

## Table 8: Absolute Maximum Ratings 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Maximum Unit Remarks<br>**----- End of picture text -----**<br>


||Symbol|Minimum|Maximum|Unit|Unit|
|---|---|---|---|---|---|
|||||||
|Supply voltage|VCCT|0|+3.6|V|+3.3 V|
|Supply voltage|VCCR|0|+3.6|V|+3.3 V|
|Optical receiver input|PIMAX||+5|dBm|Average|
|Storage temperature|TSTR|-40|+85|°C||
|ESD SFI pins|ESD1||1|kV|HBM|
|ESD except for SFI pins|ESD2||2|kV|HBM|



## 7 Operating Environment 

Electrical and optical characteristics below are defined under this operating environment, unless otherwise specified. 

## Table 9: Operating Environment 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Typical Maximum Unit Remarks<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Minimum|Typical|Maximum|Unit|Remarks|
|---|---|---|---|---|---|---|
||||||||
|Supply voltage|VCCT|3.135|3.300|3.465|V|+3.3 V|
|Supply voltage|VCCR|3.135|3.300|3.465|V|+3.3 V|
|Operating case temperature|TC|0||+70|°C|C-temp|
|||-5||+85||E-temp|
|||-40||+85||I-temp|



www.lumentum.com 

8 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

## 8 Optical Interface Characteristics Table 10  Optical Characteristics 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Typical Maximum Unit Remarks<br>**----- End of picture text -----**<br>


|_Transmitter_|_Transmitter_|_Transmitter_|_Transmitter_|_Transmitter_|_Transmitter_|_Transmitter_|
|---|---|---|---|---|---|---|
|Data rate||9.95||11.3|Gbps|NRZ|
|Frequency range||191.35||196.10|THz|50 GHz grid, 96 channels|
|Frequency accuracy||-2.5||+2.5|GHz|EOL|
|Optical transmit power|Po|-1.0||+3.0|dBm|EOL|
|Shuttered output power||||-35|dBm||
|Optical power stability|ΔPo|-1.0||+1.0|dB|All channels, SOL|
|Side mode suppression|SMSR|35|||dB|±2.5 nm, modulated|
|Spectral width|Δλ||0.3|0.5|nm|-20 dB, modulated|
|Extinction ratio|ER|9.0|||dB|Filtered, 10.709 Gbps|
|Eye diagram compliance||GR-253, ITU-T G.691|||||
|Mask margin||10|||%||
|Tuning speed||||10|s|Warmed-up, from any CH to any other CH|
|_Receiver_|||||||
|Data rate||9.95||11.3|Gbps|NRZ|
|Input operating wavelength||1525||1575|nm||
|Minimum receiver sensitivity (back<br>to back)|Prmin|||-24|dBm|10.709 Gbps, 1E-12, OSNR>35 dB|
|Minimum receiver Sensitivity<br>(-300~+1400 ps/nm)|Prmin|0||-21|dBm||
|Maximum input power (overload)|Pro|-7|||dBm||
|Receiver Refectance|RL|||-27|dB||
|LOS assert||||-27|dBm|Note 1|
|LOS de-assert||||-25|dBm|Note 1|
|LOS hysteresis||0.5||4.0|dB|Note 1|
|LOS assert time||||100|us||
|LOS de-assert time||||100|us||



Note 1: 


**----- Start of picture text -----**<br>
LVTTL -High<br>0.5dB<br>Hysteresis min. LVTTL -Low<br>Optical input power<br>(dBm ave.)<br>-27 dBm ave.  -25 dBm ave.<br>LOS assert max. LOS De-assert max.<br>**----- End of picture text -----**<br>


Figure 6 Rx LOS assert and de-assert 

www.lumentum.com 

9 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

|9||Pin out Defnition|
|---|---|---|
|Table|11|Pin Description|




**----- Start of picture text -----**<br>
Pin Logic Symbol Power Sequence Order Name/Description Notes<br>**----- End of picture text -----**<br>


|9<br>Pin out Defnition<br>Table 11<br>Pin Description|9<br>Pin out Defnition<br>Table 11<br>Pin Description|9<br>Pin out Defnition<br>Table 11<br>Pin Description|9<br>Pin out Defnition<br>Table 11<br>Pin Description|9<br>Pin out Defnition<br>Table 11<br>Pin Description|9<br>Pin out Defnition<br>Table 11<br>Pin Description|
|---|---|---|---|---|---|
|Pin|Logic|Symbol|Power Sequence Order|Name/Description|Notes|
|||||||
|1||VeeT|1st|Module Transmitter Ground|1|
|2|LVTTL-O|TX_Fault|3rd|Module Transmitter Fault|2|
|3|LVTTL-I|TX_Disable|3rd|Transmitter Disable; Turn off laser output|3|
|4|LVTTL-I/O|SDA|3rd|2-Wire Serial Interface Data Line|4|
|5|LVTTL-I/O|SCL|3rd|2-Wire Serial Interface Clock|4|
|6||Mod_Abs|3rd|Module Absent, connected to VeeT or VeeR in the module|5|
|7|LVTTL-I|RS0|3rd|NA. 30kohm pull down inside the module||
|8|LVTTL-O|RX_LOS|3rd|Receiver Loss of Signal Indicator|2|
|9|LVTTL-I|RS1|3rd|NA. 30kohm pull down inside the module||
|10||VeeR|1st|Module Receiver Ground|1|
|11||VeeR|1st|Module Receiver Ground|1|
|12|CML-O|RD-|3rd|Receiver Inverted Data Output(SFI)||
|13|CML-O|RD+|3rd|Receiver Non-Inverted Data Output(SFI)||
|14||VeeR|1st|Module Receiver Ground|1|
|15||VccR|2nd|Module Receiver 3.3V Supply|6|
|16||VccT|2nd|Module Transmitter 3.3V Supply|6|
|17||VeeT|1st|Module Transmitter Ground|1|
|18|CML-I|TD+|3rd|Transmitter Non-Inverted Data Output(SFI)||
|19|CML-I|TD-|3rd|Transmitter Inverted Data Output(SFI)||
|20||VeeT|1st|Module Transmitter Ground|1|



Note: 

1. The module signal ground pins, VeeR and VeeT, are isolated from the module case. 

2. This pin is an open drain output pin and shall be pulled up with 4.7 k-10 kohms to Host_Vcc (Table3) on the host board. Pull ups can be connected to multiple power supplies, however the host board design shall ensure that no module pin has voltage exceeding module VccT/R + 0.5 V. 

3. This pin is an input pin with 10kohms pull up to VccT in the module. 

4. See table 4 and 5: 2-Wire Electrical Specifications . 

5. This pin shall be pulled up with 4.7 k-10 kohms to Host_Vcc on the host board. 

6. VccT and VccR are tied together inside the module. 

www.lumentum.com 

10 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

## 10 Mechanical 

- Comply to SFF-8432, the improved pluggable form factor specification, with technique #2 latch. 

- Comply to optional operational mechanical shock test in issue 2 of GR468. 

## 11 Optical Connector 

LC Connector 

## 12 RoHS 

RoHS compliant per Directive 2011/65/EU of the European Parliament and of the Council of 8 June 2011 on the restriction of the use of certain hazardous substances in electrical and electronic equipment (recast). 

## 13 Mechanical Dimensions and Label Location 


**----- Start of picture text -----**<br>
Side view<br>Color code: Green<br>Top view<br>56.5<br>Side view<br>9.0 47.5<br>44.3<br>37.1<br>Upper side<br>Bottom view<br>Label location<br>13.9 13.7<br>1.55<br>8.5<br>(11.85)<br>1.8<br>**----- End of picture text -----**<br>


Figure 7 Mechanical dimensions and label location 

www.lumentum.com 

11 

Tunable SFP+ 10G DWDM Serial Optical Transceiver with up to 80 km Reach 

## USER INFORMATION 

## 14 Handling Precaution 

CAUTION: Take proper electrostatic-discharge (ESD) precautions which handling these device. These devices are sensitive to ESD 

## 15 Laser Safety 

The transceiver is certified as a Class 1 laser product per international standard IEC 60825-1:2014 3rd edition and is considered non-hazardous when operated within the limits of this specification. This device complies with 21 CFR 1040.10 except for deviations pursuant to Laser Notice No. 50. 



## Caution 

Operating this product in a manner inconsistent with intended usage and specifications may result in hazardous radiation exposure. 

Use of controls or adjustments or performance of procedures other than these specified in this product datasheet may result in hazardous radiation exposure. 

Tampering with this laser product or operating this product outside the limits of this specification may be considered an act of manufacturing and may require recertification of the modified product. 

## **Ordering Information** 

For more information on this or other products and their availability, please contact your local Lumentum account manager or Lumentum directly at customer.service@lumentum.com. 


**----- Start of picture text -----**<br>
TRS  7  0  X  X  F X  C  X X XX X x<br>1 2         3 4 5 6 7 8 9 10<br>Item Parameter Symbol<br>**----- End of picture text -----**<br>


|Item|Parameter|Symbol|
|---|---|---|
||||
||TRS70XX|Tunable SFP+, 10G, 1550 nm, 80 km reach,|
|1|Chirp|8: Negative chirp<br>9: Zero chirp|
|2|Generation|0: 1st generation<br>1: 2nd generation|
|3|Function|F: SONET/SDH and 10GE multi protocol<br>with or without FEC|
|4|Custom/operating<br>temperature range|H: Industrial operating case<br>temperature (-40°C  to 85°C)<br>E: Extended operating case<br>temperature (-5°C to 85°C)<br>N: Commercial operating case<br>temperature (0°C to 70°C)|
|5|Wavelength|“C”: C band WDM wavelength channel|
|6|Rx electrical interface|“P”:  Limiting  interface|
|7|Photo diode type|“A”: APD|
|8|Customized<br>specifcation|00: Standard product|
|9|Revision code|0|
|10|Product status|Fn:    Functional sample<br>(n: null or version number)<br>Wn:  Working sample<br>(n: null or version number)<br>Null: Mass production|





North America Toll Free: 844 810 LITE (5483) 

Outside North America Toll Free: 800 000 LITE (5483) 

China Toll Free: 400 120 LITE (5483) 

© 2020 Lumentum Operations LLC Product specifications and descriptions in this document are subject to change without notice. 

Lumentum Operations LLC 1001 Ridder Park Drive San Jose, CA 95131 

sfp+dwdm10g-ds-oc-ae  30179591  902  0920 

www.lumentum.com 

