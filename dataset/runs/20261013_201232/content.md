## **AFBR-57F5MZ** 

16GFC SFP+ Digital Diagnostic SFP, 850 nm, 16G/8G/4G Low Voltage (3.3 V) Fibre Channel Optical Transceiver 


## **Data Sheet** 

## **Description** 

## **Features** 

- Compliant to RoHS directives 

Avago Technologies’ AFBR-57F5MZ optical transceiver supports high speed serial links over multi-mode optical fiber at signalling rates up to 14.025 Gb/s (the serial line rate of 16GFC). The product is compliant with Small Form Pluggable industry agreements SFP and SFP+ for mechanical and low speed electrical specifications. High speed electrical and optical specifications are compliant with ANSI Fibre Channel FC-PI-5. 

- 850 nm Vertical Cavity Surface Emitting Laser (VCSEL) 

- Class 1 eye safe per IEC60825-1 and CDRH 

- Wide temperature range (0 °C to 70 °C) 

- LC duplex connector optical interface conforming to ANSI TIA/EIA604-10 (FOCIS 10A) 

- Diagnostic features per SFF-8472 “Diagnostic Monitoring Interface for Optical Transceivers” 

The AFBR-57F5MZ is a multi-rate 850nm transceiver which ensures compliance with FC-PI-5 16GFC, 8GFC and 4GFC specifications. Per the requirements of 16GFC, internal clock and data recovery circuits (CDRs) are present on both electrical input and electrical output of this transceiver. These CDRs will lock at 14.025 Gb/s (16GFC) but must be bypassed for operation at 8.5 Gb/s (8GFC) and 4.25 Gb/s (4GFC), accomplished by using two Rate Select inputs to configure transmit and receive sides. Transmitter and receiver can operate at different data rates, as is often seen during Fibre Channel speed negotiation. 

- Enhanced operational features including EWRAP, OWRAP and variable electrical EQ/emphasis settings 

- Real time monitoring of: 

   - Transmitter average optical power 

   - Received average optical power 

   - Laser bias current 

   - Temperature 

   - Supply Voltage 

- SFP+ mechanical specifications per SFF-8432 

- SFP+ compliant low speed interface 

Digital diagnostic monitoring information (DMI) is present in the AFBR-57F5MZ per the requirements of SFF-8472, providing real time monitoring information of transceiver laser, receiver and environment conditions over a SFF8431 2-wire serial interface. 

- Fibre Channel FC-PI-5 compliant high speed interface 

   - 1600-SN-M6-S, 800-SN-M6-S, 400-SN-M6-I 

   - 1600-SN-M5-S, 800-SN-M5-S, 400-SN-M5-I 

   - 1600-SN-M5E-I, 800-SN-M5E-I, 400-SN-M5E-I 

   - 1600-SN-M5F-I, 800-SN-M5F-I, 400-SN-M5F-I 

## **Related Products** 

   - Fibre Channel FC-PI-5 compliant optical link distances 

- AFBR-57D7APZ: 850 nm SFP for 8G/4G/2G Fibre Channel 

- AFCT-57D5ATPZ: 1310 nm SFP for 8G/4G/2G Fibre Channel 

- AFCT-57D5ANPZ: 1310 nm SFP for 8G/4G/2G Fibre Channel 

- AFBR-57R5APZ: 850 nm SFP for 4G/2G/1G Fibre Channel 

- AFCT-57R5APZ: 1310 nm SFP for 4G/2G/1G Fibre Channel 

- AFCT-57R5ATPZ: 1310 nm SFP for 4G/2G/1G Fibre Channel 

- AFCT-57R5ANPZ: 1310 nm SFP for 4G/2G/1G Fibre Channel 

## **Applications** 

- Fibre Channel switches (director, stand alone, blade) 

- Fibre Channel Host Bus Adapters 

- Fibre Channel RAID controllers 

- Fibre Channel tape drive 

- Port side connections 

- Inter-switch or inter-chassis aggregated links 

Patent - www.avagotech.com/patents 

## **Installation** 

The AFBR-57F5MZ can be installed in any SFF-8074i compliant Small Form Pluggable (SFP) port regardless of host equipment operating status. The AFBR-57F5MZ is hotpluggable, allowing the module to be installed while the host system is operating and on-line. Upon insertion, the transceiver housing makes initial contact with the host board SFP cage, mitigating potential damage due to Electro-Static Discharge (ESD). 

## **Digital Diagnostic Interface and Serial Identification** 

The 2-wire serial interface is based on ATMEL AT24C01A series EEPROM protocol and signaling detail. Conventional EEPROM memory, bytes 0-255 at memory address 0xA0, is organized in compliance with SFF-8074i. New digital diag nostic information, bytes 0-255 at memory address 0xA2, is compliant to SFF-8472. The new diagnostic information provides the opportunity for Predictive Failure Identification, Com pliance Prediction, Fault Isolation and Component Monitoring. 

## **Predictive Failure Identification** 

The AFBR-57F5MZ predictive failure feature allows a host to identify potential link problems before system performance is impacted. Prior identification of link problems enables a host to service an application via “fail over” to a redundant link or replace a suspect device, maintaining system uptime in the process. For applications where ultra-high system uptime is required, a digital SFP provides a means to monitor two real-time laser metrics asso ciated with observing laser degradation and predicting failure: average laser bias current (Tx_Bias) and average laser optical power (Tx_Power). 

## **Compliance Prediction** 

Compliance prediction is the ability to determine if an optical transceiver is operating within its operating and environmental requirements. AFBR-57F5MZ devices provide real-time access to transceiver internal supply voltage and temperature, allowing a host to identify potential component compliance issues. Received optical power is also available to assess compliance of a cable plant and remote transmitter. When operating out of requirements, the link cannot guarantee error free transmission. 

## **Fault Isolation** 

The fault isolation feature allows a host to quickly pinpoint the location of a link failure, minimizing downtime. For optical links, the ability to identify a fault at a local device, remote device or cable plant is crucial to speeding service of an installation. AFBR-57F5MZ real-time monitors of Tx_Bias, Tx_Power, Vcc, Temperature and Rx_Power can be used to assess local transceiver current operating conditions. In addition, status flags Tx_Disable and Rx Loss of Signal (LOS) are mirrored in memory and available via the two-wire serial interface. 

## **Component Monitoring** 

Component evaluation is a more casual use of the AFBR57F5MZ real-time monitors of Tx_Bias, Tx_Power, Vcc, Temperature and Rx_Power. Potential uses are as debugging aids for system installation and design, and transceiver parametric evaluation for factory or field qualification. For example, temperature per module can be observed in high density applications to facilitate thermal evaluation of blades, PCI cards and systems. 

2 


**----- Start of picture text -----**<br>
OPTICAL INTERFACE RECEIVER ELECTRICAL INTERFACE<br>RD+ (RECEIVE DATA)<br>RD- (RECEIVE DATA)<br>AMPLIFICATION Rx Rx Vout &<br>LIGHT FROM FIBER PHOTO-DETECTOR & QUANTIZATION CDR Emphasis Rx LOSS OF SIGNAL<br>Rx RATE SELECT RS(0)<br>MOD-DEF2 (SDA)<br>µ Controller<br>MOD-DEF1 (SCL)<br>MOD-DEF0<br>TRANSMITTER<br>TX_DISABLE<br>LASER TD+ (TRANSMIT DATA)<br>LIGHT TO FIBER VCSEL DRIVER &SAFETY CDRTx EqualizationTx TD- (TRANSMIT DATA)<br>CIRCUITRY TX_FAULT<br>Tx RATE SELECT RS(1)<br>**----- End of picture text -----**<br>


**Figure 1. Transceiver functional diagram.** 

## **Transmitter Section** 

The transmitter section includes a Transmitter Optical SubAssembly (TOSA), laser driver circuit, Clock and Data Recovery circuit (CDR) and an electrical input stage with variable equalization controls and electrical eye measurement capability. The TOSA contains a 850 nm Vertical Cavity Surface Emitting Laser (VCSEL) light source with integral light monitoring function and imaging optics to assure efficient  optical coupling to the LC connector interface. The TOSA is driven by a laser driver IC, which uses the differential output from an integral Tx CDR stage to modulate and regulate VCSEL optical power. As mandated by FC-PI-5, the integral CDR cleans up any incoming jitter accumulated from the host ASIC, PCB traces and SFP electrical connector. Between the SFP electrical connector and Tx CDR is a variable, I[2] C-bus controlled, equalization circuit to optimize SFP performance with non-ideal incoming electrical waveforms. Note the Tx CDR is engaged only with Tx_RATE=high (16GFC) and bypassed with Tx_ RATE=low (8G/4G). 

## **Transmit Disable (Tx_Disable)** 

The AFBR-57F5MZ accepts a TTL and CMOS compatible transmit disable control signal input (pin 3) which shuts down the transmitter optical output. A high signal implements this function while a low signal allows normal transceiver operation. In the event of a fault (e.g. eye safety circuit activated), cycling this control signal resets the module as depicted in Figure 4. An internal pull up resistor disables the transceiver transmitter until the host pulls the input low. Host systems should allow a 10 ms interval be- 

tween successive assertions of this control signal. Tx_Disable can also be asserted via the two-wire serial interface (address A2h, byte 110, bit 6) and monitored (address A2h, byte 110, bit 7). 

The contents of A2h, byte 110, bit 6 are logic OR’d with hardware Tx_Disable (pin 3) to control transmitter operation. 

## **Transmit Fault (Tx_Fault)** 

A catastrophic laser fault will activate the transmitter signal, TX_FAULT, and disable the laser. This signal is an open collector output (pull-up required on the host board). A low signal indicates normal laser operation and a high signal indicates a fault. The TX_FAULT will be latched high when a laser fault occurs and is cleared by toggling the TX_DISABLE input or power cycling the transceiver. The transmitter fault condition can also be monitored via the two-wire serial interface (address A2, byte 110, bit 2). 

## **Eye Safety Circuit** 

The AFBR-57F5MZ provides Class 1 (single fault tolerant) eye safety by design and has been tested for compliance with the requirements listed in Table 1. The eye safety circuit continuously monitors the optical output power level and will disable the transmitter upon detecting an unsafe condition beyond the scope of Class 1 certification. Such unsafe conditions can be due to inputs from the host board (Vcc fluctuation, unbalanced code) or a fault within the transceiver. 

3 

## **Receiver Section** 

The receiver section includes a Receiver Optical SubAssembly (ROSA), pre-amplification and post-amplification circuit, Clock and Data Recovery Circuit and an electrical output stage with variable emphasis controls. The ROSA, containing a high speed PIN detector, pre-amplifier and imaging optics efficiently couple light from the LC connector interface and perform an optical to electrical conversion. The resulting differential electrical signal passes through a post amplification circuit and into a Clock and Data Recovery circuit (CDR) for cleaning up accumulated jitter. The resulting signal is passed to a high speed output line driver stage with variable, I[2] C-bus controlled, emphasis settings allowing the host to optimize signal characteristics between the SFP and host ASIC. Note the Rx CDR is engaged only with Rx_RATE=high (16GFC) and bypassed with Rx_RATE=low (8G/4G). 

## **Receiver Loss of Signal (Rx_LOS)** 

The post-amplification IC also includes transition detection circuitry which monitors the ac level of incoming optical signals and provides a TTL/CMOS compatible status signal to the host (pin 8). An adequate optical input results in a low Rx_LOS output while a high Rx_LOS output indicates an unusable optical input. The Rx_LOS thresholds are factory set so that a high output indicates a definite optical fault has occurred. Rx_LOS can also be monitored via the two-wire serial interface (address A2h, byte 110, bit 1). 

## **Functional Data I/O** 

The AFBR-57F5MZ interfaces with the host circuit board through twenty I/O pins (SFP electrical connector) identified by function in Table 2. The board layout for this interface is depicted in Figure 6. 

The AFBR-57F5MZ high speed transmit and receive interfaces require SFP MSA compliant signal lines on the host board. To simplify board requirements, biasing resistors and ac coupling capacitors are incorporated into the SFP transceiver module (per SFF-8074i) and hence are not required on the host board. The Tx_Disable, Tx_Fault, and Rx_LOS lines require TTL lines on the host board (per SFF8074i) if used. If an application chooses not to take advantage of the functionality of these pins, care must be taken to ground Tx_Disable (for normal operation). 

## **Application Support** 

An Evaluation Kit and Reference Designs are available to assist in evaluation of the AFBR-57F5MZ. Please contact your local Field Sales representative for availability and ordering details. 

## **Caution** 

There are no user serviceable parts nor maintenance requirements for the AFBR-57F5MZ. All mechanical adjustments are made at the factory prior to shipment. Tampering with, modifying, misusing or improperly handling the AFBR-57F5MZ will void the product warranty. It may also result in improper operation and possibly overstress the laser source. Performance degrada tion or device failure may result. Connection of the AFBR-57F5MZ to a light source not compliant with ANSI FC-PI specifications, operating above maximum operating conditions or in a manner inconsistent with it’s design and function may result in exposure to hazardous light radiation and may constitute an act of modifying or manufacturing a laser product. Persons performing such an act are required by law to re-certify and re-identify the laser product under the provisions of U.S. 21 CFR (Subchapter J) and TUV. 

## **Ordering Information** 

Please contact your local field sales engineer or one of Avago Technologies franchised distributors for ordering information.  For technical information, please visit Avago Technologies’ WEB page at **www.avagotech.com** or contact Avago Technologies Semiconductor Products Customer Response Center at 1-800-235-0312.  For information related to SFF Committee documentation visit **www.sffcommittee.org** . 

## **Regulatory Compliance** 

The AFBR-57F5MZ complies with all applicable laws and regulations as detailed in Table 1. Certification level is dependent on the overall configuration of the host equipment. The transceiver performance is offered as a figure of merit to assist the designer. 

Figure 2 depicts the recom mended interface circuit to link the AFBR-57F5MZ to supporting physical layer ICs. Timing for MSA compliant control signals implemented in the transceiver are listed in Figure 4. 

4 

## **Electrostatic Discharge (ESD)** 

The AFBR-57F5MZ is compatible with ESD levels found in typical manufacturing and operating environments as described in Table 1. In the normal handling and operation of optical transceivers, ESD is of concern in two circumstances. 

The first case is during handling of the transceiver prior to insertion into an SFP compliant cage. To protect the device, it’s important to use normal ESD handling pre-cautions. These include use of grounded wrist straps, workbenches and floor wherever a transceiver is handled. 

The second case to consider is static discharges to the exterior of the host equipment chassis after installation. If the optical interface is exposed to the exterior of host equipment cabinet, the transceiver may be subject to system level ESD requirements. 

## **Electromagnetic Interference (EMI)** 

Equipment incorporating gigabit transceivers is typically subject to regulation by the FCC in the United States, CENELEC EN55022 (CISPR 22) in Europe and VCCI in Japan. The AFBR-57F5MZ’s compliance to these standards is detailed in Table 1. The metal housing and shielded design of the AFBR-57F5MZ minimizes the EMI challenge facing the equipment designer. 

## **EMI Immunity (Susceptibility)** 

Due to its shielded design, the EMI immunity of the AFBR57F5MZ exceeds typical industry standards. 

## **Flammability** 

The AFBR-57F5MZ optical transceiver is made of metal and high strength, heat resistant, chemical resistant and UL 94V-0 flame retardant plastic. 

**Table 1. Regulatory Compliance** 

|**Feature**||**Test Method**|**Performance**|
|---|---|---|---|
|Electrostatic Discharge (ESD)||MIL-STD-883C|Class 1  (> 2000 Volts)|
|to the Electrical Pins||Method 3015.4||
|Electrostatic Discharge (ESD)||Variation of IEC 61000-4-2|Typically, no damage occurs with 25 kV when|
|to the Duplex LC Receptacle|||the duplex LC connector receptacle is|
||||contacted bya Human BodyModelprobe.|
|||GR1089|10 contacts of 8 kV on the electrical faceplate|
||||with device inserted into apanel.|
|Electrostatic Discharge (ESD)||Variation of IEC 801-2|Air discharge of 15 kV (min.) contact to|
|to the Optical Connector|||connector without damage.|
|Electromagnetic Interference||FCC Class B|System margins are dependent on customer|
|(EMI)||CENELEC EN55022 Class B|board and chassis design.|
|||(CISPR 22A)||
|||VCCI Class 1||
|Immunity||Variation of IEC 61000-4-3|Typically shows no measurable efect from a<br>10 V/m feld swept from 10 MHz to 1 GHz.|
|Laser Eye Safety and<br>Equipment Type Testing||US FDA CDRH AEL Class 1<br>US21 CFR, Subchapter J per|CDRH certifcation 9720151-111<br>TUV fle 72102056|
|||Paragraphs 1002.10||
||**BAUART**<br>**GEPRUFT**<br>**¬**|and 1002.12||
|**TUV**<br>**Rheinland**<br>**Product Safety**<br>**¬**|**TYPE**<br>**APPROVED**|(IEC) EN60825-1: 1994 + A11 + A2<br>(IEC) EN60825-2: 1994 + A1<br>(IEC) EN60950: 1992 + A1 + A2 +||
|||A3 + A4 + A11||
|Component Recognition||Underwriters Laboratories and|UL fle 8543036783|
|||Canadian Standards Association||
|||Joint Component Recognition||
|||for Information Technology||
|||Equipment including Electrical||
|||Business Equipment||
|RoHS Compliance|||Less than 1000 ppm of cadmium, lead, mercury,|
||||hexavalent chromium, polybrominated biphenyls,|
||||andpolybrominated biphenyl ethers.|



5 

## **Special Operation Functions:** 


**----- Start of picture text -----**<br>
Pre Post Rx Rx Vout &  Pre Post Rx Rx Vout &<br>Amp Amp CDR Emphasis Amp Amp CDR Emphasis<br>µ controller µcontroller<br>Laser Tx Tx EQ Laser Tx Tx EQ<br>Driver CDR Driver CDR<br>Figure 2a. OWRAP Functionality (I [2] C-bus controlled) Figure 2b. EWRAP Functionality  (I [2] C-bus controlled)<br>SFP Connector<br>SFP Connector<br>**----- End of picture text -----**<br>


Electrical and optical high speed data “wrap” functions are enabled to assist with local host or remote diagnostic and optimization sequences. Optical data wrap (OWRAP) takes a received optical signal through a CDR jitter cleanup and retransmits it optically out. Electrical data wrap (EWRAP) takes an incoming electrical signal through a CDR jitter cleanup and retransmits it electrically out. An optional pass-through function is available to transmit outbound the wrapped information, controlled through I[2] C-bus commands. 


**----- Start of picture text -----**<br>
Pre Post Rx Rx Vout &  Pre Post Rx Rx Vout &<br>Amp Amp CDR Emphasis Amp Amp CDR Emphasis<br>µcontroller µcontroller<br>i2c setting i2c setting<br>Laser Tx Tx EQ Laser Tx Tx EQ<br>Driver CDR Driver CDR<br>Tx EQ Setting Rx Emphasis Setting<br>**----- End of picture text -----**<br>


**Figure 2c. SFP Tx Variable Input Electrical EQ (I[2] C-bus controlled)** 

**Figure 2d. SFP Rx Variable Output Electrical Emphasis (I[2] C-bus controlled)** 

The electrical SFP input stage (TD +/-) has been enhanced with features to allow host control and optimization of the transceiver’s input equalization settings. The host can then select, in situ, the most appropriate SFP setting for a given interconnect scenario. 

The SFP electrical output stage (RD+/-) has been enhanced with variable output emphasis features to allow host control and optimization of the receiver’s output settings. The host can then select, in situ, the most appropriate SFP setting for a given interconnect scenario. To assist with optimizing the receiver output setting, the user can have data transmitted by the SFP to a host ASIC by using EWRAP to loop back host generated traffic or can use a remotely generated optical signal as a data source for SFP and interconnect training. 

**Table 2. Rate Select Function** 

|**Function**|**State**<br>**Explanation**|
|---|---|
|Rx Rate Select<br>RS(0)|High<br>Receive Rate Select HIGH engages the internal Rx CDR. The CDR will look for valid 16GFC trafc and<br>lock within 500us when found. Due to diferences in coding, this CDR will not be able to lock on valid<br>8GFC or 4GFC trafc.<br>Low<br>Receive Rate Select LOW bypasses the internal Rx CDR. This is intended for use only with 8GFC and<br>4GFC trafc. When set low, the SFP behaves like a legacySFP.|
|Tx Rate Select<br>RS(1)|High<br>Transmit Rate Select HIGH engages the internal Tx CDR. The CDR will look for valid 16GFC trafc and<br>lock within 500us when found. Due to diferences in coding, this CDR will not be able to lock on valid<br>8GFC or 4GFC trafc.<br>Low<br>Transmit Rate Select LOW bypasses the internal Tx CDR. This is intended for use only with 8GFC and<br>4GFC trafc. When set low, the SFP behaves like a legacySFP.|



Note: During Fibre Channel Link Speed Negotiation sequences, the host will control Tx Rate and Rx Rate inputs separately to accomplish link initialization. Once speed negotiation is complete, it is expected both Tx Rate and Rx Rate will be placed in the same state by the host. 

6 


**----- Start of picture text -----**<br>
Tx Rate Select  VCC,T<br>RS (1)<br>40 k Ω 10 k Ω<br>Tx DIS<br>Tx_DISABLE<br>Tx FAULT<br>Tx_FAULT<br>0.1 µF<br>TD+<br>100  Ω<br>TD-<br>0.1 µF Tx CDR LASER DRIVER<br>4.7 k to 10 k Ω<br>4.7 µH VCC,T<br>0.1 µF 22 µF 0.1 µF<br>3.3 V<br>PROTOCOL IC SERDES IC 4.7 µH VCC,R VCC,R<br>VCC,R<br>0.1 µF 22 µF 0.1 µF 50  Ω<br>4.7 k to<br>10 k Ω 50  Ω<br>0.1 µF<br>RD+<br>100  Ω<br>RD-<br>0.1 µF<br>Rx LOS<br>LOSS OF SIGNAL<br>RS (0) Rx CDR POST AMPLIFIER<br>Rx Rate Select<br>3.3 V 40 k Ω<br>GND,R<br>4.7 k to 10 k Ω 4.7 k to 10 k Ω<br>4.7 k to 10 k Ω MOD_DEF0 MOD_DEF1 MOD_DEF2<br>MODULE DETECT<br>SCL<br>SDA<br>**----- End of picture text -----**<br>


**Figure 3. Typical application configuration** 


**----- Start of picture text -----**<br>
4.7 µH<br>VCC T<br>0.1 µF 22 µF 0.1 µF<br>3.3 V<br>4.7 µH<br>VCC R<br>0.1 µF 22 µF 0.1 µF<br>SFP MODULE HOST BOARD<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
NOTE: INDUCTORS MUST HAVE LESS THAN 1 Ω  SERIES RESISTANCE TO LIMIT VOLTAGE DROP TO THE SFP MODULE.<br>**----- End of picture text -----**<br>


**Figure 4. Recommended power supply filter** 

7 

## **Table 3. Pin Description** 

|**Pin**|**Name**|**Function/Description**|**Notes**|
|---|---|---|---|
|1|VeeT|Transmitter Ground||
|2|TX_FAULT|Transmitter Fault Indication – High indicates a fault condition|Note 1|
|3|TX_DISABLE|Transmitter Disable  –  Module electrical input disables on high or open|Note 2|
|4|MOD-DEF2|Module Defnition 2 – Two wire serial ID interface data line (SDA)|Note 3|
|5|MOD-DEF1|Module Defnition 1 – Two wire serial ID interface clock line (SCL)|Note 3|
|6|MOD-DEF0|Module Defnition 0 – Grounded in module (module present indicator)|Note 3|
|7|Rx Rate Select RS(0)|Receiver rate select. Logic High = 14.025 Gb/s, Logic Low = 8.5 Gb/s and 4.25 Gb/s|Note 8|
|8|RX_LOS|Loss of Signal – High indicates loss of received optical signal|Note 4|
|9|Tx Rate Select RS(1)|Transmitter rate select. Logic High = 14.025 Gb/s, Logic Low = 8.5 Gb/s and 4.25 Gb/s|Note 8|
|10|VeeR|Receiver Ground||
|11|VeeR|Receiver Ground||
|12|RD-|Inverse Received Data Out|Note 5|
|13|RD+|Received Data Out|Note 5|
|14|VeeR|Receiver Ground||
|15|VccR|Receiver Power  + 3.3 V|Note 6|
|16|VccT|Transmitter Power  +  3.3 V|Note 6|
|17|VeeT|Transmitter Ground||
|18|TD+|Transmitter Data In|Note 7|
|19|TD-|Inverse Transmitter Data In|Note 7|
|20|VeeT|Transmitter Ground||



## **Notes:** 

1. TX_FAULT is an open collector/drain output, which must be pulled up with a 4.7 k – 10 kΩ resistor on the host board. When high, this output indicates a laser fault of some kind. Low indicates normal operation. In the low state, the output will be pulled to < 0.8 V. 

2. TX_DISABLE is an input that is used to shut down the transmitter optical output. It is internally pulled up (within the transceiver) with a 6.8 kΩ resistor. 

Low (0 – 0.8 V): Transmitter on Between (0.8 V and 2.0 V): Undefined 

   - High (2.0 – Vcc max) or OPEN: Transmitter Disabled 

3. The signals Mod-Def 0, 1, 2 designate the two wire serial interface pins. They must be pulled up with a 4.7 k – 10 kΩ resistor on the host board. Mod-Def 0 is grounded by the module to indicate the module is present 

   - Mod-Def 1 is serial clock line (SCL) of two wire serial interface 

Mod-Def 2 is serial data line (SDA) of two wire serial interface 

4. RX_LOS (Rx Loss of Signal) is an open collector/drain output that must be pulled up with a 4.7 k – 10 kΩ resistor on the host board. When high, this output indicates the received optical power is below the worst case receiver sensitivity (as defined by the standard in use). Low indicates normal operation. In the low state, the output will be pulled to < 0.8 V. 

5. RD-/+ designate the differential receiver outputs. They are AC coupled 100 Ω differential lines which should be terminated with 100 Ω differential at the host SERDES input. AC coupling is done inside the transceiver and is not required on the host board. The voltage swing on these lines will be between 370 and 850 mV differential (185 – 425 mV single ended) when properly terminated. 

6. VccR and VccT are the receiver and transmitter power supplies. They are defined at the SFP connector pin. The maximum supply current is 300 mA and the associated in-rush current will typically be no more than 30 mA above steady state after 2 microseconds. 

7. TD-/+ designate the differential transmitter inputs. They are AC coupled differential lines with 100 Ω differential termination inside the module. The AC coupling is done inside the module and is not required on the host board. The inputs will accept differential swings of 180 – 1200 mV (90 – 600 mV single ended) 

8. Rate_Select is an input that is used to control transmit and receive high speed parametric optimizaton. It is internally pulled down (within the transceiver) with a 40kOhm resistor. 

Low (0 - 0.8V) or Open: Rate is set to 8.5Gb/s and below optimization. The CDR is bypassed. Between (0.8V and 2.0V) Undefined High (2.0 - Vcc max): Rate is set to 14.025Gb/s optimization. The CDR is engaged. 

8 

**Table 4. Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|-40|85|C|Note 1, 2|
|Case OperatingTemperature|TC|-40|85|C|Note 1, 2|
|Relative Humidity|RH|5|95|%|Note 1|
|SupplyVoltage|VccT, R|-0.5|3.8|V|Note 1, 2, 3|
|Low Speed Input Voltage|VIN|-0.5|Vcc+0.5|V|Note 1|



> **[Notes;]** 

1. Absolute Maximum Ratings are those values beyond which damage to the device may occur if these limits are exceeded for other than a short period of time. See Reliability Data Sheet for specific reliability performance. 

2. Between Absolute Maximum Ratings and the Recommended Operating Conditions functional performance is not intended, device reliability is not implied, and damage to the device may occur over an extended period of time. 

3. The module supply voltages, VCCT and VCCR must not differ by more than 0.5 V or damage to the device may occur. 

**Table 5. Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|Case OperatingTemperature|TC|0|70|°C|Note 1, 2|
|SupplyVoltage|VccT, R|3.135|3.465|V|Note 2|
|Data Rate||4.25|14.025|Gb/s|Note 2|



> **[Notes:]** 

1. The Ambient Operating Temperature limitations are based on the Case Operating Temperature limitations and are subject to the host system thermal design. 

2. Recommended Operating Conditions are those values for which functional performance and device reliability is implied. 

**Table 6. Transceiver Electrical Characteristics** 

(TC = 0 °C to 70 °C, VccT, VccR = 3.3V ± 5%) 

|**Table 6. Transceiver Electrical Characteristics**<br>(TC= 0 °C to 70 °C, VccT, VccR = 3.3 V ± 5%)||
|---|---|
|**Parameter**|**Symbol**<br>**Minimum**<br>**Typical**<br>**Maximum**<br>**Unit**<br>**Notes**|
|**AC Electrical Characteristics**||
|Power Supply Noise Rejection (peak-peak)|PSNR<br>100<br>mV<br>Note 1|
|**DC Electrical Characteristics**||
|Module SupplyCurrent|ICC<br>300<br>mA|
|Low Speed Outputs:<br>Transmit Fault (TX_FAULT), Loss of Signal<br>(RX_LOS), MOD-DEF 2|VOH<br>2.0<br>VccT,R+0.3<br>V<br>Note 2<br>VOL<br>0.8<br>V|
|Low Speed Inputs:<br>Transmit Disable (TX_DIS), MOD-DEF 1,<br>MOD-DEF2, RS(0), RS(1)|VIH<br>2.0<br>Vcc<br>V<br>Note 3<br>VIL<br>0<br>0.8<br>V|



## **Notes:** 

1. Filter per SFP specification is required on host board to remove 10 Hz to 2 MHz content. 

2. Pulled up externally with a 4.7 k – 10 kΩ resistor on the host board to 3.3 V. 

3. Mod-Def1 and Mod-Def2 must be pulled up externally with a 4.7 k – 10 kΩ resistor on the host board to 3.3 V. 

9 

## **Table 7. Transmitter and Receiver Electrical Characteristics** 

(TC = 0 °C to 70 °C, VccT, VccR = 3.3V ± 5%) 

|(TC= 0 °C to 70 °C, VccT, VccR = 3.3 V ± 5%)|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|High Speed Data Input|VI|180||1200|mV|Note 1|
|Transmitter Diferential Input Voltage (TD+/-)|||||||
|High Speed Data Output|Vo|370||850|mV|Note 2|
|Receiver Diferential Output Voltage (RD+/-)|||||||
|Receiver Total Jitter (14.025 Gb/s)|TJ|||0.36|UI|Note 3, Rx_Rate = high|
|Receiver Total Jitter (8.5 Gb/s)|TJ|||0.71|UI|Note 4, Rx_Rate = low|
|Receiver Contributed Total Jitter (4.25 Gb/s)|TJ|||0.26|UI|Note 4, Rx_Rate = low|
|Receiver Deterministic Jitter (14.025 Gb/s)|DJ|||0.22|UI|Note 3, Rx_Rate = high|
|Receiver Deterministic Jitter (8.5 Gb/s)|DJ|||0.42|UI|Note 4, Rx_Rate = low|
|Receiver Contributed Deterministic Jitter|DJ|||0.10|UI|Note 4, Rx_Rate = low|
|(4.25 Gb/s)|||||||
|Receiver Data Dependent Pulse Width Shrinkage|DDPWS|||0.14|UI|Note 3, Rx_Rate = high|
|(14.025 Gb/s)|||||||
|Receiver Data Dependent Pulse Width Shrinkage|DDPWS|||0.36|UI|Note 4, Rx_Rate = low|
|(8.5 Gb/s)|||||||



Notes: 

1. Internally ac coupled and terminated (100Ω differential). 

2. Internally ac coupled but requires an external load termination (100Ω differential). 

3. CDR is engaged with Rx_Rate = high. Received output jitter for 14.025 Gb/s. 

4. CDR is not engaged with Rx_Rate = low (ie. Bypassed). Receiver output jitter for 8.5 Gb/s and 4.25Gb/s. 

**Table 8. Transmitter Optical Characteristics** 

(TC = 0 °C to 70 °C, VccT, VccR = 3.3V ± 5%) 

|(TC= 0 °C to 70 °C, VccT, VccR = 3.3 V ± 5%)|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|Modulated Optical Output Power (OMA)|Tx,OMA|331|||µW||
|(Peak to Peak) 14.025Gb/s|||||||
|Modulated Optical Output Power (OMA)|Tx,OMA|302|||µW||
|(Peak to Peak) 8.5Gb/s|||||||
|Modulated Optical Output Power (OMA)|Tx,OMA|247|||µW||
|(Peak to Peak) 4.25Gb/s|||||||
|Average Optical Output Power|Pout|-7.8|||dBm|Note 1|
|Center Wavelength|lc|840||860|nm||
|Spectral Width – rms|qrms|||0.59|nm||
|Optical Rise Time (20%-80%)|tr, tf||30||ps||
|RIN12 (OMA)|RIN|||-128|dB/Hz||
|Vertical Eye Closure Penalty, 14.025Gb/s|VECP|||2.56|dB|Note 2|
|Transmitter Waveform Distortion Penalty, 8.5Gb/s|TWDP|||4.3|dB|Note 3|
|Transmitter Uncorrelated Jitter, 14.025Gb/s|UJ|||0.03|UI|Note 2|
|Transmitter Uncorrelated Jitter, 8.5Gb/s|UJ|||0.03|UI|Note 3|
|Transmitter Contributed Jitter, 4.25Gb/s|TJ|||0.25|UI|Note 3|
|Pout Tx_DISABLE Asserted|Pof|||-35|dBm||



Notes: 

1. Max Pout is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

2. CDR is engaged with Tx_Rate = high. Transmitter output jitter for 14.025 Gb/s. 

3. CDR is not engaged with Tx_Rate = low (ie. Bypassed). Transmitter output jitter for 8.5 Gb/s and 4.25 Gb/s. 

10 

## **Table 9. Receiver Optical and Electrical Characteristics** 

(TC = 0 °C to 70 °C, VccT, VccR = 3.3V ± 5%) 

|(TC= 0 °C to 70 °C, VccT, VccR = 3.3 V ± 5%)|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|Optical Input Power|PIN|||0|dBm,avg||
|Input Optical Modulation Amplitude,|OMA|89|||µW,OMA|Note 1|
|14.025Gb/s|||||||
|(Peak to Peak) [Unstressed Sensitivity]|||||||
|Input Optical Modulation Amplitude, 8.5Gb/s|OMA|76|||µW,OMA|Note 1|
|(Peak to Peak) [Unstressed Sensitivity]|||||||
|Input Optical Modulation Amplitude, 4.25Gb/s|OMA|61|||µW,OMA|Note 1|
|(Peak to Peak) [Unstressed Sensitivity]|||||||
|Stressed Receiver Sensitivity (OMA) 14.025Gb/s||170|||µW,OMA|Note 2, all fber types|
|Stressed Receiver Sensitivity (OMA) 8.5Gb/s||151|||µW,OMA|Note 3, all fber types|
|Stressed Receiver Sensitivity (OMA) 4.25Gb/s||148<br>138<br>126|||µW,OMA|OM1 62.5µm fber<br>OM2 50µm fber, Note 4<br>OM3 50µm fber|
|Return Loss||12|||dB||
|Loss of Signal – Assert|Pa|-30|||dBm,avg||
|Loss of Signal – De-asserted|PD|||-14|dBm,avg||
|Loss of Signal – Hysteresis|PA – PD|0.5|||dB||



Notes: 

1. Input Optical Modulation Amplitude (commonly known as sensitivity] requires a valid Fibre Channel encoded input. 

2. 14.025 Gb/s stressed received vertical eye closure penalty (ISI) min is 2.5 dB for all fiber types. 

3.  8.5 Gb/s stressed received vertical eye closure penalty (ISI) min is 3.1 dB for all fiber types. 

4. 4.25 Gb/s stressed received vertical eye closure penalty (ISI) min is 0.75 dB for OM3 fiber, 1.67 dB for OM2 fiber and 2.14 dB for OM1 fiber.. 

11 

**Table 10. Transceiver SOFT DIAGNOSTIC Timing Characteristics** (TC = 0 °C to 70 °C, VccT, VccR = 3.3V ± 5%) 

|(TC= 0 °C to 70 °C, VccT, VccR = 3.3 V ± 5%)||||||
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|Hardware TX_DISABLE Assert Time|t_of||10|µs|Note 1|
|Hardware TX_DISABLE Negate Time|t_on||1|ms|Note 2|
|Time to initialize, includingreset of TX_FAULT|t_init||300|ms|Note 3|
|Hardware TX_FAULT Assert Time|t_fault||100|µs|Note 4|
|Hardware TX_DISABLE to Reset|t_reset|10||µs|Note 5|
|Hardware RX_LOS Deassert Time|t_loss_on||100|µs|Note 6|
|Hardware RX_LOS Assert Time|t_loss_of||100|µs|Note 7|
|Hardware RATE_SELECT Assert Time|t_rate_high||1|ms|Note 17|
|Hardware RATE_SELECT Deassert Time|t_rate_low||1|ms|Note 17|
|Software TX_DISABLE Assert Time|t_of_soft||100|ms|Note 8|
|Software TX_DISABLE Negate Time|t_on_soft||100|ms|Note 9|
|Software Tx_FAULT Assert Time|t_fault_soft||100|ms|Note 10|
|Software Rx_LOS Assert Time|t_loss_on_soft||100|ms|Note 11|
|Software Rx_LOS Deassert Time|t_loss_of_soft||100|ms|Note 12|
|Software Rate_Select Assert Time|t_rate_on_soft||100|ms|Note 18|
|Software Rate_Select Deassert Time|t_rate_of_soft||100|ms|Note 19|
|Analogparameter data ready|t_data||1000|ms|Note 13|
|Serial bus hardware ready|t_serial||300|ms|Note 14|
|Serial bus bufer time|t_buf|20||µs|Note 16|
|Write Cycle Time|t_write||40|ms|Note 15|
|Serial ID Clock Rate|f_serial_clock||400|kHz||



## **Notes:** 

1. Time from rising edge of TX_DISABLE to when the optical output falls below 10% of nominal. 

2. Time from falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal. 

3. Time from power on or falling edge of Tx_Disable to when the modulated optical output rises above 90% of nominal. 

4. From power on or negation of TX_FAULT using TX_DISABLE. 

5. Time TX_DISABLE must be held high to reset the laser fault shutdown circuitry. 

6. Time from loss of optical signal to Rx_LOS Assertion. 

7. Time from valid optical signal to Rx_LOS De-Assertion. 

8. Time from two-wire interface assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output falls below 10% of nominal. Measured from falling clock edge after stop bit of write transaction. 

9. Time from two-wire interface de-assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the modulated optical output rises above 90% of nominal. 

10. Time from fault to two-wire interface TX_FAULT (A2h, byte 110, bit 2) asserted. 

11. Time for two-wire interface assertion of Rx_LOS (A2h, byte 110, bit 1) from loss of optical signal. 

12. Time for two-wire interface de-assertion of Rx_LOS (A2h, byte 110, bit 1) from presence of valid optical signal. 

13. From power on to data ready bit asserted (A2h, byte 110, bit 0). Data ready indicates analog monitoring circuitry is functional. 

14. Time from power on until module is ready for data transmission over the serial bus (reads or writes over A0h and A2h). 

15. Time from stop bit to completion of a 1 – 4 byte write command. Write cycle time is 80 ms max. for a 5 – 8 byte write. 

16. Time between STOP and START commands. 

17. Time from rising or falling edge of Rate_Select input until transceiver is successfully passing traffic as designated by RS(0) and RS(1). For Rate_ Select going high, the internal CDR will lock on valid 64b/66b encoded 14.025 Gb/s data within the specified time. For Rate_Select going low, the internal CDR will be bypassed within the specified time for transmission of valid 8b/10b encoded 8.5 Gb/s or 4.25 Gb/s data. 

18. Time from two-wire interface Assertion of Rate_Select (either RS(0) in A2h, byte 110, bit 3 or RS(1) in A2h, byte 118, bit 3) to when the respective CDR is engaged at 14.025 Gb/s data rate. 

19. Time from two-wire interface Deassertion of Rate_Select (either RS(0) in A2h, byte 110, bit 3 or RS(1) in A2h, byte 118, bit 3) to when the respective CDR is bypassed for low speed 8.5 Gb/s or 4.25 Gb/s operation. 

12 

**Table 11. Transceiver Digital Diagnostic Monitor (Real Time Sense) Characteristics** 

(TC = 0 °C to 70 °C, VccT, VccR = 3.3V ± 5%) 

|**Parameter**|**Symbol**|**Min.**|**Units**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal Temperature|TINT|±3.0|°C|Temperature is measured internal to the transceiver.|
|Accuracy||||Valid from =  0°C to 70°C case temperature.|
|Transceiver Internal Supply|VINT|±0.1|V|Supply voltage is measured internal to the transceiver|
|Voltage Accuracy||||and can, with less accuracy, be correlated to|
|||||voltage at the SFP Vccpin. Valid over 3.3 V ± 10%.|
|Transmitter Laser DC Bias Current|IINT|±10|%|IINTis better than ±10% of the nominal value.|
|Accuracy|||||
|Transmitted Average Optical|PT|±3.0|dB|Coupled into 50/125µm multi-mode fber. Valid from|
|Output Power Accuracy||||100µW to 500µW, avg.|
|Received Average Optical Input|PR|±3.0|dB|Coupled from 50/125 µm multi-mode fber. Valid from|
|Power Accuracy||||31µW to 500µW, avg.|




**----- Start of picture text -----**<br>
VCCT,R > 2.97 V VCCT,R > 2.97 V<br>TX_FAULT TX_FAULT<br>TX_DISABLE TX_DISABLE<br>TRANSMITTED SIGNAL TRANSMITTED SIGNAL<br>t_init t_init<br>t-init: TX DISABLE NEGATED t-init: TX DISABLE ASSERTED<br>VCCT,R > 2.97 V TX_FAULT<br>TX_FAULT TX_DISABLE<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>TRANSMITTED SIGNAL<br>t_off t_on<br>t_init<br>INSERTION<br>t-init: TX DISABLE NEGATED, MODULE HOT PLUGGED  t-off & t-on: TX DISABLE ASSERTED THEN NEGATED<br>OCCURANCE OF FAULT<br>OCCURANCE OF FAULT<br>TX_FAULT<br>TX_FAULT<br>TX_DISABLE<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>TRANSMITTED SIGNAL<br>t_fault * SFP SHALL CLEAR TX_FAULT IN t_reset t_init*<br>  < t_init IF THE FAILURE IS TRANSIENT<br>t-fault: TX FAULT ASSERTED, TX SIGNAL NOT RECOVERED t-reset: TX DISABLE ASSERTED THEN NEGATED, TX SIGNAL RECOVERED<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
OCCURANCE OF FAULT<br>TX_FAULT<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>t_fault<br>t_reset<br>* SFP SHALL CLEAR TX_FAULT IN t_init*<br>   <  t_init IF THE FAILURE IS TRANSIENT<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
t-fault: TX DISABLE ASSERTED THEN NEGATED, TX SIGNAL NOT RECOVERED<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
OCCURANCE<br>OPTICAL SIGNAL OF LOSS<br>LOS<br>t_loss_on t_loss_off<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
t-loss-on & t-loss-off<br>**----- End of picture text -----**<br>


**Figure 5. Transceiver timing diagrams (module installed except where noted)** 

13 

**Table 12. EEPROM Serial ID Memory Contents – Address A0h** 

|**Byte #**|||**Byte #**|||
|---|---|---|---|---|---|
|**Decimal**|**Hex**|**Description**|**Decimal**|**Hex**|**Description**|
|0|03|SFPphysical device|37|00|Hex Byte of Vendor OUI[4]|
|1|04|SFP function defned byserial ID only|38|17|Hex Byte of Vendor OUI[4]|
|2|07|LC optical connector|39|6A|Hex Byte of Vendor OUI[4]|
|3|00||40|41|“A”  -  Vendor Name ASCII Character|
|4|00||41|46|“F”  -  Vendor Name ASCII Character|
|5|00||42|42|“B”  -  Vendor Name ASCII Character|
|6|00||43|52|“R”  -  Vendor Name ASCII Character|
|7|60|Short and Intermediate link distance(per FC-PI-5)|44|2D|“-”  -  Vendor Name ASCII Character|
|8|40|Shortwave laser without OFC(open fber control)|45|35|“5”  -  Vendor Name ASCII Character|
|9|0C|Multi-mode 50µm and 62.5µm and optical media|46|37|“7”  -  Vendor Name ASCII Character|
|10|70|400,800 and 1600 MByte/s FC-PI-5 speed[1]|47|46|“F”  -  Vendor Name ASCII Character|
|11|06|64B/66B data at 14.025G & 8B/10B at 8.5G/4.25G|48|35|“5”  -  Vendor Name ASCII Character|
|12|8C|14.025 Mbit/s nominal bit rate(14.025 Gb/s)|49|4D|“M”  -  Vendor Name ASCII Character|
|13|0A|16/8/4G Independent Tx and Rx Rate Selects|50|5A|“Z”  -  Vendor Name ASCII Character|
|14|00||51|20|“ ”  -  Vendor Name ASCII Character|
|15|00||52|20|“ ”  -  Vendor Name ASCII Character|
|16|04|35m of OM2 50/125um fber at 14.025 Gb/s[2]|53|20|“ ”  -  Vendor Name ASCII Character|
|17|02|15m of OM1 62.5/125um fber at 14.025 Gb/s[3]|54|20|“ ”  -  Vendor Name ASCII Character|
|18|00||55|20|“ ”  -  Vendor Name ASCII Character|
|19|0A|100m of OM3 50/125um fber at 14.025 Gb/s[9]|56|20|“ ”  -  Vendor Name ASCII Character|
|20|41|“A”  -  Vendor Name ASCII Character|57|20|“ ”  -  Vendor Name ASCII Character|
|21|56|“V”  -  Vendor Name ASCII Character|58|20|“ ”  -  Vendor Name ASCII Character|
|22|41|“A”  -  Vendor Name ASCII Character|59|20|“ ”  -  Vendor Name ASCII Character|
|23|47|“G”  -  Vendor Name ASCII Character|60|03|Hex Byte of Laser Wavelength[5]|
|24|4F|“O”  -  Vendor Name ASCII Character|61|52|Hex Byte of Laser Wavelength[5]|
|25|20|“ ”  -  Vendor Name ASCII Character|62|00||
|26|20|“ ”  -  Vendor Name ASCII Character|63||Checksum for Bytes 0-62[6]|
|27|20|“ ”  -  Vendor Name ASCII Character|64|00|Receiver limitingoutput. 1Wpower class|
|28|20|“ ”  -  Vendor Name ASCII Character|65|3A|Hardware Tx_Disable, Tx_Fault, Rx_LOS,|
||||||Rate_Select|
|29|20|“ ”  -  Vendor Name ASCII Character|66|00||
|30|20|“ ”  -  Vendor Name ASCII Character|67|00||
|31|20|“ ”  -  Vendor Name ASCII Character|68 - 83||Vendor Serial Number ASCII characters[7]|
|32|20|“ ”  -  Vendor Name ASCII Character|84 - 91||Vendor Date Code ASCII characters[8]|
|33|20|“ ”  -  Vendor Name ASCII Character|92|68|Digital diagnostics,Internal Cal,Rx Pwr Avg|
|34|20|“ ”  -  Vendor Name ASCII Character|93|FA|Alarms/Warnings, Software Tx_Disable,|
||||||Tx-Fault,Rx_LOS,Rate_Select|
|35|20|“ ”  -  Vendor Name ASCII Character|94|05|SFF-8472 compliance to revision 11.0|
|36|00||95||Checksum for Bytes 62-94[6]|
||||96 – 255|00||



Notes: 

1. FC-PI-5 speed 1600 MByte/s is a serial bit rate of 14.025 Gb/s. 800 MByte/s is a serial bit rate of 8.5 Gb/s. 400 MByte/s is a serial bit rate of 4.25 Gb/s. 

2. Link distance with OM2 50/125 µ m cable at 8.5 Gb/s is 50 m. Link distance at 4.25 Gb/s is 150 m. 

3. Link distance with OM1 62.5/125 µ m cable at 8.5 Gb/s is 25 m. Link distance at 4.25 Gb/s is 70 m. 

4. The IEEE Organizationally Unique Identified (OUI) assigned to Avago Technologies is 00-17-64 (3 bytes of Hex). 

5. Laser Wavelength is represented in 16 unsigned bits. The Hex representation of 850 nm is 0352. 

6. Addresses 63 and 95 are checksums calculated (per SFF-8472 and SFF-8074) and stored before product shipment. 

7. Address 68-83 specify the AFBR-57F5MZ ASCII serial number and will vary on a per unit basis. 

8. Address 84-91 specify the AFBR-57F5MZ ASCII data code and will vary on a per date code basis. 

9. Link distance with OM3 50/125 µ m cable at 8.5 Gb/s is 150 m. Link distance at 4.25 Gb/s is 380 m. 

14 

**Table 13. EEPROM Serial ID Memory Contents – Enhanced Feature Set Memory (Address A2h)** 

|**Byte #**||**Byte #**||**Byte #**||
|---|---|---|---|---|---|
|**Decimal**|**Notes**|**Decimal**|**Notes**|**Decimal**|**Notes**|
|0|Temp H Alarm MSB[1]|26|Tx Pwr L Alarm MSB[4]|104|Real Time Rx Pwr MSB[5]|
|1|Temp H Alarm LSB[1]|27|Tx Pwr L Alarm LSB[4]|105|Real Time Rx Pwr LSB[5]|
|2|Temp L Alarm MSB[1]|28|Tx Pwr H WarningMSB[4]|106|Reserved|
|3|Temp L Alarm LSB[1]|29|Tx Pwr H WarningLSB[4]|107|Reserved|
|4|Temp H WarningMSB[1]|30|Tx Pwr L WarningMSB[4]|108|Reserved|
|5|Temp H WarningLSB[1]|31|Tx Pwr L WarningLSB[4]|109|Reserved|
|6|Temp L WarningMSB[1]|32|Rx Pwr H Alarm MSB[5]|110|Status/Control - See Table 14|
|7|Temp L WarningLSB[1]|33|Rx Pwr H Alarm LSB[5]|111|Status/Control - See Table 15|
|8|Vcc H Alarm MSB[2]|34|Rx Pwr L Alarm MSB[5]|112|FlagBits - See Table 16|
|9|Vcc H Alarm LSB[2]|35|Rx Pwr L Alarm LSB[5]|113|FlagBits - See Table 16|
|10|Vcc L Alarm MSB[2]|36|Rx Pwr H WarningMSB[5]|114|Reserved|
|11|Vcc L Alarm LSB[2]|37|Rx Pwr H WarningLSB[5]|115|Reserved|
|12|Vcc H WarningMSB[2]|38|Rx Pwr L WarningMSB[5]|116|FlagBits - See Table 16|
|13|Vcc H WarningLSB[2]|39|Rx Pwr L WarningLSB[5]|117|FlagBits - See Table 16|
|14|Vcc L WarningMSB[2]|40-55|Control Settings - See Table 18|118|Status/Control - See Table 17|
|15|Vcc L WarningLSB[2]|56-94|External Calibration Constants[6]|119-127|Reserved|
|16|Tx Bias H Alarm MSB[3]|95|Checksum for Bytes 0-94[7]|128-247|Customer Writeable|
|17|Tx Bias H Alarm LSB[3]|96|Real Time Temperature MSB[1]|248-255|Vendor Specifc|
|18|Tx Bias L Alarm MSB[3]|97|Real Time Temperature LSB[1]|||
|19|Tx Bias L Alarm LSB[3]|98|Real Time Vcc MSB[2]|||
|20|Tx Bias H WarningMSB[3]|99|Real Time Vcc LS[2]|||
|21|Tx Bias H WarningLSB[3]|100|Real Time Tx Bias MSB[3]|||
|22|Tx Bias L WarningMSB[3]|101|Real Time Tx Bias LSB[3]|||
|23|Tx Bias L WarningLSB[3]|102|Real Time Tx Power MSB[4]|||
|24|Tx Pwr H Alarm MSB[4]|103|Real Time Tx Power LSB[4]|||
|25|Tx Pwr H Alarm LSB[4]|||||



## **Notes:** 

1. Temperature (Temp) is decoded as a 16 bit signed twos compliment integer in increments of 1/256 °C. 

2. Supply Voltage (Vcc) is decoded as a 16 bit unsigned integer in increments of 100 µ V. 

3. Laser bias current (Tx Bias) is decoded as a 16 bit unsigned integer in increments of 2 µ A. 

4. Transmitted average optical power (Tx Pwr) is decoded as a 16 bit unsigned integer in increments of 0.1 µ W. 

5. Received average optical power (Rx Pwr) is decoded as a 16 bit unsigned integer in increments of 0.1 µ W. 

6. Bytes 56-94 are not intended for use with AFBR-57F5MZ, but have been set to default values per SFF-8472. 

7. Byte 95 is a checksum calculated (per SFF-8472) and stored before product shipment. 

15 

**Table 14. EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110)** 

|**Bit #**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7|TX_DISABLE State|Digital state of TX_DISABLE Input Pin (1 = TX_DISABLE asserted)|Note 1|
|6|Soft TX_DISABLE Control|Read/write bit for changingdigital state of TX_DISABLE function|Note 1, 2|
|5|RS(1) State|Digital state of TX Rate_Select Input Pin RS(1)  (1 = Rate High asserted)||
|4|RS(0) State|Digital state of RX Rate_Select Input Pin RS(0)  (1 = Rate High asserted)||
|3|Soft RS(0) Control|Read/write bit for changingdigital state of Rx Rate_Select RS(0) function|Note 3|
|2|TX_FAULT State|Digital state of TX_FAULT Output Pin (1 = TX_FAULT asserted)|Note 1|
|1|RX_LOS State|Digital state of SFP RX_LOS Output Pin (1 = RX_LOS asserted)|Note 1|
|0|Data Ready (Bar)|Indicates transceiver is powered and real time sense data is ready||
|||(0 = Data Ready)||



Notes: 

1. The response time for soft commands of the AFBR-57F5MZ is 100msec as specified by MSA SFF-8472. 

2. Bit 6 is logic OR’d with the SFP TX_DISABLE input pin 3 …. either asserted will disable the SFP transmitter. 

3. Bit 3 is logic OR’d with the SFP RS(0) RX Rate_Select input pin 7 …. either asserted will set receiver to Rate = High. 

**Table 15. EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 111)** 

|**Bit #**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|4-7|Reserved|||
|3|OWRAP FORWARD|Logic Low = FORWARD disabled. Logic High = FORWARD enabled. When||
||Control Bit|used in combination with OWRAP enable, FORWARD routes incoming SFP||
|||Rx optical data to both the Tx optical output and the Rx electrical output.||
|||Enablingsets bit 2 and clears all other bits in byte 111.||
|2|OWRAP|Logic Low = OWRAP disabled. Logic High = OWRAP enabled. When||
||Control Bit|enabled, OWRAP routes incoming SFP Rx optical data to the Tx optical||
|||output. Enablingclears all other bits in byte 111.||
|1|EWRAP FORWARD|Logic Low = FORWARD disabled. Logic High = FORWARD enabled. When||
||Control Bit|used in combination with EWRAP enable, FORWARD routes incoming||
|||SFP Tx electrical data to both Rx electrical output and Tx optical output.||
|||Enablingsets bit 0 and clears all other bits in byte 111.||
|0|EWRAP|Logic Low = EWRAP disabled. Logic High = EWRAP enabled. When en-||
||Control Bit|abled, EWRAP routes incoming SFP Tx electrical data to the Rx electrical||
|||output. Enablingclears all other bits in byte 111.||



16 

**Table 16. EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)** 

|**Byte**|**Bit**|**Flag Bit Name Description**||
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



17 

**Table 17. EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 118)** 

|**Bit #**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|4-7|Reserved|||
|3|Soft RS(1) Control|Read/write bit for changingdigital state of Tx Rate_Select RS(1) function|Note 1|
|2|Reserved|||
|1|Power Level State|Always set to zero. Value of zero indicates Power Level 1 operation (1 Watt||
|||max)||
|0|Power Level Select|Unused. This device supports power level zero (1 Watt max) only.||



Notes: 1. Bit 3 is logic OR’d with the SFP RS(1) TX Rate_Select input pin 9 …. either asserted will set transmitter to Rate = High. 

## **Table. 18. Signal Integrity Feature Configuration Bytes (2-Wire Address A2h)** 

|**Byte**|**Name**|**Description**|
|---|---|---|
|40|Tx Input EQ Setting for|Defnes SFP incoming electrical Tx equalization setting for Tx_Rate = High [ie. RS(1)=High]|
||RS(1) = High|The SFP transceiver will support two EQ settings based on LSB. With LSB = 0, the Tx input|
|||EQ is set to 0 dB (no EQ). With LSB = 1, the Tx input EQ is set to 6 dB gain at 7 GHz.|
|||WritingFFh to this byte resets to factorysettings, EQ = 0 dB.|
|41|Tx Input EQ Setting for|Defnes SFP incoming electrical Tx equalization setting for Tx_Rate = Low [ie. RS(1)=Low]|
||RS(1) = Low|The SFP transceiver will support two EQ settings based on LSB. With LSB = 0, the Tx input|
|||EQ is set to 0 dB (no EQ). With LSB = 1, the Tx input EQ is set to 6 dB gain at 7 GHz.|
|||WritingFFh to this byte resets to factorysettings, EQ = 0 dB.|
|42|Rx Output Pre Emphasis|Defnes SFP output electrical Rx pre-emphasis setting for Rx_Rate = High [ie. RS(0)=High]|
||Setting for RS(0) = High|The SFP transceiver will support 8 Pre Emphasis amplitude settings in the lower 3 bits of|
|||this byte. Emphasis can be varied from 0 dB to 6 dB in eight non-linear steps. A value of 0|
|||results in 0 dB emphasis.|
|||WritingFFh to this byte resets to factorysettings, EMPH = 0 dB.|
|43|Rx Output Pre Emphasis|Defnes SFP output electrical Rx pre-emphasis setting for Rx_Rate = Low [ie. RS(0)=Low]|
||Setting for RS(0) = Low|The SFP transceiver will support 8 Pre Emphasis amplitude settings in the lower 3 bits of|
|||this byte. Emphasis can be varied from 0 dB to 6 dB in eight non-linear steps. A value of 0|
|||results in 0 dB emphasis.|
|||WritingFFh to this byte resets to factorysettings, EMPH = 0 dB.|
|44-55|Unallocated|Contents 00h.|



Note: Checksum at address A2h byte 95 will be updated within 100 ms of a value change in these bytes. 

18 


**----- Start of picture text -----**<br>
8.9 47.5<br>13.9<br>0.64 UNCOMPRESSED<br>8.55<br>6.25<br>1.63<br>13.6<br>13.44<br>**----- End of picture text -----**<br>


**Figure 6.  Module drawing** 


**Figure 7. Module Label** 

19 


**----- Start of picture text -----**<br>
X<br>Y<br>34.5<br>10<br>3x<br>10x ˇ 1.05 ± 0.01 7.2 7.1<br>16.25 ∅ 0.1  L  X  A  S 2.5 ˇ 0.85 ± 0.05<br>MIN. PITCH 1 ∅ 0.1  S  X  Y<br>2.5<br>PCB B A 1<br>EDGE 3.68<br>8.58 5.68 PIN 1 20 2x 1.7 8.48<br>16.25 14.2511.08 9.6 11.93<br>REF.<br>4.8<br>11<br>10<br>SEE DETAIL 1<br>2.0 9x 0.95 ± 0.05<br>11x 11x 2.0 ∅ 0.1  L  X  A  S<br>26.8 5 2<br>3 10<br>3x<br>41.3<br>42.3<br>5<br>3.2<br>20x 0.5 ± 0.03<br>0.9<br>0.06   L    A  S    B  S<br>PIN 1 20 LEGEND<br>10.93 10.53 11.93 1. PADS AND VIAS ARE CHASSIS GROUND<br>9.6<br>0.8<br>TYP. 2. THROUGH HOLES, PLATING OPTIONAL<br>11<br>10 3. HATCHED AREA DENOTES COMPONENT<br>AND TRACE KEEPOUT (EXCEPT<br>CHASSIS GROUND)<br>4 4. AREA DENOTES COMPONENT<br>2x 1.55 ± 0.05 2 ± 0.005 TYP. KEEPOUT (TRACES ALLOWED)<br>0.06   L    A  S    B  S<br>∅ 0.1  L  A  S  B  S DIMENSIONS ARE IN MILLIMETERS<br>DETAIL 1<br>**----- End of picture text -----**<br>


**Figure 8.  SFP host board mechanical layout** 

20 


**----- Start of picture text -----**<br>
1.7 ± 0.9<br>Tcase REFERENCE POINT<br>3.5 ± 0.3<br>41.78 ± 0.5<br>15 MAX.<br>9.8 MAX.<br>16.25 ± 0.1<br>10<br>15.25 ± 0.1<br>**----- End of picture text -----**<br>


**Figure 9.  SFP Assembly drawing** 

## **Customer Manufacturing Processes** 

This module is pluggable and is not designed for aqueous wash, IR reflow, or wave soldering processes. 

21 

## **Appendix I. Rate Select Control** 

RX and TX rates can be independently controlled by either hardware input pins or via register writes. Module electrical input pins 7 and 9 are used to select RX and TX rate respectively. Status of each logic level is reflected to register byte 110 bit 4 and 5 on address A2h as shown in the diagram below. RX and TX rates can also be controlled by register writes to byte 110 bit 3 and 118 bit 3. Power on default of these bits are logic low. Hardware and software control inputs are OR’d to allow flexible control. 

## **RS0 RX Rate Select control flow** 


**----- Start of picture text -----**<br>
Hardware  Software<br>Input Input<br>RS0 (PIN7) Voltage A2h, byte 110<br>"1"...V>2.0 Bit 3<br>"0"...V<0.8<br>A2h, byte 110<br>Bit 4 OR<br>RX Rate<br>Control<br>**----- End of picture text -----**<br>


## **RS1 TX Rate Select control flow** 


**----- Start of picture text -----**<br>
Hardware  Software<br>Input Input<br>RS1 (PIN9) Voltage A2h, byte 118<br>"1"...V>2.0 Bit 3<br>"0"...V<0.8<br>A2h, byte 110<br>Bit 5 OR<br>TX Rate<br>Control<br>**----- End of picture text -----**<br>


|**RS0 Control Input**<br>**Hardware**<br>**Software**|**RS0 Control Input**<br>**Hardware**<br>**Software**|**RX Operation**|**RX Operation**|
|---|---|---|---|
|**Hardware**||||
|0|0|4/8G FC|RX CDR bypassed|
|0|1|16G FC|RX CDR enabled|
|1|0|16G FC||
|1|1|16G FC||



|**RS1 Control Input**<br>**Hardware**<br>**Software**|**RS1 Control Input**<br>**Hardware**<br>**Software**|**TX Operation**|**TX Operation**|
|---|---|---|---|
|**Hardware**||||
|0|0|4/8G FC|TX CDR bypassed|
|0|1|16G FC|TX CDR enabled|
|1|0|16G FC||
|1|1|16G FC||



For product information and a complete list of distributors, please go to our website: **www.avagotech.com** 

Avago, Avago Technologies, and the A logo are trademarks of Avago Technologies in the United States and other countries. Data subject to change. Copyright © 2005-2013 Avago Technologies. All rights reserved. Obsoletes AV02-2898EN. AV02-3165EN  -  May 16, 2013 

