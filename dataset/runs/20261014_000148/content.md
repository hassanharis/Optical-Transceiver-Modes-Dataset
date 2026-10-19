` 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-ER4C Rev1.0- Sep.2021 


## **LQ-LW100-ER4C** 

## 40km 100G QSFP28 ER4 Optical Transceiver Module 

## **Features:** 

- 4 lanes MUX/DEMUX design 

- Support 100GBASE-ER4 lite for line rate of 103.125Gbps and OTU4 for line rate of 111.81Gbps 

- Integrated LAN WDM EML TOSA /APD ROSA for up to 40 km reach over SMF without FEC 

- Aggregate bandwidth of > 100Gbps 

- Duplex LC connectors 

- Compliant with IEEE 802.3-2012 Clause 88 standard IEEE 802.3bm CAUI-4 chip to module electrical standard ITU-T G.959.1-2012-02 standard 

- Single +3.3V power supply operating 

- Built-in digital diagnostic functions 

- Temperature range 0°C to 70°C 

- RoHS compliant 

## **Applications** 

- 100GBASE-ER4 Ethernet Links 

- Infiniband QDR and DDR interconnects 


- Client-side 100G Telecom connections 

## **Description** 

The transceiver module designed for 40km without FEC optical communication applications. The design is compliant to 100GbASE-ER4 of the IEEE 802.3-2012 Clause88 standard IEEE 802.3bm CAUI-4 chip to module electrical standard ITU-T G.959.1-2012-02 standard . The module converts 4 inputs channels (ch) of 25.78Gbps/27.95Gbps electrical data to 4 lanes optical signals, and multiplexes them into a single channel for 100Gb/s optical transmission. Reversely, on the receiver side, the module optically de-multiplexes a 100Gb/s input into 4 lanes signals, and converts them to 4 lanes output electrical data. 

The central wavelengths of the 4 lanes are 1296 nm, 1300 nm, 1305 nm and 1309 nm . It contains a duplex LC connector for the optical interface and a 38-pin connector for the electrical interface. To minimize the optical dispersion in the long-haul system, single-mode fiber (SMF) has to be applied in this module. 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 1 of 10 

> www.l-p.com www.link-pp.com 

` 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-ER4C Rev1.0- Sep.2021 


The product is designed with form factor, optical/electrical connection and digital diagnostic interface according to the QSFP28 Multi-Source Agreement (MSA). It has been designed to meet the harshest external operating conditions including temperature, humidity and EMI interference. 

The module operates from a single +3.3V power supply and LVCMOS/LVTTL global control signals such as Module Present, Reset, Interrupt and Low Power Mode are available with the modules. A 2-wire serial interface is available to send and receive more complex control signals and to obtain digital diagnostic information. Individual channels can be addressed and unused channels can be shut down for maximum design flexibility. 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typical**|**Max.**|**Unit**|
|---|---|---|---|---|---|
|Storage Temperature|TS|-40||+85|°C|
|Supply Voltage|VCCT, R|-0.5||4|V|
|Relative Humidity|RH|0||85|%|



## **Recommended Operating Environment:** 

|**Parameter**|**Symbol**|**Min.**|**Typical**|**Max.**|**Unit**|
|---|---|---|---|---|---|
|Case operating Temperature|TC|0||+70|°C|
|Supply Voltage|VCCT, R|+3.13|3.3|+3.47|V|
|Supply Current|ICC||1000|1500|mA|
|Power Dissipation|PD|||5|W|



## **Electrical Characteristics (TOP = 0 to 70 °C, VCC = 3.13 to 3.47 Volts)** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Typ**|**Max**|**Max**|**Unit**|**Note**|
|---|---|---|---|---|---|---|---|---|
|Data Rate per Channel||-|25.78125||||Gbps||
||||27.9525||||||
|Power Consumption||-|3.3||5||W||
|Supply Current|Icc||1.0||1.5||A||
|Control I/O Voltage-High|VIH|2.0|||Vcc||V||
|Control I/O Voltage-Low|VIL|0|||0.7||V||
|Inter-Channel Skew|TSK||||35||Ps||
|RESETL Duration|||10||||Us||
|RESETL De-assert time|||||100||ms||
|Power On Time|||||100||ms||
||**Transmitter**||||||||
|Single Ended Output Voltage Tolerance||0.3||Vcc||V||1|



Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 2 of 10 

> www.l-p.com www.link-pp.com 

` 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LQ-LW100-ER4C Rev1.0- Sep.2021 

|Common mode Voltage Tolerance||15|||mV||
|---|---|---|---|---|---|---|
|Transmit Input Diff Voltage|VI|150||1200|mV||
|Transmit Input Diff Impedance|ZIN|85|100|115|||
|Data Dependent Input Jitter|DDJ||0.3||UI||
|**Receiver**|||||||
|Single Ended Output Voltage Tolerance||0.3||4|V||
|Rx Output Diff Voltage|Vo|370|600|950|mV||
|Rx Output Rise and Fall Voltage|Tr/Tf|||35|ps|1|
|Total Jitter|TJ||0.3||UI||



Note: 

1. 20～80% 

## **Optical Parameters(TOP = 0 to 70 °C, VCC = 3.0 to 3.6 Volts)** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Max**|**Unit**|**Unit**|**Ref.**|
|---|---|---|---|---|---|---|---|---|
||**Transmitter**||||||||
|Wavelength Assignment|L0|1294.53|1295.56||1296.59||nm||
||L1|1299.02|1300.05||1301.09||nm||
||L2|1303.54|1304.58||1305.63||nm||
||L3|1308.09|1309.14||1310.19||nm||
|Side-mode Suppression Ratio|SMSR|30|-||-||dB||
|Total Average Launch Power|PT|0|-||8.3||dBm||
|Average Launch Power, each Lane||-2|-||4||dBm||
|Difference in Launch Power between any two<br>Lanes(OMA)||-|-||6.5||dB||
|Optical Modulation Amplitude, each Lane|OMA|-4|||4.5||dBm||
|Launch Power in OMA minus Transmitter and<br>Dispersion Penalty (TDP),each Lane||-4.8|-||||dBm||
|TDP, each Lane|TDP||||2.2||dB||
|Extinction Ratio|ER|8|-||-||dB||
|Transmitter Eye Mask Definition {X1, X2, X3,<br>Y1, Y2, Y3}||{0.25, 0.4,<br>0.45, 0.25,<br>0.28,0.4}|||||||
|Optical Return Loss Tolerance||-|-||20||dB||
|Average Launch Power OFF Transmitter, each<br>Lane|Poff||||-30||dBm||
|Relative Intensity Noise|Rin||||-128||dB/HZ|1|
|Optical Return Loss T Total||-|-||12||dB||
||**Receiver**||||||||



Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 3 of 10 

> www.l-p.com www.link-pp.com 

` 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LQ-LW100-ER4C Rev1.0- Sep.2021 

|Damage Threshold per Lane|THd|-6|||dBm|1|
|---|---|---|---|---|---|---|
|Overload per Lane|R|-7|||dBm|1|
|Receiver Sensitivity per Lane|R|||-16|dBm|2|
||R|||-21|dBm|3|
|Average Power at Receiver Input, each Lane|R|-22||-7|dBm|3|
|RSSI Accuracy||-2||2|dB||
|Receiver Reflectance|Rrx|||-26|dB||
|Receiver Power (OMA), each Lane||-|-|-3|dBm||
|LOS De-Assert|LOSD|||-25|dBm||
|LOS Assert|LOSA|-35|||dBm||
|LOS Hysteresis|LOSH|0.5|||dB||



## **Note:** 

1. 12dB Reflection 

2. Without FEC 

3. With FEC 

## **Diagnostic Monitoring Interface** 

Digital diagnostics monitoring function is available on all QSFP28 ER4. A 2-wire serial interface provides user to contact with module. The structure of the memory is shown in flowing. The memory space is arranged into a lower, single page, address space of 128 bytes and multiple upper address space pages. This structure permits timely access to addresses in the lower page, such as Interrupt Flags and Monitors. Less time critical time entries, such as serial ID information and threshold settings, are available with the Page Select function. The interface address used is A0xh and is mainly used for time critical data like interrupt handling in order to enable a one-time-read for all data related to an interrupt situation. After an interrupt, IntL has been asserted, the host can read out the flag field to determine the affected channel and type of flag. 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 4 of 10 

> www.l-p.com www.link-pp.com 

` 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-ER4C Rev1.0- Sep.2021 



**Timing for Soft Control and Status Functions** 

|**Parameter**|**Symbol**|**Max**|**Unit**|**Conditions**|
|---|---|---|---|---|
|Initialization Time|t_init|2000|ms|Time from power on1, hot plug or rising edge of<br>Reset until the module is fullyfunctional2|
|Reset Init Assert Time|t_reset_init|2|μs|A Reset is generated by a low level longer than the<br>minimum resetpulse timepresent on the ResetLpin.|
|Serial Bus Hardware Ready<br>Time|t_serial|2000|ms|Time from power on1 until module responds to data<br>transmission over the 2-wire serial bus|
|Monitor Data Ready<br>Time|t_data|2000|ms|Time from power on1 to data not ready, bit 0 of Byte<br>2,deasserted and IntL asserted|
|Reset Assert Time|t_reset|2000|ms|Time from rising edge on the ResetL pin until the<br>module is fullyfunctional2|
|LPMode Assert Time|ton_LPMode|100|μs|Time from assertion of LPMode (Vin:LPMode =Vih)<br>until module power consumption enters lower Power<br>Level|
|IntL Assert Time|ton_IntL|200|ms|Time from occurrence of condition triggering IntL|



Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 5 of 10 

> www.l-p.com www.link-pp.com 

` 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LQ-LW100-ER4C Rev1.0- Sep.2021 

|||||until Vout:IntL = Vol|
|---|---|---|---|---|
|IntL Deassert Time|toff_IntL|500|μs|toff_IntL 500 μs Time from clear on read3 operation<br>of associated flag until Vout:IntL = Voh. This includes<br>deassert times for Rx LOS, Tx Fault and other flag<br>bits.|
|Rx LOS Assert Time|ton_los|100|ms|Time from Rx LOS state to Rx LOS bit set and IntL<br>asserted|
|Flag Assert Time|ton_flag|200|ms|Time from occurrence of condition triggering flag to<br>associated flagbit set and IntL asserted|
|Mask Assert Time|ton_mask|100|ms|Time from mask bit set4 until associated IntL<br>assertion is inhibited|
|Mask De-assert Time|toff_mask|100|ms|Time from mask bit cleared4 until associated IntlL<br>operation resumes|
|ModSelL Assert Time|ton_ModSelL|100|μs|Time from assertion of ModSelL until module<br>responds to data transmission over the 2-wire serial<br>bus|
|ModSelL Deassert Time|toff_ModSelL|100|μs|Time from deassertion of ModSelL until the module<br>does not respond to data transmission over the 2-<br>wire serial bus|
|Power_over-ride or<br>Power-set Assert Time|ton_Pdown|100|ms|Time from P_Down bit set 4 until module power<br>consumption enters lower Power Level|
|Power_over-ride or<br>Power-set De-assert Time|toff_Pdown|300|ms|Time from P_Down bit cleared4 until the module is<br>fullyfunctional3|



Note： 

1. Power on is defined as the instant when supply voltages reach and remain at or above the minimum specified value. 

2. Fully functional is defined as IntL asserted due to data not ready bit, bit 0 byte 2 de-asserted. 

3. Measured from falling clock edge after stop bit of read transaction. 

4. Measured from falling clock edge after stop bit of write transaction. 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 6 of 10 

> www.l-p.com www.link-pp.com 

` 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-ER4C Rev1.0- Sep.2021 


## **Transceiver Block Diagram** 


## **Pin Assignment** 


Diagram of Host Board Connector Block Pin Numbers and Name 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 7 of 10 

> www.l-p.com www.link-pp.com 

` 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-ER4C Rev1.0- Sep.2021 


## **Pin Description** 

|**Pin**|**Logic**|**Symbol**|**Name/Description**|**Ref.**|
|---|---|---|---|---|
|1||GND|Ground|1|
|2|CML-I|Tx2n|Transmitter Inverted Data Input||
|3|CML-I|Tx2p|Transmitter Non-Inverted Data output||
|4||GND|Ground|1|
|5|CML-I|Tx4n|Transmitter Inverted Data Output||
|6|CML-I|Tx4p|Transmitter Non-Inverted Data Output||
|7||GND|Ground|1|
|8|LVTTL-I|ModSelL|Module Select||
|9|LVTTL-I|ResetL|Module Reset||
|10||VccRx|+3.3V Power Supply Receiver|2|
|11|LVCMOS-I/O|SCL|2-Wire Serial Interface Clock||
|12|LVCMOS-I/O|SDA|2-Wire Serial Interface Data||
|13||GND|Ground|1|
|14|CML-O|Rx3p|Receiver Inverted Data Output||
|15|CML-O|Rx3n|Receiver Non-Inverted Data Output||
|16||GND|Ground|1|
|17|CML-O|Rx1p|Receiver Inverted Data Output||
|18|CML-O|Rx1n|Receiver Non-Inverted Data Output||
|19||GND|Ground|1|
|20||GND|Ground|1|
|21|CML-O|Rx2n|Receiver Inverted Data Output||
|22|CML-O|Rx2p|Receiver Non-Inverted Data Output||
|23||GND|Ground|1|
|24|CML-O|Rx4n|Receiver Inverted Data Output||
|25|CML-O|Rx4p|Receiver Non-Inverted Data Output||
|26||GND|Ground|1|
|27|LVTTL-O|ModPrsL|Module Present||
|28|LVTTL-O|IntL|Interrupt||
|29||VccTx|+3.3V Power Supply Transmitter|2|
|30||Vcc1|+3.3V Power Supply|2|
|31|LVTTL-I|LPMode|Low Power Mode||
|32||GND|Ground|1|



Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 8 of 10 

> www.l-p.com www.link-pp.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

` 


LQ-LW100-ER4C Rev1.0- Sep.2021 

|33|CML-I|Tx3p|Transmitter Inverted Data Output||
|---|---|---|---|---|
|34|CML-I|Tx3n|Transmitter Non-Inverted Data Output||
|35||GND|Ground|1|
|36|CML-I|Tx1p|Transmitter Inverted Data Output||
|37|CML-I|Tx1n|Transmitter Non-Inverted Data Output||
|38||GND|Ground|1|



## **Notes:** 

1. GND is the symbol for single and supply(power) common for QSFP28 modules, All are common within the QSFP28 module and all module voltages are referenced to this potential otherwise noted. Connect these directly to the host board signal common ground plane. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

2. VccRx, Vcc1 and VccTx are the receiver and transmitter power suppliers and shall be applied concurrently. Recommended host board power supply filtering is shown below. VccRx, Vcc1 and VccTx may be internally connected within the QSFP28 transceiver module in any combination. The connector pins are each rated for maximum current of 500mA. 

## **Recommended Circuit** 


Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 9 of 10 

> www.l-p.com www.link-pp.com 

` 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-ER4C Rev1.0- Sep.2021 


## **Mechanical Dimensions** 


## **Ordering Information** 

|**Part Number**|**Description**|
|---|---|
|LQ-LW100-ER4C|103.1G, SMF, LWDM, 40km, QSFP28, LC, 0~70℃,DDM|
|LQ-LW100-ER4I|103.1G, SMF, LWDM, 40km, QSFP28, LC, -40~85℃,DDM|



Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 10 of 10 

> www.l-p.com www.link-pp.com 

