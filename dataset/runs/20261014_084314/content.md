
# 100G QSFP28 High-TX ZR Data 

100G QSFP28 High-TX ZR Data Sheet 

## **Applications** 

- 

- 

- 

- Access and aggregation networks 

- Cable TV networks 

- Wireless mid-haul & back-haul 

## **Features** 

- Digital Coherent Optics module, hot-pluggable QSFP28 form factor with extended front section outside the cage (cf. QSFP-DD form factor Type 2) 

- 

- 

- 

- 

- 

- 

- 

- IEEE 100G Ethernet (CAUI-4) or ITU-T 100G OTN (OTL4.4) compliant host interface 

- 100G optical coherent interface with DP-DQPSK modulation and Staircase FEC per IEEE Std. 802.3-2022 100GBASE-ZR or ITU-T G.709.2 

- High Tx output power > 0dBm for compatibility with ROADM line systems 

- Full C-band tunable, 50GHz or 100GHz grid with optional Flextune™ automatic wavelength tuning 

- Case temperature range 0°C to 70°C (C-temp) 

- Typical power dissipation < 6.0W 

- Remote digital diagnostics monitoring 

## **Description** 

The 100G ZR QSFP28 High-Power DCO transceiver supports 100G transmission over distances up to 120km (dispersion limited, optionally extendable to 300km) for edge network applications. On the host side, the module can accommodate IEEE 100GE Ethernet or ITU-T OTN OTU4 signals. The line side coherent interface specifications are aligned with IEEE Std. 802.3-2022 100GBASE-ZR. 

## **Product Specifications** 

## **I. Environmental Specifications** 

|**Parameter**|**Parameter**|**Conditions**|**Conditions**|**Conditions**|**Symbol**|**Symbol**|**Min**|**Typ**|**Typ**|**Max**|**Unit**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Storage temperature|||||T_S||-40|||85|°C|||
|Case operating<br>temperature||Central office<br>appl.<br>(C-temp)|Long term||TOP||0|||70|°C|||
||||Short term <<br>96h||||-5|||75||||
|Relative humidity||Non-condensing|||RH||5|||85|%|||
|**II. Interface Modes**<br>**Host Interface Modes**<br>•||||||||||||||
|**Host Interface ID**<br>[18]|**Host Interface**<br>**Description**[18]|||**Modulation**||**Forward Error**<br>**Correction Code**|||**Nominal Symbol**<br>**Rate (GBd)**|||**Supported Line**<br>**Interface IDs**[18]||
|QSFP-ZRH-100G and QSFP-ZRH-100G-S||||||||||||||
|65 [9]|CAUI-4 C2M without<br>FEC|||NRZ||None|||25.78125|||68, 192, 193||
|66 [9]|CAUI-4 C2M with<br>RS(528,514) FEC|||NRZ||RS(528,514)|||25.78125|||68, 192, 193||
|||||||||||||||



Copyright © 2026 FS.COM AII Rights Reserved 

Page 2 of 11 

100G QSFP28 High-TX ZR Data Sheet 

||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|QSFP-ZRH-100G-S only|||||||||||||
|57 [10]|OTL4.4 (ITU-T<br>G.709/ Y.1331<br>G.Sup58)||NRZ||RS(255,239)|||27.9525|||192, 193||
|**Line Interface Modes**<br>•|||||||||||||
|**Line Interface ID**<br>[18]|**Line Interface**<br>**Description**[18]||**Modulation**||**Forward Error**<br>**Correction Code**|||**Nominal Symbol**<br>**Rate (GBd)**|||**Spectral Shaping**||
|QSFP-ZRH-100G and QSFP-ZRH-100G-S|||||||||||||
|68 [9]|100GBASE-ZR<br>(Clause<br>154)||DP-DQPSK||Staircase (SC)|||27.9525|||None||
|QSFP-ZRH-100G-S only|||||||||||||
|192 [11]|OTU4 Long Reach||DP-DQPSK||Staircase (SC)|||27.9525|||None||
|193 [10]|OTU4 Short Reach||DP-DQPSK||RS(255,239)|||27.9525|||None||
|**III. Electrical Characteristics**<br>**Power & Low Speed I/O**<br>•|||||||||||||
|**Parameter**||**Conditions**||**Symbol**||**Min**|**Typ**||**Max**|**Unit**||**Notes**|
|**Power supply - General**|||||||||||||
|Power supply voltages||Including ripple, droop<br>and noise below<br>100kHz||||3.135|3.300||3.465|V|||
|Host RMS noise output||10Hz - 10MHz|||||||25|mV|||
|Module RMS noise output||10Hz - 10MHz|||||||15|mV|||
|Module supply noise<br>tolerance||10Hz - 10MHz, peak-to-<br>peak||PSNRmod|||||66|mV|||
|Module inrush||Instantaneous peak<br>duration||Tip|||||50|µs|||
|||Initialization time||Tinit|||||500|ms|||
|**Power supply - Low power mode**|||||||||||||
|Power dissipation||||Plp|||||1.5|W|||
|Power supply current||Instantaneous peak<br>current||ICC,ip,lp|||||600|mA|||
|||Sustained peak current||ICC,sp,lp|||||495||||
|||Steady state current||ICC,lp|||||478|||1|
|**Power supply - High power mode (with 2.4 ns/nm CD)**|||||||||||||
|Power dissipation||||Php|||5.5||6.2|W|||
||||||||||||||



Copyright © 2026 FS.COM AII Rights Reserved 

Page 3 of 11 

100G QSFP28 High-TX ZR Data Sheet 

|Power supply current|Power supply current|||||||||
|---|---|---|---|---|---|---|---|---|---|
||Power supply current|Instantaneous peak<br>current|ICC,ip,hp|||2480|mA|||
|||Sustained peak current|ICC,sp,hp|||2046||||
|||Steady state current|ICC,hp|||1978||1||
||**Power supply - High power mode (with 6.0 ns/nm CD)**|||||||||
||Power dissipation||Php||5.7|6.5|W|||
||Power supply current|Instantaneous peak<br>current|ICC,ip,hp|||2600|mA|||
|||Sustained peak current|ICC,sp,hp|||2145||||
|||Steady state current|ICC,hp|||2073||1||
||**Low speed I/O**|||||||||
||Clock frequency, SCL|Default|fSCL|400|||kHz|||
|||Fast mode+||1000||||||
||Output voltage, SCL and<br>SDA|Output low|VOL|0.0||0.4|V|||
|||Output high|VOH|VCC-0.5||VCC+0.3||||
||Input voltage, SCL and<br>SDA|Input low|VIL|-0.3||0.3×VCC|V|||
|||Input high|VIH|0.7×VCC||VCC+0.5||||
||Capacitance for SCL and<br>SDA I/O signal||C_i|||14|pF|||
||Total bus capacitive load<br>for SCL and SDA|400kHz clock rate|3.0kΩ pull-<br>up<br>resistor,<br>max.|Cb||100|pF|2||
||||1.6kΩ pull-<br>up<br>resistor,<br>max.|||200||||
||Input voltage / current,<br>LPMode/TxDis, ResetL and<br>ModSelL|Input voltage, low|VIL|-0.3||0.8|V|||
|||Input voltage, high|VIH|2.0||VCC+0.3||||
|||Input current, 0V < Vin<br>< VCC|Iin|-365||125|µA|||
|Output voltage, ModPrsL<br>and IntL/RxLOSL|Output voltage, ModPrsL<br>and IntL/RxLOSL|Output low, IOL= 2mA|VOL|0.0||0.4|V|||
|||Output high, 10kΩ pull-<br>up resistor to host VCC|VOH|VCC-0.5||VCC+0.3||||
|||||||||||



> **Notes:** The module will stay within its advertised power class for all supply voltages. For 1000kHz clock rate, refer to Figure 6-4 in [2] 

## **IV. Optical Characteristics** 

• **General** 

Copyright © 2026 FS.COM AII Rights Reserved 

Page 4 of 11 

100G QSFP28 High-TX ZR Data Sheet 

|**Parameter**|**Conditions**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|
|Symbol rate||Rbaud||27.95||GBd||
|Modulation format|||DP-DQPSK|||||
|Channel frequency<br>range|100GHz grid|V_C|191.400|193.700|196.100|THz||
||50GHz grid||191.350|193.700|196.100|||
|Channel spacing|100GHz grid|∆V_C||100||GHz||
||50GHz grid|||50||||
|Frequency accuracy||δV_C|-1.8||1.8|GHz||
|Side-mode<br>suppression ratio|No modulation|SMSR|40|||dB||
|||||||||



## • **Transmitter** 

|**Parameter**|**Conditions**|**Conditions**|**Symbol**|**Symbol**|**Min**|**Min**|**Typ**|**Typ**|**Max**|**Max**|**Unit**|**Unit**|**Notes**|**Notes**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tx output power|||PTx,out||0||||||dBm||||
|Tx output power<br>monitor range|||PTx,mon||-2||||4||dBm||||
|Tx output power<br>monitor accuracy|Tx optical power<br>monitor reading<br>relative to actual Tx<br>output power||δPTx,mon||-1.5||||1.5||dB||||
|Tx output power during<br>tuning or when Tx<br>disabled|||PTx,dark||||||-35||dBm||||
|Tx in-band optical<br>signal to noise ratio|Under modulation, |Δf|<br>< 60 GHz||OSNRin||39||||||dB/12.5GH<br>z||||
|Tx out-of-band optical<br>signal to noise ratio|Under modulation, |Δf|<br>> 150 GHz||OSNRout||30||||||dB/12.5GH<br>z||||
|**Receiver**<br>•|||||||||||||||
|**Parameter**|**Conditions**|||**Symbol**||**Min**||**Typ**||**Max**||**Unit**||**Notes**|
|Rx total input power|Broadband|||PRx,tot||-30||||3||dBm|||
|Rx signal input power<br>(amplified)|Full Rx OSNR tolerance|||PRx,sig||-18||||1||dBm|||
||Extended range|||||-22||||3||||1|
|Rx OSNR tolerance|Back-to-back,<br>PRx,sig> -<br>18dBm|100G<br>DQPSK SC||||16.5||||||dB/12.5G<br>Hz||2|
|||100G<br>DQPSK RS||||21.5|||||||||
|CD tolerance|Default, OSNR penalty < 0.5dB|||||||||2.4||ns/nm|||
||Extended, OSNR penalty <<br>1.0dB|||||||||6.0||||3|
||||||||||||||||



Copyright © 2026 FS.COM AII Rights Reserved 

Page 5 of 11 

100G QSFP28 High-TX ZR Data Sheet 

|PMD tolerance|PMD tolerance||||||||||
|---|---|---|---|---|---|---|---|---|---|---|
||PMD tolerance|OSNR penalty < 0.5dB|||||10|ps|||
||DGD tolerance|OSNR penalty < 0.5dB|||||30|ps|||
||Tolerance to change in<br>SOP|OSNR penalty < 0.5dB|||||50|krad/s|||
||PDL OSNR penalty|Change in<br>principal state<br>of polarization<br>< 1rad/ms|1dB PDL||||0.5|dB/12.5G<br>Hz|||
||||2dB PDL||||1.0||||
||||4dB PDL||||3.0||||
||Rx signal input power<br>transient amplitude|Peak excursion from steady<br>state, transient within Rx signal<br>input power (amplified) range,<br>OSNR penalty < 0.5dB|||-3||3|dB|||
||Rx signal input power<br>transient rise/fall time|Rise/fall time for the above<br>peak excursion, OSNR penalty<br>< 0.5dB|||100|||µs|||
||Colorless drop OSNR<br>penalty|Rx total input power to signal<br>input power ratio < 12dB|||||0.5|dB|4||
||Colorless drop adjacent<br>channel crosstalk<br>penalty||||||0.2|dB|5||
||Rx signal input power<br>(unamplified)|OSNR ><br>35dB/12.5GHz|100G<br>DQPSK SC||-30||1|dBm|||
||||100G<br>DQPSK RS||-24||1||||
||Rx signal input power<br>monitor range|||PRx,mon(s)|-21||3|dBm|||
||Rx signal input power<br>monitor accuracy|||δPRx,mon(s<br>)|-2.5||2.5|dB|||
||Rx total input power<br>monitor range|||PRx,mon(t)|-21||6|dBm|||
||Rx total input power<br>monitor accuracy|||δPRx,mon(t<br>)|-2.0||2.0|dB|||
|Rx reflectance|Rx reflectance||||||-20|dB|||
||||||||||||



> **Notes:** Rx signal input power range over which performance can be guaranteed with <1dB OSNR penalty relative to Rx OSNR tolerance limit. 

Rx OSNR tolerance for Carrier Frequency Offset |CFO| < 1GHz. Up to 1dB penalty for worst case |CFO| = 3.6GHz. 

Power dissipation will increase by approximately 0.2W if extended CD compensation is enabled. 

Receiver is able to tolerate the specified ratio of total power of crosstalk channels and ASE to signal power with the specified OSNR penalty. Does not include contribution from adjacent channel crosstalk. No single channel power exceeding signal channel power by more than 1dB shall be included. Measured at Rx signal input power -6dBm. 

Measured at the Rx OSNR limit, 50GHz channel spacing, both adjacent channels <1dB higher power than signal channel. 

## **V. Digital Management and Diagnostics Functions** 

The QSFP-ZRH-100G-S QSFP28 module supports the digital management and diagnostics interface specified in the Common Management 

Copyright © 2026 FS.COM AII Rights Reserved 

Page 6 of 11 

100G QSFP28 High-TX ZR Data Sheet 

Interface Specification (CMIS) [16] with extensions specified in the OIF Coherent CMIS implementation agreement [17]. 

The QSFP-ZRH-100G QSFP28 module supports the diagnostics and management interface specified in the Specification for Management Interface for 4-lane Modules and Cables SFF-8636 [18], with limited control and monitoring of the coherent line interface. 

## **VI. References** 

SNIA “Specification for QSFP+ 28 Gb/s 4× Pluggable Transceiver Solution (QSFP28)”, SFF-8665 Rev. 1.9 (June 29, 2015). 

SNIA “Specification for QSFP+ 4× Hardware and Electrical Specification”, SFF-8679 Rev. 1.8 (October 4, 2018). 

SNIA “Specification for QSFP+ 4× Module” SFF-8661 Rev. 2.5 (June 22, 2018). 

SNIA “Specification for QSFP+ 4× 28 Gb/s Connector (Style A)” SFF-8662 Rev. 2.9 (June 8, 2018). 

SNIA “Specification for QSFP+ 28 Gb/s Cage (Style A)” SFF-8663 Rev. 1.7 (October 19, 2017). 

SNIA “Specification for QSFP+ 4× 28 Gb/s Connector (Style B)” SFF-8672 Rev. 1.2 (June 8, 2018). 

SNIA “Specification for QSFP+ Cage” SFF-8683 Rev. 1.3 (October 19, 2017). 

QSFP-DD MSA “QSFP-DD/QSFP-DD800/QSFP112 Hardware Specification for QSFP Double Density 8× And QSFP 4× Pluggable Transceivers” Rev. 6.3 (July 26, 2022). 

IEEE Computer Society “IEEE Standard for Ethernet”, IEEE Std 802.3-2022. 

ITU-T “Interfaces for the Optical Transport Network” G.709/Y.1331 Ed. 6.3 (February 2022). 

ITU-T “OTU4 Long-Reach Interface” G.709.2/Y.1331.2 Ed. 1.1 (September 2020). 

ITU-T “Amplified Multichannel Dense Wavelength Division Multiplexing Applications with Single Channel Optical Interfaces” G.698.2 Ed. 3.0 (November 2018). 

ITU-T “Characteristics of Optical Transport Network Hierarchy Equipment Functional Blocks” G.798 Ed. 6.6 (May 2022). 

CableLabs “P2P Coherent Optics Physical Layer 1.0 Specification” P2PCO-SP-PHYv1.0-I03- 200501 (May 2020). 

OIF “Common Electrical I/O (CEI) - Electrical and Jitter Interoperability Agreements for 6G+ bps, 11G+ bps,25G+ bps, and 56G+ bps I/O”, OIF-CEI-4.0 (December 29, 2017). 

OIF “Implementation Agreement – Common Management Interface Specification (CMIS)” OIF- CMIS-05.2 (April 2022). 

OIF “Implementation Agreement for Coherent CMIS”, OIF-C-CMIS-01.3 (October 2023). 

SNIA “Specification for Management Interface for 4-lane Modules and Cables”, SFF-8636 Rev 2.11 (January 3, 2023). 

SNIA “Specification for SFF Module Management Reference Code Tables”, SFF-8024 Rev 4.10 (November 24, 2022). 

Directive 2011/65/EU of the European Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment” as well as Commission Delegated Directive (EU) 2015/863 amending Annex II to Directive 2011/65/EU. Certain products may use one or more exemptions as allowed by the Directive. 

Application Note AN-2038: “COHERENT Implementation of RoHS Compliant Transceivers”. 

## **Test Center** 

## **I. Compatibility Testing** 

Each fiber optical transceiver has been tested in host device on site in FS Assured Program to ensure full compatibility with over 200 vendors. 

Copyright © 2026 FS.COM AII Rights Reserved 

Page 7 of 11 

100G QSFP28 High-TX ZR Data Sheet 


Above is part of our test bed network equipment. For more information, please click the Test Bed PDF. It will be updated in real time as we expand our portfolio. 

## **II. Performance Testing** 

Each fiber optical transceiver has been fully tested in FS Assured Program equipped with world's most advanced analytical equipment to ensure that our transceivers work perfectly on your device. 

Copyright © 2026 FS.COM AII Rights Reserved 

Page 8 of 11 

100G QSFP28 High-TX ZR Data Sheet 


## **Order Information** 

**Part Number Description** 

Copyright © 2026 FS.COM AII Rights Reserved 

Page 9 of 11 

|QSFP-ZRH-100G-S|QSFP-ZRH-100G-S|100G ZR QSFP28 High-TX w/o TOF Coherent Optics Transceiver, 120km over SMF, CMIS|100G ZR QSFP28 High-TX w/o TOF Coherent Optics Transceiver, 120km over SMF, CMIS|
|---|---|---|---|
||QSFP-ZRH-100G-S|100G ZR QSFP28 High-TX w/o TOF Coherent Optics Transceiver, 120km over SMF, CMIS||
||QSFP-ZRH-100G|100G ZR QSFP28 High-TX w/o TOF Coherent Optics Transceiver, 120km over SMF, SFF-8636||
||QSFP-ZRHF-100G-S|100G ZR QSFP28 High-TX with TOF Coherent Optics Transceiver, 120km over SMF, CMIS||
|QSFP-ZRHF-100G|QSFP-ZRHF-100G|100G ZR QSFP28 High-TX with TOF Coherent Optics Transceiver, 120km over SMF, SFF-8636||



Copyright © 2026 FS.COM AII Rights Reserved 

Page 10 of 11 

. FS and FS FS has several offices around the world. Addresses, phone numbers are listed on the FS Website at https://www.fs.com/contact_us.html 

