**AFBR-710ISMZ** 10Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver -40 ° C to 85 ° C **Data Sheet Description Features** • Avago 850nm VCSEL source and Transmitter Optical The Avago AFBR-710ISMZ transceiver is part of a family Subassembly technology of SFP+ products. This transceiver utilizes Avago’s 850nm VCSEL and PIN Detector technology to provide an IEEE • Avago PIN detector and Receiver Optical Subassembly 10Gb Ethernet design compliant with the 10GBASE-SR technology and 10GBASE-SW standards. The AFBR-710ISMZ trans• Typical power dissipation 600mW ceiver is designed to enable 10Gb Ethernet equipment • Industrial case temperature -40 to 85 ° C designs with very high port density based on the new electrical and mechanical specification enhancements • Full digital diagnostic management interface to the well known SFP specifications developed by the • Avago SFP+ package design enables equipment EMI SFF Committee. These specifications are referred to as performance in high port density applications with SFP+ to recognize these enhancements to previous SFP margin to Class B limits specifications used for lower speed products. Avago Technologies is a an active participant in the SFF Com- **Specifications** mittee specification development activities. • Optical interface specifications per IEEE 802.3ae 10GBASE-SR and 10GBASE-SW **Related Products** • Link lengths at 10.3125 GBd: • AFBR-710SMZ is an SFP+ 10 Gigabit Ethernet 300m with 50um OM3 MM fiber 10GBASE-SR/SW transceiver with case temperature 400m with 50um OM4 MM fiber operated at 0-70 °C for use on multimode fiber cables. • It is best suited for OM3 high bandwidth MMF link Electrical interface specifications per SFF Committee applications with link lengths up to 300 meters. SFF 8431 Specifications for Enhanced 8.5 and 10 • AFBR-710DMZ SFP+ 10Gb/1Gb Gigabit Ethernet Gigabit Small Form Factor Pluggable Module “SFP+” 10GBASE-SR transceiver for operation in 300m reach • Management interface specifications per SFF Committee SFF 8431 and SFF 8472 Diagnostic using OM3 MMF. Monitoring Interface for Optical Transceivers • AFCT-739SMZ (AFCT-739ASMZ) with case tempera• Mechanical specifications per SFF Committee SFF ture 0-70 (0-85) °C SFP+ 10 Gigabit Ethernet 8432 Improved Pluggable Formfactor “IPF” 10GBASE-LR transceiver for operation in SMF link • applications to 10 km LC Duplex optical connector interface confirming to ANSI TIA/EA 604-10 (FOCIS 10A) • AFCT-5016Z SFP+ Evaluation Board The purpose of this SFP+ evaluation board is to provide the designer • Compliant to Restriction on Hazardous Substances with a convenient means for evaluating SFP+ fiber (RoHS) per EU and China requirements optic transceivers. • Class 1 Eye safe per requirements of IEC 60825-1 / CDRH Patent - www.avagotech.com/patents 

## **Description,** continued 

## **Installation** 

The AFBR-710ISMZ transceiver package is compliant with the SFF 8432 Improved Pluggable Formfactor housing specification for the SFP+.  It can be installed in any INF-8074 or SFF-8431/2 compliant Small Form Pluggable (SFP) port regardless of host equipment operating status The AFBR-710ISMZ is hot-pluggable, allowing the module to be installed while the host system is operating and on-line. Upon insertion, the transceiver housing makes initial contact with the host board SFP cage, mitigating potential damage due to Electro-Static Discharge (ESD). 

## **Digital Diagnostic Interface and Serial Identification** 

The two-wire interface protocol and signaling detail are based on SFF-8431. Conventional EEPROM memory, bytes 0-255 at memory address 0xA0, is organized in compliance with SFF-8431. New digital diagnostic information, bytes 0-255 at memory address 0xA2, is compliant to SFF-8472. The new diagnostic information provides the opportunity for Predictive Failure Identification, Compliance Prediction, Fault Isolation and Component Monitoring. 

## **Predictive Failure Identification** 

The AFBR-710ISMZ predictive failure feature allows a host to identify potential link problems before system performance is impacted. Prior identification of link problems enables a host to service an application via “fail over” to a redundant link or replace a suspect device, maintaining system uptime in the process. For applications where ultra-high system uptime is required, a digital SFP provides a means to monitor two real-time laser metrics associated with observing laser degradation and predicting failure: average laser bias current (Tx_Bias) and average laser optical power (Tx_Power). 

## **Compliance Prediction** 

Compliance prediction is the ability to determine if an optical transceiver is operating within its operating and environmental requirements. AFBR-710ISMZ devices provide real-time access to transceiver internal supply voltage and temperature, allowing a host to identify potential component compliance issues. Received optical power is also available to assess compliance of a cable plant and remote transmitter. When operating out of requirements, the link cannot guarantee error free transmission. 

## **Fault Isolation** 

The fault isolation feature allows a host to quickly pinpoint the location of a link failure, minimizing downtime. For optical links, the ability to identify a fault at a local device, remote device or cable plant is crucial to speeding service of an installation. AFBR-710ISMZ real-time monitors of Tx_Bias, Tx_Power, Vcc, Temperature and Rx_Power can be used to assess local transceiver current operating conditions. In addition, status flags TX_DISABLE and Rx Loss of Signal (LOS) are mirrored in memory and available via the two-wire serial interface. 

## **Component Monitoring** 

Component evaluation is a more casual use of the AFBR710ISMZ real-time monitors of Tx_Bias, Tx_Power, Vcc, Temperature and Rx_Power. Potential uses are as debugging aids for system installation and design, and transceiver parametric evaluation for factory or field qualification. For example, temperature per module can be observed in high density applications to facilitate thermal evaluation of blades, PCI cards and systems. 

2 


**----- Start of picture text -----**<br>
OPTICAL INTERFACE ELECTRICAL INTERFACE<br>RECEIVER<br>AMPLIFICATION RD+ (RECEIVE DATA)<br>LIGHT FROM FIBER PHOTO-DETECTOR<br>& QUANTIZATION RD– (RECEIVE DATA)<br>RX_LOS<br>RS0<br>RS1<br>CONTROLLER & MEMORY<br>SDA<br>SCL<br>MOD-ABS<br>TRANSMITTER<br>TX_DISABLE<br>LASER<br>DRIVER & TD+ (TRANSMIT DATA)<br>LIGHT TO FIBER VCSEL SAFETY<br>TD– (TRANSMIT DATA)<br>CIRCUITRY<br>TX_FAULT<br>**----- End of picture text -----**<br>


**Figure 1. Transceiver functional diagram** 

## **Transmitter Section** 

The transmitter section includes the Transmitter Optical Sub-Assembly (TOSA) and laser driver circuitry. The TOSA, containing an Avago designed and manufactured 850 nm VCSEL (Vertical Cavity Surface Emitting Laser) light source, is located at the optical interface and mates with the LC optical connector. The TOSA is driven by an IC which uses the incoming differential high speed logic signal to modulate the laser diode driver current. This Tx laser driver circuit regulates the optical power at a constant level provided the incoming data pattern is DC balanced. 

## **Transmit Fault (TX_FAULT)** 

A catastrophic laser fault will activate the transmitter signal, TX_FAULT, and disable the laser. This signal is an open collector output (pull-up required on the host board). A low signal indicates normal laser operation and a high signal indicates a fault. The TX_FAULT will be latched high when a laser fault occurs and is cleared by toggling the TX_DISABLE input or power cycling the transceiver. The transmitter fault condition can also be monitored via the two-wire serial interface (address A2, byte 110, bit 2). 

## **Transmit Disable (TX_DISABLE)** 

The AFBR-710ISMZ accepts an LVTTL compatible transmit disable control signal input which shuts down the transmitter optical output. A high signal implements this function while a low signal allows normal transceiver operation. In the event of a fault (e.g. eye safety circuit activated), cycling this control signal resets the module as depicted in Figure 6. An internal pull up resistor disables the transceiver transmitter until the host pulls the input low. TX_DISABLE can also be asserted via the two-wire interface (address A2h, byte 110, bit 6) and monitored (address A2h, byte 110, bit 7). 

The contents of A2h, byte 110, bit 6 are logic OR’d with hardware TX_DISABLE (contact 3) to control transmitter operation. 

3 

## **Receiver Section** 

The receiver section includes the Receiver Optical SubAssembly (ROSA) and the amplification/quantization circuitry. The ROSA, containing a PIN photodiode and custom transimpedance amplifier, is located at the optical interface and mates with the LC optical connector. The ROSA output is fed to a custom IC that provides post-amplification and quantization. 

## **Receiver Loss of Signal (Rx_LOS)** 

The post-amp IC also includes transition detection circuitry which monitors the AC level of incoming optical signals and provides a LVTTL/CMOS compatible status signal to the host. A high status signal indicates loss of modulated signal, indicating link failures such as broken fiber or failed transmitter. Rx_LOS can also be monitored via the two-wire serial interface(address A2h, byte 110, bit 1). 

## **Functional Data I/O** 

The AFBR-710ISMZ interfaces with the host circuit board through the twenty contact SFP+ electrical connector.   See Table 2 for contact descriptions.  The module edge connector is shown in Figure 4. The host board layout for this interface is depicted in Figure 8. 

The AFBR-710ISMZ high speed transmit and receive interfaces require SFF-8431 compliant signal lines on the host board. To simplify board requirements, biasing resistors and AC coupling capacitors are incorporated into the SFP+ transceiver module (per SFF-8431) and hence are not required on the host board. The TX_DISABLE, TX_ FAULT and RX_LOS signals require LVTTL signals on the host board (per SFF-8431) if used. If an application does not take advantage of these functions, care must be taken to ground TX_DISABLE to enable normal operation. 

## **Caution** 

There are no user serviceable parts nor maintenance requirements for the AFBR-710ISMZ. All mechanical adjustments are made at the factory prior to shipment. Tampering with, modifying, misusing or improperly handling the AFBR-710ISMZ will void the product warranty. It may also result in improper operation and possibly overstress the laser source. Performance degradation or device failure may result. Connection of the AFBR710ASMZ to a light source not compliant with IEEE Std. 802.3ae Clause 52 and SFF-8341 specifications, operating above maximum operating conditions or in a manner inconsistent with it’s design and function may result in exposure to hazardous light radiation and may constitute an act of modifying or manufacturing a laser product. Persons performing such an act are required by law to recertify and re-identify the laser product under the provisions of U.S. 21 CFR (Subchapter J) and TUV. 

## **Customer Manufacturing Processes** 

This module is pluggable and is not designed for aqueous wash, IR reflow, or wave soldering processes. 

## **Ordering Information** 

Please contact your local field sales engineer or one of Avago Technologies franchised distributors for ordering information. For technical information, please visit Avago Technologies’ WEB page at www.avagotech.com  For information related to SFF Committee documentation visit www.sffcommittee.org. 

Figure 2 depicts the recom mended interface circuit to link the AFBR-710ISMZ to supporting physical layer ICs. Timing for the dedicated SFP+ control signals implemented in the transceiver are listed in Figure 6. 

## **Application Support** 

An Evaluation Kit and Reference Designs are available to assist in evaluation of the AFBR-710ISMZ. Please contact your local Field Sales representative for availability and ordering details. 

4 

## **Regulatory Compliance** 

The AFBR-710ISMZ complies with all applicable laws and regulations as detailed in Table 1. Certification level is dependent on the overall configuration of the host equipment. The transceiver performance is offered as a figure of merit to assist the designer. 

## **Electrostatic Discharge (ESD)** 

The AFBR-710ISMZ is compatible with ESD levels found in typical manufacturing and operating environments as described in Table 1. In the normal handling and operation of optical transceivers, ESD is of concern in two circumstances. 

The first case is during handling of the transceiver prior to insertion into an SFP compliant cage. To protect the device, it’s important to use normal ESD handling precautions. These include use of grounded wrist straps, work-benches and floor wherever a transceiver is handled. 

The second case to consider is static discharges to the exterior of the host equipment chassis after installation. If the optical interface is exposed to the exterior of host equipment cabinet, the transceiver may be subject to system level ESD requirements. 

## **Electromagnetic Interference (EMI)** 

Equipment incorporating 10 gigabit transceivers is typically subject to regulation by the FCC in the United States, CENELEC EN55022 (CISPR 22) in Europe and VCCI in Japan. The AFBR-710ISMZ enables equipment compliance to these standards detailed in Table 1. The metal housing and shielded design of the AFBR-710ISMZ minimizes the EMI challenge facing the equipment designer.  For superior EMI performance it is recommended that equipment designs utilize SFP+ cages per SFF 8432. 

## **RF Immunity (Susceptibility)** 

Due to its shielded design, the EMI immunity of the AFBR-710ISMZ exceeds typical industry standards. 

## **Eye Safety** 

The AFBR-710ISMZ provides Class 1 (single fault tolerant) eye safety by design and has been tested for compliance with the requirements listed in Table 1. The eye safety circuit continuously monitors the optical output power level and will disable the transmitter upon detecting a condition beyond the scope of Class 1 certification Such conditions can be due to inputs from the host board (Vcc fluctuation, unbalanced code) or a fault within the transceiver.  US CDRH and EU TUV certificates are listed in table 1. 

## **Flammability** 

The AFBR-710ISMZ optical transceiver is made of metal and high strength, heat resistant, chemical resistant and UL 94V-0 flame retardant plastic. 

5 

**Table 1. Regulatory Compliance** 

|**Table 1. Regulatory Compliance**||
|---|---|
|**Feature**|**Test Method**<br>**Performance**|
|Electrostatic Discharge (ESD)<br>to the Electrical Pins|MIL-STD-883C<br>Method 3015.4<br>Class 1  (> 2000 Volts)|
|Electrostatic Discharge (ESD)<br>to the Duplex LC Receptacle|IEC 61000-4-2<br>Typically, no damage occurs with 25 kV when<br>the duplex LC connector receptacle is con-<br>tacted bya Human BodyModelprobe.|
||IEC 61000-4-2<br>10 contacts of 8 kV on the electrical faceplate<br>with device inserted into apanel.|
|Electrostatic Discharge (ESD)<br>to the Optical Connector|IEC 61000-4-2<br>Air discharge of 15 kV (min.)<br>contact to connector without damage.|
|Electromagnetic Interference<br>(EMI)|FCC Class B<br>CENELEC EN55022 Class B<br>(CISPR 22A)<br>VCCI Class A<br>System margins are dependent on customer<br>board and chassis design.|
|Immunity|IEC 61000-4-3<br>Typically shows no measurable efect from a<br>10 V/m feld swept from 10 MHz to 1 GHz.|
|Laser Eye Safety and<br>Equipment Type Testing<br>**BAUART**<br>**GEPRUFT**<br>**TYPE**<br>**APPROVED**<br>**TUV**<br>**Rheinland**<br>**Product Safety**<br>**¬**<br>**¬**|US FDA CDRH AEL Class 1<br>US21 CFR, Subchapter J per<br>Paragraphs 1002.10<br>and 1002.12<br>(IEC) EN 60825-1: 2007<br>(IEC) EN 60825-2: 2004+A1<br>(IEC) EN 60950-1: 2006+A11<br>CDRH Certifcation No.: 9720151-128<br>TUV fle: R 72121699|
|Component Recognition|Underwriters Laboratories and Canadian<br>Standards Association Joint Component<br>Recognition for Information Technology<br>Equipment including Electrical Business<br>Equipment<br>UL fle: E173874, Vol. 1|
|RoHS Compliance|RoHS Directive 2002/95/EC and<br>it’s amendment directives 6/6<br>SGS Test Report No. LPC/13392 (AD-1)/07<br>CTS Ref. CTS/07/3283/Avago|



6 


**----- Start of picture text -----**<br>
VCC ,T<br>GND,T<br>10 k Ω<br>Tx DIS<br>Tx_DISABLE<br>Tx FAULT<br>Tx_FAULT<br>0.1 µF<br>TD+<br>100  Ω<br>TD-<br>0.1 µF LASER DRIVER<br>4.7 k to 10 k Ω<br>4.7 µH VCC ,T<br>0.1 µF 22 µF 0.1 µF<br>3.3 V<br>PROTOCOL IC SERDES IC 4.7 µH VCC ,R VCC ,R<br>0.1 µF 22 µF 0.1 µF VCC ,R<br>µF 50  Ω<br>4.7 k to<br>10 k Ω 50  Ω<br>0.1 µF<br>RD+<br>100  Ω<br>RD-<br>0.1 µF<br>Rx LOS<br>LOSS OF SIGNAL<br>3.3 V<br>GND,R<br>POST AMPLIFIER<br>4.7 k to 10 k Ω 4.7 k to 10 k Ω<br>4.7 k to 10 k Ω MOD_DEF0 MOD_DEF1 MOD_DEF2<br>MODULE DETECT<br>SCL<br>SDA<br>**----- End of picture text -----**<br>


**Figure 2. Typical application configuration.** 


**----- Start of picture text -----**<br>
4.7 µH<br>VCC T<br>0.1 µF 22 µF 0.1 µF<br>3.3 V<br>4.7 µH<br>VCC R<br>0.1 µF 22 µF 0.1 µF<br>SFP MODULE HOST BOARD<br>NOTE: INDUCTORS MUST HAVE LESS THAN 1 Ω  SERIES RESISTANCE TO LIMIT VOLTAGE DROP TO THE SFP MODULE.<br>**----- End of picture text -----**<br>


**Figure 3. Recommended power supply filter.** 

7 

**Table 2. Contact Description** 

|**Contact**|**Symbol**|**Function/Description**|**Notes**|
|---|---|---|---|
|1|VeeT|Transmitter Signal Ground|Note 1|
|2|TX_FAULT|Transmitter Fault(LVTTL-O)– High indicates a fault condition|Note 2|
|3|TX_DISABLE|Transmitter Disable(LVTTL-I)– High or open disables the transmitter|Note 3|
|4|SDA|Two Wire Serial Interface Data Line (LVCMOS – I/O)||
|||(same as MOD-DEF2 in INF-8074)|Note 4|
|5|SCL|Two Wire Serial Interface Clock Line (LVCMOS – I/O)||
|||(same as MOD-DEF1 in INF-8074)|Note 4|
|6|MOD_ABS|Module Absent(Output),connected to VeeT or VeeR in the module|Note 5|
|7|RS0|Rate Select 0 - Not used,Presents high input impedance.||
|8|RX_LOS|Receiver Loss of Signal(LVTTL-O)|Note 2|
|9|RS1|Rate Select 1 - Not used,Presents high input impedance.||
|10|VeeR|Receiver Signal Ground|Note 1|
|11|VeeR|Receiver Signal Ground|Note 1|
|12|RD-|Receiver Data Out Inverted(CML-O)||
|13|RD+|Receiver Data Out(CML-O)||
|14|VeeR|Receiver Signal Ground||
|15|VccR|Receiver Power  + 3.3 V||
|16|VccT|Transmitter Power  +  3.3 V||
|17|VeeT|Transmitter Signal Ground|Note 1|
|18|TD+|Transmitter Data In(CML-I)||
|19|TD-|Transmitter Data In Inverted(CML-I)||
|20|VeeT|Transmitter Signal Ground|Note 1|



## **Notes:** 

1. The module signal grounds are isolated from the module case. 

2. This is an open collector/drain output that on the host board requires a 4.7 kΩ to 10 kΩ pullup resistor to VccHost. See Figure 2. 

3. This input is internally biased high with a 4.7 kΩ to 10 kΩ pullup resistor to VccT. 

4. Two-Wire Serial interface clock and data lines require an external pullup resistor dependent on the capacitance load. 

5. This is a ground return that on the host board requires a 4.7 kΩ to 10 kΩ pullup resistor to VccHost. 


**----- Start of picture text -----**<br>
10 11<br>BOTTOM OF<br>TOWARDHOST BOARD ASVIEWED FROMTOP THROUGHBOARD TOP VIEWOF BOARD<br>1 20<br>**----- End of picture text -----**<br>


**Figure 4. Module edge connector contacts** 

8 

## **Table 3. Absolute Maximum Ratings** 

Stress in excess of any of the individual Absolute Maximum Ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions. It should not be assumed that limiting values of more than one parameter can be applied concurrently. Exposure to any of the Absolute Maximum Ratings for extended periods can adversely affect reliability. 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|-40|85|C||
|Case OperatingTemperature|TC|-40|85|C||
|Relative Humidity(Non condensing)|RH|5|95|%||
|SupplyVoltage|VccT, VccR|-0.3|3.8|V|Note 1|
|Low Speed Input Voltage||-0.5|Vcc+0.5|V||
|Two-Wire Interface Input Voltage||-0.5|Vcc+0.5|V||
|High Speed Input Voltage, Single Ended||-0.3|Vcc+0.5|V||
|High Speed Input Voltage, Diferential|||2.5|V||
|Low Speed Output Current||-20|20|mA||
|Optical Receiver Input Average Power|||0|dBm||



**Note;** 

1. The module supply voltages, VccT and VccR must not differ by more than 0.5 V or damage to the device may occur. 

## **Table 4. Recommended Operating Conditions** 

Recommended Operating Conditions specify parameters for which the electrical and optical characteristics hold unless otherwise noted. Optical and electrical charactristics are not defined for operation outside the Recommended Operating Conditions, reliability is not implied and damage to the module may occur for such operation over an extended period of time. 

|extended period of time.||||||
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|Case OperatingTemperature|TC|0|85|°C|Note 1|
|Module SupplyVoltage|VccT, VccR|3.135|3.465|V|Fig. 3|
|Host SupplyVoltage|VccHost|3.14|3.46|V||
|Signal Rate||9.8|10.313|GBd||
|Power Supply Noise Tolerance|||66|mVp-p|Fig. 3|
||||10Hz to 10MHz|||
|Tx Input Single Ended DC|V|-0.3|4.0|V||
|Voltage Tolerance (Ref VeeT)||||||
|Rx Output Single Ended Voltage Tolerance|V|-0.3|4.0|V||



## **Notes:** 

1.  Ambient operating temperature limits are based on the Case Operating Temperature limits and are subject to the host system thermal design. See Figure 7 for the module Tc reference point. 

9 

## **Table 5. Low Speed Signal Electrical Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. Typical values are for Tc = 40°C. VccT and VccR = 3.3 V. 

|<br>Typical values are for Tc = 40°C. VccT and VccR = 3.3 V.||
|---|---|
|**Parameter**<br>**Symbol**|**Minimum**<br>**Typical**<br>**Maximum**<br>**Unit**<br>**Notes**|
|Module SupplyCurrent<br>ICC|180<br>289<br>mA<br>Note 1|
|Power Dissipation<br>PDISS|600<br>1000<br>mW|
|TX_FAULT, RX_LOS<br>IOH<br>VOL|- 50<br>+ 37.5<br>mA<br>Note 2<br>-0.3<br>0.4<br>V|
|TX_DISABLE<br>VIH<br>VIL|2.0<br>VccT + 0.3<br>V<br>Note 3<br>-0.3<br>0.8<br>V|



## **Notes:** 

1. Supply current includes both VccT and VccR connections. 

2. Measured with a 4.7 k Ω load to VccHost. 

3. TX_DISABLE has an internal 4.7 kΩ to 10 kΩ pull-up to VccT 

## **Table 6. High Speed Signal Electrical Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. Typical values are for Tc = 40°C. VccT and VccR = 3.3 V. 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Tx Input Diferential Voltage (TD +/-)|VI|180||700|mV|Note 1|
|Tx Input AC Common Mode Voltage Tolerance||||15|mV(RMS)||
|Tx Input Diferential S-parameter (100 Ω Ref.)|SDD11|||-10|dB|0.01-1.0 GHz|
|||||Note 3|dB|1.0-11.1 GHz|
|Tx Input Diferential to Common|SCD11|||-10|dB|0.01-11.1 GHz|
|Mode Conversion (25 Ω Ref.)|||||||
|Rx Output Diferential Voltage (RD +/-)|Vo|300||850|mV|Note 2|
|Rx Output Termination Mismatch @ 1MHz|DZm|||5|%||
|Rx Output AC Common Mode Voltage||||7.5|mV(RMS)|Note 5|
|Rx Output Output Rise and Fall Time|tr, tf|28|||ps||
|(20% to 80%)|||||||
|Rx Output Total Jitter|TJ|||0.70|Ulp-p||
|Rx Output 99% Jitter|J2|||0.42|Ulp-p||
|Rx Output Diferential S-parameter|SDD22|||-12|dB|0.01-1.0 GHz|
|(100 Ω Ref.)||||Note 4|dB|1.0-11.1 GHz|
|Rx Output Common Mode Refection|SCC22|||-6|dB|0.01-2.5 GHz|
|Coefcient (25 Ω Ref.)||||-3|dB|2.5-11.1 GHz|
|Receiver Output Eye Mask||||||See Figure 5a|



## **[Notes:]** 

1. Internally AC coupled and terminated (100 Ohm differential). 

2. Internally AC coupled but requires an external load termination (100 Ohm differential). 

3. Maximum reflection coefficient is expressed as SDD11=Max(-12+2*sqrt(f) , -6.3+13*log10(f/5.5)), for f in GHz. 

4. Maximum reflection coefficient is expressed as SDD22=Max(-12+2*sqrt(f) , -6.3+13*log10(f/5.5)), for f in GHz. 

5. The RMS value is measured by calculating the standard deviation of the histogram for one UI of the common mode signal. 

10 


**----- Start of picture text -----**<br>
1.40<br>425<br>1.0<br>0.75<br>150<br>0.73<br>0<br>0.5<br>-150<br>0.28<br>0.25<br>0<br>-425<br>-0.40<br>0 0.35 0.65 1.0 0 0.25 0.40 0.45 0.55 0.60 0.75 1<br>NORMALIZED TIME (UNIT INTERVAL) NORMALIZED TIME (UNIT INTERVAL)<br>NORMALIZED AMPLITUDE<br>ABSOLUTE AMPLITUDE - mV<br>**----- End of picture text -----**<br>


**Figure 5a. Receiver Electrical Optical Eye Mask Definition** 

**Figure 5b. Transmitter Optical Eye Mask Definition** 

**Table 7. Two-Wire Interface Electrical Characteristics** 

|**Parameter**|**Symbol**<br>**Min.**<br>**Max.**<br>**Unit**<br>**Conditions**|
|---|---|
|Host Vcc Range|VccHTWI<br>3.135<br>3.465<br>V|
|SCL and SDA|VOL<br>0.0<br>0.40<br>V<br>Rp[1]pulled to VccHTWI,<br>VOH<br>VccHTWI - 0.5<br>VccHTWI + 0.3<br>V<br>measured at host side of<br>connector|
|SCL and SDA|VIL<br>-0.3<br>VccT*0.3<br>V|
||VIH<br>VccT*0.7<br>VccT + 0.5<br>V|
|Input Current on the<br>SCL and SDA Contacts|Il<br>-10<br>10<br>µA|
|Capacitance on SCL<br>and SDA Contacts|Ci[2]<br>14<br>pF|
|Total bus capacitance<br>for SCL and for SDA|Cb[3]<br>100<br>pF<br>At 400  kHz, 3.0 kΩ Rp, max<br>At 100  kHz, 8.0 kΩ Rp, max|
||290<br>pF<br>At 400  kHz, 1.1 kΩRp, max<br>At 100  kHz, 2.75 kΩ Rp, max|



## **Notes:** 

1. Rp is the pull up resistor. Active bus termination may be used by the host in place of a pullup resistor. Pull ups can be connected to various power supplies, however the host board design shall ensure that no module contact has voltage exceeding VccT or VccR by 0.5 V nor requires the module to sink more than 3.0 mA current. 

2. Ci is the capacitance looking into the module SCL and SDA contacts 

3. Cb is the total bus capacitance on the SCL or SDA bus. 

11 

## **Table 8. Optical Specifications** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. Typical values are for Tc = 40°C. VccT and VccR = 3.3 V. 

|<br>Typical values are for Tc = 40°C. VccT and|<br>VccR = 3.3 V.|||||
|---|---|---|---|---|---|
|**Parameter**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|**Transmitter**||||||
|Laser OMA outputpower|-4.3|||dBm|1,2,3,Table 9|
|Laser mean outputpower|||-1.0|dBm|1,2,4|
|Laser ofpower|||-30|dBm|1|
|Extinction ratio|3.0|||dB|1,2|
|Transmitter and dispersionpenalty (TDP)|||3.9|dB|1|
|Center Wavelength|840||860|nm|1,3,Table 9|
|RMS spectral width,standard deviation|||||1,3,Table 9|
|RIN12OMA|||-128|dB/Hz|1|
|Optical Return Loss Tolerance|||12|dB|1|
|Encircled Flux|||||5|
|Transmitter Output Eye Mask|||||1,See Figure 5b|
|**Receiver**||||||
|Stressed sensitivity (OMA)|–||-7.5|dBm|1|
|Receive sensitivity (OMA)|||-11.1|dBm||
|Receive Power(Pave)Overload|-1.0|||dBm|1|
|Refectance|||-12|dB|1|
|Center Wavelength|840||860|nm|1|
|RX_LOS(OMA)Of|||-12|dBm||
|RX_LOS(OMA)On|-30|||dBm||
|RX_LOS(OMA)Hysteresis|0.5|||dB||
|Vertical eye closurepenalty|3.5|||dB|6|
|Stressed eyejitter|0.3|||UIp-p|6|



## **General Specification Considerations (Notes):** 

1.  IEEE 802.3ae Clause 52 compliant. 

2.  These parameters are interrelated:  see IEEE 802.3ae, Clause 52. 

3.  See Table 9.  Trade-offs are available among spectral width, center wavelength, and minimum optical modulation amplitude. 4.  The 10GBASE-SR/SW launch power shall be the lesser of the Class 1 safety limit as defined in IEEE 802.3ae 52.10.2 or the average receive power maximum defined by IEEE 802.3ae -2002 Table 52-9. 

4.  The 10GBASE-SR/SW launch power shall be the lesser of the Class 1 safety limit as defined in IEEE 802.3ae 52.10.2 or the average receive 

5.  The transceiver’s launch condition meets the requirement of 10 Gigabit Ethernet multimode fiber as detailed in TIA 492AAAC. 

6.   Vertical eye closure penalty and Stressed eye jitter are test conditions for Stressed sensitivity (OMA) measurements. 

12 

**Table 9. Minimum Optical Modulation Amplitude** 

|**Center**<br>**Wavelength**<br>**(nm)**|**RMS Spectral Width (nm)**|
|---|---|
||**Up to**<br>**0.05 to**<br>**0.1 to**<br>**0.15 to**<br>**0.2 to**<br>**0.25 to**<br>**0.3 to**<br>**0.35 to**<br>**0.4 to**<br>**0.05**<br>**0.1**<br>**0.15**<br>**0.2**<br>**0.25**<br>**0.3**<br>**0.35**<br>**0.4**<br>**0.45**|
|840 to 842|-4.2<br>-4.2<br>-4.1<br>-4.1<br>-3.9<br>-3.8<br>-3.5<br>-3.2<br>-2.8|
|842 to 844|-4.2<br>-4.2<br>-4.2<br>-4.1<br>-3.9<br>-3.8<br>-3.6<br>-3.3<br>-2.9|
|844 to 846|-4.2<br>-4.2<br>-4.2<br>-4.1<br>-4.0<br>-3.8<br>-3.6<br>-3.3<br>-2.9|
|846 to 848|-4.3<br>-4.2<br>-4.2<br>-4.1<br>-4.0<br>-3.8<br>-3.6<br>-3.3<br>-2.9|
|848 to 850|-4.3<br>-4.2<br>-4.2<br>-4.1<br>-4.0<br>-3.8<br>-3.6<br>-3.3<br>-3.0|
|850 to 852|-4.3<br>-4.2<br>-4.2<br>-4.1<br>-4.0<br>-3.8<br>-3.6<br>-3.4<br>-3.0|
|852 to 854|-4.3<br>-4.2<br>-4.2<br>-4.1<br>-4.0<br>-3.9<br>-3.7<br>-3.4<br>-3.1|
|854 to 856|-4.3<br>-4.3<br>-4.2<br>-4.1<br>-4.0<br>-3.9<br>-3.7<br>-3.4<br>-3.1|
|856 to 858|-4.3<br>-4.3<br>-4.2<br>-4.1<br>-4.0<br>-3.9<br>-3.7<br>-3.5<br>-3.1|
|858 to 860|-4.3<br>-4.3<br>-4.2<br>-4.2<br>-4.1<br>-3.9<br>-3.7<br>-3.5<br>-3.2|



13 

## **Table 10. Control Functions: Low Speed Signals Timing Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|TX_DISABLE Assert Time|t_of||10|µs|Note 1,Fig. 6|
|TX_DISABLE Negate Time|t_on||2|ms|Note 2,Fig. 6|
|Time to initialize,includingreset of TX_FAULT|t_init||300|ms|Note 3,Fig. 6|
|TX_FAULT Assert Time|t_fault||1|ms|Note 4,Fig. 6|
|TX_DISABLE to Reset|t_reset|10||µs|Note 5,Fig. 6|
|RX_LOS Assert Time|t_los_on||100|µs|Note 6,Fig. 6|
|RX_LOS Deassert Time|t_los_of||100|µs|Note 7,Fig. 6|



## **Notes:** 

1. Time from rising edge of TX_DISABLE to when the optical output falls below 10% of nominal.  A 10 ms interval between assertions of TX_ DISABLE is required. 

2. Time from falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal. 

3. Time from power on or falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal and the Two-Wire interface is available. 

4. From power on or negation of TX_FAULT using TX_DISABLE. 

5. Time TX_DISABLE must be held high to reset the laser fault shutdown circuitry. 

6. Time from loss of optical signal to Rx_LOS Assertion. 

7. Time from valid optical signal to Rx_LOS De-Assertion. 

## **Table 11. Control Functions: Two-Wire Interface Timing Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|TX_DISABLE Assert Time|t_of_twi||100|ms|Note 1|
|TX_DISABLE Negate Time|t_on_twi||100|ms|Note 2|
|TX_FAULT Assert Time|t_fault_twi||100|ms|Note 3|
|Rx_LOS Assert Time|t_loss_on_twi||100|ms|Note 4|
|Rx_LOS Deassert Time|t_loss_of_twi||100|ms|Note 5|
|Analog parameter data ready|t_data||1000|ms|Note 6|
|Two-Wire Interface Ready|t_serial||300|ms|Note 7|
|Write Cycle Time Parameter|t_write||80|ms|Note 8|
|Two-Wire Interface Clock Rate|f_serial_clock||400|kHz|Note 9|
|Time bus free before new|t_BUF|20||ms|Note 10|
|transmission can start||||||



## **Notes:** 

1. Time from two-wire interface assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output falls below 10% of nominal. Measured from falling clock edge after stop bit of write transaction. 

2. Time from two-wire interface de-assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the modulated optical output rises above 90% of nominal. 

3. Time from fault to two-wire interface TX_FAULT (A2h, byte 110, bit 2) asserted. 

4. Time for two-wire interface assertion of Rx_LOS (A2h, byte 110, bit 1) from loss of optical signal. 

5. Time for two-wire interface de-assertion of Rx_LOS (A2h, byte 110, bit 1) from presence of valid optical signal. 

6. From power on to data ready bit asserted (A2h, byte 110, bit 0). Data ready indicates analog monitoring circuitry is functional. 

7. Time from power on until module is ready for data transmission over the two-wire interface (reads or writes over A0h and A2h). 

8. Time from stop bit to completion of a 1-8 byte write command. For a one to four byte write the maximum cycle time is 40ms and for a five to eight byte write the maximum cycle time is 80ms. 

9. Module may clock stretch for f_serial_clock greater than 100 kHz. 

10. Between STOP and START. See SFF 8431 Section 4.3 

14 

**Table 12. Transceiver Digital Diagnostic Monitor (Real Time Sense) Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. Typical values are for Tc = 40°C. VccT and VccR = 3.3 V. 

|**Parameter**|**Symbol**|**Min.**|**Units**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal Temperature|TINT|±5.0|°C|Temperature is measured internal to the transceiver.|
|Accuracy||||Valid from =  -40°C to 85°C case temperature.|
|Transceiver Internal Supply|VINT|±0.1|V|Supply voltage is measured internal to the transceiver|
|Voltage Accuracy||||and can, with less accuracy, be correlated to|
|||||voltage at the VccT contact. Valid over 3.3 V ± 10%.|
|Transmitter Laser DC Bias Current|IINT|±10|%|IINTaccuracy is better than ±10% of the nominal value.|
|Accuracy|||||
|Transmitted Average Optical|PT|±3.0|dB|Average Power coupled into 50/125 µm multi-mode|
|Output Power Accuracy||||fber. Valid from100 µW to 500 µW.|
|Received Average Optical Input|PR|±3.0|dB|Average Power coupled from 50/125 µm multi-mode|
|Power Accuracy||||fber. Valid from 77 µW to 500 µW.|




**----- Start of picture text -----**<br>
VCCT, VCCR > 2.97 V VCCT, VCCR > 2.97 V<br>TX_FAULT TX_FAULT<br>TX_DISABLE TX_DISABLE<br>TRANSMITTED SIGNAL TRANSMITTED SIGNAL<br>t_init t_init<br>t-init: TX DISABLE NEGATED t-init: TX DISABLE ASSERTED<br>VCCT, VCCR > 2.97 V TX_FAULT<br>TX_FAULT TX_DISABLE<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>TRANSMITTED SIGNAL<br>t_off t_on<br>t_init<br>INSERTION<br>t-init: TX DISABLE NEGATED, MODULE HOT PLUGGED  t-off & t-on: TX DISABLE ASSERTED THEN NEGATED<br>OCCURANCE OF FAULT<br>OCCURANCE OF FAULT<br>TX_FAULT<br>TX_FAULT<br>TX_DISABLE<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>TRANSMITTED SIGNAL<br>t_fault * SFP SHALL CLEAR TX_FAULT IN t_reset t_init*<br>  < t_init IF THE FAILURE IS TRANSIENT<br>t-fault: TX FAULT ASSERTED, TX SIGNAL NOT RECOVERED t-reset: TX DISABLE ASSERTED THEN NEGATED, TX SIGNAL RECOVERED<br>OCCURANCE OF FAULT<br>TX_FAULT OCCURANCE<br>OPTICAL SIGNAL OF LOSS<br>TX_DISABLE<br>TRANSMITTED SIGNAL LOS<br>t_fault<br>t_reset t_loss_on t_loss_off<br>* SFP SHALL CLEAR TX_FAULT IN t_init*<br>   <  t_init IF THE FAILURE IS TRANSIENT<br>t-fault: TX DISABLE ASSERTED THEN NEGATED, TX SIGNAL NOT RECOVERED t-los-on & t-los-off<br>**----- End of picture text -----**<br>


**Figure 6. Transceiver timing diagrams (module installed and power applied except where noted)** 

15 

**Table 13. EEPROM Serial ID Memory Contents – Conventional SFP Memory (Address A0h)** 

|**Byte #**|**Data**|**Notes**|**Byte #**|**Data**|**Notes**|
|---|---|---|---|---|---|
|**Decimal**|**Hex**||**Decimal**|**Hex**||
|0|03|SFPphysical device|37|00|Hex Byte of Vendor OUI[1]|
|1|04|SFP function defned by serial ID only|38|17|Hex Byte of Vendor OUI[1]|
|2|07|LC optical connector|39|6A|Hex Byte of Vendor OUI[1]|
|3|10|10G Base-SR|40|41|“A” - Vendor Part Number ASCII character|
|4|00||41|46|“F” - Vendor Part Number ASCII character|
|5|00||42|42|“B” - Vendor Part Number ASCII character|
|6|00||43|52|“R” - Vendor Part Number ASCII character|
|7|00||44|2D|“-” - Vendor Part Number ASCII character|
|8|00||45|37|“7” - Vendor Part Number ASCII character|
|9|00||46|30|“1” - Vendor Part Number ASCII character|
|10|00||47|39|“0” - Vendor Part Number ASCII character|
|11|06|64B/66B|48|41|“I” - Vendor Part Number ASCII character|
|12|67|10312.5 Mbit/sec nominal bit rate|49|53|“S” - Vendor Part Number ASCII character|
|||(10.3125 Gbit/s)||||
|13|00|Unspecifed|50|4D|“M” - Vendor Part Number ASCII character|
|14|00||51|5A|“Z” - Vendor Part Number ASCII character|
|15|00||52|20|“ ” - Vendor Part Number ASCII character|
|16|08|82 m of OM2 50/125µm fber|53|20|“ ” - Vendor Part Number ASCII character|
|17|03|33 m of OM1 62.5/125µm fber|54|20|“ ” - Vendor Part Number ASCII character|
|18|00||55|20|“ ” - Vendor Part Number ASCII character|
|19|1E|300 m of OM3 50/125µm fber|56|20|“ ” - Vendor Revision Number ASCII character|
|20|41|“A” - Vendor Name ASCII character|57|20|“ ” - Vendor Revision Number ASCII character|
|21|56|“V” - Vendor Name ASCII character|58|20|“ ” - Vendor Revision Number ASCII character|
|22|41|“A” - Vendor Name ASCII character|59|20|“ ” - Vendor Revision Number ASCII character|
|23|47|“G” - Vendor Name ASCII character|60|03|Hex Byte of Laser Wavelength[2]|
|24|4F|“O” - Vendor Name ASCII character|61|52|Hex Byte of Laser Wavelength[2]|
|25|20|“ ” - Vendor Name ASCII character|62|00||
|26|20|“ ” - Vendor Name ASCII character|63||Checksum for Bytes 0-62[3]|
|27|20|“ ” - Vendor Name ASCII character|64|00|Receiver limitingoutput. 1 Wattpower class.|
|28|20|“ ” - Vendor Name ASCII character|65|1A|Hardware SFP TX_DISABLE, TX_FAULT,|
||||||& RX_LOS|
|29|20|“ ” - Vendor Name ASCII character|66|00||
|30|20|“ ” - Vendor Name ASCII character|67|00||
|31|20|“ ” - Vendor Name ASCII character|68-83||Vendor Serial Number ASCII characters[4]|
|32|20|“ ” - Vendor Name ASCII character|84-91||Vendor Date Code ASCII characters[5]|
|33|20|“ ” - Vendor Name ASCII character|92|68|Digital Diagnostics, Internal Cal, Rx Pwr Avg|
|34|20|“ ” - Vendor Name ASCII character|93|F0|A/W, Soft SFP TX_DISABLE, TX_FAULT,|
||||||& RX_LOS, RATE_SELECT|
|35|20|“ ” - Vendor Name ASCII character|94|03|SFF-8472 Compliance to revision 10.0|
|36|00||95||Checksum for Bytes 64-94[3]|
||||96 - 255|00||



## **Notes:** 

1. The IEEE Organizationally Unique Identifier (OUI) assigned to Avago Technologies is 00-17-6A (3 bytes of hex). 

2.  Laser wavelength is represented in 16 unsigned bits. The hex representation of 850 (nm) is 0352. 

3.  Addresses 63 and 95 are checksums calculated (per SFF-8472) and stored prior to product shipment. 

4. Addresses 68-83 specify the AFBR-710ISMZ ASCII serial number and will vary on a per unit basis. 

5. Addresses 84-91 specify the AFBR-710ISMZ ASCII date code and will vary on a per date code basis. 

16 

**Table 14. EEPROM Serial ID Memory Contents – Enhanced Feature Set Memory (Address A2h)** 

|**Byte #**||**Byte #**||**Byte #**||
|---|---|---|---|---|---|
|**Decimal**|**Notes**|**Decimal**|**Notes**|**Decimal**|**Notes**|
|0|TempH Alarm MSB[1]|26|Tx Pwr L Alarm MSB[4]|104|Real Time Rx Pwr MSB[5]|
|1|TempH Alarm LSB[1]|27|Tx Pwr L Alarm LSB[4]|105|Real Time Rx Pwr LSB[5]|
|2|TempL Alarm MSB[1]|28|Tx Pwr H WarningMSB[4]|106|Reserved|
|3|TempL Alarm LSB[1]|29|Tx Pwr H WarningLSB[4]|107|Reserved|
|4|TempH WarningMSB[1]|30|Tx Pwr L WarningMSB[4]|108|Reserved|
|5|TempH WarningLSB[1]|31|Tx Pwr L WarningLSB[4]|109|Reserved|
|6|Temp L Warning MSB[1]|32|Rx Pwr H Alarm MSB[5]|110|Status/Control|
||||||- See Table 15|
|7|TempL WarningLSB[1]|33|Rx Pwr H Alarm LSB[5]|111|Reserved|
|8|Vcc H Alarm MSB[2]|34|Rx Pwr L Alarm MSB[5]|112|FlagBits - See Table 16|
|9|Vcc H Alarm LSB[2]|35|Rx Pwr L Alarm LSB[5]|113|FlagBits - See Table 16|
|10|Vcc L Alarm MSB[2]|36|Rx Pwr H WarningMSB[5]|114|Reserved|
|11|Vcc L Alarm LSB[2]|37|Rx Pwr H WarningLSB[5]|115|Reserved|
|12|Vcc H WarningMSB[2]|38|Rx Pwr L WarningMSB[5]|116|FlagBits - See Table 16|
|13|Vcc H WarningLSB[2]|39|Rx Pwr L WarningLSB[5]|117|FlagBits - See Table 16|
|14|Vcc L WarningMSB[2]|40-55|Reserved|118-127|Reserved|
|15|Vcc L WarningLSB[2]|56-94|External Calibration Constants[6]|128-247|Customer Writeable|
|16|Tx Bias H Alarm MSB[3]|95|Checksum for Bytes 0-94[7]|248-255|Vendor Specifc|
|17|Tx Bias H Alarm LSB[3]|96|Real Time Temperature MSB[1]|||
|18|Tx Bias L Alarm MSB[3]|97|Real Time Temperature LSB[1]|||
|19|Tx Bias L Alarm LSB[3]|98|Real Time Vcc MSB[2]|||
|20|Tx Bias H WarningMSB[3]|99|Real Time Vcc LS[2]|||
|21|Tx Bias H WarningLSB[3]|100|Real Time Tx Bias MSB[3]|||
|22|Tx Bias L WarningMSB[3]|101|Real Time Tx Bias LSB[3]|||
|23|Tx Bias L WarningLSB[3]|102|Real Time Tx Power MSB[4]|||
|24|Tx Pwr H Alarm MSB[4]|103|Real Time Tx Power LSB[4]|||
|25|Tx Pwr H Alarm LSB[4]|||||



## **Notes:** 

1. Temperature (Temp) is decoded as a 16 bit signed twos compliment integer in increments of 1/256°C. 

2. Supply Voltage (Vcc) is decoded as a 16 bit unsigned integer in increments of 100 µV. 

3. Laser bias current (Tx Bias) is decoded as a 16 bit unsigned integer in increments of 2 µA. 

4. Transmitted average optical power (Tx Pwr) is decoded as a 16 bit unsigned integer in increments of 0.1 µW. 

5. Received average optical power (Rx Pwr) is decoded as a 16 bit unsigned integer in increments of 0.1 µW. 

6. Bytes 56-94 are not intended for use with AFBR-710ISMZ, but have been set to default values per SFF-8472. 

7. Byte 95 is a checksum calculated (per SFF-8472) and stored prior to product shipment. 

17 

**Table 15. EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110)** 

||**Status/**|||
|---|---|---|---|
|**Bit #**|**Control Name**|**Description**|**Notes**|
|7|TX_DISABLE State|Digital state of SFP TX_DISABLE Input(1 = TX_DISABLE asserted)|Note 1|
|6|Soft TX_DISABLE|Read/write bit for changingdigital state of TX_DISABLE function|Note 1,2|
|5|Reserved|||
|4|Reserved|||
|3|Reserved|||
|2|TX_FAULT State|Digital state of the SFP TX_FAULT Output(1 = TX_FAULT asserted)|Note 1|
|1|RX_LOS State|Digital state of the SFP RX_LOS Output(1 = RX_LOS asserted)|Note 1|
|0|Data Ready (Bar)|Indicates transceiver ispowered and real time sense data is ready.(0 = Ready)||



> **[Notes:]** 

1. The response time for soft commands of the AFBR-710ISMZ is 100 msec as specified by SFF-8472. 

2. Bit 6 is logic OR’d with the SFP TX_DISABLE input on contact 3; either asserted will disable the SFP+ transmitter. 

**Table 16. EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)** 

|**Byte**|**Bit**|**Flag Bit Name Description**||
|---|---|---|---|
|112|7|Temp High Alarm|Set when transceiver internal temperature exceeds high alarm threshold|
||6|Temp Low Alarm|Set when transceiver internal temperature exceeds low alarm threshold|
||5|Vcc High Alarm|Set when transceiver internal supplyvoltage exceeds high alarm threshold|
||4|Vcc Low Alarm|Set when transceiver internal supplyvoltage exceeds low alarm threshold|
||3|Tx Bias High Alarm|Set when transceiver laser bias current exceeds high alarm threshold|
||2|Tx Bias Low Alarm|Set when transceiver laser bias current exceeds low alarm threshold|
||1|Tx Power High Alarm|Set when transmitted average optical power exceeds high alarm threshold|
||0|Tx Power Low Alarm|Set when transmitted average optical power exceeds low alarm threshold|
|113|7|Rx Power High Alarm|Set when received average optical power exceeds high alarm threshold|
||6|Rx Power Low Alarm|Set when received average optical power exceeds low alarm threshold|
||0-5|Reserved||
|116|7|Temp High Warning|Set when transceiver internal temperature exceeds high warningthreshold|
||6|Temp Low Warning|Set when transceiver internal temperature exceeds low warningthreshold|
||5|Vcc High Warning|Set when transceiver internal supplyvoltage exceeds high warningthreshold|
||4|Vcc Low Warning|Set when transceiver internal supplyvoltage exceeds low warningthreshold|
||3|Tx Bias High Warning|Set when transceiver laser bias current exceeds high warningthreshold|
||2|Tx Bias Low Warning|Set when transceiver laser bias current exceeds low warningthreshold|
||1|Tx Power High Warning|Set when transmitted average optical power exceeds high warningthreshold|
||0|Tx Power Low Warning|Set when transmitted average optical power exceeds low warningthreshold|
|117|7|Rx Power High Warning|Set when received average optical power exceeds high warningthreshold|
||6|Rx Power Low Warning|Set when received average optical power exceeds low warningthreshold|
||0-5|Reserved||



18 

**Figure 7.  Module drawing** 

**AFBR-7 1 0 I SMZ** 

**Figure 8. Module label** 

For product information and a complete list of distributors, please go to our website: **www.avagotech.com** 

Avago, Avago Technologies, and the A logo are trademarks of Avago Technologies in the United States and other countries. Data subject to change. Copyright © 2005-2013 Avago Technologies. All rights reserved. AV02-3837EN  -  April 17, 201 9 

