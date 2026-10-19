## **Data Sheet** 

## **AFBR-710SMZ 10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver** 

## **Description** 

The Broadcom[®] AFBR-710SMZ transceiver is part of a family of SFP+ products. This transceiver utilizes Broadcom’s 850 nm VCSEL and PIN Detector technology to provide an IEEE 10Gb Ethernet design compliant with the 10GBASE-SR and 10GBASE-SW standards. The AFBR710SMZ transceiver is designed to enable 10Gb Ethernet equipment designs with very high port density based on the new electrical and mechanical specification enhancements to the well known SFP specifications developed by the SFF Committee. These specifications are referred to as SFP+ to recognize these enhancements to previous SFP specifications used for lower speed products. Broadcom is an active participant in the SFF Committee specification development activities. 

## **Related Products** 

- AFBR-710ASMZ is an SFP+ 10 Gigabit Ethernet 10GBASE-SR/SW transceiver with case temperature operated at 0°C to 85°C for use on multimode fiber cables. It is best suited for OM3 high bandwidth MMF link applications with link lengths up to 300 meters. 

- AFBR-710DMZ SFP+ 10Gb/1Gb Gigabit Ethernet 10GBASE-SR transceiver for operation in 300m reach using OM3 MMF. 

- AFCT-739SMZ (AFCT-739ASMZ) with case temperature 0°C to 70°C (0°C to 85°C) SFP+ 10 Gigabit Ethernet 10GBASE-LR transceiver for operation in SMF link applications to10 km. 

- AFCT-5716Z SFP+ Evaluation Board. The purpose of this SFP+ evaluation board is to provide the designer with a convenient means for evaluating SFP+ fiber optic transceivers. 

## **Features** 

- Broadcom 850 nm VCSEL source and Transmitter Optical Subassembly technology 

- Broadcom PIN detector and Receiver Optical Subassembly technology 

- Typical power dissipation 600 mW 

- Full digital diagnostic management interface 

- Broadcom SFP+ package design enables equipment EMI performance in high port density applications with margin to Class B limits 

## **Specifications** 

- Optical interface specifications per IEEE 802.3ae 10GBASE-SR and 10GBASE-SW 

- Link lengths at 10.3125 GBd: – 300m with 50 μm OM3 MM fiber 

   - 400m with 50 μm OM4 MM fiber 

- Electrical interface specifications per SFF Committee SFF 8431 _Specifications for Enhanced 8.5 and 10 Gigabit Small Form Factor Pluggable Module SFP+_ 

- Management interface specifications per SFF Committee SFF 8431 and SFF 8472 _Diagnostic Monitoring Interface for Optical Transceivers_ 

- Mechanical specifications per SFF Committee SFF 8432 _Improved Pluggable Formfactor IPF_ 

- LC Duplex optical connector interface confirming to ANSI TIA/EA 604-10 (FOCIS 10A) 

- Compliant to Restriction on Hazardous Substances (RoHS) per EU and China requirements 

- Class 1 Eye safe per requirements of IEC 60825-1 / CDRH 

AV02-3399EN November 09, 2023 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Installation** 

The AFBR-710SMZ transceiver package is compliant with the SFF 8432 _Improved Pluggable Formfactor_ housing specification for the SFP+. It can be installed in any INF-8074 or SFF-8431/2 compliant Small Form Pluggable (SFP) port regardless of host equipment operating status The AFBR-710SMZ is hot-pluggable, allowing the module to be installed while the host system is operating and online. Upon insertion, the transceiver housing makes initial contact with the host board SFP cage, mitigating potential damage due to Electro-Static Discharge (ESD). 

## **Compliance Prediction** 

Compliance prediction is the ability to determine if an optical transceiver is operating within its operating and environmental requirements. AFBR-710SMZ devices provide real-time access to transceiver internal supply voltage and temperature, allowing a host to identify potential component compliance issues. Received optical power is also available to assess compliance of a cable plant and remote transmitter. When operating out of requirements, the link cannot guarantee error free transmission. 

## **Fault Isolation** 

## **Digital Diagnostic Interface and Serial Identification** 

The two-wire interface protocol and signaling detail are based on SFF-8431. Conventional EEPROM memory, bytes 0-255 at memory address 0xA0, is organized in compliance with SFF-8431. New digital diagnostic information, bytes 0-255 at memory address 0xA2, is compliant to SFF-8472. The new diagnostic information provides the opportunity for Predictive Failure Identification, Compliance Prediction, Fault Isolation and Component Monitoring. 

The fault isolation feature allows a host to quickly pinpoint the location of a link failure, minimizing downtime. For optical links, the ability to identify a fault at a local device, remote device or cable plant is crucial to speeding service of an installation. AFBR-710SMZ real-time monitors of Tx_Bias, Tx_Power, Vcc, Temperature and Rx_Power can be used to assess local transceiver current operating conditions. In addition, status flags TX_DISABLE and Rx Loss of Signal (LOS) are mirrored in memory and available via the two-wire serial interface. 

## **Component Monitoring** 

## **Predictive Failure Identification** 

The AFBR-710SMZ predictive failure feature allows a host to identify potential link problems before system performance is impacted. Prior identification of link problems enables a host to service an application via “fail over” to a redundant link or replace a suspect device, maintaining system uptime in the process. For applications where ultra-high system uptime is required, a digital SFP provides a means to monitor two real-time laser metrics associated with observing laser degradation and predicting failure: average laser bias current (Tx_Bias) and average laser optical power (Tx_Power). 

Component evaluation is a more casual use of the AFBR710SMZ real-time monitors of Tx_Bias, Tx_Power, Vcc, Temperature and Rx_Power. Potential uses are as debugging aids for system installation and design, and transceiver parametric evaluation for factory or field qualification. For example, temperature per module can be observed in high density applications to facilitate thermal evaluation of blades, PCI cards and systems. 

AV02-3399EN 

Broadcom 

2 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

**Figure 1:  Transceiver Functional Diagram** 


**----- Start of picture text -----**<br>
OPTICAL INTERFACE ELECTRICAL INTERFACE<br>RECEIVER<br>AMPLIFICATION RD+ (RECEIVE DATA)<br>LIGHT FROM FIBER PHOTO-DETECTOR<br>& QUANTIZATION RD– (RECEIVE DATA)<br>RX_LOS<br>RS0<br>RS1<br>CONTROLLER & MEMORY<br>SDA<br>SCL<br>MOD-ABS<br>TRANSMITTER<br>TX_DISABLE<br>LASER<br>DRIVER & TD+ (TRANSMIT DATA)<br>LIGHT TO FIBER VCSEL SAFETY<br>TD– (TRANSMIT DATA)<br>CIRCUITRY<br>TX_FAULT<br>**----- End of picture text -----**<br>


## **Transmitter Section** 

The transmitter section includes the Transmitter Optical Sub-Assembly (TOSA) and laser driver circuitry. The TOSA, containing a Broadcom designed and manufactured 850 nm VCSEL (Vertical Cavity Surface Emitting Laser) light source, is located at the optical interface and mates with the LC optical connector. The TOSA is driven by an IC which uses the incoming differential high speed logic signal to modulate the laser diode driver current. This Tx laser driver circuit regulates the optical power at a constant level provided the incoming data pattern is DC balanced. 

## **Transmit Disable (TX_DISABLE)** 

The contents of A2h, byte 110, bit 6 are logic OR’d with hardware TX_DISABLE (contact 3) to control transmitter operation. 

## **Transmit Fault (TX_FAULT)** 

A catastrophic laser fault will activate the transmitter signal, TX_FAULT, and disable the laser. This signal is an open collector output (pull-up required on the host board). A low signal indicates normal laser operation and a high signal indicates a fault. The TX_FAULT will be latched high when a laser fault occurs and is cleared by toggling the TX_DISABLE input or power cycling the transceiver. The transmitter fault condition can also be monitored via the twowire serial interface (address A2, byte 110, bit 2). 

The AFBR-710SMZ accepts an LVTTL compatible transmit disable control signal input which shuts down the transmitter optical output. A high signal implements this function while a low signal allows normal transceiver operation. In the event of a fault (e.g. eye safety circuit activated), cycling this control signal resets the module as depicted in Figure 6. An internal pull up resistor disables the transceiver transmitter until the host pulls the input low. TX_DISABLE can also be asserted via the two-wire interface (address A2h, byte 110, bit 6) and monitored (address A2h, byte 110, bit 7). 

AV02-3399EN 3 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Receiver Section** 

The receiver section includes the Receiver Optical SubAssembly (ROSA) and the amplification/quantization circuitry. The ROSA, containing a PIN photodiode and custom transimpedance amplifier, is located at the optical interface and mates with the LC optical connector. The ROSA output is fed to a custom IC that provides postamplification and quantization. 

## **Receiver Loss of Signal (Rx_LOS)** 

The post-amp IC also includes transition detection circuitry which monitors the AC level of incoming optical signals and provides a LVTTL/CMOS compatible status signal to the host. A high status signal indicates loss of modulated signal, indicating link failures such as broken fiber or failed transmitter. Rx_LOS can also be monitored via the two-wire serial interface (address A2h, byte 110, bit 1). 

## **Functional Data I/O** 

The AFBR-710SMZ interfaces with the host circuit board through the twenty contact SFP+ electrical connector. See Table 2 for contact descriptions. The module edge connector is shown in Figure 4. 

The AFBR-710SMZ high speed transmit and receive interfaces require SFF-8431 compliant signal lines on the host board. To simplify board requirements, biasing resistors and AC coupling capacitors are incorporated into the SFP+ transceiver module (per SFF-8431) and hence are not required on the host board. The TX_DISABLE, TX_ FAULT and RX_LOS signals require LVTTL signals on the host board (per SFF-8431) if used. If an application does not take advantage of these functions, care must be taken to ground TX_DISABLE to enable normal operation. 

## **Caution** 

There are no user serviceable parts nor maintenance requirements for the AFBR-710SMZ. All mechanical adjustments are made at the factory prior to shipment. Tampering with, modifying, misusing or improperly handling the AFBR-710SMZ will void the product warranty. It may also result in improper operation and possibly overstress the laser source. Performance degradation or device failure may result. Connection of the AFBR-710SMZ to a light source not compliant with IEEE Std. 802.3ae Clause 52 and SFF-8341 specifications, operating above maximum operating conditions or in a manner inconsistent with it’s design and function may result in exposure to hazardous light radiation and may constitute an act of modifying or manufacturing a laser product. Persons performing such an act are required by law to recertify and re-identify the laser product under the provisions of U.S. 21 CFR (Subchapter J) and TUV. 

## **Customer Manufacturing Processes** 

This module is pluggable and is not designed for aqueous wash, IR reflow, or wave soldering processes. 

## **Ordering Information** 

Please contact your local field sales engineer or one of Broadcom’s franchised distributors for ordering information. For technical information, please visit the Broadcom web page at www.broadcom.com. For information related to SFF Committee documentation visit www.sffcommittee.org. 

Figure 2 depicts the recommended interface circuit to link the AFBR-710SMZ to supporting physical layer ICs. Timing for the dedicated SFP+ control signals implemented in the transceiver are listed in Figure 6. 

## **Application Support** 

An Evaluation Kit and Reference Designs are available to assist in evaluation of the AFBR-710SMZ. Please contact your local Field Sales representative for availability and ordering details. 

AV02-3399EN 4 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Regulatory Compliance** 

The AFBR-710SMZ complies with all applicable laws and regulations as detailed in Table 1. Certification level is dependent on the overall configuration of the host equipment. The transceiver performance is offered as a figure of merit to assist the designer. 

## **Electrostatic Discharge (ESD)** 

The AFBR-710SMZ is compatible with ESD levels found in typical manufacturing and operating environments as described in Table 1. In the normal handling and operation of optical transceivers, ESD is of concern in two circumstances. 

The first case is during handling of the transceiver prior to insertion into an SFP compliant cage. To protect the device, it’s important to use normal ESD handling precautions. These include use of grounded wrist straps, work-benches and floor wherever a transceiver is handled. 

The second case to consider is static discharges to the exterior of the host equipment chassis after installation. If the optical interface is exposed to the exterior of host equipment cabinet, the transceiver may be subject to system level ESD requirements. 

## **Electromagnetic Interference (EMI)** 

Equipment incorporating 10 gigabit transceivers is typically subject to regulation by the FCC in the United States, CENELEC EN55022 (CISPR 22) in Europe and VCCI in Japan. The AFBR-710SMZ enables equipment compliance to these standards detailed in Table 1. The metal housing and shielded design of the AFBR-710SMZ minimizes the EMI challenge facing the equipment designer. For superior EMI performance it is recommended that equipment designs utilize SFP+ cages per SFF 8432. 

## **RF Immunity (Susceptibility)** 

Due to its shielded design, the EMI immunity of the AFBR-710SMZ exceeds typical industry standards. 

## **Eye Safety** 

The AFBR-710SMZ provides Class 1 (single fault tolerant) eye safety by design and has been tested for compliance with the requirements listed in Table 1. The eye safety circuit continuously monitors the optical output power level and will disable the transmitter upon detecting a condition beyond the scope of Class 1 certification Such conditions can be due to inputs from the host board (Vcc fluctuation, unbalanced code) or a fault within the transceiver. US CDRH and EU TUV certificates are listed in Table 1. 

## **Flammability** 

The AFBR-710SMZ optical transceiver is made of metal and high strength, heat resistant, chemical resistant and UL 94V-0 flame retardant plastic. 

AV02-3399EN 5 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Table 1:  Regulatory Compliance** 

|**Feature**|**Test Method**|**Performance**|
|---|---|---|
|Electrostatic Discharge (ESD)<br>to the Electrical Pins|JEDEC A114|Class 1 (> 2000 Volts)<br>>1000V for high speed signalpins TD+-, RD+-|
|Electrostatic Discharge (ESD)<br>to the Duplex LC Receptacle|IEC 61000-4-2|Typically, no damage occurs with 25 kV when the<br>duplex LC connector receptacle is contacted by a<br>Human BodyModelprobe.|
||IEC 61000-4-2|10 contacts of 8 kV on the electrical faceplate with<br>device inserted into apanel.|
|Electrostatic Discharge (ESD)<br>to the Optical Connector|IEC 61000-4-2|Air discharge of 15 kV (min.)<br>contact to connector without damage.|
|Electromagnetic Interference<br>(EMI)|FCC Class B<br>CENELEC EN55022 Class B<br>(CISPR 22A)<br>VCCI Class A|System margins are dependent on customer<br>board and chassis design.|
|Immunity|IEC 61000-4-3|Typically shows no measurable effect from a<br>10 V/m field swept from 10 MHz to 1 GHz.|
|Laser Eye Safety and<br>Equipment Type Testing|Complies with 21 CFR 1040.10 except for<br>conformance with IEC 60825-1 Ed. 3., as<br>described in Laser Notice No. 56, dated<br>May8, 2019.|CDRH certification # 9720151-197|
||IEC/EN 62368-1<br>IEC/EN 60825-1<br>IEC/EN 60825-2|TUV file # R 50394970|
|Component Recognition|Underwriters Laboratories and Canadian<br>Standards Association Joint Component<br>Recognition for Information Technology<br>Equipment including Electrical Business<br>Equipment|UL File # 484615|
|RoHS Compliance|—|Less than 100 ppm of cadmium and less than<br>1000 ppm of lead, mercury, hexavalent<br>chromium, polybrominated biphenyls (PPB) and<br>polybrominated biphenyl ethers (PBDE), Butyl<br>benzyl phthalate (BBP), Dibutyl phthalate (DBP),<br>Diisobutylphthalate.|



AV02-3399EN 6 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Figure 2:  Typical Application Configuration** 


**----- Start of picture text -----**<br>
VCC ,T<br>GND,T<br>10 k �<br>Tx DIS<br>Tx_DISABLE<br>Tx FAULT<br>Tx_FAULT<br>0.1 μF<br>TD+<br>100  �<br>TD-<br>0.1 μF LASER DRIVER<br>4.7 k to 10 k �<br>4.7 μH VCC ,T<br>0.1 μF 22 μF 0.1 μF<br>3.3 V<br>PROTOCOL IC SERDES IC 4.7 μH VCC ,R VCC ,R<br>0.1 μF 22 μF 0.1 μF VCC ,R<br>μF 50  �<br>4.7 k to<br>10 k � 50  �<br>0.1 μF<br>RD+<br>100  �<br>RD-<br>0.1 μF<br>Rx LOS<br>LOSS OF SIGNAL<br>3.3 V<br>GND,R<br>POST AMPLIFIER<br>4.7 k to 10 k � 4.7 k to 10 k �<br>4.7 k to 10 k � MOD_DEF0 MOD_DEF1 MOD_DEF2<br>MODULE DETECT<br>SCL<br>SDA<br>**----- End of picture text -----**<br>


**Figure 3:  Recommended Power Supply Filter** 


**----- Start of picture text -----**<br>
4.7 μH<br>VCC T<br>0.1 μF 22 μF 0.1 μF<br>3.3 V<br>4.7 μH<br>VCC R<br>0.1 μF 22 μF 0.1 μF<br>SFP MODULE HOST BOARD<br>**----- End of picture text -----**<br>


**NOTE: INDUCTORS MUST HAVE LESS THAN 1** � **SERIES RESISTANCE TO LIMIT VOLTAGE DROP TO THE SFP MODULE.** 

AV02-3399EN 7 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

**Table 2:  Contact Description** 

|**Contact**|**Symbol**|**Function/Description**|**Notes**|
|---|---|---|---|
|1|VeeT|Transmitter Signal Ground|Note1|
|2|TX_FAULT|Transmitter Fault(LVTTL-O)– High indicates a fault condition|Note2|
|3|TX_DISABLE|Transmitter Disable(LVTTL-I)– High or open disables the transmitter|Note3|
|4|SDA|Two Wire Serial Interface Data Line (LVCMOS – I/O)<br>(same as MOD-DEF2 in INF-8074)|Note4|
|5|SCL|Two Wire Serial Interface Clock Line (LVCMOS – I/O)<br>(same as MOD-DEF1 in INF-8074)|Note4|
|6|MOD_ABS|Module Absent(Output), connected to VeeT or VeeR in the module|Note5|
|7|RS0|Rate Select 0 - Not used, Presents high input impedance.||
|8|RS_LOS|Receiver Loss of Signal(LVTTL-O)|Note2|
|9|RS1|Rate Select 1 - Not used, Presents high input impedance.||
|10|VeeR|Receiver Signal Ground|Note1|
|11|VeeR|Receiver Signal Ground|Note1|
|12|RD–|Receiver Data Out Inverted(CML-O)||
|13|RD+|Receiver Data Out(CML-O)||
|14|VeeR|Receiver Signal Ground||
|15|VccR|Receiver Power + 3.3V||
|16|VccT|Transmitter Power + 3.3V||
|17|VeeT|Transmitter Signal Ground|Note1|
|18|TD+|Transmitter Data In(CML-I)||
|19|TD–|Transmitter Data In Inverted(CML-I)||
|20|VeeT|Transmitter Signal Ground|Note1|



## **NOTE:** 

1. The module signal grounds are isolated from the module case. 

2. This is an open collector/drain output that on the host board requires a 4.7 kΩ to 10 kΩ pullup resistor to VccHost. See Figure 2. 

3. This input is internally biased high with a 4.7 kΩ to 10 kΩ pullup resistor to VccT. 

4. Two-Wire Serial interface clock and data lines require an external pullup resistor dependent on the capacitance load. 

5. This is a ground return that on the host board requires a 4.7 kΩ to 10 kΩ pullup resistor to VccHost. 

## **Figure 4:  Module Edge Connector Contacts** 


**----- Start of picture text -----**<br>
10 11<br>BOTTOM OF<br>TOWARDHOST BOARD ASVIEWED FROMTOP THROUGHBOARD TOP VIEWOF BOARD<br>1 20<br>**----- End of picture text -----**<br>


AV02-3399EN 8 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Table 3:  Absolute Maximum Ratings** 

Stress in excess of any of the individual Absolute Maximum Ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions. It should not be assumed that limiting values of more than one parameter can be applied concurrently. Exposure to any of the Absolute Maximum Ratings for extended periods can adversely affect reliability. 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|–40|85|°C||
|Case Operating Temperature|TC|–40|85|°C||
|Relative Humidity (Non-condensing)|RH|5|95|%||
|SupplyVoltage|VccT, VccR|–0.3|3.8|V|Note1|
|Low Speed Input Voltage||–0.5|Vcc + 0.5|V||
|Two-Wire Interface Input Voltage||–0.5|Vcc + 0.5|V||
|High Speed Input Voltage, Single-Ended||–0.3|Vcc + 0.5|V||
|High Speed Input Voltage, Differential||—|2.5|V||
|Low Speed Output Current||–20|20|mA||
|Optical Receiver Input Average Power||—|0|dBm||



## **NOTE:** 

1. The module supply voltages, VccT and VccR must not differ by more than 0.5V or damage to the device may occur. 

## **Table 4:  Recommended Operating Conditions** 

Recommended Operating Conditions specify parameters for which the electrical and optical characteristics hold unless otherwise noted. Optical and electrical charactristics are not defined for operation outside the Recommended Operating Conditions, reliability is not implied and damage to the module may occur for such operation over an extended period of time. 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Case Operating Temperature|TC|0|70|°C|Note1|
|Module SupplyVoltage|VccT, VccR|3.135|3.465|V|Figure 3|
|Host SupplyVoltage|VccHost|3.14|3.46|V||
|Signal Rate||9.8|10.313|GBd||
|Power Supply Noise Tolerance||—|66<br>10 Hz to 10 MHz|mVp-p|Figure 3|
|Tx Input Single Ended DC<br>Voltage Tolerance(Ref VeeT)|V|–0.3|4.0|V||
|Rx Output Single Ended Voltage Tolerance|V|–0.3|4.0|V||



## **NOTE:** 

1. Ambient operating temperature limits are based on the Case Operating Temperature limits and are subject to the host system thermal design. See Figure 7 for the module TC reference point. 

AV02-3399EN 9 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Table 5:  Low Speed Signal Electrical Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. Typical values are for TC = 40°C, VccT and VccR = 3.3V. 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Module Supply Current|ICC|—|180|289|mA|Note1|
|Power Dissipation|PDISS|—|600|1000|mW||
|TX_FAULT, RX_LOS|IOH|–50|—|+37.5|μA|Note2|
||VOL|–0.3|—|0.4|V||
|TX_DISABLE|VIH|2.0|—|VccT + 0.3|V|Note3|
||VIL|–0.3|—|0.8|V||



## **NOTE:** 

1. Supply current includes both VccT and VccR connections. 

2. Measured with a 4.7 kΩ load to VccHost. 

3. TX_DISABLE has an internal 4.7 kΩ to 10 kΩ pull-up to VccT. 

## **Table 6:  High Speed Signal Electrical Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. Typical values are for TC = 40°C, VccT and VccR = 3.3V. 

|**Parameter**|**Symbol**|**Minimum**|**Typical**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Tx Input Differential Voltage (TD +/-)|VI|180|—|700|mV|Note1|
|Tx Input AC Common Mode Voltage Tolerance||—|—|15|mV(RMS)||
|Tx Input Differential S-parameter (100Ω Ref.)|SDD11|—|—|–10|dB|0.01 to 1.0 GHz|
||SCD11|—|—|Note3|dB|1.0 to 11.1 GHz|
|Tx Input Differential to Common<br>Mode Conversion(25Ω Ref.)|SCD11|—|—|–10|dB|0.01 to 11.1 GHz|
|Rx Output Differential Voltage (RD +/-)|VO|300|—|850|mV|Note2|
|Rx Output Termination Mismatch @ 1 MHz|ΔZm|—|—|5|%||
|Rx Output AC Common Mode Voltage||—|—|7.5|mV(RMS)|Note5|
|Rx Output Output Rise and Fall Time(20% to 80%)|tr, tf|28|—|—|ps||
|Rx Output Total Jitter|TJ|—|—|0.70|UIp-p||
|Rx Output 99% Jitter|J2|—|—|0.42|UIp-p||
|Rx Output Differential S-parameter (100Ω Ref.)|SDD22|—|—|–12|dB|0.01 to 1.0 GHz|
|||||Note4|dB|1.0 to 11.1 GHz|
|Rx Output Common Mode Reflection Coefficient<br>(25Ω Ref.)|SCC22|—|—|–6|dB|0.01 to 2.5 GHz|
|||||–3|dB|2.5 to 11.1 GHz|
|Receiver Output Eye Mask||—|—|—|—|Figure 5a|



## **NOTE:** 

1. Internally AC coupled and terminated (100 Ohm differential). 

2. Internally AC coupled but requires an external load termination (100 Ohm differential). 

3. Maximum reflection coefficient is expressed as SDD11=Max(–12+2*sqrt(f) , –6.3+13*log10(f/5.5)), for f in GHz. 

AV02-3399EN 10 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

4. Maximum reflection coefficient is expressed as SDD22=Max(–12+2*sqrt(f) , –6.3+13*log10(f/5.5)), for f in GHz. 

5. The RMS value is measured by calculating the standard deviation of the histogram for one UI of the common mode signal. 

**Figure 5a:  Receiver Electrical Optical Eye Mask Definition** 

## **Figure 5b:  Transmitter Optical Eye Mask Definition** 


**----- Start of picture text -----**<br>
425<br>150<br>0<br>-150<br>-425<br>0 0.35 0.65 1.0<br>NORMALIZED TIME (UNIT INTERVAL)<br>ABSOLUTE AMPLITUDE - mV<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
1.40<br>1.0<br>0.75<br>0.73<br>0.5<br>0.28<br>0.25<br>0<br>-0.40<br>0 0.25 0.40 0.45 0.55 0.60 0.75 1<br>NORMALIZED TIME (UNIT INTERVAL)<br>NORMALIZED AMPLITUDE<br>**----- End of picture text -----**<br>


**Table 7:  Two-Wire Interface Electrical Characteristics** 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Conditions**|
|---|---|---|---|---|---|
|Host Vcc Range|VccHTWI|3.135|3.465|V||
|SCL and SDA|VOL|0.0|0.40|V|Rp[1]pulled to VccHTWI, measured at<br>host side of connector|
||VOH|VccHTWI – 0.5|VccHTWI + 0.3|V||
|SCL and SDA|VIL|–0.3|VccT*0.3|V||
||VIH|VccT*0.7|VccT + 0.5|V||
|Input Current on the SCL and<br>SDA Contacts|II|–10|10|μA||
|Capacitance on SCL and SDA<br>Contacts|Ci<br>[2]|—|14|pF||
|Total bus capacitance for SCL<br>and for SDA|Cb<br>[3]|—|100|pF|At 400 kHz, 3.0 kΩ Rp, max.<br>At 100 kHz, 8.0 kΩ Rp, max.|
|||—|290|pF|At 400 kHz, 1.1 kΩ Rp, max.<br>At 100 kHz, 2.75 kΩ Rp, max.|



## **NOTE:** 

1. Rp is the pull up resistor. Active bus termination may be used by the host in place of a pullup resistor. Pull ups can be connected to various power supplies, however the host board design shall ensure that no module contact has voltage exceeding VccT or VccR by 0.5V nor requires the module to sink more than 3.0 mA current. 

2. Ci is the capacitance looking into the module SCL and SDA contacts 

3. Cb is the total bus capacitance on the SCL or SDA bus. 

AV02-3399EN 11 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Table 8:  Optical Specifications** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. Typical values are for Tc = 40°C, VccT and VccR = 3.3V. 

|**Parameter**|**Minimum**|**Typical**|**Maximum**|**Units**|**Notes**|
|---|---|---|---|---|---|
|**Transmitter**||||||
|Laser OMA Output Power|–4.3|—|—|dBm|1,2,3,Table 9|
|Laser Mean Output Power|—|—|–1.0|dBm|1,2,4|
|Laser Off Power|—|—|–30|dBm|1|
|Extinction Ratio|3.0|—|—|dB|1,2|
|Transmitter and Dispersion Penalty (TDP)|—|—|3.9|dB|1|
|Center Wavelength|840|—|860|nm|1,3,Table 9|
|RMS Spectral Width, Standard Deviation|—|—|—||1,3,Table 9|
|RIN12OMA|—|—|–128|dB/Hz|1|
|Optical Return Loss Tolerance|—|—|12|dB|1|
|Encircled Flux|—|—|—||5|
|Transmitter Output Eye Mask|—|—|—||1,Figure 5b|
|**Receiver**||||||
|Stressed Sensitivity (OMA)|—|—|–7.5|dBm|1|
|Receive Sensitivity (OMA)|—|—|–11.1|dBm||
|Receive Power(Pave)Overload|–1.0|—|—|dBm|1|
|Reflectance|—|—|–12|dB|1|
|Center Wavelength|840|—|860|nm|1|
|RX_LOS(OMA)Off|—|—|–12|dBm||
|RX_LOS(OMA)On|–30|—|—|dBm||
|RX_LOS(OMA)Hysteresis|0.5|—|—|dB||
|Vertical Eye Closure Penalty|3.5|—|—|dB|6|
|Stressed Eye Jitter|0.3|—|—|UIp-p|6|



**NOTE:** General Specification Considerations 

1. IEEE 802.3ae Clause 52 compliant. 

2. These parameters are interrelated: see IEEE 802.3ae, Clause 52. 

3. See Table 9. Trade-offs are available among spectral width, center wavelength, and minimum optical modulation amplitude. 

4. The 10GBASE-SR/SW launch power shall be the lesser of the Class 1 safety limit as defined in IEEE 802.3ae 52.10.2 or the average receive power maximum defined by IEEE 802.3ae -2002 Table 52-9. 

5. The transceiver’s launch condition meets the requirement of 10 Gigabit Ethernet multimode fiber as detailed in TIA 492AAAC. 

6. Vertical Eye Closure Penalty and Stressed Eye Jitter are test conditions for Stressed Sensitivity (OMA) measurements. 

AV02-3399EN 

Broadcom 

12 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

**Table 9:  Minimum Optical Modulation Amplitude** 

|**Center Wavelength**<br>**(nm)**|**RMS Spectral Width (nm)**|**RMS Spectral Width (nm)**|**RMS Spectral Width (nm)**|**RMS Spectral Width (nm)**|**RMS Spectral Width (nm)**|**RMS Spectral Width (nm)**|**RMS Spectral Width (nm)**|**RMS Spectral Width (nm)**|**RMS Spectral Width (nm)**|
|---|---|---|---|---|---|---|---|---|---|
||<br>**Up to**<br>**0.05**|**0.05 to**<br>**0.1**|**0.1 to**<br>**0.15**|**0.15 to**<br>**0.2**|**0.2 to**<br>**0.25**|**0.25 to**<br>**0.3**|**0.3 to**<br>**0.35**|**0.35 to**<br>**0.4**|**0.4 to**<br>**0.45**|
|840 to 842|–4.2|–4.2|–4.1|–4.1|–3.9|–3.8|–3.5|–3.2|–2.8|
|842 to 844|–4.2|–4.2|–4.2|–4.1|–3.9|–3.8|–3.6|–3.3|–2.9|
|844 to 846|–4.2|–4.2|–4.2|–4.1|–4.0|–3.8|–3.6|–3.3|–2.9|
|846 to 848|–4.3|–4.2|–4.2|–4.1|–4.0|–3.8|–3.6|–3.3|–2.9|
|848 to 850|–4.3|–4.2|–4.2|–4.1|–4.0|–3.8|–3.6|–3.3|–3.0|
|850 to 852|–4.3|–4.2|–4.2|–4.1|–4.0|–3.8|–3.6|–3.4|–3.0|
|852 to 854|–4.3|–4.2|–4.2|–4.1|–4.0|–3.9|–3.7|–3.4|–3.1|
|854 to 856|–4.3|–4.3|–4.2|–4.1|–4.0|–3.9|–3.7|–3.4|–3.1|
|856 to 858|–4.3|–4.3|–4.2|–4.1|–4.0|–3.9|–3.7|–3.5|–3.1|
|858 to 860|–4.3|–4.3|–4.2|–4.2|–4.1|–3.9|–3.7|–3.5|–3.2|



## **Table 10:  Control Functions: Low Speed Signals Timing Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|TX_DISABLE Assert Time|t_off|—|10|μs|1,Figure 6|
|TS_DISABLE Negate Time|t_on|—|2|ms|2,Figure 6|
|Time to Initialize, includingreset of TX_FAULT|t_init|—|300|ms|3,Figure 6|
|TX_FAULT Assert Time|t_fault|—|1|ms|4,Figure 6|
|TX_DISABLE to Reset|t_reset|10|—|μs|5,Figure 6|
|RX_LOS Assert Time|t_los_on|—|100|μs|6,Figure 6|
|RX_LOS Deassert Time|t_los_off|—|100|μs|7,Figure 6|



## **NOTE:** 

1. Time from rising edge of TX_DISABLE to when the optical output falls below 10% of nominal. A 10 ms interval between assertions of TX_DISABLE is required. 

2. Time from falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal. 

3. Time from power on or falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal and the Two-Wire interface is available. 

4. From power on or negation of TX_FAULT using TX_DISABLE. 

5. Time TX_DISABLE must be held high to reset the laser fault shutdown circuitry. 

6. Time from loss of optical signal to Rx_LOS Assertion. 

7. Time from valid optical signal to Rx_LOS Deassertion. 

AV02-3399EN 13 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Table 11:  Control Functions: Low Speed Signals Timing Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|TX_DISABLE Assert Time|t_off_twi|—|100|ms|1|
|TS_DISABLE Negate Time|t_on_twi|—|100|ms|2|
|TX_FAULT Assert Time|t_fault_twi|—|100|ms|3|
|RX_LOS Assert Time|t_los_on_twi|—|100|ms|4|
|RX_LOS Deassert Time|t_los_off_twi|—|100|ms|5|
|AnalogParameter Data Ready|t_data|—|1000|ms|6|
|Two-Wire Interface Ready|t_serial|—|300|ms|7|
|Write Cycle Time Parameter|t_write|—|80|ms|8|
|Two-Wire Interface Clock Rate|f_serial_clock|—|400|kHz|9|
|Time Bus Free before New Transmission Can Start|t_BUF|20|—|μs|10|



## **NOTE:** 

1. Time from two-wire interface assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output falls below 10% of nominal. Measured from falling clock edge after stop bit of write transaction. 

2. Time from two-wire interface deassertion of TX_DISABLE (A2h, byte 110, bit 6) to when the modulated optical output rises above 90% of nominal. 

3. Time from fault to two-wire interface TX_FAULT (A2h, byte 110, bit 2) asserted. 

4. Time for two-wire interface assertion of Rx_LOS (A2h, byte 110, bit 1) from loss of optical signal. 

5. Time for two-wire interface deassertion of Rx_LOS (A2h, byte 110, bit 1) from presence of valid optical signal. 

6. From power on to data ready bit asserted (A2h, byte 110, bit 0). Data ready indicates analog monitoring circuitry is functional. 

7. Time from power on until module is ready for data transmission over the two-wire interface (reads or writes over A0h and A2h). 

8. Time from stop bit to completion of a 1-8 byte write command. For a one to four byte write the maximum cycle time is 40 ms and for a five to eight byte write the maximum cycle time is 80 ms. 

9. Module may clock stretch for f_serial_clock greater than 100 kHz. 

10. Between STOP and START. See SFF 8431 Section 4.3. 

AV02-3399EN 14 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Table 12:  Transceiver Digital Diagnostic Monitor (Real Time Sense) Characteristics** 

The following characteristics are defined over the Recommended Operating Conditions unless otherwise noted. Typical values are for Tc = 40°C, VccT and VccR = 3.3V. 

|**Parameter**|**Symbol**|**Minimum**|**Units**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal Temperature Accuracy|TINT|±3.0|°C|Temperature is measured internal to the<br>transceiver. Valid from –10°C to 85°C case<br>temperature.|
|Transceiver Internal Supply Voltage Accuracy|VINT|±0.1|V|Supply voltage is measured internal to the<br>transceiver and can, with less accuracy, be<br>correlated to voltage at the VccT contact.<br>Valid over 3.3V ±10%.|
|Transmitter Laser DC Bias Current Accuracy|IINT|±10|%|IINTaccuracy is better than ±10% of the<br>nominal value.|
|Transmitted Average Optical Output Power<br>Accuracy|PT|±3.0|dB|Average Power coupled into 50/125 μm<br>multi-mode fiber. Valid from 100 μW to<br>500μW.|
|Received Average Optical Input Power<br>Accuracy|PR|±3.0|dB|Average Power coupled into 50/125 μm<br>multi-mode fiber. Valid from 77 μW to<br>500μW.|



AV02-3399EN 15 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Figure 6:  Transceiver Timing Diagrams (Module Installed and Power Applied except where Noted)** 


**----- Start of picture text -----**<br>
VCCT, VCCR > 2.97 V VCCT, VCCR > 2.97 V<br>TX_FAULT TX_FAULT<br>TX_DISABLE TX_DISABLE<br>TRANSMITTED SIGNAL TRANSMITTED SIGNAL<br>t_init t_init<br>t-init: TX DISABLE NEGATED t-init: TX DISABLE ASSERTED<br>VCCT, VCCR > 2.97 V TX_FAULT<br>TX_FAULT TX_DISABLE<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>TRANSMITTED SIGNAL<br>t_off t_on<br>t_init<br>INSERTION<br>t-init: TX DISABLE NEGATED, MODULE HOT PLUGGED  t-off and t-on: TX DISABLE ASSERTED THEN NEGATED<br>OCCURANCE OF FAULT<br>OCCURANCE OF FAULT<br>TX_FAULT<br>TX_FAULT<br>TX_DISABLE<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>TRANSMITTED SIGNAL<br>t_fault * SFP SHALL CLEAR TX_FAULT IN t_reset t_init*<br>                                                                              < t_init IF THE FAILURE IS TRANSIENT<br>t-fault: TX FAULT ASSERTED, TX SIGNAL NOT RECOVERED t-reset: TX DISABLE ASSERTED THEN NEGATED, TX SIGNAL RECOVERED<br>OCCURANCE OF FAULT<br>TX_FAULT OCCURANCE<br>OPTICAL SIGNAL OF LOSS<br>TX_DISABLE<br>TRANSMITTED SIGNAL LOS<br>t_fault<br>t_reset t_loss_on t_loss_off<br>* SFP SHALL CLEAR TX_FAULT IN t_init*<br>   <  t_init IF THE FAILURE IS TRANSIENT<br>t-fault: TX DISABLE ASSERTED THEN NEGATED, TX SIGNAL NOT RECOVERED t-los-on and t-los-off<br>**----- End of picture text -----**<br>


AV02-3399EN 16 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

**Table 13:  EEPROM Serial ID Memory Contents - Conventional SFP Memory (Address A0h)** 

|**Byte #**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Byte#**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|
|---|---|---|---|---|---|
|0|03|SFP physical device|37|00|Hex Byte of Vendor OUI[1]|
|1|04|SFP function defined by serial ID only|38|17|Hex Byte of Vendor OUI[1]|
|2|07|LC optical connector|39|6A|Hex Byte of Vendor OUI[1]|
|3|10|10G Base-SR|40|41|“A” - Vendor Part Number ASCII character|
|4|00||41|46|“F” - Vendor Part Number ASCII character|
|5|00||42|42|“B” - Vendor Part Number ASCII character|
|6|00||43|52|“R” - Vendor Part Number ASCII character|
|7|00||44|2D|“-” - Vendor Part Number ASCII character|
|8|00||45|37|“7” - Vendor Part Number ASCII character|
|9|00||46|31|“1” - Vendor Part Number ASCII character|
|10|00||47|30|“0” - Vendor Part Number ASCII character|
|11|06|64B/66B|48|53|“S” - Vendor Part Number ASCII character|
|12|67|10312.5 Mbit/sec nominal bit rate<br>(10.3125 Gbit/s)|49|4D|“M” - Vendor Part Number ASCII character|
|13|00|Unspecified|50|5A|“Z” - Vendor Part Number ASCII character|
|14|00||51|20|“  ” - Vendor Part Number ASCII character|
|15|00||52|20|“  ” - Vendor Part Number ASCII character|
|16|08|82 m of OM2 50/125µm fiber|53|20|“  ” - Vendor Part Number ASCII character|
|17|03|33 m of OM1 62.5/125µm fiber|54|20|“  ” - Vendor Part Number ASCII character|
|18|00||55|20|“  ” - Vendor Part Number ASCII character|
|19|1E|300 m of OM3 50/125 µm fiber|56|20|“  ” - Vendor Revision Number ASCII<br>character|
|20|41|“A” - Vendor Name ASCII character|57|20|“  ” - Vendor Revision Number ASCII<br>character|
|21|56|“V” - Vendor Name ASCII character|58|20|“  ” - Vendor Revision Number ASCII<br>character|
|22|41|“A” - Vendor Name ASCII character|59|20|“  ” - Vendor Revision Number ASCII<br>character|
|23|47|“G” - Vendor Name ASCII character|60|03|Hex Byte of Laser Wavelength[2]|
|24|4F|“O” - Vendor Name ASCII character|61|52|Hex Byte of Laser Wavelength[2]|
|25|20|“  ” - Vendor Name ASCII character|62|00||
|26|20|“  ” - Vendor Name ASCII character|63||Checksum for Bytes 0-62[3]|
|27|20|“  ” - Vendor Name ASCII character|64|00|Receiver limitingoutput. 1 Wattpower class.|
|28|20|“  ” - Vendor Name ASCII character|65|1A|Hardware SFP TX_DISABLE, TX_FAULT,<br>and RX_LOSS|
|29|20|“  ” - Vendor Name ASCII character|66|00||
|30|20|“  ” - Vendor Name ASCII character|67|00||
|31|20|“  ” - Vendor Name ASCII character|68-83||Vendor Serial Number ASCII characters[4]|
|32|20|“  ” - Vendor Name ASCII character|84-91||Vendor Date Code ASCII characters[5]|
|33|20|“  ” - Vendor Name ASCII character|92|68|Digital Diagnostics, Internal Cal, Rx Pwr Avg|



AV02-3399EN 

Broadcom 

17 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

**Table 13:  EEPROM Serial ID Memory Contents - Conventional SFP Memory (Address A0h) (Continued)** 

|**Byte #**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|**Byte#**<br>**Decimal**|**Data**<br>**Hex**|**Notes**|
|---|---|---|---|---|---|
|34|20|“  ” - Vendor Name ASCII character|93|F0|A/W, Soft SFP TX_DISABLE, TX_FAULT,<br>and RX_LOS, RATE_SELECT|
|35|20|“  ” - Vendor Name ASCII character|94|03|SFF-8472 Compliance to revision 10.0|
|36|00||95||Checksum for Bytes 64-94[3]|
||||96 - 255|00||



## **NOTE:** 

1. The IEEE Organizationally Unique Identifier (OUI) assigned to Avago Technologies is 00-17-6A (3 bytes of hex). 

2. Laser wavelength is represented in 16 unsigned bits. The hex representation of 850 (nm) is 0352. 

3. Addresses 63 and 95 are checksums calculated (per SFF-8472) and stored prior to product shipment. 

4. Addresses 68-83 specify the AFBR-710SMZ ASCII serial number and will vary on a per unit basis. 

5. Addresses 84-91 specify the AFBR-710SMZ ASCII date code and will vary on a per date code basis. 

**Table 14:  EEPROM Serial ID Memory Contents - Enhanced Feature Set Memory (Address A2h)** 

|**Byte #**<br>**Decimal**|**Notes**|**Byte#**<br>**Decimal**|**Notes**|**Byte#**<br>**Decimal**|**Notes**|
|---|---|---|---|---|---|
|0|TempH Alarm MSB[1]|26|Tx Pwr L Alarm MSB[4]|104|Real Time Rx Pwr MSB[5]|
|1|TempH Alarm LSB[1]|27|Tx Pwr L Alarm LSB[4]|105|Real Time Rx Pwr LSB[5]|
|2|TempL Alarm MSB[1]|28|Tx Pwr H WarningMSB[4]|106|Reserved|
|3|TempL Alarm LSB[1]|29|Tx Pwr H WarningLSB[4]|107|Reserved|
|4|TempH WarningMSB[1]|30|Tx Pwr L WarningMSB[4]|108|Reserved|
|5|TempH WarningLSB[1]|31|Tx Pwr L WarningLSB[4]|109|Reserved|
|6|TempL WarningMSB[1]|32|Rx Pwr H Alarm MSB[5]|110|Status/Control - SeeTable 15|
|7|TempL WarningLSB[1]|33|Rx Pwr H Alarm LSB[5]|111|Reserved|
|8|Vcc H Alarm MSB[2]|34|Rx Pwr L Alarm MSB[5]|112|Flag Bits - SeeTable 16|
|9|Vcc H Alarm LSB[2]|35|Rx Pwr L Alarm LSB[5]|113|Flag Bits - SeeTable 16|
|10|Vcc L Alarm MSB[2]|36|Rx Pwr H WarningMSB[5]|114|Reserved|
|11|Vcc L Alarm LSB[2]|37|Rx Pwr H WarningLSB[5]|115|Reserved|
|12|Vcc H WarningMSB[2]|38|Rx Pwr L WarningMSB[5]|116|Flag Bits - SeeTable 16|
|13|Vcc H WarningLSB[2]|39|Rx Pwr L WarningLSB[5]|117|Flag Bits - SeeTable 16|
|14|Vcc L WarningMSB[2]|40-55|Reserved|118-127|Reserved|
|15|Vcc L Warning LSB[2]|56-94|External Calibration<br>Constants[6]|128-247|Customer Writeable|
|16|Tx Bias H Alarm MSB[3]|95|Checksum for Bytes 0-94[7]|248-255|Vendor Specific|
|17|Tx Bias H Alarm LSB[3]|96|Real Time Temperature MSB[1]|||
|18|Tx Bias L Alarm MSB[3]|97|Real Time Temperature LSB[1]|||
|19|Tx Bias L Alarm LSB[3]|98|Real Time Vcc MSB[2]|||



AV02-3399EN 

Broadcom 

18 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

**Table 14:  EEPROM Serial ID Memory Contents - Enhanced Feature Set Memory (Address A2h) (Continued)** 

|**Byte #**<br>**Decimal**|**Notes**|**Byte#**<br>**Decimal**|**Notes**|**Byte#**<br>**Decimal**|**Notes**|
|---|---|---|---|---|---|
|20|Tx Bias H WarningMSB[3]|99|Real Time Vcc LS[2]|||
|21|Tx Bias H WarningLSB[3]|100|Real Time Tx Bias MSB[3]|||
|22|Tx Bias L WarningMSB[3]|101|Real Time Tx Bias LSB[3]|||
|23|Tx Bias L WarningLSB[3]|102|Real Time Tx Power MSB[4]|||
|24|Tx Pwr H Alarm MSB[4]|103|Real Time Tx Power LSB[4]|||
|25|Tx Pwr H Alarm LSB[4]|||||



## **NOTE:** 

1. Temperature (Temp) is decoded as a 16-bit signed two’s-complement integer in increments of 1/256°C. 

2. Supply Voltage (Vcc) is decoded as a 16-bit unsigned integer in increments of 100 μV. 

3. Laser bias current (Tx Bias) is decoded as a 16-bit unsigned integer in increments of 2 μA. 

4. Transmitted average optical power (Tx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 μW. 

5. Received average optical power (Rx Pwr) is decoded as a 16-bit unsigned integer in increments of 0.1 μW. 

6. Bytes 56-94 are not intended for use with AFBR-710SMZ, but have been set to default values per SFF-8472. 

7. Byte 95 is a checksum calculated (per SFF-8472) and stored prior to product shipment 

. 

**Table 15:   EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110)** 

|**Bit #**|**Status/**<br>**Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7|TX_DISABLE State|Digital state of SFP TX_DISABLE Input(1 = TX_DISABLE asserted)|1|
|6|Soft TX_DISABLE|Read/write bit for changingdigital state of TX_DISABLE function|1,2|
|5|Reserved|||
|4|Reserved|||
|3|Reserved|||
|2|TX_FAULT State|Digital state of the SFP TX_FAULT Output(1 = TX_FAULT asserted)|1|
|1|RX_LOS State|Digital state of the SFP RX_LOS Output(1 = RX_LOS asserted)|1|
|0|Data Ready (Bar)|Indicates transceiver is powered and real time sense data is ready.<br>(0 = Ready)||



## **NOTE:** 

1. The response time for soft commands of the AFBR-709HDZ is 100 ms as specified by SFF-8472. 

2. Bit 6 is logic OR’d with the SFP TX_DISABLE input on contact 3; either asserted will disable the SFP+ transmitter. 

AV02-3399EN 19 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

**Table 16:  EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)** 

|**Byte**|**Bit**|**Flag Bit Name**|**Description**|
|---|---|---|---|
|112|7|TempHigh Alarm|Set when transceiver internal temperature exceeds high alarm threshold|
||6|TempLow Alarm|Set when transceiver internal temperature exceeds low alarm threshold|
||5|Vcc High Alarm|Set when transceiver internal supplyvoltage exceeds high alarm threshold|
||4|Vcc Low Alarm|Set when transceiver internal supplyvoltage exceeds low alarm threshold|
||3|Tx Bias High Alarm|Set when transceiver laser bias current exceeds high alarm threshold|
||2|Tx Bias Low Alarm|Set when transceiver laser bias current exceeds low alarm threshold|
||1|Tx Power High Alarm|Set when transmitted average opticalpower exceeds high alarm threshold|
||0|Tx Power Low Alarm|Set when transmitted average opticalpower exceeds low alarm threshold|
|113|7|Rx Power High Alarm|Set when received average opticalpower exceeds high alarm threshold|
||6|Rx Power Low Alarm|Set when received average opticalpower exceeds low alarm threshold|
||0-5|Reserved||
|116|7|TempHigh Warning|Set when transceiver internal temperature exceeds high warningthreshold|
||6|TempLow Warning|Set when transceiver internal temperature exceeds low warningthreshold|
||5|Vcc High Warning|Set when transceiver internal supplyvoltage exceeds high warningthreshold|
||4|Vcc Low Warning|Set when transceiver internal supplyvoltage exceeds low warningthreshold|
||3|Tx Bias High Warning|Set when transceiver laser bias current exceeds high warningthreshold|
||2|Tx Bias Low Warning|Set when transceiver laser bias current exceeds low warningthreshold|
||1|Tx Power High Warning|Set when transmitted average opticalpower exceeds high warningthreshold|
||0|Tx Power Low Warning|Set when transmitted average opticalpower exceeds low warningthreshold|
|117|7|Rx Power High Warning|Set when received average opticalpower exceeds high warningthreshold|
||6|Rx Power Low Warning|Set when received average opticalpower exceeds low warningthreshold|
||0-5|Reserved||



AV02-3399EN 20 

Broadcom 

**AFBR-710SMZ** Data Sheet 

10 Gb Ethernet, 850 nm, 10GBASE-SR/SW, SFP+ Transceiver 

## **Figure 7:  Module Drawing** 


**----- Start of picture text -----**<br>
TOP LABEL RECESS<br>TCASE REFERENCE POINT 8.9 47.5<br>12.2<br>13.9 13.4 [±0.1]<br>30.8<br>13.6<br>0.64 UNCOMPRESSED<br>13<br>8.55 [±0.1]<br>6.25<br>0.69 UNCOMPRESSED<br>BOTTOM LABEL RECESS<br>25.2<br>12<br>TX RX<br>15.14 UNCOMPRESSED<br>**----- End of picture text -----**<br>


**Figure 8:  Module Label** 


AV02-3399EN 21 

Broadcom 

Copyright © 2005–2023 Broadcom. All Rights Reserved. The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos referenced herein belong to their respective companies. 

Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others. 

