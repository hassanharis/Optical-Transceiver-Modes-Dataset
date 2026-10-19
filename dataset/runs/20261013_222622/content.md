## **AFCT-57G5MZ** 

## 32GFC SFP+ for Single-Mode Optical Fiber Digital Diagnostic SFP, 1310nm, 32G/16G/8G Low Voltage (3.3V) Fibre Channel Optical Transceiver 

## **Data Sheet** 

## **Description** 

Avago Technologies’ AFCT-57G5MZ optical transceiver supports high speed serial links over single-mode optical fiber at signalling rates up to 28.05Gb/s (the serial line rate of 32GFC). The product is compliant with Small Form Pluggable industry agreements SFP and SFP+ for mechanical and low speed electrical specifications. High speed electrical and optical specifications are compliant with ANSI Fibre Channel FC-PI-6. 

The AFCT-57G5MZ is a multi-rate 1310nm transceiver which ensures compliance with FC-PI-6 32GFC, 16GFC and 8GFC specifications. Per the requirements of 32GFC, internal clock and data recovery circuits (CDRs) are present on both electrical input and electrical output of this transceiver. These CDRs will lock at 28.05Gb/s and 14.025Gb/s (32GFC and 16GFC) but must be bypassed for operation at 8.5Gb/s (8GFC), accomplished by using two Rate Select inputs to configure transmit and receive sides. Transmitter and receiver can operate at different data rates, as is often seen during Fibre Channel speed negotiation. 

Digital diagnostic monitoring information (DMI) is present in the AFCT-57G5MZ per the requirements of SFF-8472, providing real time monitoring information of transceiver laser, receiver and environment conditions over a SFF8431 2-wire serial interface. 

## **Related Products** 

- AFBR-57G5MZ: 850nm SFP for 32G/16G/8G Fibre Channel 

- AFBR-57F5MZ: 850nm SFP for 16G/8G/4G Fibre Channel 

- AFCT-57F3TMZ: 1310nm SFP for 16G/8G/4G Fibre Channel 

- AFBR-57D9AMZ: 850nm SFP for 8G/4G/2G Fibre Channel 

- AFCT-57D3ATPZ: 1310nm SFP for 8G/4G/2G Fibre Channel 

- AFCT-57D3ANPZ: 1310nm SFP for 8G/4G/2G Fibre Channel 

- AFBR-57R5APZ: 850nm SFP for 4G/2G/1G Fibre Channel 

- AFCT-57R5APZ: 1310nm SFP for 4G/2G/1G Fibre Channel 

## **Features** 

- Compliant to RoHS directives 

- 1310nm Distributed Feedback Laser (DFB) 

- Class 1 eye safe per IEC60825-1 and CDRH 

- Wide temperature range (0°C to 70°C) 

- LC duplex connector optical interface conforming to ANSI TIA/EIA604-10 (FOCIS 10A) 

- Diagnostic features per SFF-8472 “Diagnostic Monitoring Interface for Optical Transceivers” 

- Real time monitoring of: 

   - Transmitter average optical power 

   - Received average optical power 

   - Laser bias current 

   - Temperature 

   - Supply Voltage 

- SFP+ mechanical specifications per SFF-8432 

- Pull Tab delatch mechanism 

- SFP+ compliant low speed interface 

- Fibre Channel FC-PI-6 compliant high speed interface - 3200-M5-SN-S, 1600-M5-SN-S, 800-M5-SN-S 

   - 3200-M5E-SN-I, 1600-M5E-SN-I, 800-M5E-SN-I 

   - 3200-M5F-SN-I, 1600-M5F-SN-I, 800-M5F-SN-I 

- Fibre Channel FC-PI-6 compliant optical link distances 

## **Applications** 

- Fibre Channel switches (director, stand alone, blade) 

- Fibre Channel Host Bus Adapters 

- Fibre Channel RAID controllers 

- Fibre Channel tape drive 

- Port side connections 

- Inter-switch or inter-chassis aggregated links 

Patent - www.avagotech.com/patents 

- AFCT-57R5ATPZ: 1310nm SFP for 4G/2G/1G Fibre Channel 

- AFCT-57R5ANPZ: 1310nm SFP for 4G/2G/1G Fibre Channel 

**Avago Technologies Proprietary** 

## **Transmitter Section** 

The transmitter section includes a Transmitter Optical SubAssembly (TOSA), laser driver circuit, Clock and Data Recovery circuit (CDR) and an electrical input stage with variable equalization controls and electrical eye measurement capability. The TOSA contains a 1310nm Distributed Feedback Laser (DFB) light source with integral light monitoring function and imaging optics to assure efficient optical coupling to the LC connector interface. The TOSA is driven by a laser driver IC, which uses the differential output from an integral Tx CDR stage to modulate and regulate DFB laser optical power. As mandated by FC-PI-6, the integral CDR cleans up any incoming jitter accumulated from the host ASIC, PCB traces and SFP electrical connector. Between the SFP electrical connector and Tx CDR is a variable, i2c controlled, equalization circuit to optimize SFP performance with non-ideal incoming electrical waveforms. Note the Tx CDR is engaged with Tx_RATE=high (32GFC) and auto-configured (engaged or bypassed) with Tx_RATE=low (16G/8G). 

## **Receiver Section:** 

The receiver section includes a Receiver Optical SubAssembly (ROSA), pre-amplification and post-amplification circuit, Clock and Data Recovery Circuit and an electrical output stage with variable emphasis controls and integral PRBS generator. The ROSA, containing a high speed PIN detector, pre-amplifier and imaging optics efficiently couple light from the LC connector interface and perform an optical to electrical conversion. The resulting differential electrical signal passes through a post amplification circuit and into a Clock and Data Recovery circuit (CDR) for cleaning up accumulated jitter. Note the Rx CDR is engaged with Rx_RATE=high (32GFC) and auto-configured (engaged or bypassed) with Rx_RATE=low (16G/8G). 

## **Digital Diagnostics:** 

The AFCT-57G5MZ is compliant to the Diagnostic Monitoring Interface (DMI) defined in document SFF-8472. These features allow the host to access, via i2c, real time diagnostic monitors of transmit optical power, received optical power, temperature, supply voltage and laser operating current. 

## **Low Speed Interfaces:** 

Conventional low speed interface I/Os are available as defined in documents SFF-8074 and SFF-8431 to manage coarse and fine functions of the optical transceiver. On the transmit side, a Tx_DISABLE input is provided for the host to turn on and off the outgoing optical signal. A transmitter rate select control input, Tx_RATE, is provided to configure the transmitter stages for 32GFC, 16GFC or 8GFC operation (logic HIGH reserved for 32GFC, logic LOW reserved for 16GFC and 8GFC). A transmitter fault indicator output, Tx_FAULT, is available for the SFP to signal a host of a transmitter operational problem. A receiver rate select control input, Rx_RATE, is provided to configure receiver stages for 32GFC, 16GFC, or 8GFC operation (logic HIGH reserved for 32GFC, logic LOW reserved for 16GFC and 8GFC). A received optical power loss of signal indicator, RX_LOS, is available to advise the host of a receiver operational problem. 


**----- Start of picture text -----**<br>
OPTICAL INTERFACE RECEIVER ELECTRICAL INTERFACE<br>RD+ (RECEIVE DATA)<br>RD- (RECEIVE DATA)<br>AMPLIFICATION Rx Rx Vout &<br>LIGHT FROM FIBER PHOTO-DETECTOR & QUANTIZATION CDR Emphasis Rx LOSS OF SIGNAL<br>Rx RATE SELECT RS(0)<br>MOD-DEF2 (SDA)<br>µ Controller<br>MOD-DEF1 (SCL)<br>MOD-DEF0<br>TRANSMITTER<br>TX_DISABLE<br>LASER TD+ (TRANSMIT DATA)<br>LIGHT TO FIBER DFB Laser DRIVER &SAFETY CDRTx EqualizationTx TD- (TRANSMIT DATA)<br>CIRCUITRY TX_FAULT<br>Tx RATE SELECT RS(1)<br>**----- End of picture text -----**<br>


**Figure 1. Transceiver functional diagram.** 

**Avago Technologies Proprietary** 

2 

## **Table 1. Regulatory Compliance** 

|**Feature**||**Test Method**|**Performance**|
|---|---|---|---|
|Electrostatic Discharge (ESD)||JEDEC Human Body Model (HBM)|High speed contacts shall withstand|
|to the Electrical Contacts||(JESD22-A114-B)|1000V. All other contacts shall withstand|
||||2000 V.|
|Electrostatic Discharge (ESD) to||EN61000-4-2, Criterion B|When installed in a properly grounded|
|the Optical Connector Receptacle|||housing and chassis the units are subject-|
||||ed to 15kV air discharges during operation|
||||and 8kV direct discharges to the case.|
|Electromagnetic Interference (EMI)||FCC Part 15 CENELEC EN55022|System margins are dependent on cus-|
|||(CISPR 22A) VCCI Class 1|tomer board and chassis design.|
|Immunity||Variation of IEC 61000-4-3|Typically shows no measurable efect from<br>a 10V/m feld swept from 80 MHz to 1 GHz|
||||applied to the module without a chassis|
||||enclosure|
|Laser Eye Safety and Equipment||US FDA CDRH AEL Class 1|CDRH Certification  9521220-224|
|Type Testing||US21 CFP, Subchapter J per Paragraphs 1002.10|TUV File:  R50229221|
|||and 1002.12||
||**BAUART**<br>**GEPRUFT**<br>**¬**|(IEC) EN60825-1:1994 +A11 +A2||
|**TUV**<br>**Rheinland**<br>**Product Safety**<br>**¬**|**TYPE**<br>**APPROVED**|(IEC) EN60825-2:1994 +A1<br>(IEC) EN60950:1992 +A1 +A2 +A3 +A4 +A11||
|Component Recognition||Underwriters Laboratories (UL) and Canadian|UL File:   E484615|
|||Standards Association (CSA) Joint Component||
|||Recognition for Information Technology Equip-||
|||ment includingElectrical Business Equipment||
|RoHS Compliance|||Less than 1000 ppm of cadmium, lead,|



Less than 1000 ppm of cadmium, lead, mercury, hexavalent chromium, polybrominated biphenyls (PPB) and polybrominated biphenyl ethers (PBDE). 

**Avago Technologies Proprietary** 

3 


**----- Start of picture text -----**<br>
Tx Rate Select  VCC,T<br>RS (1)<br>40 k Ω 10 k Ω<br>Tx DIS<br>Tx_DISABLE<br>Tx FAULT<br>Tx_FAULT<br>0.1 µF<br>TD+<br>100  Ω<br>TD-<br>0.1 µF Tx CDR LASER DRIVER<br>4.7 k to 10 k Ω<br>4.7 µH VCC,T<br>0.1 µF 22 µF 0.1 µF<br>3.3 V<br>PROTOCOL IC SERDES IC 4.7 µH VCC,R VCC,R<br>VCC,R<br>0.1 µF 22 µF 0.1 µF 50  Ω<br>4.7 k to<br>10 k Ω 50  Ω<br>0.1 µF<br>RD+<br>100  Ω<br>RD-<br>0.1 µF<br>Rx LOS<br>LOSS OF SIGNAL<br>RS (0) Rx CDR POST AMPLIFIER<br>Rx Rate Select<br>3.3 V 40 k Ω<br>GND,R<br>4.7 k to 10 k Ω 4.7 k to 10 k Ω<br>4.7 k to 10 k Ω MOD_DEF0 MOD_DEF1 MOD_DEF2<br>MODULE DETECT<br>SCL<br>SDA<br>**----- End of picture text -----**<br>


**Figure 2. Typical application configuration** 


**----- Start of picture text -----**<br>
4.7 µH<br>VCC T<br>0.1 µF 22 µF 0.1 µF<br>3.3 V<br>4.7 µH<br>VCC R<br>0.1 µF 22 µF 0.1 µF<br>SFP MODULE HOST BOARD<br>**----- End of picture text -----**<br>


**NOTE: INDUCTORS MUST HAVE LESS THAN 1** Ω **SERIES RESISTANCE TO LIMIT VOLTAGE DROP TO THE SFP MODULE.** 

**Figure 3. Recommended power supply filter** 

**Avago Technologies Proprietary** 

4 

## **Table 2. Pin Description** 

|**Pin**|**Name**|**Function/Description**|**Notes**|
|---|---|---|---|
|1|VeeT|Transmitter Ground||
|2|TX_FAULT|Transmitter Fault Indication – High indicates a fault condition|Note 1|
|3|TX_DISABLE|Transmitter Disable  –  Module optical output disables on high or open|Note 2|
|4|MOD-DEF2|Module Defnition 2 – Two wire serial ID interface data line (SDA)|Note 3|
|5|MOD-DEF1|Module Defnition 1 – Two wire serial ID interface clock line (SCL)|Note 3|
|6|MOD-DEF0|Module Defnition 0 – Grounded in module (modulepresent indicator)|Note 3|
|7|Rx Rate Select, RS(0)|Receiver Rate Select. Logic High = 28.05Gb/s, Logic Low = 14.025Gb/s and 8.5Gb/s|Note 8|
|8|RX_LOS|Loss of Signal – High indicates loss of received optical signal|Note 4|
|9|Tx Rate Select, RS(1)|Transmitter Rate Select. Logic High = 28.05Gb/s, Logic Low = 14.025Gb/s and 8.5Gb/s|Note 8|
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



## Notes: 

1. TX_FAULT is an open collector/drain output, which must be pulled up with a 4.7k – 10k Ω resistor on the host board. When high, this output indicates a laser fault of some kind. Low indicates normal operation.  In the low state, the output will be pulled to < 0.8V. 

2. TX_DISABLE is an input that is used to shut down the transmitter optical output.  It is internally pulled up (within the transceiver) with a 6.8k resistor. 

Low (0 – 0.8V): Transmitter on Between (0.8V and 2.0V): Undefined High (2.0 – Vcc max) or OPEN: Transmitter Disabled 

3. The signals Mod-Def 0, 1, 2 designate the two wire serial interface pins. They must be pulled up with a 4.7k – 10k Ω resistor on the host board. Mod-Def  0 is grounded by the module to indicate the module is present Mod-Def  1 is serial clock line (SCL) of two wire serial interface 

   - Mod-Def  2 is serial data line (SDA) of two wire serial interface 

4. RX_LOS (Rx Loss of Signal) is an open collector/drain output that must be pulled up with a 4.7k – 10k Ω resistor on the host board. When high, this output indicates the received optical power is below the worst case receiver sensitivity (as defined by the standard in use).  Low indicates normal operation.  In the low state, the output will be pulled to < 0.8V. 

5. RD-/+ designate the differential receiver outputs.  They are AC coupled 100 Ω differential lines which should be terminated with 100 Ω differential at the host SERDES input.  AC coupling is done inside the transceiver and is not required on the host board. The voltage swing on these lines will be between 50 and 900 mV differential (25 – 450 mV single ended) when properly terminated. 

6. VccR and VccT are the receiver and transmitter power supplies.  They are defined at the SFP connector pin.   The maximum supply current is 300 mA and the associated in-rush current will typically be no more than 30 mA above steady state after 500 nanoseconds. 

7. TD-/+ designate the differential transmitter inputs.  They are AC coupled differential lines with 100 Ω differential termination inside the module. The AC coupling is done inside the module and is not required on the host board. The inputs will accept differential swings of 40 – 1200 mV (20 – 600 mV single ended), though it is recommended that values between 50 and 900 mV differential (25 – 450 mV single ended) be used for best EMI performance. 

8. RATE_SELECT is an input used to control transmitter and receiver compliance among multiple rates. It is internally pulled down with a  40k Ω resistor. 

Low (0 - 0.8V) or OPEN: Low Bit Rate Compliance (14.025Gb/s and 8.5 Gb/s) Between (0.8V and 2.0V): Undefined per SFF-8074i High (2.0 – Vcc max): High Bit Rate Compliance (28.05Gb/s) 

**Avago Technologies Proprietary** 

5 

## **Table 3. Absolute Maximum Ratings** 

Stress in excess of any of the individual Absolute Maximum Ratings can cause immediate catastrophic damage to the module even if all other parameters are within Recommended Operating Conditions.  It should not be assumed that limiting values of more than one parameter can be applied to the module concurrently.  Exposure to any of the Absolute Maximum Ratings for extended periods can adversely affect reliability. 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|**Reference**|
|---|---|---|---|---|---|
|Storage Temperature|TS|-40|85|°C|Note 1|
|Case OperatingTemperature|TC|-40|85|°C||
|Relative Humidity|RH|5|95|%||
|SupplyVoltage|VCC|-0.5|3.6|V||
|Low Speed Input Voltage|Vi|-0.5|Vcc+0.5, 3.6|V||



## **Table 4. Recommended Operating Conditions** 

Recommended Operating Conditions specify parameters for which the optical and electrical characteristics hold unless otherwise noted.  Optical and electrical characteristics are not defined for operation outside the Recommended Operating Conditions, reliability is not implied and damage to the module may occur for such operation over an extended period of time. 

|period of time.|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Units**|**Reference**|
|Case OperatingTemperature|Tc|0||70|°C|Note 2|
|SupplyVoltage|VCC|3.135|3.3|3.465|V||
|Data Rate||8.5||28.05|Gb/s|Note 3|
|Two Wire Serial (TWS) Interface Clock Rate||||400|kHz|Note 4|
|**Table 5. Transceiver Electrical Characteristics**|||||||
|The following characteristics are defned over|the Recommended||Operating|Conditions unless|otherwise|noted.|
|**Parameter**|**Symbols**|**Min.**|**Typ.**|**Max.**|**Units**|**Reference**|
|Transceiver Power Consumption||||1.2|W||
|Power SupplyNoise Rejection (peak-peak)|PSNR|||66|mV|Note 5|
|Low Speed Outputs:|VOH|2.0||VCCT,R+0.3|V|Note 6|
|TX_FAULT, RX_LOS, MOD_DEF2|VOL|||0.8|V||
|Low Speed Inputs|VIH|2.0||Vcc|V|Note 7|
|TX_DIS, MOD_DEF1, MOD_DEF2, RS(0), RS(1)|VOL|0||0.8|V||



Notes: 

1. Absolute maximum ratings are those values beyond which damage to the device may occur if these limits are exceeded for other than a short period of time. See Reliability Data Sheet for specific reliability performance. Between Absolute Maximum Ratings and the Recommended Operating Conditions functional performance is not intended, device reliability is not implied, and damage to the device may occur over an extended period of time. 

2. The position of case temperature measurement is shown in Figure 5.  Continuous operation at the maximum Recommended Operating Case Temperature should be avoided in order not to degrade reliability. 

3. 32GFC requires FEC RS(528,514) encoding per FC-PI-6. 16GFC and 8GFC are not compatible with FEC, per FC-PI-5. 

4. With 500us clock stretch per SFP+ MSA (INF-8431) 

5. Filter per SFP specification is required on the host board to remove 10Hz to 2MHz content. 

6. Pulled up externally with a 4.7k-10k Ω resistor on the host board to 3.3V 

7. Mod_Def1 and Mod_Def2 must be pulled up externally with a 4.7k-10k Ω resistor on the host board to 3.3V 

**Avago Technologies Proprietary** 

6 

## **Table 6. Transmitter and Receiver Electrical Characteristics** 

(Tc = 0°C to 70°C, VccT, VccR = 3.3V ± 5%) 

|(Tc = 0°C to 70°C, VccT, VccR = 3.3V±5%)||||||
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|**Notes**|
|High Speed Data Input Transmitter Diferential|VI|50|900|mV|Note 1|
|Input Voltage (TD±)||||||
|High Speed Data Output Receiver Diferential|VO|250|900|mV|Note 2|
|Output Voltage (RD±)||||||
|Module Electrical Input, Diferential Termination|||10|%||
|Resistance Mismatch||||||
|Module Electrical Input Diferential return loss SDD11|||||See FC-PI-6 Equation 6-1,|
||||||Figure 10|
|Module Electrical Input Common Mode to|||||See FC-PI-6 Equation 6-2,|
|Diferential Conversion, SCD11|||||Figure 12|
|Module Electrical Input, Diferential Mode to|||||See FC-PI-6 Equation 6-2,|
|Common Conversion, SDC11|||||Figure 12|
|Module Electrical Input, Stressed Input Random Jitter,|||0.09|UI||
|p-p, 10E-6 BER||||||
|Module Electrical Input, Stressed Input Eye Width||0.46||UI||
|at 1E-6 ProbabilityEW6||||||
|Module Electrical Input, Stressed Input Eye Height||50||mV||
|at 1E-6 ProbabilityEH6||||||
|Module Electrical Output, Common Mode Noise rms|||17.5|mV,rms||
|Module Electrical Output, Diferential termination|||10|%||
|resistance mismatch||||||
|Module Electrical Output, Diferential return loss|||||See FC-PI-6 Equation 6-1,|
|SDD22|||||Figure 10|
|Module Electrical Output, Common Mode to|||||See FC-PI-6 Equation 6-3,|
|Diferential Conversion, SCD22|||||Figure 12|
|Module Electrical Output, Diferential Mode to|||||See FC-PI-6 Equation 6-3,|
|Common Conversion, SDC22|||||Figure 12|
|Module Electrical Output, Common Mode Return|||-2|dB||
|Loss, SCC22||||||
|Module Electrical Output, Vertical Eye Closure|||4|dB||
|Module Electrical Output, Eye Width at 1E-6||0.65||UI||
|ProbabilityEW6||||||
|Module Electrical Output, Eye Height at 1E-6||250||mV||
|ProbabilityEH12||||||
|Receiver Total Jitter (28.05Gb/s)|TJ|||UI|Compliance Test. Note 3, 5|
|Receiver Total Jitter (14.025Gb/s)|TJ||0.36|UI|Note 3,|
|Receiver Total Jitter (8.5Gb/s)|TJ||0.71|UI|Note 4,|
|Receiver Deterministic Jitter (14.025Gb/s)|DJ||0.22|UI|Note 3,|
|Receiver Deterministic Jitter (8.5Gb/s)|DJ||0.42|UI|Note 4,|
|Receiver Data Dependent Pulse Width Shrinkage|DDPWS||0.14|UI|Note 3,|
|(14.025Gb/s)||||||
|Receiver Data Dependent Pulse Width Shrinkage|DDPWS||0.36|UI|Note 4,|
|(8.5Gb/s)||||||



Notes: 

1. Internally ac coupled and terminated (100Ω differential). 

2. Internally ac coupled but requires an external load termination (100Ω differential). 

3. CDR is engaged with 28.05Gb/s and 14.025 Gb/s. 

4. CDR is not engaged with 8.5 Gb/s. 

5. 32GFC (28.05Gb/s) assumes a FEC encoded RS(528, 514) signal and allows  a BER of 1E-6 for receiver and transmitter measurements. 

**Avago Technologies Proprietary** 

7 

## **Table 7. Transmitter Optical Characteristics** 

(Tc = 0°C to 70°C, VccT, VccR = 3.3V ± 5%) 

|**Table 7. Transmitter Optical Characteristics**<br>(Tc = 0°C to 70°C, VccT, VccR = 3.3V±5%)|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|Modulated Optical Output Power (OMA) (Peak to Peak)|Tx,OMA|631|||uW||
|28.05Gb/s|||||||
|Modulated Optical Output Power (OMA) (Peak to Peak)|Tx,OMA|631|||uW||
|14.025Gb/s|||||||
|Modulated Optical Output Power (OMA) (Peak to Peak)|Tx,OMA|290|||uW||
|8.5Gb/s|||||||
|Average Optical Output Power 28.05Gb/s|Pout|-5.0||+2.0|dBm|Note 1|
|Average Optical Output Power 14.025Gb/s|Pout|-5.0|||dBm|Note 1|
|Average Optical Output Power 8.5Gb/s|Pout|-8.4|||dBm|Note 1|
|Center Wavelength|λc|1295||1325|nm||
|Spectral Width – rms|s-20db|||1.0|nm||
|RIN20OMA|RIN|||-130|dB/Hz||
||||||||
|Transmitter Distortion Penalty, 28.05Gb/s|TDP|||2.7|dB|Note 2|
|Transmitter Distortion Penalty, 14.025Gb/s|TDP|||4.4|dB|Note 2|
|Transmitter Distortion Penalty, 8.5Gb/s|TDP|||3.2|dB|Note 3|
|Pout Tx_DISABLE Asserted|Pof|||-35|dBm||



Notes: 

1. Max Pout is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

2. CDR is engaged with 28.05Gb/s and 14.025Gb/s. 

3. CDR is not engaged with 8.5 Gb/s. 

## **Table 8. Receiver Optical and Electrical Characteristics** 

(Tc = 0°C to 70°C, VccT, VccR = 3.3V ± 5%) 

|**Table 8. Receiver Optical and Electrical Characteristics**<br>(Tc = 0°C to 70°C, VccT, VccR = 3.3V±5%)|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|Optical Input Power, 28.05 Gb/s|PIN|||+2.0|dBm,avg||
|Optical Input Power, 14.025Gb/s|PIN|||+2.0|dBm,avg||
|Optical Input Power, 8.5Gb/s|PIN|||+0.5|dBm,avg||
|Input Optical Modulation Amplitude, 28.05Gb/s|OMA|72|||uW,OMA|Note 1, 2|
|(Peak to Peak) [Unstressed Sensitivity]|||||||
|Input Optical Modulation Amplitude, 14.025Gb/s|OMA|63|||uW,OMA|Note 1|
|(Peak to Peak) [Unstressed Sensitivity]|||||||
|Input Optical Modulation Amplitude, 8.5Gb/s|OMA|42|||uW,OMA|Note 1|
|(Peak to Peak) [Unstressed Sensitivity]|||||||
|Return Loss||26|||dB||
|Loss of Signal – Assert|Pa|-30|||dBm,OMA||
|Loss of Signal – De-asserted|PD|||-11|dBm,OMA||
|Loss of Signal – Hysteresis|PA– PD|0.5|||dB||



Notes: 

1. Max Pout is the lesser of Class 1 safety limits (CDRH and EN 60825) or received power, max. 

2. 32GFC (28.05Gb/s) assumes a FEC encoded RS(528, 514) signal and allows  a BER of 1E-6 for receiver and transmitter measurements. 

**Avago Technologies Proprietary** 

8 

**Table 9. Rate Select Definition** 


**----- Start of picture text -----**<br>
||||
|---|---|---|
|Function|State|Operation|
|Tx Rate Select RS(1)|High|Transmit Rate Select HIGH is defined for 32GFC operation. It configures the Tx CDR to lock|
|on 28.05Gb/s 64b/66b encoded data, sets the Tx optical power and linear bandwidth for|
|32GFC operation. FEC is expected for 32GFC.|
|Low|Transmit Rate Select LOW auto configures the internal Tx CDR for 16GFC (CDR locked) or|
|8GFC (CDR bypassed) operation. Transmit optical power and linear bandwidth are opti-|
|mized accordingly. FEC is not expected for 16GFC or 8GFC. This is intended for use only|
|with 16GFC and 8GFC traffic, however when the CDR is bypassed, the SFP behaves like a|
|legacy SFP (and is not bit rate sensitive).|
|Rx Rate Select RS(0)|High|Receive Rate Select HIGH is defined for 32GFC operation. It configures the Rx CDR to lock|
|on 28.05Gb/s 64b/66b encoded data, sets the Rx optical sensitivity and bandwidth for|
|32GFC operation. FEC is expected for 32GFC..|
|Low|Receive Rate Select LOW auto configures the internal Rx CDR for 16GFC (CDR locked) or|
|8GFC (CDR bypassed) operation. Receiver optical sensitivity and linear bandwidth are op-|
|timized accordingly. FEC is not expected for 16GFC or 8GFC. This is intended for use only|
|with 16GFC and 8GFC traffic, however when the CDR is bypassed, the SFP behaves like a|
|legacy SFP (and is not bit rate sensitive).|

**----- End of picture text -----**<br>


Note: During Fibre Channel Link Speed Negotiation sequences, the host will control Tx Rate and Rx Rate inputs separately to accomplish link initialization. Once speed negotiation is complete, it is expected both Tx Rate and Rx Rate will be placed in the same state by the host. 

## **Rate Select Control** 

RX and TX rates can be independently controlled by either hardware input pins or via register writes. Module electrical input pins 7 and 9 are used to select RX and TX rate respectively. Status of each logic level is reflected to register byte 110 bit 4 and 5 on address A2h as shown in the diagram below. RX and TX rates can also be controlled via register writes to bytes 110 bit 3 and 118 bit 3. Power on default of these bits are logic low. Hardware and software control inputs are OR’d to allow flexible control. 

**RS0 RX Rate Select control flow** 

**RS1 TX Rate Select control flow** 


**----- Start of picture text -----**<br>
|||||||||
|---|---|---|---|---|---|---|---|
|Hardware|Software|Hardware|Software|
|Input|Input|Input|Input|
|RS0 (PIN7) Voltage|A2h, byte 110|RS1 (PIN9) Voltage|A2h, byte 118|
|"1"...V>2.0|Bit 3|"1"...V>2.0|Bit 3|
|"0"...V<0.8|"0"...V<0.8|
|A2h, byte 110|A2h, byte 110|
|Bit 4|OR|Bit 5|OR|
|RX Rate|TX Rate|
|Control|Control|
|RS0 Control Input|RS1 Control Input|
|Hardware|Software|RX Operation|Hardware|Software|TX Operation|
|0|0|16G/8G FC|Rx CDR auto detect|0|0|16G/8G FC|Tx CDR auto detect|
|0|1|32GFC|Rx CDR engaged|0|1|32GFC|Tx CDR engaged|
|1|0|32GFC|Rx CDR engaged|1|0|32GFC|Tx CDR engaged|
|1|1|32GFC|Rx CDR engaged|1|1|32GFC|Tx CDR engaged|

**----- End of picture text -----**<br>


**Avago Technologies Proprietary** 

9 

## **Table 10. Transceiver SOFT DIAGNOSTIC Timing Characteristics** 

(TC  =  0°C to 70°C,   VccT, VccR = 3.3V ± 5%) 

|(TC=  0°C to 70°C,   VccT, VccR = 3.3V±5%)||||||
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Minimum**|**Maximum**|**Unit**|**Notes**|
|Hardware TX_DISABLE Assert Time|t_of||100|µs|Note 1|
|Hardware TX_DISABLE Negate Time|t_on||2|ms|Note 2|
|Time to initialize, includingreset of TX_FAULT|t_init||300|ms|Note 3|
|Hardware TX_FAULT Assert Time|t_fault||1|ms|Note 4|
|Hardware TX_DISABLE to Reset|t_reset|10||µs|Note 5|
|Hardware RX_LOS DeAssert Time|t_los_on||100|µs|Note 6|
|Hardware RX_LOS Assert Time|t_los_of||100|µs|Note 7|
|Hardware RATE_SELECT Assert Time|t_rate_high||10|µs|Note 8|
|Hardware RATE_SELECT DeAssert Time|t_rate_low||10|µs|Note 8|
|Software TX_DISABLE Assert Time|t_of_soft||100|ms|Note 9|
|Software TX_DISABLE Negate Time|t_on_soft||100|ms|Note 10|
|Software Tx_FAULT Assert Time|t_fault_soft||100|ms|Note 11|
|Software Rx_LOS Assert Time|t_los_on_soft||100|ms|Note 12|
|Software Rx_LOS De-Assert Time|t_los_off_soft||100|ms|Note 13|
|Software RATE_SELECT Assert Time|t_rate_soft_high||5|ms|Note 14|
|Software RATE_SELECT DeAssert Time|t_rate_soft_low||5|ms|Note 15|
|Analog parameter data ready|t_data||1000|ms|Note 16|
|Serial bus hardware ready|t_serial||300|ms|Note 17|
|Serial bus bufer time|t_buf|20||µs|Note 18|
|Complete Single or Sequential Write up to 4 Byte|twR||40|ms|Note 19|
|Complete Sequential Write of  5-8 Byte|twR||80|ms|Note 19|
|Serial Interface Clock Holdof “Clock Stretching”|T_clock_hold||500|µs|Note 20|
|Serial ID Clock Rate|f_serial_clock||400|kHz|Note 21|



## Notes 

1. Time from rising edge of TX_DISABLE to when the optical output falls below 10% of nominal. 

2. Time from falling edge of TX_DISABLE to when the modulated optical output rises above 90% of nominal. 

3. Time from power on or falling edge of Tx_Disable to when the modulated optical output rises above 90% of nominal. 

4. From power on or negation of TX_FAULT using TX_DISABLE. 

5. Time TX_DISABLE must be held high to reset the laser fault shutdown circuitry. 

6. Time from loss of optical signal to Rx_LOS Assertion. 

7. Time from valid optical signal to Rx_LOS De-Assertion. 

8. Time from rising or falling edge of Rate_Select input until transceiver is successfully passing traffic as designated by RS(0) and RS(1). For Rate_Se-lect going high, the internal CDR will lock on valid 32GFC encoded data within the specified time. For Rate_Select going low, the internal CDR will attempt to lock on valid 16GFC encoded data for a certain gating period. If valid 16GFC data is not detected in that gating period, the inter-nal CDR will automatically be bypassed for use at 8GFC rates. 

9. Time from two-wire interface assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output falls below 10% of nominal. Measured from falling clock edge after stop bit of write transaction. 

10. Time from two-wire interface de-assertion of TX_DISABLE (A2h, byte 110, bit 6) to when the optical output rises above 90% of nominal. 

11. Time from fault to two-wire interface TX_FAULT (A2h, byte 110, bit 2) asserted. 

12. Time for two-wire interface assertion of Rx_LOS (A2h, byte 110, bit 1) from loss of optical signal. 

13. Time for two-wire interface de-assertion of Rx_LOS (A2h, byte 110, bit 1) from presence of valid optical signal. 

14. Time from two-wire interface Assertion of Rate_Select (either RS(0) in A2h, byte 110, bit 3 or RS(1) in A2h, byte 118, bit 3) to when the respective CDR is engaged at 32GCFC data rate. 

15. Time from two-wire interface De-Assertion of Rate_Select (either RS(0) in A2h, byte 110, bit 3 or RS(1) in A2h, byte 118, bit 3) to when the respective CDR is either engaged at 16GCFC data rate or bypassed for 8GFC operation. 

16. From power on  to data ready bit asserted (A2h, byte 110, bit 0). Data ready indicates analog monitoring circuitry is functional. 

17. Time from power on until module is ready for data transmission over the serial bus (reads or writes over A0h and A2h). 

18. Time between START and STOP commands. 

19. Time from stop bit to completion of a write command. 

20. Maximum time the SFP+ module may hold the SCL line low before continuing with a read or write operation. 21. With a maximum Clock Stretch of 500us. A maximum of 100kHz operation can be supported without a Clock Stretch. 

**Avago Technologies Proprietary** 

10 

**Table 11. Transceiver Digital Diagnostic Monitor (Real Time Sense) Characteristics** 

(TC  =  0°C to 70°C,   VccT, VccR = 3.3V ± 10%) 

|**Parameter**|**Symbol**|**Min.**|**Units**|**Notes**|
|---|---|---|---|---|
|Transceiver Internal|TINT|±3.0|°C|Temperature is measured internal to the transceiver.|
|Temperature Accuracy||||Valid from =  0°C to 70 °C case temperature.|
|Transceiver Internal Supply|VINT|±0.1|V|Supply voltage is measured internal to the transceiver and|
|Voltage Accuracy||||can, with less accuracy, be correlated to voltage at the SFP|
|||||Vccpin. Valid over 3.3 V±5%.|
|Transmitter Laser DC Bias|IINT|±10|%|IINTis better than±10% of the nominal value.|
|Current Accuracy|||||
|Transmitted Average Optical|PT|±3.0|dB|Coupled into 50um multi-mode fber.|
|Output Power Accuracy||||Valid from 100µW to 900µW, avg.|
|Received Optical Input Power|PR|±3.0|dB|Coupled from 50um multi-mode fber.|
|Accuracy||||Valid from 50µW to 900µW avg.|




**----- Start of picture text -----**<br>
VCC T,R > 2.97 V VCC T,R > 2.97 V<br>TX_FAULT TX_FAULT<br>TX_DISABLE TX_DISABLE<br>TRANSMITTED SIGNAL TRANSMITTED SIGNAL<br>t_init t_init<br>t-init: TX DISABLE NEGATED t-init: TX DISABLE ASSERTED<br>VCC T,R > 2.97 V TX_FAULT<br>TX_FAULT TX_DISABLE<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>TRANSMITTED SIGNAL<br>t_off t_on<br>t_init<br>INSERTION<br>t-init: TX DISABLE NEGATED, MODULE HOT PLUGGED  t-off & t-on: TX DISABLE ASSERTED THEN NEGATED<br>OCCURANCE OF FAULT<br>OCCURANCE OF FAULT<br>TX_FAULT<br>TX_FAULT<br>TX_DISABLE<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>TRANSMITTED SIGNAL<br>t_fault * SFP SHALL CLEAR TX_FAULT IN t_reset t_init*<br>< t_init IF THE FAILURE IS TRANSIENT<br>t-fault: TX FAULT ASSERTED, TX SIGNAL NOT RECOVERED t-reset: TX DISABLE ASSERTED THEN NEGATED, TX SIGNAL RECOVERED<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
OCCURANCE OF FAULT<br>TX_FAULT<br>TX_DISABLE<br>TRANSMITTED SIGNAL<br>t_fault<br>t_reset<br>* SFP SHALL CLEAR TX_FAULT IN t_init*<br><  t_init IF THE FAILURE IS TRANSIENT<br>t-fault: TX DISABLE ASSERTED THEN NEGATED, TX SIGNAL NOT RECOVERED<br>**----- End of picture text -----**<br>



**----- Start of picture text -----**<br>
OCCURANCE<br>OPTICAL SIGNAL OF LOSS<br>LOS<br>t_los_on t_los_off<br>**----- End of picture text -----**<br>



**Figure 4. Transceiver timing diagrams (module installed except where noted)** 

**Avago Technologies Proprietary** 

11 

**Table 12. EEPROM Serial ID Memory Contents – Address A0h** 

|**Byte #**|||**Byte #**|||
|---|---|---|---|---|---|
|**Decimal **|**Hex**|**Description**|**Decimal**|**Hex**|**Description**|
|0|03|SFPphysical device|38|17|Hex Byte of Vendor OUI[4]|
|1|04|SFP function defned byserial ID only|39|6A|Hex Byte of Vendor OUI[4]|
|2|07|LC optical connector|40|41|“A”  -  Vendor Name ASCII Character|
|3|00||41|46|“F”  -  Vendor Name ASCII Character|
|4|00||42|43|“C”  -  Vendor Name ASCII Character|
|5|00||43|54|“T”  -  Vendor Name ASCII Character|
|6|00||44|2D|“-”  -  Vendor Name ASCII Character|
|7|12|Longdistance(per FC-PI-6),Longwave Laser(LC)|45|35|“5”  -  Vendor Name ASCII Character|
|8|00||46|37|“7”  -  Vendor Name ASCII Character|
|9|01|Single-mode optical media|47|47|"G”  -  Vendor Name ASCII Character|
|10|68|800,1600 & 3200 MBytes/sec FC-PI-6 speed[1]|48|35|“5”  -  Vendor Name ASCII Character|
|11|06|64B/66B data at 32GFC/16GFC & 8B/10B at 8GFC|49|4D|“M”  -  Vendor Name ASCII Character|
|12|FF|Greater than 25.5Gb/s(See Address 66/67)|50|5A|“Z”  -  Vendor Name ASCII Character|
|13|0C|Rate Select(High=32GFC,Low=16GFC,8GFC)|51|20|“ ”  -  Vendor Name ASCII Character|
|14|0A|10km of single mode fber|52|20|“ ”  -  Vendor Name ASCII Character|
|15|64|10km of single mode fber|53|20|“ ”  -  Vendor Name ASCII Character|
|16|00||54|20|“ ”  -  Vendor Name ASCII Character|
|17|00||55|20|“ ”  -  Vendor Name ASCII Character|
|18|00||56|20|“ ”  -  Vendor Name ASCII Character|
|19|00||57|20|“ ”  -  Vendor Name ASCII Character|
|20|41|“A”  -  Vendor Name ASCII Character|58|20|“ ”  -  Vendor Name ASCII Character|
|21|56|“V”  -  Vendor Name ASCII Character|59|20|“ ”  -  Vendor Name ASCII Character|
|22|41|“A”  -  Vendor Name ASCII Character|60|03|Hex Byte of Laser Wavelength[5]|
|23|47|“G”  -  Vendor Name ASCII Character|61|52|Hex Byte of Laser Wavelength[5]|
|24|4F|“O”  -  Vendor Name ASCII Character|62|00||
|25|20|“ ”  -  Vendor Name ASCII Character|63||Checksum for Bytes 0-62[6]|
|26|20|“ ”  -  Vendor Name ASCII Character|64|08|CDRspresent.  1Wpower class|
|27|20|“ ”  -  Vendor Name ASCII Character|65|3A|Hardware Tx_Disable, Tx_Fault, Rx_LOS,|
||||||Rate_Select|
|28|20|“ ”  -  Vendor Name ASCII Character|66|70|28.050 Mbit/sec nominal bit rate(32GFC)|
|29|20|“ ”  -  Vendor Name ASCII Character|67|00||
|30|20|“ ”  -  Vendor Name ASCII Character|68 - 83||Vendor Serial Number ASCII characters[7]|
|31|20|“ ”  -  Vendor Name ASCII Character|84 - 91||Vendor Date Code ASCII characters[8]|
|32|20|“ ”  -  Vendor Name ASCII Character|92|68|Digital diagnostics,Internal Cal,Rx Pwr Avg|
|33|20|“ ”  -  Vendor Name ASCII Character|93|FA|Alarms/Warnings, Software Tx_Disable,|
||||||Tx-Fault,Rx_LOS,Rate_Select|
|34|20|“ ”  -  Vendor Name ASCII Character|94|08|SFF-8472 compliance to revision 12.2|
|35|20|“ ”  -  Vendor Name ASCII Character|95||Checksum for Bytes 62-94[6]|
|36|00||96 – 255|00||
|37|00|Hex Byte of Vendor OUI[4]||||



Notes: 

1. FC-PI-6 speed 3200 MBytes/sec is a serial bit rate of 28.05Gb/s using FEC encoded data (RS 528/514). FC-PI-5 speed 1600 MBytes/sec is a serial bit rate of 14.025Gb/s. 800 MBytes/sec is a serial bit rate of 8.5Gb/s. 

2. Link distance with OM2 50/125um cable at 16GFC is 35m and at 8GFC is 50m. 

3. Link distance with OM1 62.5/125um cable at 8.5Gb/s is 25m (and is unspecified at 16GFC). 

4. The IEEE Organizationally Unique Identified (OUI) assigned to Avago Technologies is 00-17-6A (3 bytes of hex). 

5. Laser Wavelength is represented in 16 unsigned buts. The hex representation of 850nm is 0352. 

6. Addresses 63 and 95 are checksums calculated (per SFF-8472 and SFF-8074) and stored prior to product shipment. 

7. Address 68-83 specify the AFCT-57G5MZ ASCII serial number and will vary on a per unit basis. 

8. Address 84-91 specify the AFCT-57G5MZ ASCII data code and will vary on a per date code basis. 

9. Link distance with OM3 50/125um cable at 16GFC is 100m and at 8GFC is 150m.. 

10. Link distance with OM4 50/125um cable at 16GFC is 125m and at 8GFC is 190m. 

**Avago Technologies Proprietary** 

12 

**Table 13. EEPROM Serial ID Memory Contents - Enhanced SFP Memory (Address A2h)** 

|**Byte #**||**Byte #**||**Byte #**||
|---|---|---|---|---|---|
|**Decimal**|**Notes**|**Decimal**|**Notes**|**Decimal**|**Notes**|
|0|TempH Alarm MSB[1]|26|Tx Power L Alarm MSB[4]|104|Real Time Rx Power MSB[5]|
|1|TempH Alarm LSB[1]|27|Tx Power L Alarm LSB[4]|105|Real Time Rx Power LSB[5]|
|2|TempL Alarm MSB[1]|28|Tx Power H WarningMSB[4]|106|Reserved|
|3|TempL Alarm LSB[1]|29|Tx Power H WarningLSB[4]|107|Reserved|
|4|TempH WarningMSB[1]|30|Tx Power L WarningMSB[4]|108|Reserved|
|5|TempH WarningLSB[1]|31|Tx Power L WarningLSB[4]|109|Reserved|
|6|TempL WarningMSB[1]|32|Rx Power H Alarm MSB[5]|110|Status/Control – See Table 14|
|7|TempL WarningLSB[1]|33|Rx Power H Alarm LSB[5]|111|Status/Control – See Table 15|
|8|Vcc H Alarm MSB[2]|34|Rx Power L Alarm MSB[5]|112|FlagBits – See Table 16|
|9|Vcc H Alarm LSB[2]|35|Rx Power L Alarm LSB[5]|113|FlagBits – See Table 16|
|10|Vcc L Alarm MSB[2]|36|Rx Power H WarningMSB[5]|114|Tx Input EQControl|
|11|Vcc L Alarm LSB[2]|37|Rx Power H WarningLSB[5]|115|Rx Output Emphasis Control|
|12|Vcc H WarningMSB[2]|38|Rx Power L WarningMSB[5]|116|FlagBits – See Table 16|
|13|Vcc H WarningLSB[2]|39|Rx Power L WarningLSB[5]|117|FlagBits – See Table 16|
|14|Vcc L WarningMSB[2]|40-55|Control Settings – See Table 18|118|Status/Control – See Table 17|
|15|Vcc L WarningLSB[2]|56-94|External Calibration Constants[6]|119|CDR Loss of Lock Status|
|16|Tx Bias H Alarm MSB[3]|95|Checksum for Bytes 0-94[7]|120-127|Reserved|
|17|Tx Bias H Alarm LSB[3]|96|Real Time Temperature MSB[1]|128|Page Select Control|
|18|Tx Bias L Alarm MSB[3]|97|Real Time Temperature LSB[1]|129-247|Customer Writable|
|19|Tx Bias L Alarm LSB[3]|98|Real Time Vcc MSB[2]|248-255|Vendor Specifc|
|20|Tx Bias H WarningMSB[3]|99|Real Time Vcc LSB[2]|||
|21|Tx Bias H WarningLSB[3]|100|Real Time Tx Bias MSB[3]|||
|22|Tx Bias L WarningMSB[3]|101|Real Time Tx Bias LSB[3]|||
|23|Tx Bias L WarningLSB[3]|102|Real Time Tx Power MSB[4]|||
|24|Tx Power H Alarm MSB[4]|103|Real Time Tx Power LSB[4]|||
|25|Tx Power H Alarm LSB[4]|||||



Notes: 

1. Temperature (Temp) is decoded as a 16 bit signed two’s complement integer in increments of 1/256 °C. 

2. Supply Voltage (Vcc) is decoded as a 16 bit unsigned integer in increments of 100 µ V. 

3. Tx bias current (Tx Bias) is decoded as a 16 bit unsigned integer in increments of 2 µ A. 

4. Transmitted average optical power (Tx Pwr) is decoded as a 16 bit unsigned integer in increments of 0.1 µ W. 

5. Received average optical power (Rx Pwr) is decoded as a 16 bit unsigned integer in increments of 0.1 µ W. 

6. Bytes 56-94 are not intended for use, but have been set to default values per SFF-8472. 

7. Byte 95 is a checksum calculated (per SFF-8472) and stored prior to product shipment. 

**Avago Technologies Proprietary** 

13 

**Table 14. EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 110).** 

|**Bit #**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7|TX_DISABLE State|Digital state of TX_DISABLE Input Pin (1 = TX_DISABLE asserted)|Note 1|
|6|Soft TX_DISABLE Control|Read/write bit for changingdigital state of TX_DISABLE function|Note 1, 2|
|5|RS(1) State|Digital state of TX Rate_Select Input Pin RS(1)  (1 = Rate High asserted)||
|4|RS(0) State|Digital state of RX Rate_Select Input Pin RS(0)  (1 = Rate High asserted)||
|3|Soft RS(0) Control|Read/write bit for changingdigital state of Rx Rate_Select RS(0) function|Note 3|
|2|TX_FAULT State|Digital state of TX_FAULT Output Pin (1 = TX_FAULT asserted)|Note 1|
|1|RX_LOS State|Digital state of SFP RX_LOS Output Pin (1 = RX_LOS asserted)|Note 1|
|0|Data Ready(Bar)|Indicates transceiver ispowered and real time sense data is ready(0 = Data Ready)||



Notes: 

1. The response time for soft commands of the AFCT-57G5MZ is 100msec as specified by MSA SFF-8472. 

2. Bit 6 is log OR’d with the SFP TX_DISABLE input pin 3 …. either asserted will disable the SFP transmitter. 

3. Bit 3 is log OR’d with the SFP RS(0) RX Rate_Select input pin 7 …. either asserted will set receiver to Rate = High. 

**Table 15. EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 111).** 

|**Bit #**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|4-7|Reserved|||
|3|OWRAP FORWARD|Logic Low = FORWARD disabled. Logic High = FORWARD enabled. When used in||
||Control Bit|combination with OWRAP enable, FORWARD routes incoming SFP Rx optical data||
|||to both the Tx optical output and the Rx electrical output. Enabling sets bit 2 and||
|||clears all other bits in byte 111.||
|2|OWRAP Control Bit|Logic Low = OWRAP disabled. Logic High = OWRAP enabled. When enabled, OW-||
|||RAP routes incoming SFP Rx optical data to the Tx optical output. Enabling clears||
|||all other bits in byte 111.||
|1|EWRAP FORWARD|Logic Low = FORWARD disabled. Logic High = FORWARD enabled. When used in||
||Control Bit|combination with EWRAP enable, FORWARD routes incoming SFP Tx electrical||
|||data to both Rx electrical output and Tx optical output. Enabling sets bit 0 and||
|||clears all other bits in byte 111.||
|0|EWRAP Control Bit|Logic Low = EWRAP disabled. Logic High = EWRAP enabled. When enabled,||
|||EWRAP routes incoming SFP Tx electrical data to the Rx electrical output. Enabling||
|||clears all other bits in byte 111.||



**Avago Technologies Proprietary** 

14 

**Table 16. EEPROM Serial ID Memory Contents – Alarms and Warnings (Address A2h, Bytes 112, 113, 116, 117)** 

|**Byte**|**Bit**<br>**Flag Bit Name**<br>**Description**|
|---|---|
|112|7<br>TempHigh Alarm<br>Set when transceiver internal temperature exceeds high alarm threshold.|
||6<br>TempLow Alarm<br>Set when transceiver internal temperature exceeds low alarm threshold.|
||5<br>Vcc High Alarm<br>Set when transceiver internal supplyvoltage exceeds high alarm threshold.|
||4<br>Vcc Low Alarm<br>Set when transceiver internal supplyvoltage exceeds low alarm threshold.|
||3<br>Tx Bias High Alarm<br>Set when transceiver laser bias current exceeds high alarm threshold.|
||2<br>Tx Bias Low Alarm<br>Set when transceiver laser bias current exceeds low alarm threshold.|
||1<br>Tx Power High Alarm<br>Set when transmitted average opticalpower exceeds high alarm threshold.|
||0<br>Tx Power Low Alarm<br>Set when transmitted average opticalpower exceeds low alarm threshold.|
|113|7<br>Rx Power High Alarm<br>Set when received average opticalpower exceeds high alarm threshold.|
||6<br>Rx Power Low Alarm<br>Set when received average opticalpower exceeds low alarm threshold.|
||0-5<br>reserved|
|116|7<br>TempHigh Warning<br>Set when transceiver internal temperature exceeds high warningthreshold.|
||6<br>TempLow Warning<br>Set when transceiver internal temperature exceeds low warningthreshold.|
||5<br>Vcc High Warning<br>Set when transceiver internal supplyvoltage exceeds high warningthreshold.|
||4<br>Vcc Low Warning<br>Set when transceiver internal supplyvoltage exceeds low warningthreshold.|
||3<br>Tx Bias High Warning<br>Set when transceiver laser bias current exceeds high warningthreshold.|
||2<br>Tx Bias Low Warning<br>Set when transceiver laser bias current exceeds low warningthreshold.|
||1<br>Tx Power High Warning<br>Set when transmitted average opticalpower exceeds high warningthreshold.|
||0<br>Tx Power Low Warning<br>Set when transmitted average opticalpower exceeds low warningthreshold.|
|117|7<br>Rx Power High Warning<br>Set when received average opticalpower exceeds high warningthreshold.|
||6<br>Rx Power Low Warning<br>Set when received average opticalpower exceeds low warningthreshold.|
||0-5<br>reserved|



**Table 17. EEPROM Serial ID Memory Contents – Soft Commands (Address A2h, Byte 118).** 

|**Bit #**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|4-7|Reserved|||
|3|Soft RS(1) Control|Read/write bit for changingdigital state of Tx Rate_Select RS(1) function|Note 1|
|2|Reserved|||
|1|Power Level State|Always set to zero. Value of zero indicates Power Level 1 operation (1 Watt max)||
|0|Power Level Select|Unused. This device supportspower level zero (1 Watt max) only.||



Notes: 

1. Bit 3 is log OR’d with the SFP RS(1) TX Rate_Select input pin 9 …. either asserted will set transmitter to Rate = High. 

**Table 18. EEPROM Serial ID Memory Contents – CDR Loss of Lock (LOL) Status Indicators (Address A2h, Byte 119).** 

|**Bit #**|**Status/Control Name**|**Description**|**Notes**|
|---|---|---|---|
|7-2|Reserved|||
|1|Tx CDR LOL Flag|A value of 0 indicates the CDR is locked. A value of 1 indicates CDR loss of lock. If||
|||the CDR is operationallybypassed (ie. for 8.5Gb/s operation), a value of 0 is shown.||
|0|Rx CDR LOL Flag|A value of 0 indicates the CDR is locked. A value of 1 indicates CDR loss of lock. If||
|||the CDR is operationallybypassed (ie. for 8.5Gb/s operation), a value of 0 is shown.||



**Avago Technologies Proprietary** 

15 

**Table 19. EEPROM Serial ID Memory Contents – Transmitter Input Electrical Equalization Control (Address A2h, Byte 114).** 

|**Bit #**|**Status/Control Name**|**Description**|
|---|---|---|
|7-4|TX EQ, RS(1)=HIGH|Selects an input equalization valueper Table 9-13 of SFF-8472 for high rate operation.|
|3-0|TX EQ, RS(1)=LOW|Selects an input equalization valueper Table 9-13 of SFF-8472 for low rate operation.|



## **Table 20. Transmitter Input Equalization Control Values (Address A2h, Byte 114)** 

From Table 9-13 of SFF-8472 

|**Code**|**Transmitter Input Equalization**|
|---|---|
||**Nominal**<br>**Units**|
|11xx|Reserved|
|1011|Reserved|
|1010|10<br>dB|
|1001|9<br>dB|
|1000|8<br>dB|
|0111|7<br>dB|
|0110|6<br>dB|
|0101|5<br>dB|
|0100|4<br>dB|
|0011|3<br>dB|
|0010|2<br>dB|
|0001|1<br>dB|
|0000|0<br>No Equalization|



**Table 21. EEPROM Serial ID Memory Contents – Receiver Output Electrical Emphasis Control (Address A2h, Byte 115).** 

|**Bit #**|**Status/Control Name**|**Description**|
|---|---|---|
|7-4|RX EMPH, RS(0)=HIGH|Selects an output emphasis valueper Table 9-14 of SFF-8472 for high rate operation.|
|3-0|RX EMPH, RS(0)=LOW|Selects an output emphasis valueper Table 9-14 of SFF-8472 for low rate operation.|



## **Table 22. Receiver Output Emphasis Control Values (Address A2h, Byte 115)** 

From Table 9-14 of SFF-8472 

|**Code**|**Receiver Output Emphasis**<br>**At nominal Output Amplitude**|
|---|---|
||**Nominal**<br>**Units**|
|1xxx|Vendor Specifc|
|0111|7<br>dB|
|0110|6<br>dB|
|0101|5<br>dB|
|0100|4<br>dB|
|0011|3<br>dB|
|0010|2<br>dB|
|0001|1<br>dB|
|0000|0<br>No Emphasis|



**Avago Technologies Proprietary** 

16 


**Figure 5.  Module drawing** 


**Figure 6. Module Label** 

**Avago Technologies Proprietary** 

17 


**----- Start of picture text -----**<br>
X<br>Y<br>34.5<br>10<br>3x<br>10x 1.05 ± 0.01 7.2 7.1<br>16.25 ∅ 0.1 L X A S 2.5 0.85 ± 0.05<br>MIN. PITCH 1 ∅ 0.1 S X Y<br>2.5<br>PCB B A 1<br>EDGE 3.68<br>5.68 PIN 1 20<br>8.58 2x 1.7 8.48<br>11.08 11.93<br>16.25<br>14.25 9.6<br>REF .<br>4.8<br>11<br>10<br>SEE DETAIL 1<br>2.0 9x 0.95 ± 0.05<br>11x 11x 2.0 ∅ 0.1 L X A S<br>26.8 5 2<br>3 10<br>3x<br>41.3<br>42.3<br>5<br>3.2<br>20x 0.5 ± 0.03<br>0.9<br>0.06 L A S B S<br>LEGEND<br>PIN 1 20 1. PADS AND VIAS ARE CHASSIS GROUND<br>10.93 10.53 2. THROUGH HOLES, PLATING OPTIONAL<br>11.93<br>9.6 3. HATCHED AREA DENOTES COMPONENT<br>0.8<br>AND TRACE KEEPOUT (EXCEPT<br>TYP .<br>11 CHASSIS GROUND)<br>10 4. AREA DENOTES COMPONENT<br>KEEPOUT (TRACES ALLOWED)<br>DIMENSIONS ARE IN MILLIMETERS<br>4<br>2 ± 0.005 TYP.<br>2x 1.55 ± 0.05<br>0.06 L A S B S<br>∅ 0.1 L A S B S<br>DETAIL 1<br>**----- End of picture text -----**<br>


**Figure 7.  SFP host board mechanical layout** 

**Avago Technologies Proprietary** 

18 


**----- Start of picture text -----**<br>
1.7 ± 0.9<br>3.5 ± 0.3<br>42.08 ± 0.5<br>15 MAX.<br>9.8 MAX.<br>16.25 ± 0.1<br>10<br>15.25 ± 0.1<br>**----- End of picture text -----**<br>


**Figure 8.  SFP Assembly drawing** 

## **Customer Manufacturing Processes** 

This module is pluggable and is not designed for aqueous wash, IR reflow, or wave soldering processes. 

For product information and a complete list of distributors, please go to our website: **www.avagotech.com** 

Avago Technologies, and the A logo are trademarks of Avago Technologies in the United States and other countries. Data subject to change. Copyright © 2016 Avago Technologies. All rights reserved. pub-005394  -  December 5, 2017 

**Avago Technologies Proprietary** 

