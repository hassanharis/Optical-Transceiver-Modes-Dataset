LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


## **LQD-DCO400-ZRC** 

## 400G QSFP-DD ZR Multi-Rate Digial Coherent Optical Transceiver 

## **Product Features** 

- Support DP-QPSK, DP-8QAM, and DP-16QAM Modulation; Compliant to OpenZR+ MSA technical specifications 

- Interoperable Forward Error Correction (oFEC); 400G/300G/200G/100G selectable line rates 

- Operating case temperature: 0°C to 70°C 

- Compact size (18.35mm x 93.26mm x 8.5 mm) 

- LC-Duplex optical receptacle; +3.3V power supply 

- Hot pluggable to 76-pin electrical connector 

- Support ethernet-only client traffic such as 100GbE, 200GbE and 400GbE 

- Conform to existing protocol standards (e.g., IEEE 802.3TM-2018) and operate over standard physical layer interface 

## **Applications** 

- Extended Reach DCI; 

- Metro, Long Haul (LH), Ultra Long Haul (ULH) 

## **Compliance** 

- OpenZR+ MSA technical specifications 


- IEEE Std 802.3-2018 

## **Descriptions** 

The QSFP-DD ZR+ modules are low power consumption multi-rate and interoperable coher-ent optical transceivers, which can be plugged into various routing, switching, and optical transport host platforms. QSFP-DD ZR+ modules support a total capacity of 25.6Tbit/s through 75 GHz- spaced DWDM within C- band. They are compliant with Open ZR+ MSA technical spec- ifications. Digital diagnostics functions are available via a TWI interface, as specified by the CMIS 5.1. 

400G ZR is built on high performance 7 nm coherent DSP, best in class narrow line-width tunable lasers, and integrated silicon photonic coherent optical subassembly (COSA). The mod- ule supports four lineside www.link-pp.com **www.l-p.com** Copyright © 2025 LINK-PP AlI Rights Reserved Page 1 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


data rates including 400G/300G/200G/100G, three modulation for- mats such as DP-QPSK, DP-8QAM and DP-16QAM. The client signal types supported are 100GbE, 200GbE and 400GbE. QSFP-DD ZR+ modules support multi haul transmission reach- es, ranging from a minimum reach of well beyond 480 km at 24 dB typical terrestrial span loss to Ultra Long Haul (ULH) system reach. 

The 400G QSFP-DD ZR+ coherent transceiver Compliant with the OIF QSFP-DD MSA. Digital diagnostics functions are available via an I2C interface as specified by the QSFP-DD MSA. Mechanical dimensions, connectors and footprint conform to QSFP-DD MSA. The module is 18.35 mm x 93.26 mm x 8.50 mm in size and hot pluggable by 76 PIN PAD and host connector. 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage temperature|Ts|-40||85|℃|Exceeding the Absolute<br>Maximum Ratings may cause<br>irreversible damage to the<br>device. The device is not<br>intended to be operated under<br>the condition of simultaneous<br>Absolute Maximum Ratings, a<br>condition which may cause<br>irreversible damage to the<br>device.|
|Power supply|Vcc|-0.3|3.3|3.6|V||
|Relative humidity|RH|15||85|%||



## **Recommended Operating Conditions** 

|**Parameter**|**symbol**|**min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Tcase|0|+25|+70|ºC||
|Module Supply Voltage|Vcc|3.135|3.3|3.465|V||
|Operating Power Supply Current|Icc|-|-|8.8|A|Instantaneous peak current|
|||-|-|7.26||Sustained peak current|
|||-|-|7.02||Steady current|
|Module Power consumption|Pcc|-|-|22|W|Full temperature and voltage range|



## **Signaling rate per lane for 400G** 

|**Parameter**|**symbol**|**min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Signalingrateper lane|BPS|-|53.1|-|BPS|PAM4 Mode|



www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 2 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


|Differential voltage pk-pk|TVdiff|750|-|900|mVpp||
|---|---|---|---|---|---|---|
|Differential Output Impedance|TRD|80|100|120|Ω||
|Transition time|Trise/Tfall|12|-|-|ps||
|Return Loss|-|-|see note|-|dB||



Notes: 


- 1、GAUI-8/CAUI-4 TP4 Differential Output Return Loss SDD22(db)= 

   - -9.5+0.37*f, for 0.01<=f<=8GHz 

   - -4.75+7.4*log10(f/14),for 8<=f<=19GHz 

- 2、GAUI-8/CAUI-4 TP4 Common mode to Differential mode Output Return Loss SDD22(db)= -22+(20/25.78)*f, for 0.01<=f<=12.89GHz 

   - -15+(6/25.78)*f,for 12.89<=f<=19GHz 

- 3、CEI-56G VSR PAM4 SDD22(db)= 

   - -11, for 0.05<f<fb/7.5 

   - -6.0+9.2*1og10((15*f)/(7*fb)),for fb/7.5<=f<=fb 

      - -25+20*(f/fb), for 0.05<f<fb/2 

   - -18+6* (f/fb), for fb/2<f<fb 

- 4、CEI-56G VSR PAM4 SDC22(db) SCD22(db) 

- 5、CEI-28G VSR TP4 SDD22(db) -11, for 0.05<f<fb/7 -6+9.2*log10(2f/fb), for fb/7<f<fb 6、CEI-28G VSR TP4 SDC22(db), SDC22(db) -25+20*(f/fb), for 0.05<f<fb/2 -18+6*(f/fb), for fb/2<f<fb 

|**Parameter**|**symbol**|**min**|**Typ**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Signaling rate per lane|BPS|-|53.1|-|BPS|PAM4 Mode|
|Differential voltage pk-pk|RVdiff|900|-|-|mVppd|AC coupled|
|Differential Input Impedance|RRD|80|100|120|Ω||
|Return Loss|-|-|see note|-|dB||
|Stress input test|-|-|see IEEE<br>802.3bs<br>802.3bm<br>CEI-56G-VSR-<br>PAM4<br>OIF-CEI-03.1|-|-||



Notes: 

- 1.GAUI-8/CAUI-4 TP1 Differential Output Return Loss SDD11(db)= 

   - -9.5+0.37*f, for 0.01<=f<=8GHz 

   - -4.75+7.4*log10(f/14),for 8<=f<=19GHz 

- 2.GAUI-8/CAUI-4 TP1 Common mode to Differential mode Output Return Loss SDC11(db)= -22+(20/25.78)*f, for 0.01<=f<=12.89GHz 

   - -15+(6/25.78)*f,for 12.89<=f<=19GHz 

- 3.CEI-56G VSR PAM4 TP1 SDD11(db)= 

   - -11, for 0.05<f<fb/7.5 

   - -6.0+9.2*1og10((15*f)/(7*fb)),for fb/7.5<=f<=fb 

- 4.CEI-56G VSR PAM4 TP1 SDC11(db) SCD11(db) -25+20*(f/fb), for 0.05<f<fb/2 -18+6* (f/fb), for fb/2<f<fb 

- 5.CEI-28G VSR TP1 SDD11(db) -11, for 0.05<f<fb/7 

   - -6+9.2*log10(2f/fb), for fb/7<f<fb 

- -25+20*(f/fb), for 0.05<f<fb/2 -18+6*(f/fb), for fb/2<f<fb 

6. CEI-28G VSR TP1 SDC11(db), SDC11(db) 

## **Low speed control and monitor signals** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|**Conditions/ Notes**|
|---|---|---|---|---|---|
|SCL and SDA|VOL|0|0.4|V|Iol(max) =3mA for fast mode,20mA<br>for Fast- modeplus|



www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 3 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


|SCL and SDA|VIL|-0.3|Vcc*0.3|V||
|---|---|---|---|---|---|
||VIH|VCC*0.7|VCC+0.5|V||
|Capacitance for SCL and SDA I/O<br>signal|Ci||14|pF||
|Total bus capacitive Load for SDA and<br>SCL|<br>Cb||100|pF|For 400kHz clock rate us 3.0k Ohms<br>pull up resistor, max,. For 1000kHz<br>clock rate refer to Figure 45|
||||200|pF|For 400kHz clock rate us 1.6k Ohms<br>pull up resistor, max,. For 1000kHz<br>clock rate refer to Figure 45|
|LPMode, ResetL, ModselL and ePPS|VIL|-0.3|0.8|V||
||VIH|2|VCC+0.3|V||
|LPMode,ResetL and ModSelL||Iin|||360|uA|0<Vin<Vcc|
|IntL|VOL|0|0.4|V|IOL=2.0mA|
||VOH|VCC-0.5|VCC+0.3|V|10k Ohms pull-up to Host Vcc|
|ModPrsL|VOL|0|0.4|V|IOL=2.0mA|
||VOH||||ModPrsL can be implemented as a<br>short circuit to GND on the module|



Notes: 

- 1.Maximum total power value is specified across the full temperature(0。C-70。C) and voltage range(3.2V-3.4V). 

- 2.Unless otherwise noted, all the electrical characteristics are specified per QSFP-DD MSA Hardware Specification, Revision 5.0. 

**Timing for QSFP-DD soft control and status functions** 

|**Parameter**|**Symbol**|**Min**|**Max**|**unit**|**condition**|
|---|---|---|---|---|---|
|Mgmt InitDuration|Max MgmtInit Duration|-|2000|ms|Time from power on,hot<br>plug or rising edge of<br>reset until completion<br>of the MgmtInit State|



www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 4 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


|ResetL Assert Time|t_reset_init|10|-|us|Minimum Pulse time on<br>the ResetL signal to<br>initiate a<br>module reset|
|---|---|---|---|---|---|
|IntL Assert Time|ton_intL|-|200|ms||
|IntL Deassert Time|Toff_intL|-|500|us|Time from clear on read<br>operation of associated<br>flag until Vout:IntL=Voh.<br>This<br>includes deasset times<br>for Rx<br>LOS，TX Fault and<br>other flagbits|
|Rx LOS Assert Time|Ton_los|-|100|ms|Time from Rx Los<br>condition present to Rx<br>Los bit set<br>(value=1b)and IntL<br>asserted|
|Tx Fault Assert Time|Ton_Txfault|-|200|ms|Time from Tx fault state<br>to Tx fault bit set<br>(value=1b)<br>and IntL asserted.|
|Flag Assert Time|Ton_flag|-|200|ms|Time from occurrence<br>of condition trigging flag<br>to associated IntL<br>assertion is<br>inhibited|
|Mask Asset Time|Ton_mask|-|100|ms|Time from mask bit set<br>(value=1b) until<br>associated IntL assertion<br>is inhibited|
|Mask Deassert Time|Toff_mask|-|100|ms|Time from mask bit<br>(value=1b)cleared<br>until associated IntL<br>opera-<br>tion resumes|
|Data Path Tx Turn On Max<br>Duration Data Path TxT urn Off<br>Max Duration Data Path Deinit<br>Max Duration<br>Data Path Init Max Duration<br>Module Pwr Up Max Duration<br>Module Pwr Dn Max Duration|DataPathTxTurnOn_MaxDuration<br>DataPathTxTurnOff_MaxDuration<br>DataPathDeinit_MaxDuration<br>DataPathInit_MaxDuration<br>ModulePwrUp_MaxDuration<br>ModulePwrDn_MaxDuration||||See Common<br>Management Interface<br>Specification T Rev5.2|
|Note 1. Power on is defined as the instant when supply voltage reach and remain at or above the minimum level||||||
|Note 2.Measured from low to high SDA edge of the STOP condition of the read transaction||||||
|Note3. measured from low to high SDA edge of the Stop condition of the write transaction||||||
|Note 4. Rx LOS condition is defined at the optical input by the relevant standard||||||



www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 5 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED LQD-DCO400-ZRC Rev1.0- Sep.2025 


## **I/O Timing for Squelch & Disable** 

|**Parameter**|**Symbol**|**Max**|**unit**|**condition**|
|---|---|---|---|---|
|Tx disable assert Time|Ton_txdis|100|ms|Time<br>from<br>the<br>stop<br>condition of the tx disable<br>write<br>sequence<br>until<br>optical output falls below<br>10% of nominal|
|Tx disable Deassert Time|Toff_txdis|100|ms|Time from Tx disable bit<br>cleared<br>(value=0b)until<br>optical output rises above<br>90% of nominal|
|Note 1: Measured from LOW to HIGH SDA signal transition of the STOP condition of the write transaction|||||



## **Transmitter Optical Specifications** 

|**Parameter**|**Line Rate**|**Min**|**Max**|**Unit**|**Condition**|
|---|---|---|---|---|---|
|Modulation format|400G-CFEC|DP-16QAM||||
||400G-OFEC|DP-16QAM||||
||300G-OFEC|DP-8QAM||||
||200G-OFEC|DP-QPSK||||
||100G-OFEC|DP-QPSK||||
|Baud rate|400G/300G/2<br>00G|60.138547 ±20 ppm||GBd||
||100G|30.069274 ±20 ppm||GBd||
|Laser frequency accuracy|All|–1.8|1.8|GHz||
|Typical TX output signal power|400G-CFEC|–10||dBm||
||400G-OFEC|–10||dBm||
||300G-OFEC|–10||dBm||
||200G-OFEC|–9||dBm||
||100G-OFEC|–8||dBm||
|Tx output power with transmi<br>disabled|t<br>All||–25|dBm||
|Total<br>output<br>power<br>during<br>wavelength switching|All||–25|dBm||
|Inband (IB) OSNR|All|40||dB/0.1 nm||
|Out-of-band (OOB) OSNR|All|40||dB/0.1 nm||



www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 6 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


## **The Receiver Optical Specification** 

||**Parameter**|**Mode**|**Min**|**Max**|**Unit**|**Conditions/Comments**|
|---|---|---|---|---|---|---|
||Modulation format|400G-CFEC|DP-16QAM||||
|||400G-OFEC|DP-16QAM||||
|||300G-OFEC|DP-8QAM||||
|||200G-OFEC|DP-QPSK||||
|||100G-OFEC|DP-QPSK||||
||Baud rate|400G/300G/<br>200G|60.138547 ±20ppm||GBd||
|||100G|30.069274 ±20ppm||GBd||
||Frequency offset<br>between received<br>carrier and LO|All|–3.6|3.6|GHz||
||Input power range|400G-CFEC|–12|0|dBm|Signal power of the channel<br>needed to meet the OSNR<br>tolerance requirement|
|||400G-OFEC|–12|0|dBm||
|||300G-OFEC|–15|0|dBm||
|||200G-OFEC|–18|0|dBm||
|||100G-OFEC|–18|0|dBm||
||Sensitivity|400G-CFEC|-21||dBm||
|||400G-OFEC|-23||dBm||
|||300G-OFEC|-26||dBm||
|||200G-OFEC|-31||dBm||
||Optical return loss|All|20||dB|At Rx connector input.|
||CD tolerance|400G-CFEC||2400|ps/nm|Tolerance to CD with ≤0.5 dB<br>penalty to<br>OSNR sensitivity when change in<br>SOP is ≤1 rad/ms.|
|||400G-OFEC||13,000|ps/nm||
|||300G-OFEC||40,000|ps/nm||
|||200G-OFEC||50,000|ps/nm||
|||100G-OFEC||100,000|ps/nm||
||Optical path OSNR<br>penal- ty tolerance|All||0.5|dB|OSNR<br>penalty<br>due<br>to<br>interferometric<br>crosstalk<br>and<br>chromatic dispersion.|
|||400G-CFEC||16|ps|Min tolerance limits includes|
|www.link-pp.com<br>**www.l-p.com**||Copyright © 2025 LINK-PP AlI Rights Reserved<br>Page 7 of 14|||||



LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


|Mean DGD|400G-OFEC||22|ps|the transmitter maximum X-Y<br>skew.<br>Tolerance to PMD with ≤0.5<br>dB penalty to<br>OSNR sensitivity when change<br>in SOP is ≤1 rad/ms.<br>PMD (avg) is equivalent to<br>DGDmean. DGDmax occurs when<br>SOPMD = 0 ps2. Due to the<br>statistical nature of PMD the<br>DGDmax to DGDmean Ratio is<br>calculated at<br>3.3 (4.1 x 10-6 probability that<br>DGD<br>being<br>great-<br>er<br>than<br>DGDmax).|
|---|---|---|---|---|---|
||300G-OFEC||33|ps||
||200G-OFEC||33|ps||
||100G-OFEC||33|ps||
|Peak PDL tolerance|All|3.5||dB|Tolerance to peak PDL with ≤<br>1.3 dB addition- al OSNR penalty<br>when<br>change<br>in<br>SOP<br>is<br>≤1<br>rad/ms.|
|Tolerance to change<br>in SOP|400G-CFEC||20|KHz|With ≤0.5 dB additional OSNR<br>penalty over all PMD and PDL<br>values.|
||400G-OFEC||20|KHz||
||300G-OFEC||30|KHz||
||200G-OFEC||100|KHz||
||100G-OFEC||100|KHz||
|Optical input power<br>transi- ent tolerance|All|- 2|2|dB|With ≤0.5 dB additional OSNR<br>penalty over all PMD and PDL<br>values.|



## **Module Requirements TX** 

|**Parameter**<br>Transmitter laser disable time<br>Transmitter turn-up time from<br>warm start<br>Transmitter turn-up time from<br>cold start<br>Transmitter wavelength|**Min**|**Max**|**Units**|**Condition/comments**|
|---|---|---|---|---|
||-|100|ms||
||-|120|s|The maximum time from Module LowPwr<br>to DataPath activated state|
||-|150|s|The maximum time from deassertion of<br>Re- setS==false to DataPathActivated<br>state while LoPweS==false|
||-|60|s|The maximum time to change<br>wavelengths includ- ing turn up time|
||||||



www.link-pp.com **www.l-p.com** Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 8 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


|switching time||||Applicable to modules with tunable optics|
|---|---|---|---|---|
|Output power monitor Accuracy|-1|1|dB|Total output power measurement<br>including all ASE contribution.<br>Measurement accuracy does not<br>contribute to al- lowable output power<br>signal window|



## **Module Requirements RX** 

|**Parameter**|**Mode**|**Default**|**Min**|**Max**|**Units**|**Condition/comments**|
|---|---|---|---|---|---|---|
|Receiver turn-up time from<br>warm start|All|-|-|10|s|Upon RX_LOS de-assert, Receiv- er<br>has been turned up previously|
|Receiver turn-up time from<br>cold start|All|-|-|150|s|From module reset, with valid<br>optical input signalpreset|
|Input total power monitor<br>accuracy|All|-|-2|2|dB||
|Input Channel power<br>monitor – Accuracy|All|-|-2|2|dB|The module reports the channel<br>power as received bythe module|
|RX power monitoring range|All|-|-21|0|dBm|RX power monitoring range with<br>accuracydefined dbove|
|Optical Rx_LOS Assert<br>Threshold|400G-<br>CFEC|-21|-23|-19|dBm|Optical loss-of-signal(LOS) assert<br>Threshold is programmable|
||400G-<br>OFEC|-23|-25|-21|dBm||
||300G-<br>OFEC|-26|-28|-24|dBm||
||200G-<br>OFEC|-31|-33|-29|dBm||
||100G-<br>OFEC|-33|-35|-31|dBm||
|Optical RX_LOS Hysteesis|400G-<br>CFEC|-|1|2.5|dBm|Rx_LOS cleared|
||400G-<br>OFEC||1|2.5|dBm||
||300G-<br>OFEC||1|2.5|dBm||
||200G-<br>OFEC||1|4.5|dBm||
||100G-<br>OFEC|-|1|4.5|dBm||



www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 9 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


## **Pin-out Definition** 



**Figure1** 

www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 10 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


|**Pin**|**Logic**|**Symbol**|**Name/Description**|**Plug**<br>**Sequence[4]**|**Note**|
|---|---|---|---|---|---|
|1||GND|Ground|1B|[1]|
|2|CML-I|Tx2n|Transmitter Inverted Data Input|3B||
|3|CML-I|Tx2p|Transmitter Non-Inverted Data Input|3B||
|4||GND|Ground|1B|[1]|
|5|CML-I|Tx4n|Transmitter Inverted Data Input|3B||
|6|CML-I|Tx4p|Transmitter Non-Inverted Data Input|3B||
|7||GND|Ground|1B|[1]|
|8|LVTTL-I|ModSelL|Module Select|3B||
|9|LVTTL-I|ResetL|Module Reset|3B||
|10||VccRx|+3.3V Power Supply Receiver|2B|[2]|
|11|LVCMOS-I/O|SCL|2-wire serial interface clock|3B||
|12|LVCMOS-I/O|SDA|2-wire serial interface data|3B||
|13||GND|Ground|1B|[1]|
|14|CML-O|Rx3p|Receiver Non-Inverted Data Output|3B||
|15|CML-O|Rx3n|Receiver Inverted Data Output|3B||
|16||GND|Ground|1B|[1]|
|17|CML-O|Rx1p|Receiver Non-Inverted Data Output|3B||
|18|CML-O|Rx1n|Receiver Inverted Data Output|3B||
|19||GND|Ground|1B|[1]|
|20||GND|Ground|1B|[1]|
|21|CML-O|Rx2n|Receiver Inverted Data Output|3B||
|22|CML-O|Rx2p|Receiver Non-Inverted Data Output|3B||
|23||GND|Ground|1B|[1]|
|24|CML-O|Rx4n|Receiver Inverted Data Output|3B||
|25|CML-O|Rx4p|Receiver Non-Inverted Data Output|3B||
|26||GND|Ground|1B|[1]|
|27|LVTTL-O|ModPrsL|Module Present|3B||
|28|LVTTL-O|IntL|Interrupt|3B||
|29||VccTx|+3.3V Power supply transmitter|2B|[2]|
|30||Vcc1|+3.3V Power supply|2B|[2]|
|31|LVTTL-I|LPMode|Low Power mode;|3B||



www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 11 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


|32||GND|Ground|1B|[1]|
|---|---|---|---|---|---|
|33|CML-I|Tx3p|Transmitter Non-Inverted Data Input|3B||
|34|CML-I|Tx3n|Transmitter Inverted Data Input|3B||
|35||GND|Ground|1B|[1]|
|36|CML-I|Tx1p|Transmitter Non-Inverted Data Input|3B||
|37|CML-I|Tx1n|Transmitter Inverted Data Input|3B||
|38||GND|Ground|1B|[1]|
|39||GND|Ground|1A|[1]|
|40|CML-I|Tx6n|Transmitter Inverted Data Input|3A||
|41|CML-I|Tx6p|Transmitter Non-Inverted Data Input|3A||
|42||GND|Ground|1A|[1]|
|43|CML-I|Tx8n|Transmitter Inverted Data Input|3A||
|44|CML-I|Tx8p|Transmitter Non-Inverted Data Input|3A||
|45||GND|Ground|1A|[1]|
|46||Reserved|For future use|3A|[3]|
|47||VS1|Module Vendor Specific 1|3A|[3]|
|48||VccRx1|3.3V Power Supply|2A|[2]|
|49||VS2|Module Vendor Specific 2|3A|[3]|
|50||VS3|Module Vendor Specific 3|3A|[3]|
|51||GND|Ground|1A|[1]|
|52|CML-O|Rx7p|Receiver Non-Inverted Data Output|3A||
|53|CML-O|Rx7n|Receiver Inverted Data Output|3A||
|54||GND|Ground|1A|[1]|
|55|CML-O|Rx5p|Receiver Non-Inverted Data Output|3A||
|56|CML-O|Rx5n|Receiver Inverted Data Output|3A||
|57||GND|Ground|1A|[1]|
|58||GND|Ground|1A|[1]|
|59|CML-O|Rx6n|Receiver Inverted Data Output|3A||
|60|CML-O|Rx6p|Receiver Non-Inverted Data Output|3A||
|61||GND|Ground|1A|[1]|
|62|CML-O|Rx8n|Receiver Inverted Data Output|3A||
|63|CML-O|Rx8p|Receiver Non-Inverted Data Output|3A||
|64||GND|Ground|1A|[1]|



www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 12 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


|65||NC|No Connect|3A|[3]|
|---|---|---|---|---|---|
|66||Reserved|For future use|3A|[3]|
|67||VccTx1|3.3V Power Supply|2A|[2]|
|68||Vcc2|3.3V Power Supply|2A|[2]|
|69|LVTTL-I|ePPS|Precision Time Protocol (PTP)<br>reference clock input. Not used|3A|[3]|
|70||GND|Ground|1A|[1]|
|71|CML-I|Tx7p|Transmitter Non-Inverted Data Input|3A||
|72|CML-I|Tx7n|Transmitter Inverted Data Input|3A||
|73||GND|Ground|1A|[1]|
|74|CML-I|Tx5p|Transmitter Non-Inverted Data Input|3A||
|75|CML-I|Tx5n|Transmitter Inverted Data Input|3A||
|76||GND|Ground|1A|[1]|



## **Notes:** 

[1] QSFP-DD uses common ground (GND)for all signals and supply (power). All are common within the QSFP-DD module and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host board signal common ground plane. 

[2] VccRx, VccRx1, Vcc1, Vcc2, VccTx and VccTx1 shall be applied concurrently.Requirements defined for the host side of the Host Card Edge Connector. VccRx, VccRx1, Vcc1, Vcc2, VccTx and VccTx1 may be internally connected within the module in any combination. The connector Vcc pins are each rated for a maximum current of 1500 mA. [3] All Vendor Specific, Reserved and No Connect pins may be terminated with 50ohms to ground on the host. Pad 65 (No Connect) shall be left unconnected within the module. Vendor specific and Reserved pads shall have an impedance to GND that is greater than 10K ohms and less than 100pF. 

[4] Plug Sequence specifies the mating sequence of the host connector and module. The sequence is 1A, 2A, 3A, 1B, 2B, 3B. (see Figure 1 for pad locations) Contact sequence A will make, then break contact with additional QSFPDD pads. Sequence 1A,1B will then occur simultaneously, followed by 2A,2B,followed by 3A,3B. 

## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LQD-DCO400-ZRC|400Gbps, Digial Coherent Optical , QSFP-DD, ZR, 0°C~+70°C, with DDM|



www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 13 of 14 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-DCO400-ZRC Rev1.0- Sep.2025 


## **Warnings** 

## **Handling Precautions** : 

This device is susceptible to damage as a result of electrostatic discharge (ESD). A static free environment is highly recommended. Follow guidelines according to proper ESD procedures. 

## **Laser Safety:** 

Radiation emitted by laser devices can be dangerous to human eyes. Avoid eye exposure to direct or indirect radiation. 

## **Notice:** 

The information provided on this page contains the product target specifications which are subject to change without notice. 

Check with your Hisense Sales Office for product updates, changes in specifications, sample availability and production release dates. 

## **EYESAFETY** 

Complies with 21 CFR 1040.10 and 1040.11 except for conformance with IEC 60825-1 Ed.3., as described in Laser Notice No. 56, 

dated May 8, 2019. 

Complies with IEC 60825-1:2014, EN 60825-1:2014+A11:2021 and IEC 60825-2: 2021, EN 60825-2:2004+A1:2007+A2:2010. Class 1 laser safety compliant. 

INVISIBLE LASER RADIATION. 

## **CAUTION:** 

Use of controls or adjustments or performance of procedures other than those specified herein may result in hazardous radiation 

www.link-pp.com **www.l-p.com** 

Copyright © 2025 LINK-PP AlI Rights Reserved 

Page 14 of 14 

