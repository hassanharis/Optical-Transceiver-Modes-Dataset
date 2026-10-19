Optical Transceivers 

## FTLX2471DC0XX 

## **RoHS-6 Compliant CWDM 10Gb/s 10km Single Mode Datacom SFP+ Transceiver** 

FTLX2471DC0xx 10Gb/s Enhanced Small Form Factor Pluggable SFP+ transceivers are designed for use in CWDM 10km Single Mode fiber links. They are compliant with SFF-8431[1] , SFF-8432[2] and compatible with IEEE 802.3ae 10GBASE_x005F_ xFFFE_LR/LW[3] , and 10G Fibre Channel 1200-SM-LL-L4. Digital diagnostics functions are available via a 2-wire serial interface, as specified in SFF-8472[5] . The optical transceiver is compliant per the RoHS Directive 2011/65/EU. See Finisar Application Note AN_x005F_xFFFE_2038 for more details. 


## FEATURES 

## APPLICATIONS 

- Hot-pluggable SFP+ footprint 

- Supports 9.95 to 10.5Gb/s bit rates 

- Power dissipation < 1W 

   - CWDM 10km links supporting: 

   - 10GBASE-LR/LW 10G Ethernet 

   - 1200-SM-LL-L 10G Fibre Channel 

- RoHS-6 compliant (lead-free) 

- Commercial temperature range -5°C to 70°C 

- Single 3.3V power supply 

- Maximum link length of 10km 

- Uncooled 1310nm DFB laser 

- Receiver limiting electrical interface 

- Duplex LC connector 

- Built-in digital diagnostic functions 

**FTLX2471DC0XX** 

## **Product Selection** 

## **FTLX2471DC0xx** 


**----- Start of picture text -----**<br>
Part Number Wavelength Bail Latch Color<br>**----- End of picture text -----**<br>


|Part Number|Wavelength|Bail Latch Color|
|---|---|---|
||||
|FTLX2471DC027|1271 nm|Gray|
|FTLX2471DC029|1291 nm|Violet|
|FTLX2471DC031|1311 nm|Blue|
|FTLX2471DC033|1331 nm|Green|



## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLX2471DC0XX** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|VEET|Transmitter Ground|1|
|2|TFAULT|Transmitter Fault|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line|2|
|5|SCL|2-wire Serial Interface Clock Line|2|
|6|MOD_ABS|Module Absent. Grounded within the module|2|
|7|RS0|Rate Select 0. Not Used.|4|
|8|RX_LOS|Loss of Signal indication. Logic 0 indicates normal operation.|5|
|9|RS1|Rate Select 1. Not Used.|4|
|10|VEER|Receiver Ground|1|
|11|VEER|Receiver Ground|1|
|12|RD-|Receiver Inverted DATA out. AC Coupled.||
|13|RD+|Receiver Non-inverted DATA out. AC Coupled.||
|14|VEER|Receiver Ground|1|
|15|VCCR|Receiver Power Supply||
|16|VCCT|Transmitter Power Supply||
|17|VEET|Transmitter Ground|1|
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in. AC Coupled.||
|20|VEET|Transmitter Ground|1|



Notes 

1. Circuit ground is internally isolated from chassis ground. 

2. T FAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V. A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Internally pulled down per SFF-8431 Rev 2.0. 

5. LOS is open collector output. Should be pulled up with 4.7k – 10kΩ on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

## **II. Absolute Maximum Ratings** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Relative Humidity (Non-condensing)|RH|0||85|%|1|



3 

**FTLX2471DC0XX** 

## **III. Electrical Characteristics (TOP= -5 to 70 °C , VCC = 3.14 to 3.46 Volts )** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.14|3.30|3.46|V||
|Supply Current|Icc||200|285|mA||
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|1|
|Diferential data input swing|Vin,pp|180||700|mV||
|Transmit Disable Voltage|VD|2||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee + 0.8|V||
|Receiver|||||||
|Single ended data output swing|Vout,pp|300||850|mV|2,6|
|Data output rise/fall time, 4.25 Gb/s|tr, tf|28|||ps|3|
|LOS Fault|VLOS fault|2||VccHOST|V|4|
|LOS Normal|VLOS norm|Vee-0.0||Vee+0.8|V|4|
|Power Supply Noise Tolerance|VccT/VccR|Per SFF-8431 Rev 3.0|||mVpp|5|



Notes: 

1. Connected directly to TX data input pins. AC coupling from pins into laser driver IC. 

2. Into 100Ω differential termination. 

3. 20 – 80%. Measured with Module Compliance Test Board and OMA test pattern. Use of four 1’s and four 0’s sequence in the PRBS 9 is an acceptable alternative. SFF-8431 Rev 3.0. 

4. LOS is an open collector output. Should be pulled up with 4.7kΩ – 10kΩ on the host board. Normal operation is logic 0; loss of signal is logic 1. 

5. See Section 2.8.3 of SFF-8431 Rev 3.0. 

6. The FTLX2471D3Cxx is a “limiting module”, i.e., it employs a limiting receiver. Host board designers using an EDC PHY IC should follow the IC manufacturer’s recommended settings for interoperating the host-board EDC PHY with a limiting receiver SFP+ module. 

4 

**FTLX2471DC0XX** 

## **IV. Optical Characteristics (TO = -5 to 70°C, VCC3 = 3.14 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Optical Modulation Amplitude (OMA)|POMA|-2.5|||dBm||
|Average Launch Power|PAVE|-3||+3|dBm|1|
|Optical Wavelength|λ|(λ-6.5)|(λ)|(λ+6.5)|nm|2|
|Side-Mode Suppression Ratio|SMSR|30|||dB||
|Optical Extinction Ratio|ER|3.5|||dB||
|Dispersion Penalty|DP|||2|dB||
|Transmitter and Dispersion Penalty|TDP|||3.2|dB||
|Average Launch power of OFF transmitter|POFF|||-30|dBm||
|Tx Jitter|Txj|Per 802.3ae requirements|||||
|Relative Intensity Noise|RIN|||-128|dB/Hz||
|Receiver|||||||
|Receiver Sensitivity (OMA) @ 10.5Gb/s|RSENS OMA|||-12.6|dBm|3,4|
|Stressed Receiver Sensitivity (OMA) @ 10.3Gb/s|RSENS STRESS|||-10.3|dBm|5|
|Average Receive Power|PAVE|||+0.5|dBm||
|Optical Wavelength|λC|1260||1600|nm||
|Receiver Refectance|Rrx|||-12|dB||
|LOS De-Assert|LOSD|||-17|dBm||
|LOS Assert|LOSA|-30|||dBm||
|LOS Hysteresis||0.5|||dB||



Notes: 

1. Average power figures are informative only, per IEEE 802.3ae. 

2. The available transmitter center wavelengths ( λ are: 1271nm, 1291nm, 1311nm and 1331nm as specified in the “Product Selection” section on page 1. 

3. Valid between 1260 and 1355 nm. Measured with worst ER; BER<10[-12] ; 2[31] – 1 PRBS. 

4. IEEE 802.3ae defines a minimum average receive power of -14.4dBm, as informative only. 

5. Valid between 1260 and 1355 nm. Per IEEE 802.3ae. 

5 

**FTLX2471DC0XX** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Bit Rate|BR|9.95||10.5|Gb/s|1|
|Bit Error Rate|BER|||10-12||2|
|Max. Supported Link Length|LMAX||10||km|1|



Notes: 

1. 10GBASE-LR, 10GBASE-LW, 1200-SM-LL-L 10GFC. 

2. Tested with a 2[31] – 1 PRBS. 

## **VII. Environmental Specifications** 

|Environmental Specifcations|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Top|-5||70|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements of EN (IEC) 60825 and the electrical safety requirements of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

6 

**FTLX2471DC0XX** 

## **VIII. Digital Diagnostic Functions** 

Finisar FTLX2471DC0xx SFP+ transceivers support the 2-wire serial communication protocol as defined in the SFP MSA[1] . It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. 

The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar SFP+ transceivers provide a enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in E[2] PROM that is accessible over a 2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN- 2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFP MSA documentation1,5 and Finisar Application Note AN-2030. 

Please note that evaluation board FDB-1018 is available with Finisar ModDEMO software that allows simple to use communication over the 2-wire serial interface. 

7 

**FTLX2471DC0XX** 

## **IX. Digital Diagnostic Specifications** 

FTLX2471DC0xx transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Units Min Typ Max Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Units|Min|Typ|Max|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Internally measured transceiver temperature|ΔDTemp|ºC|-10|75|±5ºC|1|
|Internally measured transceiver supply voltage|ΔDVoltage|%|2.8|4.0|±3%||
|Measured TX bias current|ΔDBias|%|0|20|±10%|2|
|Measured TX output power|ΔDTx-Power|dB|-5|+2|±2dB||
|Measured RX received average optical power|ΔDRx-Power|dB|-20|+2|±2dB||



Notes: 

1. Internally measured 

2. Accuracy of measured Tx bias current is 10% of the actual bias current from the laser driver to the laser. 

8 

**FTLX2471DC0XX** 

## **X. Mechanical Specifications** 

Finisar FTLX2471DC0xx SFP+ transceivers are compatible with the SFF-8432 specification for improved pluggable form factor, and shown here for reference purposes only. Bail color is blue. 


Figure 2. FTLX2471DC0xx Mechanical Dimensions 

9 

**FTLX2471DC0XX** 

## **XI. PCB Layout and Bezel Recommendations** 


Figure 3. PCB Layout and Bezel Recommendations, as per [9] 

10 

**FTLX2471DC0XX** 



Figure 4. 

11 

**FTLX2471DC0XX** 

## **XII. Host - Transceiver Interface Block Diagram** 


Figure 6-Host-Module Interface 

12 

**FTLX2471DC0XX** 

## **XIII. References** 

1. “Specifications for Enhanced 8.5 and 10 Gigabit Small Form Factor Pluggable Module ‘SFP+ ‘”, SFF Document Number SFF-8431, Revision 3.0. 

2. “Improved Pluggable Form factor”, SFF Document Number SFF-8432, Revision 4.2, April 18, 2007. 

3. IEEE Std 802.3ae, Clause 52, PMD Type 10GBASE-LR. IEEE Standards Department. 

4. American National Standard for Information Technology - Fibre Channel - 10 Gigabit Fibre Channel, Rev 3.5, April 9, 2003. 

5. “Digital Diagnostics Monitoring Interface for Optical Transceivers”. SFF Document Number SFF-8472, Revision 10.1, March 1, 2007. 

6. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. Certain products may use one or more exemptions as allowed by the Directive. 

7. “Application Note AN-2038: Finisar Implementation Of RoHS Compliant Transceivers” 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

