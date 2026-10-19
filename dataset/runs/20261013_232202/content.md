4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## 400G QSFP-DD DCO DWDMTunable Coherent 120km DOM Transceiver 

QDD-ZRPH-400G 

## Applications 

- Metro/ Regional ROADM Networks 

- Data Centre Interconnect 

## Features 

- Digital Coherent Optics module, QSFP-DD  form factor, Type 2A 

- IEEE 400GE or n×100GE (n = 1…4) Ethernet  compliant host interface 

- Coherent 400G/300G/200G/100G optical  interface based on OpenZR+ MSA 

- High Tx output power (0dBm) and Tx OSNR  for compatibility with deployed ROADM line  systems 

- Transmission reach > 600km at 400G, with  extended reaches at lower data rates 

- Full C-band tunable with flexible grid support 

- Case temperature range 0°C to 70°C 

- Power dissipation < 22.5W 

www.fs.com                                                                                                                                                                                                                                                                                                                                 1 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## Description 

The QDD-ZRPH-400G QSFP-DD Digital Coherent Optics (DCO) transceiver supports multi-rate coherent  transmission for metro/regional and data center interconnect applications. On the host side, the module can accommodate either a single IEEE 400GE Ethernet signal or multiple 100GE Ethernet signals  (n = 1…4) [1] that are multiplexed onto a single line interface. On the line side the module supports 400G,  300G, or 200G line interfaces with 60GBd dual-polarization 16QAM, 8QAM, or QPSK modulation, respectively, as well as a  100G line interface with 30GBd dual-polarization QPSK modulation, as specified  by the OpenZR+ MSA [2]. 

Extending the capabilities of a basic OpenZR+ transceiver, the QDD-ZRPH-400G offers up to  10dB higher Tx output power as well as improved Rx sensitivity, providing compatibility with deployed and emerging   ROADM line systems. 

## Product Specifications 

## I. Absolute Maximum Ratings 

Stresses in excess of the absolute maximum ratings can cause permanent damage to the device. These  are absolute stress ratings only. Functional operation of the device is not implied at these or any other  conditions in excess of those given in the operational sections of the data sheet. Exposure to absolute maximum ratings for extended periods can adversely affect device reliability. 

|Parameter|Conditions|Conditions|Symbol|Min|Typ|Max|Unit|Note|
|---|---|---|---|---|---|---|---|---|
|DC Supply Voltage|||VCC|-0.3||3.6|V||
|Low Speed I/O<br>Voltages||||-0.3||3.6|V||
|Storage<br>Temperature|||TS|-40||85|°C||
|Case Operating<br>Temperature|||TOP|-5||75|°C||
|Relative Humidity|Non-condensing||RH|5||95|%||
|Rx input Power|||PRxin|||18|dBm||
|ESD Damage<br>Threshold|Human body<br>model  (HBM)|DC pins||2000|||V||
|||RF pins||1000|||||



www.fs.com                                                                                                                                                                                                                                                                                                                                2 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## II. Environmental Specifications 

|Parameter<br>Storage<br>Temperature|Conditions|Symbol|Min|Typ|Max|Unit|Note|
|---|---|---|---|---|---|---|---|
|||TS|-40||85|°C||
|Case Operating<br>Temperature||TOP|0||70|°C||
|Relative Humidity|Non-condensing|RH|5||85|%||



## III. Hostand Line Interface Modes 

A. Host Interface Modes 

|Hos Interface ID [7]|Host Interface Description [7]|Modulation|Forward Error<br>Correction Code|Nominal Symbol<br>Rate (GBd)|Supported Line<br>Interface IDs [7]|
|---|---|---|---|---|---|
|17|400GAUI-8|PAM4|RS(544,514)|26.5625|70, 62|
|13|4× 100GAUI-2|PAM4|RS(544,514)|26.5625|70, 62|
|13|3× 100GAUI-2|PAM4|RS(544,514)|26.5625|71|
|13|2× 100GAUI-2|PAM4|RS(544,514)|26.5625|72|
|13|100GAUI-2|PAM4|RS(544,514)|26.5625|73|



## B. Line Interface Modes 

|Hos Interface ID [6]|Line Interface Description [6]|Modulation|Forward Error<br>Correction Code|Nominal Symbol<br>Rate (GBd)|Spectral Shaping|
|---|---|---|---|---|---|
|70|ZR400-OFEC-16QAM|16QAM|O-FEC|60.1385|None|
|71|ZR300-OFEC-8QAM|8QAM|O-FEC|60.1385|None|
|72|ZR200-OFEC-QPSK|QPSK|O-FEC|60.1385|None|
|73|ZR100-OFEC-QPSK|QPSK|O-FEC|30.0693|None|
|62|400ZR,  DWDM, Amplified|16QAM|C-FEC|59.8438|None|



www.fs.com                                                                                                                                                                                                                                                                                                                                3 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## IV. Electrical Characteristics 

A. Power & Low Speed I/O 

|Parameter<br>Conditions<br>Symbol|Parameter<br>Conditions<br>Symbol|Parameter<br>Conditions<br>Symbol|Min<br>Typ<br>Max<br>Unit|Min<br>Typ<br>Max<br>Unit|Min<br>Typ<br>Max<br>Unit|Min<br>Typ<br>Max<br>Unit|Notes|
|---|---|---|---|---|---|---|---|
|Power Supply - General||||||||
|Power Supply Voltages|Including ripple, droop and noise below<br>100kHz||3.135|3.300|3.465|V||
|Host RMS Noise Output|40Hz - 10MHz||||25|mV||
|Module RMS Noise Output|10Hz - 10MHz||||30|mV||
|Module Supply Noise<br>Tolerance|10Hz - 10MHz, peak-to-peak|PSNRmod|||66|mV||
|Module Inrush|Instantaneous peak duration|Tip|||50|µs||
||Initialization timeTinit||||500|ms||
|Power Supply - Low Power Mode||||||||
|Power Dissipation||Plp|||1.5|W||
|Power Supply Current|Instantaneous peak current|ICC, ip, lp|||600|mA||
||Sustained peak current|ICC,sp, lp|||495|||
||Steady state current|ICC, lp|||475|||
|Power Supply - High Power Mode||||||||
|Power Dissipation||Php|||22.5|W||
|Power Supply Current|Instantaneous peak current|ICC, ip, hp|||9.0|A||
||Sustained peak current|ICC,sp, hp|||7.5|||
||Steady state current|ICC, hp|||7.2|||
|Low Speed I/O||||||||
|Output Voltage, SCL and<br>SDA|Output low|VOL|0.0||0.4|V||
||Output high|VOH|VCC- 0.5||VCC+ 0.3|||
|Input Voltage, SCL and<br>SDA|Input low|VIL|-0.3||0.3×VCC|V||
||Input high|VIH|0.7×VCC||VCC+0.5|||
|Capacitance for SCL and<br>SDA I/O signal||Ci|||14|pF||
|Total Bus Capacitive Load<br>for SCL and SDA|400kHz clock rate, 3.0kΩ pull-up,  max.|Cb|||100|pF|1|
||400kHz clock rate, 1.6kΩ pull-up, max.||||200|||



www.fs.com                                                                                                                                                                                                                                                                                                                                4 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Parameter||Conditions<br>Symbol<br>Min<br>Typ<br>Max||||||||||Unit<br>Notes|||
|Low Speed I/O|||||||||||||||
|Input voltage / current,<br>InitMode, ResetL and<br>ModSelL||Input volt||age, low||VIL|-0.3||||0.8|V|||
|||Input volta||ge, high||VIH|2.0||||VCC+0.3||||
|||Input current, 0||V < Vin < VCC|||Iin ||||||360|µA|||
|Output voltage, IntL||Output low,||IOL = 2mA||VOL|0.0||||0.4|V|||
|||Output high, 10kΩ pull-||up resistor to host VCC||VOH|VCC-0.5||||VCC+0.3||||
|Output voltage, ModPrsL||Output low,||IOL = 2mA||VOL|0.0||||0.4|V|2||
|||Output||high||VOH|||||||||
||Notes:<br>1. For 1000kHz clock rate refer to  Figure 6 in [4].<br>2. ModPrsL can be implemented as a short-circuit to GND<br>B. High Speed Data I/O<br>on the module.||||||||||||||
||Parameter||Conditions|||Symbol|Min||Typ|Max||Unit||Notes|
||Transmitter (Module Input) – 400GAUI-8, 100GAUI-2||||||||||||||
||Signaling Rate Per Lane|||||||||||GBd|||
||Differential pk-pk Input Voltage<br>Tolerance|||||||||||mV|||
||Differential Input Return Loss||||||Per IEEE Std 802.3 [1],<br>Annex 120E,<br>Table 120E-7|||||dB|||
||Differential to Common Mode<br>Input Return Loss|||||||||||dB|||
||Differential Termination Mismatch|||||||||||%|||
||Module Stressed Input Test||||||||||||||
||Single-ended Voltage Tolerance<br>Range|||||||||||V|||
||DC Common Mode Voltage|||||||||||mV|||
||Receiver (Module Output) – 400GAUI-8, 100GAUI-2||||||||||||||
||Signaling Rate Per Lane||||||Per IEEE Std 802.3 [1],<br>Annex 120E,<br>Table 120E-3|||||GBd|||
||AC Common-Mode Output Voltage|||||||||||mV|||



www.fs.com                                                                                                                                                                                                                                                                                                                                5 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


|Parameter|Conditions|Symbol|Min|Typ|Max|Unit|Notes|
|---|---|---|---|---|---|---|---|
|||||||||
|Receiver (Module Output) – 400GAUI-8, 100GAUI-2||||||||
|Differential Peak-to-Peak Output<br>Voltage|||Per IEEE Std 802.3 [1],<br>Annex 120E,<br>Table 120E–3|||mV||
|Near-end ESMW||||||UI||
|Near-end Eye Height, Differential||||||mV||
|Far-end ESMW||||||UI||
|Far-end Eye Height, Differential||||||mV||
|Far-end Pre-cursor ISI Ratio||||||%||
|Differential Output Return Loss||||||dB||
|Common to Differential Mode<br>Conversion Return Loss||||||dB||
|Differential Termination Mismatch||||||%||
|Transition Time||||||ps||
|DC Common Mode Voltage||||||||
|||||||~~m V~~||
|V. Digital Diagnostic Functions<br>The  Q D D - Z R P - 4 0 0G - HT  QS F P - D D - DCO  mod u le  s u p po rts  t he  diag nostics  i nte rface  s pecified  i n  the  Mechanical<br>Specification with extensions specified  in the O IF Coherent cC MIS  implementation  agreement[6]. See also Coherent<br>application  note AN-2200 .||||||||



www.fs.com                                                                                                                                                                                                                                                                                                                                6 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## VI.Pin Description 


Figure 1 Module Pad Layout 

www.fs.com                                                                                                                                                                                                                                                                                                                                    7 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## VII. Pin Function Definitions 

|Pin|Logic|Symbol|Description|Plug<br>Sequence3|Notes|
|---|---|---|---|---|---|
|1||GND|Ground|1B|1|
|2|CML-I|Tx2n|Transmitter inverted data input|3B||
|3|CML-I|Tx2p|Transmitter non-inverted data input|3B||
|4||GND|Ground|1B|1|
|5|CML-I|Tx4n|Transmitter inverted data input|3B||
|6|CML-I|Tx4p|Transmitter non-inverted data input|3B||
|7||GND|Ground|1B|1|
|8|LVTTL-I|ModSelL|Module select|3B||
|9|LVTTL-I|ResetL|Module  reset|3B||
|10||VccRx|+3.3V power supply receiver|2B|2|
|11|LVCMOS-I/O|SCL|2-wire serial interface clock|3B||
|12|LVCMOS-I/O|SDA|2-wire serial interface data|3B||
|13||GND|Ground|1B|1|
|14|CML-O|Rx3p|Receiver non-inverted data output|3B||
|15|CML-O|Rx3n|Receiver inverted data output|3B||
|16||GND|Ground|1B|1|
|17|CML-O|Rx1p|Receiver non-inverted data output|3B||
|18|CML-O|Rx1n|Receiver inverted data output|3B||
|19||GND|Ground|1B|1|
|20||GND|Ground|1B|1|
|21|CML-O|Rx2n|Receiver inverted data output|3B||
|22|CML-O|Rx2p|Receiver non-inverted data output|3B||
|23||GND|Ground|1B|1|



www.fs.com                                                                                                                                                                                                                                                                                                                                   8 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


|Pin|Logic|Symbol|Description|Plug<br>Sequence3|Notes|
|---|---|---|---|---|---|
|24|CML-O|Rx4n|Receiver inverted data output|3B||
|25|CML-O|Rx4p|Receiver non-inverted data output|3B||
|26||GND|Ground|1B|1|
|27|LVTTL-O|ModPrsL|Module present|3B|1|
|28|LVTTL-O|IntL/RxLOSL|Interrupt / Optional RxLOS|3B||
|29||VccTx|+3.3V power supply transmitter|2B|2|
|30||Vcc1|+3.3V power supply|2B|2|
|31|LVTTL-I|LPMode/TxDIS|Low power mode/Optional Tx disable|3B||
|32||GND|Ground|1B|1|
|33|CML-I|Tx3p|Transmitter non-inverted data input|3B||
|34|CML-I|Tx3n|Transmitter inverted data input|3B||
|35||GND|Ground|1B|1|
|36|CML-I|Tx1p|Transmitter non-inverted data input|3B||
|37|CML-I|Tx1n|Transmitter inverted data input|3B||
|38||GND|Ground|1B|1|
|39||GND|Ground|1A|1|
|40|CML-I|Tx6n|Transmitter inverted data input|3A||
|41|CML-I|Tx6p|Transmitter non-inverted data input|3A||
|42||GND|Ground|1A|1|
|43|CML-I|Tx8n|Transmitter inverted data input|3A||
|44|CML-I|Tx8p|Transmitter non-inverted data input|3A||
|45||GND|Ground|1A|1|
|46|LVCMOS/CML-I|P/VS4|Programmable/Module vendor specific 4|3A|5|



4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


|Pin|Logic|Symbol|Description|Plug<br>Sequence3|Notes|
|---|---|---|---|---|---|
|47|LVCMOS/CML-I|P/VS1|Programmable/Module vendor specific 1|3A|5|
|48||VccRx1|+3.3V power supply|2A|2|
|49|LVCMOS/CML-O|P/VS2|Programmable/Module vendor specific 2|3A|5|
|50|LVCMOS/CML-O|P/VS3|Programmable/Module vendor specific 3|3A|5|
|51||GND|Ground|1A|1|
|52|CML-O|Rx7p|Receiver non-inverted data output|3A||
|53|CML-O|Rx7n|Receiver inverted data output|3A||
|54||GND|Ground|1A|1|
|55|CML-O|Rx5p|Receiver non-inverted data output|3A||
|56|CML-O|Rx5n|Receiver inverted data output|3A||
|57||GND|Ground|1A|1|
|58||GND|Ground|1A|1|
|59|CML-O|Rx6n|Receiver inverted data output|3A||
|60|CML-O|Rx6p|Receiver non-inverted data output|3A||
|61||GND|Ground|1A|1|
|62|CML-O|Rx8n|Receiver inverted data output|3A||
|63|CML-O|Rx8p|Receiver non-inverted data output|3A||
|64||GND|Ground|1A|1|
|65||NC|No connect|3A|3|
|66||Reserved|For future use|3A|3|
|67||VccTx1|+3.3V power supply|2A|2|
|68||Vcc2|+3.3V power supply|2A|2|
|69|LVCMOS-I|ePPS/Clock|1PPS PTP clock or reference clock input|3A|6|



10 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


|Pin|Logic|Symbol|Description|Plug<br>Sequence3|Notes|
|---|---|---|---|---|---|
|70||GND|Ground|1A|1|
|71|CML-I|Tx7p|Transmitter non-inverted data input|3A||
|72|CML-I|Tx7n|Transmitter inverted data input|3A||
|73||GND|Ground|1A|1|
|74|CML-I|Tx5p|Transmitter non-inverted data input|3A||
|75|CML-I|Tx5n|Transmitter inverted data input|3A||
|76||GND|Ground|1A|1|



Notes: 

1. QSFP-DD uses common ground (GND) for all signals and supply ( power). All are common within the QSFP-DD module and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host board signal-common ground plane. Each connector GND contact is rated for a maximum current of 500 mA. 

2.  VccRx, VccRx1, Vcc1, Vcc2, VccTx and VccTx1 shall be applied concurrently. Each connector Vcc contact is rated for a   maximum current of 1500 mA. 

3.  Reserved and No Connect pads recommended to be terminated with 10 kΩ to ground on the host. Pad 65 ( No Connect)  shall be left unconnected within the module. 

4.  Plug Sequence specifies the mating sequence of the  host connector and module. The sequence is 1A, 2A, 3A, 1 B, 2 B, 3 B. Contact sequence A will make, then break contact with additional QSFP-DD pads. Sequence 1A and 1 B will then occur simultaneously, followed by 2A and 2 B, followed by 3A and 3 B. 

5.  On new designs not used P/VSx signals are recommended to be terminated on the host with 10 kΩ . 

6.  ePPS/Clock if not used recommended to be terminated with 50 Ω to ground on the host. 

www.fs.com                                                                                                                                                                                                                                                                                                                                     11 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## VIII. Optical Characteristics 

## A. General 

|Parameter|Conditions|Symbol|Min|Typ|Max|Unit|Notes|
|---|---|---|---|---|---|---|---|
|Symbol Rate||Rbaud|30.07||60.14|GBd||
|Modulation Format|||16QAM, 8QAM, QPSK|||||
|Channel Frequency Range||νC|191.300||196.100|THz||
|Channel Spacing|Flexible grid|∆νC|6.25|100||GHz||
|Frequency Accuracy||δνC|-1.5||1.5|GHz||
|Frequency Fine Tune Range|Fine tuning with Tx output enabled<br>(bright tuning)|νadj|-6.25||6.25|GHz||
|Frequency Fine Tune Resolution|||||0.10|GHz||
|Laser Intrinsic Linewidth|Calculated based on FM noise power<br>spectral density (PSD) measurement|<br>LW|||300|kHz||
|Side-mode Suppression Ratio|No modulation|SMSR|40|||dB||
|IRelative Intensity Noise|Peak over 0.2GHz < f < 10GHz|RIN|||-140|dB/Hz||
||Average over 0.2GHz < f < 10GHz||||-145|||



## B. Transmitter 

|Parameter<br>Tx Output Power Configurable<br>Range<br>Tx Output Power Adjustment<br>Resolution<br>Tx Output Power Tolerance<br>Tx Output Power Monitor Range<br>Tx Output Power Monitor<br>Accuracy<br>Tx Output Power During Tuning<br>or When Tx Disabled<br>Tx Output Power Imbalance<br>Between X- and Y-polarizations|Conditions|Symbol|Min|Typ|Max|Unit|Notes|
|---|---|---|---|---|---|---|---|
|||PTx,out|-6|0|1|dBm|1|
||||||0.1|dB||
|||δPTx,out|-1.0||1.0|dB|2|
|||PTx,m|-8||2|dBm||
|||δPTx, m|-1.0||1.0|dB|3|
|||PTx,dark|||-40|dBm||
|||∆PX/Y|||1.0|dB||



www.fs.com                                                                                                                                                                                                                                                                                                                                     12 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


|Parameter|Conditions|Conditions|Symbol|Min|Typ|Max|Unit|Notes|
|---|---|---|---|---|---|---|---|---|
|Tx XY Skew||||||5.0|ps||
|Tx IQ Offset||||||-26|dB||
|Tx IQ Imbalance||||||0.8|dB||
|Tx Quadrature Error||||-5.0||5.0|°||
|Tx IQ Skew||||||0.75|ps||
|Tx In-band Optical Signal to<br>Noise Ratio|Under modulation, |Δf| < 150 GHz||OSNRin|43|||dB/<br>0.1nm||
|Tx Out-of-band Optical Signal to<br>Noise Ratio|Under modulation,<br>|Δf| > 150 GHz,<br>excluding side<br>mode peaks|<br>Max PTx,out|OSNRout|43|||dB/<br>0.1nm||
|||Min PTx,out||40|||||
|Tx Reflectance||||||-27|dB||



## Note: 

1.  Range of target Tx output power values for which other Tx specifications can be maintained. 

2.  Deviation from target value under closed loop control, over all operating conditions and life. 

3.  Tx optical output power monitor reading relative to actual Tx output power. 

## C. Receiver 

|Parameter|Conditions|Conditions|Symbol|Min|Typ|Max|Unit|Notes|
|---|---|---|---|---|---|---|---|---|
|Rx Total Input Power|||PRx,tot|-30||13|dBm||
|Rx Signal Input Power<br>(amplified)|Full Rx OSNR tolerance||PRx,sig|-12||0|dBm||
||Extended range|ZRx00-OFEC||-18||3||1|
|||400ZR||-15||3|||
|Rx OSNR Tolerance||ZR400-OFEC-16QAM||23.5|||dB/<br>0.1nm||
|||ZR300-OFEC-8QAM||20.0|||||
|||ZR200-OFEC-QPSK||15.0|||||
|||ZR100-OFEC-QPSK||12.0|||||
|||400ZR||26.0|||||



www.fs.com                                                                                                                                                                                                                                                                                                                                     13 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


|Parameter|Conditions|Conditions|Symbol|Min|Typ|Max|Unit|Notes|
|---|---|---|---|---|---|---|---|---|
|CD Tolerance|OSNR penalty<br>< 0.5dB|ZR400-OFEC-16QAM|||||ns/nm|2|
|||||||12.0|||
|||ZR300-OFEC-8QAM||||18.0|||
|||ZR200-OFEC-QPSK||||24.0|||
|||ZR100-OFEC-QPSK||||48.0|||
|||400ZR||-2.4||2.4|||
|PMD Tolerance|OSNR penalty<br>< 0.5dB|ZR400-OFEC-16QAM||||20|ps|2|
|||ZR300-OFEC-8QAM||||25|||
|||ZR200-OFEC-QPSK||||25|||
|||ZR100-OFEC-QPSK||||30|||
|||400ZR||||10|||
|Tolerance to Change in SOP|OSNR penalty<br>< 0.5dB|ZR400-OFEC-16QAM||||100|krad/s|2|
|||ZR300-OFEC-8QAM||||180|||
|||ZR200-OFEC-QPSK||||300|||
|||ZR100-OFEC-QPSK||||600|||
|||400ZR||||60|||
|Polarization Dependent Loss<br>OSNR Penalty|QPSK|1dB PDL||||0.3|dB|2|
|||2dB PDL||||0.5|||
|||4dB PDL||||1.5|||
||8QAM, 16QAM|1dB PDL||||0.5|||
|||<br>2dB PDL||||1.0|||
|||4dB PDL||||2.0|||
|Rx Signal Input Power Transient<br>Amplitude|Peak excursion from steady state<br>(within Rx signal input power range)|||-7||7|dB||
|Rx Signal Input Power Transient<br>Rise/Fall Time||||0.1|||ms||
|Rx Signal Input Power<br>(unamplified)|OSNR ><br>35dB/0.1nm|ZR400-OFEC-16QAM||-23||0|dBm||
|||ZR300-OFEC-8QAM||-26||0|||
|||ZR200-OFEC-QPSK||-30||0|||
|||ZR100-OFEC-QPSK||-32||0|||
|||400ZR||-20||0|||



www.fs.com                                                                                                                                                                                                                                                                                                                                     14 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


|Parameter|Conditions|Conditions|Symbol|Min|Typ|Max|Unit|Notes|
|---|---|---|---|---|---|---|---|---|
|Rx Signal Input Power Monitor<br>Range|||PRx,m(s)|-22||1|dBm||
|Rx Signal Input Power Monitor<br>Accuracy|||δPRx, m(s)|-2.0||2.0|dB||
|Rx Total Input Power Monitor<br>Range|||PRx,m(t)|-22||13|dBm||
|Rx Total Input Power Monitor<br>Accuracy||-22dBm to -18dBm|δPRx, m(t)|-2.0||2.0<br>1.5<br>2.0|dB||
|||-18dBm to +3dBm||-1.5|||||
|||+3dBm to + 13dBm||-2.0|||||
|Rx Reflectance||||||-27|dB||



## Note: 

1. Rx signal input power range over which performance can be guaranteed with < 1dB OSNR penalty relative to Rx OSNR  tolerance limit. 

2. Rx OSNR penalty is specified for Rx signal input powers < 0dBm. 

## IX. Module Management Timing Characteristics 

|Parameter|Conditions|Symbol|Min|Typ|Max|Unit|Notes|
|---|---|---|---|---|---|---|---|
|Optical||||||||
|Tx Turn on Time|Warm start||||100|ms||
||Cold start||||150|s||
|Rx Acquisition Time|Warm start||||30|ms||
||Cold start||||150|s||
|Tx/Rx Channel<br>Tuning Time|||||30|s||
|Soft Control and Status Functions||||||||
|MgmtInit Duration|Time from poweron1 , hot plug or rising edge of reset until<br>completion of the MgmtInit State||||2000|ms|1|
|ResetL Assert Time|Minimum pulse time on the ResetL signal to initiate a module<br>reset.||10|||µs||
|IntL/RxLOS Mode<br>Change Time|Time to change between IntL and RxLOSL modes ofthe dual-<br>mode signal IntL/RxLOSL.||||100|ms||



www.fs.com                                                                                                                                                                                                                                                                                                                                     15 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


|Parameter<br>Conditions<br>Symbol<br>Min<br>Typ<br>Max<br>Unit<br>Notes|Parameter<br>Conditions<br>Symbol<br>Min<br>Typ<br>Max<br>Unit<br>Notes|Parameter<br>Conditions<br>Symbol<br>Min<br>Typ<br>Max<br>Unit<br>Notes|Parameter<br>Conditions<br>Symbol<br>Min<br>Typ<br>Max<br>Unit<br>Notes|Parameter<br>Conditions<br>Symbol<br>Min<br>Typ<br>Max<br>Unit<br>Notes|Parameter<br>Conditions<br>Symbol<br>Min<br>Typ<br>Max<br>Unit<br>Notes|Parameter<br>Conditions<br>Symbol<br>Min<br>Typ<br>Max<br>Unit<br>Notes|Parameter<br>Conditions<br>Symbol<br>Min<br>Typ<br>Max<br>Unit<br>Notes||
|---|---|---|---|---|---|---|---|---|
|Soft Control and Status Functions|||||||||
|LPMode/TxDis Mode<br>Change Time|Time to change between  LPMode and TxDis modes ofthe<br>LPMode/TxDis signal.||||100|ms|||
|IntL Assert Time|Time from occurrence of condition triggering IntL until<br>Vout:IntL=Vol||||200|ms|||
|IntL Deassert Time|Time from clear on read2 operation of  associated flag until<br>Vout:IntL=Voh. This  includes deassert times for Rx LOS, Tx<br>Fault and other flag bits.||||500|µs|2||
|RxLOS Assert Time|Time from Rx LOS condition present to Rx  LOS bit set (value =<br>1b) and IntL asserted3.||||1|ms|3||
|RxLOS Deassert Time|Time from optical signal above the LOS  deassert threshold to<br>when the module  releases the RxLOS signal to high.||||15|ms|||
|Tx Disable Assert<br>Time|Time from Tx Disable bit set (value = 1b)4 until optical output<br>falls below 10% of nominal||||1|ms|4||
|Tx Disable Deassert<br>Time|Time from Tx Disable bit cleared (value = 0b)4 until optical<br>output rises above 90% of nominal||||100|ms|4||
|Tx Fault Assert Time|Time from Tx Fault state to Tx Fault bit set (value= 1b) and IntL<br>asserted.||||200|ms|||
|Flag Assert Time|Time from occurrence of condition triggering flag to<br>associated flag bit set (value= 1b) and IntL asserted.||||200|ms|||
|Mask Assert Time|Time from mask bit set (value= 1b)5  until associated IntL<br>assertion is inhibited.||||100|ms|5||
|Mask Deassert Time|Time from mask bit cleared (value=0b)5 until associated IntL<br>operation resumes.||||100|ms|5||
|Data Path Tx Turn On<br>Max Duration6|Maximum duration of Tx Turn On state.||see CMIS memory<br>01h:168||||6||
|Data Path Tx Turn Off<br>Max Duration6|Maximum duration of Tx Turn Off state.||see CMIS memory<br>01h:168||||6||
|Data Path Deinit Max<br>Duration6|Maximum duration of Data Path DeInit state.||see CMIS memory<br>01h:144||||6||
|Data Path Init Max<br>Duration6|Maximum duration of Data Path Init state.||see CMIS memory<br>01h:144||||6||
|Module Pwr Up Max<br>Duration7|Maximum duration of Module Pwr Up state.||see CMIS memory<br>01h:167||||7||
|Module Pwr Dn Max<br>Duration7|Maximum duration of Module Pwr Dn state.||see CMIS memory<br>01h:167||||7||



www.fs.com                                                                                                                                                                                                                                                                                                                                     16 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


|Parameter|Conditions|Symbol|Min|Typ|Max|Unit|Notes|
|---|---|---|---|---|---|---|---|
|I/O Timing for Squelch & Disable||||||||
|Rx Squelch Assert<br>Time|Time from loss of Rx input signal until the squelched output<br>condition is reached.||||15|ms||
|Rx Squelch Deassert<br>Time|Time from resumption of Rx input signals until normal Rx<br>output condition is reached.||||50|ms||
|Tx Squelch Assert<br>Time|Time from loss ofTx input signal until the squelched output<br>condition is reached.||||400|ms||
|Tx Squelch Deassert<br>Time|Time from resumption of Tx input signal until the normal Tx<br>output condition is  reached.||||1.5|s||
|Rx Output Disable<br>Assert Time|Time from Rx Output Disable bit set (value= 1b)4 until Rx<br>output falls below 10% of  nominal||||100|ms|4|
|Rx Output Disable<br>Deassert Time|Time from Rx Output Disable bit cleared  (value = 0b)4 until Rx<br>output rises above 90% of nominal||||100|ms|4|
|Squelch Disable<br>Assert Time|This applies to Rx and Tx Squelch and is  the time from bit set<br>(value = 1b)4  until squelch functionality is disabled.||||100|ms|4|
|Squelch Disable<br>Deassert Time|This applies to Rx and Tx Squelch and is  the time from bit<br>cleared (value = 0b)4 until squelch functionality is enabled.||||100|ms|4|



## Note: 

1.  Power on is defined as the instant when supply voltages reach and remain at or above the minimum level specified. 

2.  Measured from low to high SDA edge of the Stop condition of the read transaction. 

3.   RxLOS condition is defined as (a) Rx input power below threshold or (b) DSP loss of signal. 

4.   Measured from LOW to HIGH SDA signal transition of the STOP condition of the write transaction. 

5.   Measured from low to high SDA edge of the Stop condition of the write transaction. 

6.   Measured from the low to high SDA edge of the Stop condition of the Write transaction until the IntL for the state change Vout:IntL=Vol, unless the module advertises a less than 1 ms duration in which case there is no defined measurement. 

7.    Measured from the low to high SDA edge of the Stop condition of the Write transaction until the IntL for the state change Vout:IntL=Vol. 

www.fs.com                                                                                                                                                                                                                                                                                                                                     17 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## X. Mechanical Specifications 


## XI. **References** 

1. IEEE Computer Society “IEEE Standard for  Ethernet”,  IEEE Std.  802.3[TM] -2022. 

2. OpenZ R+  MSA “Technical Specification”,  Revision  1.0  (September 4, 2020) . 

- 3 .  OIF “ Implementation Agreement 4 0 0ZR” ,  OIF- 4 0 0ZR- 0 1 . 0  ( March  1 0 ,  2 0 2 0 ) . 

4. QS FP-DD   MSA   “QS FP-DD/QS FP-DD800/QS FP 1 12   Hardware   Specification   for   QSFP   Double   Density 8 × and  QS FP 4 × Pluggable Transceivers”  Revision 6.01  ( May 28, 2021) . 

5. QSFP-DD ,   OSFP,   and  COBO  Advisory   Group   “Common  Management   Interface  Specification”  Revision  5. 1  ( November  2 ,  2 0 2 1 ) . 

6.   O IF “Implementation Agreement for Coherent CMIS ”, O IF-C-CMIS-01 .2 ( March 21, 2022) . 

7.   S NIA  “Specification  for  SFF   Module   Management   Reference  Code  Tables”,   SFF-8024   Rev  4.9  ( May 24 ,  2021) . 

8.   Directive 201 1/65/EU of the  European  Parliament and of the Council, “on the  restriction  of the  use  of certain  hazardous  substances  in electrical and electronic equipment” as well as Commission 

Delegated  Directive ( EU) 2015/863 amending Annex  II to  Directive  201 1/65/EU.  Certain  products    may  use  one or  more exemptions as allowed  by the  Directive. 

9.  Application  Note AN-2038: “Implementation of RoHS Compliant Transceivers ”. 

www.fs.com                                                                                                                                                                                                                                                                                                                                     18 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## Test Center 

## I.CompatibilityTesting 

Each fiber optical transceiver has been tested in host device on site in FS Assured Program to ensure full compatibility with over 200  vendors. 



Cisco Nexus9000 C 9316 D-GX 

Arista- DCS- 7 2 8 0 DR3 K- 2 4 - F 



Juniper PTX10 0 0 1- 3 6MR 

Juniper QFX 5 2 2 0 - 3 2cd 



Dell Z9332F-ON 

FS N9510-64D 

Above is partofour testbed network equipment. For more information, please click the Test Bed PDF. Itwillbe updated in realtime as  we expand our portfolio. 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## II. Test Assured Program 

FS.COM truly understands the value of compatibility and interoperability to each optics. Every module FS.COM provides must run  through programming and an extensive series of platform diagnostic tests to prove its performance and compatibility. In our test center, we care of every detail from staff to facilities-professionally trained staff, advanced test facilities and comprehensive original-brand switches, to ensure our customers to receivetheoptics withsuperior quality. 



Our smart data system allows effective product management and quality control according to the unique serial number, properly tracingtheorder, shipment and every part. 

O u r  i n - ho use  codi ng  faci lity  p rog ra ms  a l l  of o ur  parts  to standard OEM specs for compatibility on all major vendors and systems such as Cisco, Juniper, Brocade, HP, Dell, Arista and so on. 



With a comprehensive line of original-brand switches, we can recreate an  environment  and  test  each  optics  in  practical applicationto ensure quality and distance. 

The last test assured stepto ensure our products to be shipped with perfect package. 

4 0 0G  QS FP- DD  D CO  D WD M  T UNABLE  COHERENT  12 0KM  DOM  TRANSCEIVER 


## Ordering Information 

|Part Number||Description|
|---|---|---|
|||400G QSFP-DD DCO DWDM Tunable Coherent 450km DOM Transceiver ( EDFA)|
|QDD- ZRP- 4 0 0G- HT|||
|||4 0 0G QSFP- DD DCO Coherent 8 0 km DOM Transceiver ( 4 0 0G Gray Light)|
|Note:|||
|1.400ZRP mode.|||
|2.4 0 0G Gray Light mode,  unamplified|point|to point link.|



www.fs.com                                                                                                                                                                                                                                                                                                                                   21 

