Optical Transceivers 

## FTLX8574D3BCL 

## **10Gb/s 850nm Multimode Datacom SFP+ Transceiver** 

FTLX8574D3BCL 10Gb/s SFP+ transceivers are designed for use in 10-Gigabit Ethernet links over multimode fiber. They are compliant with SFF-8431[1] , SFF-8432[2] ,IEEE 802.3-2012 10GBASE-SR/SW3 and 10G Fibre Channel 1200-Mx-SN-I4. Digital diagnostics functions are available via a 2-wire serial interface, as specified in SFF_x005F_xFFFE_84725. TheFTLX8574D3BCL is a “limiting module”, i.e., it employs a limiting receiver. Host board designers using an EDC PHY IC should follow the IC manufacturer’s recommended settings for interoperating the host-board EDC PHY with a limiting receiver SFP+ module. The optical transceiver is compliant per the RoHS Directive 2011/65/EU[6] . See Finisar Application Note AN-2038[7] for more details. 


## FEATURES 

## APPLICATIONS 

- Hot-pluggable SFP+ footprint 

- Supports 9.95 to 10.5 Gb/s bit rates* 

   - 10GBASE-SR/SW 10G Ethernet 

   - 1200-Mx-SN-I 10G Fibre Channel 

- Power dissipation < 1W 

- RoHS-6 compliant (lead-free) 

- Commercial temperature range -5°C to 70°C 

- Single 3.3Vpower supply 

- Maximum link length of 400m on OM4 MMF 

- Uncooled 850nm VCSEL laser 

- Receiver limiting electrical interface 

- Duplex LC connector 

- Built-in digital diagnostic functions 

**FTLX8574D3BCL** 

## **Product Selection** 

## **FTLX8574D3BCL** 

*Contact Finisar for higher data-rate support up to 11.1Gbps. 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TXFault<br>TD+ 18<br>3 TX Disable<br>VeeT 17<br>4 MOD-DEF(2)<br>VccT 16<br>5 MOD-DEF(1)<br>Towards Towards<br>VccR 15<br>Bezel 6 MOD-DEF(0) ASIC<br>VeeR 14<br>7 Rate Select<br>RD+ 13<br>8 LOS<br>RD- 12<br>9 VeeR<br>VeeR 11<br>1 VeeR<br>**----- End of picture text -----**<br>


Diagram of Host Board Connector Block Pin Numbers and Names 

2 

**FTLX8574D3BCL** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|1|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line|4|
|5|SCL|2-wire Serial Interface Clock Line|4|
|6|MOD_ABS|Module Absent. Grounded within the module|4|
|7|RS0|No connection required||
|8|RX_LOS|Loss of Signal indication. Logic 0 indicates normal operation.|5|
|9|RS1|No connection required||
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

2. T FAULT is an open collector/drain output, which should be pulled up with a 4.7k – 10k Ohms resistor on the host board if intended for use. Pull up voltage should be between 2.0V to Vcc + 0.3V. A high output indicates a transmitter fault caused by either the TX bias current or the TX output power exceeding the preset alarm thresholds. A low output indicates normal operation. In the low state, the output is pulled to <0.8V. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. MOD_ABS pulls line low to indicate module is plugged in. 5. LOS is open collector output. Should be pulled up with 4.7k – 10kohms on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 

3 

**FTLX8574D3BCL** 

## **II. Absolute Maximum Ratings** 

Exceeding the limits below may damage the transceiver module permanently. 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Relative Humidity|RH|-5||70|°C|1|
|Receiver Optical Damage Threshold|RxDamage|0||85|dBm||



Notes: 

1. Non Condensing 

## **III. Electrical Characteristics (TOP = -5 to 70 °C, VCC = 3.14 to 3.46 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.14||3.46|V||
|Power Consumption|Pdiss|||250|W|1|
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω||
|Diferential data input swing|Vin,pp|180||700|mV|2|
|Transmit Disable Voltage|VD|2||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V||
|Receiver|||||||
|Diferential data output swing|Vout,pp|300||850|mV|2,6|
|Data output rise time, fall time|tr|28|||ps|3|
|LOS Fault|VLOS fault|2||VccHOST|V|4|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|4|
|Power Supply Noise Tolerance|VccT/VccR|Per SFF-8431 Rev 4.1|||mVpp|5|



## Notes: 

1. Connected directly to TX data input pins. AC coupling from pins into laser driver IC. 

2. Into 100Ω differential termination. 

3. 20 – 80 %. Measured with Module Compliance Test Board and OMA test pattern. Use of four 1’s and four 0’s in sequence in the PRBS^9 is an acceptable alternative. SFF-8431 Rev 4.1 

4. LOS is an open collector output. Should be pulled up with 4.7kΩ – 10kΩ on the host board. Normal operation is logic 0; loss of signal is logic 1. Maximum pull-up voltage is 5.5V. 

5. Testing methodology per SFF-8431. Rev 4.1 

6. The FTLX8574D3BCL is a “limiting module”, i.e., it employs a limiting receiver. Host board designers using an EDC PHY IC should follow the IC manufacturer’s recommended settings for interoperating the host-board EDC PHY with a limiting receiver SFP+ module. 

4 

**FTLX8574D3BCL** 

## **IV. Optical Characteristics (TOP = -5 to 70 °C, VCC = 3.14 to 3.46 Volts))** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Optical Modulation Amplitude (OMA)|POMA||-1.5||dBm||
|Average Launch Power|PAVE|-5||-1|dBm|2|
|Optical Wavelength|λ|840|850|860|nm|1|
|RMS Spectral Width|Δλrms|||0.45|dB|1|
|Optical Extinction Ratio|ER|3.0|5.5||dB||
|Transmitter and Dispersion Penalty|TDP|||3.9|dB||
|Average Launch power of OFF transmitter|POFF|||-30|dBm||
|Tx Jitter|Txj|Per IEEE 802.3-2012 requirements|||||
|Encircled Flux|<4.5µm|||30|%|3|
||<19µm|86|||||
|Relative Intensity Noise|RIN12OMA|||-128|dB/Hz||
|Receiver|||||||
|Receiver Sensitivity (OMA) @ 10.3Gb/s|RSENS1|||-11.1|dBm|4|
|Stressed Receiver Sensitivity (OMA) @ 10.3Gb/s|RSENS2|||-7.5|dBm|5|
|Maximum Input Power|PMAX|+0.5|||dBm||
|Wavelength Range|λC|840||860|nm||
|Receiver Refectance|Rrx|||-12|dB||
|LOS De-Assert|LOSD|||-14|dBm||
|LOS Assert|LOSA|-30|-23||dBm||
|LOS Hysteresis||0.5|||dB||



Notes: 

1. Per Tradeoff Table 52.8, IEEE 802.3-2012. 

2. Average Power figures are informative only, per IEEE 802.3-2012. 

3. Measured into Type A1a (50/125 μm multimode) fiber per ANSI/TIA/EIA-455-203-2. 

4. Measured with worst ER; BER<10-12; 231 – 1 PRBS. 

5. Per IEEE 802.3-2012. 

5 

**FTLX8574D3BCL** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|---|
|||||||||
|Bit Rate||BR|9.95||10.5|Gb/s|1|
|Bit Error Ratio||BER|||10-12||2|
|Maximum Supported Distances||||||||
|Fiber Type|850nm OFL Band-<br>width|||||||
|62.5µm|160 MHz-km|Lmax|||26|m||
||OM1<br>200 MHz-km||||33|||
|50µm|400 MHz-km|Lmax|||66|m||
||OM2 500 MHz-km||||82|||
||OM3 2000 MHz-<br>km||||300|||
||OM4 4700 MHz-<br>km||||400|||



Notes: 

1. 10GBASE-SR/SW. Contact Finisar for higher data-rate support. 

2. Tested with a 2[31] – 1 PRBS 

## **VI. Environmental Specifications** 

Finisar 850nm SFP transceivers have a commercial operating temperature range from -5°C to +70°C case temperature. 

|Parameter|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-5||70|°C||
|Storage Temperature|Tsto|-40||85|°C||



## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements of EN (IEC) 60825 and the electrical safety requirements of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

6 

**FTLX8574D3BCL** 

## **VIII. Digital Diagnostic Functions** 

Finisar FTLX8574D3BCL SFP+ transceivers support the 2-wire serial communication protocol as defined in the SFF-8472. It is very closely related to the E[2] PROM defined in the GBIC standard, with the same electrical specifications. 

The standard SFP+ serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Finisar SFP+ transceivers provide an enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

SFF-8472 defines a 256-byte memory map in E[2] PROM that is accessible over a 

2-wire serial interface at the 8 bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8 bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. The complete interface is described in Finisar Application Note AN- 2030: “Digital Diagnostics Monitoring Interface for SFP Optical Transceivers”. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E[2] PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

For more information, please see the SFF-8472 documentation and Finisar Application Note AN-2030. 

7 

**FTLX8574D3BCL** 

## **IX. Digital Diagnostic Specifications** 

FTLX1871D3BCL transceivers can be used in host systems that require either internally or externally calibrated digital diagnostics. 


**----- Start of picture text -----**<br>
Parameter Symbol Min Max Units Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Max|Units|Ref.|
|---|---|---|---|---|---|
|||||||
|Accuracy||||||
|Internally measured transceiver temperature|DDTemp|-3|3|ºC||
|Internally measured transceiver supply voltage|DDVoltage|-100|100|mV||
|Measured TX bias current|DDBias|-10|10|%|1|
|Measured TX output power|DDTx-Power|-2|2|dB||
|Measured RX received average optical power|DDRx-Power|-2|2|dB||
|Dynamic Range for Rated Accuracy||||||
|Internally measured transceiver temperature|DDTemp|-5|70|ºC||
|Internally measured transceiver supply voltage|DDVoltage|3.14|3.46|V||
|Measured TX bias current|DDBias|0|20|mA||
|Measured TX output power|DDTx-Power|-9|-2.5|dBm||
|Measured RX received average optical power|DDRx-Power|-20|0|dBm||
|Max Reporting Range||||||
|Internally measured transceiver temperature|DDTemp|-40|125|ºC||
|Internally measured transceiver supply voltage|DDVoltage|2.8|4.0|V||
|Measured TX bias current|DDBias|0|20|mA||
|Measured TX output power|DDTx-Power|-10|-1|dBm||
|Measured RX received average optical power|DDRx-Power|-22|0|dBm||



Notes: 

1. Accuracy of Measured Tx Bias Current is 10% of the actual Bias Current from the laser driver to the laser. 

8 

**FTLX8574D3BCL** 

## **X. Mechanical Specifications** 

Finisar FTLX8574D3BCL SFP+ transceivers are compatible with the SFF-8432 specification for improved pluggable form factor, and shown here for reference purposes only. Bail color is beige. 


Figure 2. FTLX8574D3BCL Mechanical Dimensions. 

. 

9 

**FTLX8574D3BCL** 

## **XI. PCB Layout and Bezel Recommendations** 


Figure 3. PCB Layout and Bezel Recommendations, as per [9] 

10 

**FTLX8574D3BCL** 



Figure 4. 

11 

**FTLX8574D3BCL** 

## **XIII. Host-Module Interface Diagram** 


Figure 5. Host-Module Interface 

12 

**FTLX8574D3BCL** 

## **XIV. References** 

1. “Specifications for Enhanced 8.5 and 10 Gigabit Small Form Factor Pluggable Module ‘SFP+ ‘”, SFF Document Number SFF-8431, Revision 4.1. 

2. “Improved Pluggable Formfactor”, SFF Document Number SFF-8432, Revision 5.0. 

3. IEEE Std 802.3, Clause 52, PMD Type 10GBASE-SR. IEEE Standards Department. 

4. American National Standard for Information Technology - Fibre Channel - 10 Gigabit Fibre Channel, Rev 3.5, April 9, 2003. 

5. “Digital Diagnostics Monitoring Interface for Optical Transceivers”. SFF Document Number SFF-8472, Revision 11.1. 

6. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. 

7. “Application Note AN-2038: Finisar Implementation Of RoHS Compliant Transceivers”. 

© 2023 Coherent Corp. photonics.sales@coherent.com Legal notices : coherent.com/legal www.coherent.com 

