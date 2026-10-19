Optical Transceivers 

## FTLX1475D3BCV 

## **RoHS-6 Compliant 10Gb/s 10km Single Mode Datacom SFP+ Transceiver** 

FTLX1475D3BCV 10Gb/s Enhanced Small Form Factor Pluggable SFP+ transceivers are designed for use in 1-Gigabit and 10-Gigabit Ethernet links up to 10km over Single Mode fiber. They are compliant with SFF-8431[1] , SFF-8432[2] and IEEE 802.3ae 10GBASE-LR/LW[3] , and 10G Fibre Channel 1200-SM-LL-L4. This product is for applications specifically designed for 10G SFP+ ports and 1G/10G SFP+ ports and not native 1G SFP ports. Digital diagnostics monitoring is available via a 2-wire serial interface, as specified in SFF-8472[5] . TheFTLX1475D3BCV employs a limiting receiver.  FTLX1475D3BCV transceivers are RoHS compliant per Directive 2011/65/EU[6] , and Finisar Application Note AN-2038[7] . 


## FEATURES 

## APPLICATIONS 

- Hot-pluggable SFP+ footprint 

- Supports rate selectable 1.25Gb/s and 9.95 to 10.5Gb/s bit rates 

   - 1000BASE-LX 1G Ethernet 

   - 10GBASE-LR/LW 10G Ethernet 

- Power dissipation < 1W 

- RoHS-6 compliant (lead-free) 

- Commercial temperature range -5°C to 70°C 

- Single 3.3V power supply 

- Maximum link length of 10km 

- Uncooled 1310nm DFB laser 

- Receiver limiting electrical interface 

- Duplex LC connector 

- Built-in digital diagnostic functions 

**FTLX1475D3BCV** 

## **Product Selection** 

## **FTLX1475D3BCV** 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLX1475D3BCV** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|VEET|Transmitter Ground.|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line.|4|
|5|SCA|2-wire Serial Interface Clock Line.|4|
|6|MOD_ABS|Module Absent. Grounded within the module.|4|
|7|RS0|Rate Select 0. Open or Low = Module supp<br>High = Module supports 9.95 Gb/s to 10.312|5|
|8|RX_LOS|Loss of Signal indication. Logic 0 indicates normal operation.|6|
|9|RS1|Rate Select 1. No Connection Required||
|10|VEER|Receiver Ground.|1|
|11|VEER|Receiver Ground.|1|
|12|RD-|Receiver Inverted DATA out. AC Coupled.||
|13|RD+|Receiver Non-inverted DATA out. AC Coupled.||
|14|VEER|Receiver Ground.|1|
|15|VCCR|Receiver Power Supply.||
|16|VCCT|Transmitter Power Supply.||
|17|VEET|Transmitter Ground.|1|
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in. AC Coupled.||
|20|VEET|Transmitter Ground.|1|



Notes 

1. Circuit ground is internally isolated from chassis ground. 

2. T FAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V. A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Internally pulled down per SFF-8431 Rev 4.1. 

5. Transceiver data rate selected through the 2-wire bus in accordance with SFF-8472 Rev. 10.3. Soft RS0 is set at Bit3, Byte 110, Address A2h. Soft RS0 default state on power up is ‘0’ LOW, and the state is reset following a power cycle. Writing ‘1’ HIGH selects max. data rate operation. Transceiver data rate is the logic OR of the input state of the RS0 pin and soft RS0 bit. Thus, if either the RS0 pin OR the soft RS0 bit is HIGH then the selected data rate will be 9.95 and 10.3 Gb/s. Conversely, to select data rate 1.25 Gb/s both the RS0 pin and the soft RS0 bit are set LOW. 

6. LOS is open collector output. Should be pulled up with 4.7k – 10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

3 

**FTLX1475D3BCV** 

## **II. Absolute Maximum Ratings** 

Exceeding the limits below may damage the transceiver module permanently. 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Relative Humidity|RH|0||85|%|1|



Notes: 

1. Non Condensing 

## **III. Electrical Characteristics (TOP = -5 to 70ºC,  VCC = 3.14 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.14|3.30|3.46|V||
|Supply Current|Icc||200|285|mA||
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|1|
|Diferential data input swing|Vin,pp|180||700|mV||
|Transmit Disable Voltage|VD|2||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V||
|Receiver|||||||
|Diferential data output swing|Vout,pp|300||850|mV|2,6|
|Data output rise time, fall time|tr|28|||ps|3|
|LOS Fault|VLOS fault|2||VccHOST|V|4|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|4|
|Power Supply Noise Tolerance|VccT/VccR|Per SFF-8431 Rev 4.1|||mVpp|5|



Notes: 

1. Connected directly to TX data input pins. AC coupling from pins into laser driver IC. 

2. Into 100Ω differential termination. 

3. 20 – 80%. Measured with Module Compliance Test Board and OMA test pattern. Use of four 1’s and four 0’s sequence in the PRBS 9 is an acceptable alternative. SFF-8431 Rev 4.1. 

4. LOS is an open collector output. Should be pulled up with 4.7kΩ – 10kΩ on the host board. Normal operation is logic 0; loss of signal is logic 1. 

5. See Section 2.8.3 of SFF-8431 Rev 4.1. 

6. The FTLX1475D3BCV is a “limiting module”, i.e., it employs a limiting receiver. Host board designers using an EDC PHY IC should follow the IC manufacturer’s recommended settings for interoperating the host-board EDC PHY with a limiting receiver SFP+ module. 

4 

**FTLX1475D3BCV** 

## **IV.  Optical Characteristics for RS0 = Low (1G Operation)** 

## **(TOP = -5 to 70ºC,  VCC = 3.14 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Average Launch Power|PAVE|-11||-3|dBm|1|
|Optical Wavelength|λ|1260||1355|nm||
|Rise-Fall Time|Trise/Tfall|||0.26|ns|2|
|RMS Spectral Width|Δλrms|||4|nm||
|Optical Extinction Ratio|ER|9|||dB||
|Average Launch power of OFF transmitter|POFF|||-30|dBm||
|Tx Jitter|Txj|Per 802.3-2005 requirements|||||
|Relative Intensity Noise|RIN|||-120|dB/Hz||
|Receiver|||||||
|Receiver Sensitivity|RSENS|||-19|dBm|3|
|Stressed Receiver Sensitivity|SRS|||-14.4|dBm|4|
|Average Receive Power|PAVE|||-3|dBm||
|Optical Center Wavelength|λC|1260||1600|nm||
|Return Loss|Rrx|12|||dB||
|Receive electrical 3dB upper cutof frequency|||1500||MHz||
|LOS De-Assert|LOSD|||-17|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|||dB||



Notes: 

1. Average power figures are informative only, per IEEE 802.3-2005. 

2. 20%-80%. 

3. Valid between 1260 and 1355 nm. Measured with worst-case ER; BER<10[-12] ; 2[31] – 1 PRBS. 

4. Valid between 1260 and 1355 nm. Per IEEE 802.3-2005. 9dB extinction ratio transmitter. 

5 

**FTLX1475D3BCV** 

## **V.  Optical Characteristics for RS0 = Low (10G Operation) (TOP = -5 to 70ºC,  VCC = 3.14 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Optical Modulation Amplitude (OMA)|POMA|-5.2|||dBm||
|Average Launch Power|PAVE|-8.2||+0.5|dBm|1|
|Optical Wavelength|λ|1260||1355|nm||
|Side-Mode Suppression Ratio|SMSR|30|||dB||
|Optical Extinction Ratio|ER|3.5|||dB||
|Transmitter and Dispersion Penalty|TDP|||3.2|dB||
|Average Launch power of OFF|POFF|||-30|dBm||
|transmitter|Txj|Per 802.3-2005 requirements|||||
|Tx Jitter|RIN|||-128|dB/Hz||
|Relative Intensity Noise|||||||
|Receiver Sensitivity (OMA) @ 10.3Gb/s|RSENS1|||-12.6|dBm|2|
|Stressed Receiver Sensitivity (OMA) @<br>10.3Gb/s|RSENS2|||-10.3|dBm|3|
|Average Receive Power|PAVE|-14.2||+0.5|dBm||
|Optical Center Wavelength|λC|1260||1600|nm||
|Receiver Refectance|Rrx|||-12|dB||
|LOS Assert|LOSD|||-17|dBm||
|LOS Hysteresis|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|||dB||



Notes: 

1. Average power figures are informative only, per IEEE 802.3-2005. 

2. Valid between 1260 and 1355 nm. Measured with worst ER; BER<10[-12] ; 2[31] – 1 PRBS. 

3. Valid between 1260 and 1355 nm. Per IEEE 802.3-2005. 

6 

**FTLX1475D3BCV** 

## **VI. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Bit Rate (RS0 = LOW)|BR||1.25||Gb/s|1|
|Bit Rate (RS0 = HIGH)|BR|9.95|10.3||Gb/s|2|
|Max. Supported Link Length|LMAX||10||km||



Notes: 

1. 1000BASE-LX. Tested with a 2[7] – 1 PRBS. See Section I, Note 5 for RS0 conditions for 1.25Gb/s operation. 

2. 10GBASE-LR/LW. Tested with a 2[31] – 1 PRBS. See Section I, Note 5 for RS0 conditions for 10.3 Gb/s operation. 

## **VII. Environmental Specifications** 

Finisar FTLX1475D3BCV transceivers have an operating temperature range from -5°C to +70°C case temperature. 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-5||70|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VIII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements of  EN  (IEC)  60825  and  the  electrical  safety  requirements  of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

7 

**FTLX1475D3BCV** 

## **VIX. Digital Diagnostic Functions** 

Finisar FTLX1475D3BCV SFP+ transceivers support the 2-wire serial communication protocol as defined in the SFP MSA[1] . It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar SFP+ transceivers provide a enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in E[2] PROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN-2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFP MSA documentation1,5 and Finisar Application Note AN-2030. 

8 

**FTLX1475D3BCV** 

## **X. Digital Diagnostic Specifications** 

FTLX1475D3BCV transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Min Max Units Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Max|Units|Ref.|
|---|---|---|---|---|---|
|||||||
|Accuracy||||||
|Internally measured transceiver temperature|ΔDDTemp||±5|ºC||
|Internally measured transceiver supply voltage|ΔDDVoltage||3|mV||
|Measured TX bias current|ΔDDBias||10|%|1|
|Measured TX output power|ΔDDTx-Power||2|dB||
|Measured RX received average optical power|ΔDDRx-Power||2|dB||
|Dynamic Range for Rated Accuracy||||||
|Internally measured transceiver temperature|DDTemp|-5|70|ºC||
|Internally measured transceiver supply voltage|DDVoltage|3.1|3.5|V||
|Measured TX bias current|DDBias|10|90|mA||
|Measured TX output power|DDTx-Power|-8.2|+0.5|dBm||
|Measured RX received average optical power|DDRx-Power|-14.2|+0.5|dBm||
|Max Reporting Range||||||
|Internally measured transceiver temperature|DDTemp|-40|125|ºC||
|Internally measured transceiver supply voltage|DDVoltage|2.8|4.0|V||
|Measured TX bias current|DDBias|0|20|mA||
|Measured TX output power|DDTx-Power|-10|+2|dBm||
|Measured RX received average optical power|DDRx-Power|-22|+2|dBm||



Notes: 

1. Accuracy of Measured Tx Bias Current is 10% of the actual Bias Current from the laser driver to the laser 

9 

**FTLX1475D3BCV** 

## **XI. Mechanical Specifications** 

Finisar FTLX1475D3BCV SFP+ transceivers are compatible with the SFF-8432 specification for improved pluggable form factor, and shown here for reference purposes only. Bail color is blue. 


Figure 2. FTLX1475D3BCV Mechanical Dimensions and Tolerances. 

10 

**FTLX1475D3BCV** 

## **XII. PCB Layout and Bezel Recommendations** 


11 

**FTLX1475D3BCV** 



12 

**FTLX1475D3BCV** 

## **XIII. Host - Transceiver Interface Block Diagram** 


Figure 6. Host-Module Interface 

13 

**FTLX1475D3BCV** 

## **XIII. References** 

1. “Specifications for Enhanced 8.5 and 10 Gigabit Small Form Factor Pluggable Module ‘SFP+ ‘”, SFF Document Number SFF-8431, Revision 4.1. 

2.  “Improved Pluggable Form factor”, SFF Document Number SFF-8432, Revision 4.2, April 18, 2007. 

3. IEEE Std 802.3ae, Clause 52, PMD Type 10GBASE-LR. IEEE Standards Department. 

4. American National Standard for Information Technology - Fibre Channel - 10 Gigabit Fibre Channel, Rev 3.5, April 9, 2003. 

5. “Digital Diagnostics Monitoring Interface for Optical Transceivers”. SFF Document Number SFF-8472, Revision 11.3. 

6. Directive 2011/65/EU of the European Parliament and of the Council “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. Certain products may use one or more exemption as allowed by the directive. 

7. “Application Note AN-2038: Finisar Implementation Of RoHS Compliant Transceivers”, Finisar Corporation, January 21, 2005. 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

