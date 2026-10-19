

## Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver TRS7091FNCDP000-x 

www.lumentum.com 

Data Sheet 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

The Lumentum tunable SFP+ optical transceiver is a high-performance tunable pluggable transceiver for use in the C-band window covering 1528 nm to 1566 nm. The module supports data rates from 9.95 Gbps to 11.3 Gbps and is provided in an SFP+, MSA-compliant package. 

The optical transmitter utilizes the Lumentum tunable ILMZ chip to provide a high performance, low cost 10G transceiver. Channel tuning is supported on the ITU-T 50 GHz grid across full C band with ±2.5 GHz stability. Wavelength and frequency tuning modes are supported in accordance with SFF-8690. 

The receive path comprises a PIN PD receiver with CDR. 

## Key Features 

- 1550 nm ITU-T C-band 50 GHz spacing tunable DWDM SFP+ optical transceiver 

- Data rate 9.95-11.3 Gbps 

- Support ±700 ps/nm dispersion 

- Zero chirp transmitters with ILMZ TOSA 

- PIN PD receiver with CDR 

Mechanical dimensions, connecters and footprint conform to SFP+ MSA. The module size is 56.5 mm L x 13.9 mm W x 11.85 mm H with 20-pin electrical connector. The maximum power consumption is 2.0 W at 70°C, and power supply voltage is +3.3 V. 

- Low power consumption: <2.0 W at 70°C 

- Positive power supply lines: 3.3 V 

- Operating case temperature range: 0°C to 70°C 

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

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

## FUNCTIONAL DESCRIPTION 

1. SFI Data Interface 


**----- Start of picture text -----**<br>
ASIC / Host  SerDes SFP+ Module<br>DC block 50Ω<br>100Ω D C' C Amp / ROSA<br>DC block 50Ω<br>Connect o r<br>50Ω DC block<br>A B' B 100Ω LD Driver / TOSA<br>50Ω DC block<br>**----- End of picture text -----**<br>


Figure 1 Interface to host 

Table 1: SFP+ Module Transmitter Electrical Characteristics at B’’ 


**----- Start of picture text -----**<br>
Parameter @ B’’ Symbol Minimum Maximum Units<br>Eye mask X1 0.12 UI<br>Eye mask X2 0.33 UI<br>Eye mask Y1 95 mV<br>Eye mask Y2 350 mV<br>Y2<br>Y1<br>0<br>-Y1<br>-Y2<br>0.0   X1           X2   1-X2        1-X1 1.0<br>Normalized Time (UI)<br>**----- End of picture text -----**<br>


Figure 2 Eye mask at B’’ 

Table 2: SFP+ Module Receiver Electrical Characteristics at C’ 


**----- Start of picture text -----**<br>
Parameter @ C’ Symbol Minimum Maximum Units<br>Eye mask X1 0.35 UI<br>Eye mask Y1 150 mV<br>Eye mask Y2 425 mV<br>Y2<br>Y1<br>0<br>-Y1<br>-Y2<br>0.0               X1         1-X1              1.0<br>Normalized Time (UI)<br>**----- End of picture text -----**<br>


Figure 3 SFP+ eye mask at C’ 

www.lumentum.com 

3 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

## 2. Low Speed Control Pins 

- TX_Fault 

- TX_Disable 

- Mod_ABS 

- RX_LOS 

Table 3: Low Speed Control Pin Logic Levels 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Maximum Unit Conditions<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Minimum|Maximum|Unit|Conditions|
|---|---|---|---|---|---|
|||||||
|Host VCC Range|Host_VCC|3.14|3.47|V|With ± 5% variation|
|TX_Fault,<br>RX_LOS|VOL|0.0|0.40|V|Note 1|
||VOH|Host_VCC– 0.5|Host_VCC+ 0.3|V|Note 1|
|TX_Disable|VIL|-0.3|0.8|V|Pulled up with 10k ohms to VccT in<br>the module.|
||VIH|2.0|VCCT + 0.3|V||



Note: 

1. Rpullup (Rp) is the pull up resistor. Active bus termination may be used by the host in place of a pullup resistor. Pull ups can be connected to multiple power supplies, however the host board design shall ensure that no module pin has voltage exceeding module. Measured at the Host side of the connector. 

TX_Fault is a module output pin that when High, indicates that the module transmitter has detected a fault condition related to laser operation or safety. The TX_Fault output pin is an open drain/collector and must be pulled up to the Host_Vcc with 4.7k-10k Ω on the host board 

TX_Disable is a module input pin. When TX_Disable is asserted High or left open, the SFP+ module transmitter output must be turned off. The TX_Disable pin is pulled up to VccT with 10k Ω in the SFP+ module. The TX_Disable pin works for TX_fault_Reset as well. 

Mod_ABS is pulled up to Host_Vcc with 4.7k-10k Ω on the host board and connected to VeeT or VeeR in the SFP+ module. Mod_ABS is then asserted “High” when the SFP+ module is physically absent from a host slot. In the SFP MSA (INF8074i) this pin had the same function but is called MOD_DEF0. 

RX_LOS when high indicates an optical signal level below that specified in the relevant standard. The RX_LOS pin is an open drain/ collector output and must be pulled up to host Vcc with a 4.7k-10kΩ on the host board. RX_LOS assert min and de-assert max are defined in the relevant standard. 

www.lumentum.com 

4 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

## 3. 2-Wire Interface I[2] C: SDA & SCL 

SCL is the 2-wire interface clock and SDA is the 2-wire interface data line. SCL and SDA are pulled up with a voltage in the range of 3.14 V to 3.47 V on the host. SFP+ low speed interface is based on 2-wire interface. SFP+ 2-Wire interface is based on Low Voltage TTL (LVTTL) operating with a supply of 3.3 V ±5% and are given in Table 4. This specification ensures compatibility between host masters and SFP+ SCL/SDA lines and compatibility with I[2] C. All voltages are referenced to VeeT. 

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
||VOH|Host_VCC– 0.5|Host_VCC+ 0.3|V|Rpullup1pulled to<br>Host_VCC|
|SCL and SDA|VIL|-0.3|VCCT + 0.5|V||
||VIH|VCCT * 0.7|10|µA||
|Input current on SCL and SDA pins|IL|-10|10|µA||
|Capacitance on SCL and SDA pins|Ci<br>2||14|pF||
|Total bus capacitance for SCL and<br>SDA|Cb<br>3||100|pF|At 400 kHz, Rp(max) = 3.0 kΩ<br>At 100 kHz, Rp(max) = 8.0 kΩ|
||||290|pF|At 400 kHz, Rp(max) = 1.1 kΩ<br>At 100 kHz, Rp(max) = 2.75 kΩ|



Note: 

1. Rpullup (Rthat no module pin has voltage exceeding module. M easured at the Host side of the connector. VccT/R + 0.5 V nor requires the module to sink more than 3.0 mA current. p) is the pull up resistor. Active bus termination may be used by the host in place of a pullup resistor. Pull ups can be connected to multiple power supplies, however the host board design shall ensure 

2. Ci is the capacitance looking into the module SCL and SDA pins 

3. Cb is the total bus cap acitance on the SCL or SDA bus 


**----- Start of picture text -----**<br>
Host SFP+ Module<br>Host_Vcc<br>Rp<br>SDA<br>Cb Ci<br>Host_Vcc<br>Rp<br>SCL<br>Cb Ci<br>**----- End of picture text -----**<br>


Figure 4 2-Wire interface physical interface 

www.lumentum.com 

5 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

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
|Serial interface clock holdoff “clock<br>stretching”|T_clock<br>_hold||500||Maximum time the SFP+ may<br>hold the SCL line low before<br>continuing R or W operation|
|Complete single or<br>sequential write|tWR||40|ms|Complete (up to) 8 Byte write|
|Endurance (write cycles)||10 k||Cycles|@ Max operating temperature|



Note: 

1. From (VIL,MAX – 0.15) to (VIH,MIN + 0.15) 


**----- Start of picture text -----**<br>
tHIGH tR tF<br>SCL tLow<br>tHD,STA<br>tSU,STA tHD,DAT tSU,DAT tSU,STO<br>tR<br>tF<br>SDA In<br>START ReSTART STOP<br>SDA Out<br>**----- End of picture text -----**<br>


Figure 5 SFP+ timing diagram 

www.lumentum.com 

6 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

## **4. SFP+ Module Timing** 

In the below figures are shown the required timing for TX_Fault and TX_Disable in various conditions. For more detail, please refer to SFF-8431. 

## Table 6: SFP+ Timing Requirements 


**----- Start of picture text -----**<br>
Parameter Symbol M in  M ax  Unit Conditions<br>**----- End of picture text -----**<br>


|Parameter|Symbol|M in|M ax|Unit|Conditions|
|---|---|---|---|---|---|
|||||||
|TX_disable assert time|t_off||100|µs|Rising edge of TX_disable to fall of output signal below 10% of nominal.|
|TX_disable negate time|T_on||2|ms|Falling edge of TX_disable to rise of output signal above 90% of nominal.<br>This only applies in normal operation, not during start up or fault recovery.|
|Time to initialize 2-wire interface|t_2w_start_up||300|ms|From power on or hot plug after the supply meeting Table 9.|
|Time to initialize cooled module and<br>time to power up a cooled module to<br>Power Level II|t_start_up_c ooled||90|sec|From power supplies meeting Table 9 or hot plug, or Tx disable   negated<br>during power up or Tx_fault recovery, until cooled power level II part<br>during fault recovery is fully operational. Also, from stop bit low-to-<br>high SDA transition enabling power level II until cooled module is   fully<br>operational|
|Tx_fault assert for cooled module|Tx_fault_on_cooled||1|ms|From occurence of fault to assertion of TX_Fault|
|Tx_fault_reset|t_reset|10||µs|Time TX_disable must be held high to reset TX_Fault.|
|RX_LOS assert delay|t_los_on||100|µs|From occurrence of loss of signal to assertion of RX_LOS|
|RX_LOS negate delay|t_los_off||100|µs|From occurrence of presence of signal to negation of RX_LOS|



## 5. Maximum Current Ramp on Power supply 

In the below figure and table are shown the required inrush current characteristics for the module power pins. 

|Table 7:<br>Inrush Current|Table 7:<br>Inrush Current|Table 7:<br>Inrush Current|Table 7:<br>Inrush Current|Table 7:<br>Inrush Current|Table 7:<br>Inrush Current|
|---|---|---|---|---|---|
|Parameter|Symbol|Min.|Max.|Unit|Remarks|
|Icc instantaneous peak current|||600|mA|Note 1, 2|
|Icc sustained peak current|||500|mA|Note 1, 2|



Note: 

1. The maximum currents are the allowed currents for each power supply VccT or VccR, therefore the total module peak currents can be twice this value. The instantaneous peak current is allowed to exceed the specified maximum current capacity of the connector contact for a short period. 

2. Not to exceed the sustained peak limit for more than 50 μs; may exceed this limit for shorter durations 

www.lumentum.com 

7 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

## PERFORMANCE SPECIFICATIONS 

## Absolute Maximum Ratings 

Stresses in excess of the absolute maximum ratings can cause permanent damage to the transceiver. 

## Table 8: Absolute Maximum Ratings 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Maximum Unit Remarks<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Minimum|Maximum|Unit|Remarks|
|---|---|---|---|---|---|
|||||||
|Supply voltage|VCCT|0|+3.6|V|+3.3 V|
|Supply voltage|VCCR|0|+3.6|V|+3.3 V|
|Optical receiver input|PIMAX||+5|dBm|Average|
|Operating case temperature|Tc|-10|+75|°C|Note 1|
|Storage temperature|TSTR|-40|+85|°C||
|ESD SFI pins|ESD1||1|kV|HBM|
|ESD except for SFI pins|ESD2||2|kV|HBM|



Note: 

1. Case temperature reference point is shown below 


**----- Start of picture text -----**<br>
13.9<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
Case temperature reference point (Top).<br>30<br>56.5<br>10<br>**----- End of picture text -----**<br>


## Operating Environment 

Electrical and optical characteristics below are defined under this operating environment, unless otherwise specified. 

Table 9: Operating Environment 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Typical Maximum Unit Remarks<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Minimum|Typical|Maximum|Unit|Remarks|
|---|---|---|---|---|---|---|
||||||||
|Supply voltage|VCCT|3.135|3.300|3.465|V|+3.3 V|
|Supply voltage|VCCR|3.135|3.300|3.465|V|+3.3 V|
|Operating case temperature|TC|0|25|+70|°C||



## Electrical Performance 

Table 10:  Power Supply Characteristics 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Typical Maximum Unit Remarks<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Minimum|Typical|Maximum|Unit|Remarks|
|---|---|---|---|---|---|---|
||||||||
|Supply voltage|VCCT|3.135|3.300|3.465|V||
||VCCR|3.135|3.300|3.465|V||
|Operating case temperature|Icc3|||0.63|A|Note 1|
||PDS|||2.0|W|Note 2|



Notes: 

1. <0.67 A Tc<5°C 

2. <2.1 W Tc<5°C 

www.lumentum.com 

8 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

## Optical Interface Characteristics 

## Table 11 Optical Characteristics 


**----- Start of picture text -----**<br>
Parameter Symbol Min. Typ Max Unit Remarks<br>**----- End of picture text -----**<br>


|_Transmitter_|_Transmitter_|_Transmitter_|_Transmitter_|_Transmitter_|_Transmitter_|_Transmitter_|
|---|---|---|---|---|---|---|
|Data rate||9.95||11.3|Gbit/s|NRZ|
|Frequency range||191.30||196.05|THz|50 GHz grid, 96 channels|
|Frequency accuracy||-2.5||+2.5|GHz|EOL|
|Optical transmit power|Po|-2.0||+3.0|dBm|EOL|
|Shuttered output power||||-35|dBm||
|Optical power stability|ΔPo|-1.0||+1.0|dB|All channels, SOL|
|Side mode suppression|SMSR|35|||dB|±2.5 nm, modulated|
|Spectral width|Δλ||0.3|0.5|nm|-20 dB, modulated|
|Extinction ratio|ER|9.0|||dB|Filtered, 10.709 Gbps|
|Eye diagram compliance||GR-253, ITU-T G.691|||||
|Mask margin||10|||%||
|_Receiver_|||||||
|Data rate||9.95||11.3|Gbit/s|NRZ|
|Input operating wavelength||1525||1575|nm||
|Minimum receiver sensitivity<br>(back to back)|Prmin|||-14|dBm|10.709 Gbps,<br>1E-12, OSNR>35 dB|
|Maximum input power (overload)|Pro|0|||dBm||
|Receiver refectance|RL|-27|||dB||
|LOS assert||-27|||dBm||
|LOS de-assert||||-20|dBm||
|LOS hysteresis||0.5||4.0|dB||
|LOS assert time||||100|us||
|LOS de-assert time||||100|us||



## System Performance 

## Table 12 System Performance 

|Parameter|Dispersion|OSNR<br>Resolution BW 0.1nm|BER|Remarks|
|---|---|---|---|---|
|OSNR dispersion tolerance|-700 ps/nm|17 dB|1E-04|10.709 Gbps, -3 to -14 dBm,<br>-0.25 nm flter BW, Rx DTV<br>optimized|
||0 ps/nm|15 dB|1E-04||
||700 ps/nm|17 dB|1E-04||



## Jitter Characteristics 

## Table 13  Transmitter Jitter Characteristics (Note 1) 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Typical Maximum Unit Remarks<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Minimum|Typical|Maximum|Unit|Remarks|
|---|---|---|---|---|---|---|
||||||||
|Jitter peaking||||0.03|dB||
|||||1|dB|frequency > 120 kHz|
|Module Jitter Generation at<br>Optical Output||||100|mUIpp|4 MHz to 80 MHz|
|||||300|mUIpp|20 MHz to 80 MHz|



Note: 

1. Data Rate; NRZ at 9.953 Gbps, SONET framed PRBS=2[31] -1 data Jitter Characteristics 

www.lumentum.com 

9 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

Table 14  Receiver Jitter Characteristics (Note[1] ) 


**----- Start of picture text -----**<br>
Parameter Symbol Minimum Typical Maximum Unit Remarks<br>Jitter peaking 0.03 dB<br>1 dB frequency > 120 kHz<br>Jitter tolerance Figure 7<br>Note:<br>1. Data rate; NRZ at 9.953 Gbps, SONET framed PRBS=2 [31] -1 data<br>Slope= -20dB/dec<br>444.6<br>15<br>1.5<br>0.15<br>10 296 2k 20k 400k 4M 80M<br>Frequency [Hz]<br>[UIpp]<br>Amplitude<br>**----- End of picture text -----**<br>


Figure 6 Jitter tolerance 

## Pin out Definition 

Table 15:  Pin Description 


**----- Start of picture text -----**<br>
Pin Logic Symbol Power Sequence Order Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Logic|Symbol|Power Sequence Order|Name/Description|Notes|
|---|---|---|---|---|---|
|||||||
|1||VeeT|1st|Module transmitter ground|1|
|2|LVTTL-O|TX_Fault|3rd|Module transmitter fault|2|
|3|LVTTL-I|TX_Disable|3rd|Transmitter disable; turn off laser output|3|
|4|LVTTL-I/O|SDA|3rd|2-wire serial interface data line|4|
|5|LVTTL-I/O|SCL|3rd|2-wire serial interface clock|4|
|6||Mod_Abs|3rd|Module absent, connected to VeeT or VeeR in the module|5|
|7|LVTTL-I|RS0|3rd|NA. 30 kohm pull down inside the module||
|8|LVTTL-O|RX_LOS|3rd|Receiver loss of signal indicator|2|
|9|LVTTL-I|RS1|3rd|NA. 30 kohm pull down inside the module||
|10||VeeR|1st|Module receiver ground|1|
|11||VeeR|1st|Module receiver ground|1|
|12|CML-O|RD-|3rd|Receiver inverted data output(SFI)||
|13|CML-O|RD+|3rd|Receiver non-inverted data output(SFI)||
|14||VeeR|1st|Module receiver ground|1|
|15||VccR|2nd|Module receiver 3.3V supply|6|
|16||VccT|2nd|Module transmitter 3.3V supply|6|
|17||VeeT|1st|Module transmitter ground|1|
|18|CML-I|TD+|3rd|Transmitter non-inverted data output(SFI)||
|19|CML-I|TD-|3rd|Transmitter inverted data output(SFI)||
|20||VeeT|1st|Module transmitter ground|1|



Note: 

1. The module signal ground pins, VeeR and VeeT, are isolated from the module case. 

2. This pin is an open drain output pin and shall be pulled up with 4.7 k-10 kohms to Host_Vcc (Table3) on thehost board. Pull ups can be connected to multiple power supplies, however the host board design shall ensure that no module pin has voltage exceeding module VccT/R + 0.5 V. 

3. This pin is an input pin with 10kohms pull up to VccT in themodule. 

4. See table 4 and 5: 2-Wire Electrical Specifications . 

5. This pin shall be pulled up with 4.7 k-10 kohms to Host_Vcc on the host board. 

6. VccT and VccR are tied together inside the module. 

www.lumentum.com 

10 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

## Mechanical 

Comply to SFF-8432, the improved Pluggable form factor specification, with technique #2 latch. 

Comply to optional operational mechanical shock test in issue 2 of GR468. 

## Optical Connector 

LC Connector 

## RoHS 

RoHS compliant per Directive 2011/65/EU of the European Parliament and of the Council of 8 June 2011 on the restriction of the use of certain hazardous substances in electrical and electronic equipment (recast). 

## Mechanical Dimensions and label location 


**----- Start of picture text -----**<br>
Side view<br>Color code: Green<br>Top view<br>56.5<br>Side view<br>9.0 47.5<br>44.3<br>37.1<br>Upper side<br>Bottom view<br>Label location<br>13.9 13.7<br>1.55<br>8.5<br>(11.85)<br>1.8<br>**----- End of picture text -----**<br>


Figure 7 Mechanical dimensions and label location 

www.lumentum.com 

11 

Zero Chirp Tunable SFP+ 10G Serial Optical Transceiver 

## USER INFORMATION 

## Handling Precaution 

CAUTION: Take proper electrostatic-discharge (ESD) precautions which handling these device. These devices are sensitive to ESD 

## Laser Safety 

The transceiver is certified as a Class 1 laser product per international standard IEC 60825-1:2014 3rd edition and is considered non-hazardous when operated within the limits of this specification. This device complies with 21 CFR 1040.10 except for deviations pursuant to Laser Notice No. 50. 



## Caution 

Operating this product in a manner inconsistent with intended usage and specifications may result in hazardous radiation exposure. 

Use of controls or adjustments or performance of procedures other than these specified in this product datasheet may result in hazardous radiation exposure. 

## **Ordering Information** 

For more information on this or other products and their availability, please contact your local Lumentum account manager or Lumentum directly at customer.service@lumentum.com. 


**----- Start of picture text -----**<br>
TRS  7  0  9  1  F  N  C  X  X     X X X x<br> 1  2     3    4     5<br>Item Parameter Product Description<br>**----- End of picture text -----**<br>


|Item|Parameter|Product Description|
|---|---|---|
||||
||TRS7091FNC|10G SFP+ tunable optical transceiver,<br>zero chirp, 1550 nm, SONET/SDH<br>and 10GE multiprotocol with or<br>without FEC, normal operating case<br>temperature|
|1|Rx electrical interface|“D”: CDR|
|2|Photo diode type|“P”: PIN|
|3|Customized specifcation|00: Standard product|
|4|Revision code|0|
|5|Product status|Fn:      Functional sample<br>(n: null or version number)<br>Wn:    Working sample<br>(n: null or version number)<br>Null:  Mass production|



Tampering with this laser product or operating this product outside the limits of this specification may be considered an act of manufacturing and may require recertification of the modified product. 



North America Toll Free: 844 810 LITE (5483) 

Outside North America Toll Free: 800 000 LITE (5483) 

China Toll Free: 400 120 LITE (5483) 

© 2019 Lumentum Operations LLC Product specifications and descriptions in this document are subject to change without notice. 

Lumentum Operations LLC 1001 Ridder Park Drive San Jose, CA 95131 USA 

sfp+zerochirp-ds-oc-ae  30179587  901  0419 

www.lumentum.com 

