LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW200-FR4C Rev1.0- Sep.2022 


## **LQ-CW200-FR4C** 

## 200GBASE-FR4 QSFP56, Optical Transceiver Module, 2km Reach 

## **Features** 

- IEEE 802.3-2018 200GE FR4 specification compliant 

- 4 CWDM lanes MUX/DEMUX design 

- 4x 53.125 Gbps PAM4 electrical interface (200GAUI-4, CEI-56G-VSR-PAM4) 

- Non-hermetic package design 

- Maximum power consumption 6.0 W 

- LC duplex connector 

- 212.5 Gbps aggregate bit rate 

- Up to 2 km transmission on single mode fiber with FEC 

- Operating case temperature: 0 to 70℃ 

- Single 3.3 V power supply 

- I2C digital management interface 

- Hardware SFF-8679 Rev 1.8 compliant 

- Software QSFP-DD CMIS Rev 4.0 compliant 

- RoHS 2 compliant 

## **Applications** 

- IEEE 802.3bs 200GBASE-FR4 Ethernet (PAM4) 

- 5G Back-haul 

- Data center 


## **Description** 

LINK-PP LQ-CW200-FR4C 200GE QSFP56 Optical Transceiver is a QSFP56 transceiver module designed for 2km optical communication applications with single mode fiber. It is compliant with IEEE 802.3-2018 200GBASE FR4, SFF-8679, and CEI-56G-VSR-PAM4 standards. Digital diagnostic management interface (DDMI) is realized by I2C interface in compliance with CMIS4. The module is RoHS 2 compliant. 

The module can convert 4-channel 53.125 Gbps electrical data to 4-channel optical signals, and multiplex them 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2022 LINK-PP AlI Rights Reserved 

Page 1 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW200-FR4C Rev1.0- Sep.2022 


into a single channel for 212.5 Gbps optical transmission. Similarly, it optically de-multiplexes a 212.5 Gbps input into 4-channel signals, and converts them to 4-channel output electrical data on the receiver side. It has been designed to meet the harshest external operating conditions including temperature, humidity and EMI interference. A block diagram is shown in belowpicture. 


Figure 1. Transceiver block diagram 

## **Absolute Maximum Ratings** 

It has to be noted that the operation in excess of any individual absolute maximum ratings might cause permanent damage to this module. 

|**Parameter**|**Symbol**|**Min**|**Typ.**|**Max**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Maximum supply voltage|Vcc|-0.3|3.3|3.6|V||
|Storage temperature|Ts|-40||85|°C||
|Relative humidity|RH|0||85|%|Non-condensing|
|Damage threshold, each lane|THd|5.7|||dBm||



## **Operating Environments** 

Electrical and optical characteristics below are defined under this operating environment, unless otherwise specified. 

|**Parameter**<br>|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|---|
|Supply voltage|Vcc|3.135|3.3|3.465|V|
|Case temperature|T|0||70|°C|
|Signaling rate, each lane|||26.5625||GBd|
|Data rate accuracy||-100||100|ppm|
|Link distance with G.652||2||2000|m|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2022 LINK-PP AlI Rights Reserved 

Page 2 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW200-FR4C Rev1.0- Sep.2022 


## **Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|Power dissipation||||6.0|W||
|Supply current|Icc|||1.9138|A||
|**Transmitter (module output)**|||||||
|Signaling rate per lane (range)||26.5625 ± 100 ppm|||GBd||
|Differential voltage pk-pk|Vpp|||900|mV|At 1 MHz|
|Common mode voltage|Vcm|-350||2850|mV||
|Common mode noise, RMS||||17.5|mV||
|Differential termination resistance<br>mismatch||||10|%||
|Differential return loss|SDD22|Complaint to CEI-56G-VSR-PAM4|||||
|Common mode to differential mode<br>conversion|SDC22|Complaint to CEI-56G-VSR-PAM4|||||
|Transition time|Trise/Tf all|9.5|||ps|20%~80%|
|Near-end eye width at 10-6<br>probability|EW6|0.265|||UI||
|Near-end eye height at 10-6<br>probability|EH6|70|||mV||
|Far-end eye width at 10-6<br>probability|EW6|0.2|||UI||
|Far-end eye height at 10-6<br>probability|EH6|30|||mV||
|Near-end eye linearity||0.85|||||
|**Receiver (module input)**|||||||
|Signaling rate per lane (range)||26.5625 ± 100 ppm|||GBd||
|Overload differential voltage pk-pk|Vpp|900|||mV||



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2022 LINK-PP AlI Rights Reserved 

Page 3 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LQ-CW200-FR4C Rev1.0- Sep.2022 

|Common mode voltage|Vcm|-350||2850|mV||
|---|---|---|---|---|---|---|
|Differential termination||||10|%|At 1 MHz|
|resistance mismatch|||||||
|Differential return loss|SDD11|Complaint to CEI-56G-VSR-PAM4|||||
|Differential mode to common mode<br>conversion|SCD11|Complaint to CEI-56G-VSR-PAM4|||||
|Stressed input test||Complaint to CEI-56G-VSR-PAM4|||||



## **Optical Characteristics** 

|**Parameters**|**Unit**|**Min.**|**Typ.**|**Max.**|
|---|---|---|---|---|
||**Transmitter**||||
|Signaling rate, each lane|GBd|26.5625 ± 100 ppm|||
|Total average launch power|dBm|||10.7|
|Average launch power, each lane|dBm|-4.2||4.7|
|Line wavelengths|nm|1264.5||1277.5|
|||1284.5||1297.5|
|||1304.5||1317.5|
|||1324.5||1337.5|
|Optical modulation amplitude(OMAouter),each lane|<br>dBm|-1.2||4.5|
|Difference in launch power between any two lanes<br>(OMAouter)|dB|||4|
|Extinction ratio (ER)|dB|3.5|||
|Side-mode suppression ratio (SMSR)|dB|30|||
|Launch power in OMAouter mi-nus TDECQ, each lane<br>for extinction ratio > = 4.5 dB<br>for extinction ratio < 4.5 dB|dBm|-2.6<br>-2.5|||
|Transmitter and dispersion eye closure for PAM4<br>(TDECQ), each lane|dB|||3.3|
|Average launch power of OFF transmitter, each lane|dBm|||-30|
|Optical return loss tolerance|dB|||17.1|
|Transmitter reflectance|dB|||-26|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2022 LINK-PP AlI Rights Reserved 

Page 4 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LQ-CW200-FR4C Rev1.0- Sep.2022 

|**Receiver**|**Receiver**||||
|---|---|---|---|---|
|Signaling rate, each lane|GBd|26.5625 ± 100 ppm|||
|Line wavelengths|nm|1264.5||1277.5|
|||1284.5||1297.5|
|||1304.5||1317.5|
|||1324.5||1337.5|
|Average receiver power, each lane|dBm|-8.2||4.7|
|Receiver power, each lane (OMA)|dBm|||4.5|
|Damage threshold, each lane|dBm|5.7|||
|Difference in receive power between any two<br>lanes(OMAouter)|dB|||4.1|
|Receiver sensitivity (OMA), each lane|dBm|||max (-5.5,<br>SECQ-6.9)|
|Receiver reflectance|dB|||-26|
|Stressed receiver Sensitivity (OMA), each lane|dBm|||-3.6|
|**Conditions of stressed receiver sensitivity**|||||
|Stressed eye closure for PAM4 (SECQ), lane under<br>test|dB||3.3||
|OMAouter of each aggressor lane|dBm||0.5||



## **Pin Description** 

|1|GND|Ground|1|
|---|---|---|---|
|2|Tx2n|Transmitter Inverted Data Input||
|3|Tx2p|Transmitter Non-Inverted Data Input||
|4|GND|Ground|1|
|5|Tx4n|Transmitter Inverted Data Input||
|6|Tx4p|Transmitter Non-Inverted Data Input||



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Page 5 of 8 

Copyright © 2022 LINK-PP AlI Rights Reserved 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LQ-CW200-FR4C Rev1.0- Sep.2022 

|7|GND|Ground|1|
|---|---|---|---|
|8|ModSelL|Module Select||
|9|ResetL|Module Reset||
|10|VccRx|+3.3 V Power Supply Receiver|2|
|11|SCL|2-wire Serial Interface Clock||
|12|SDA|2-wire Serial Interface Data||
|13|GND|Ground|1|
|14|Rx3p|Receiver Non-Inverted Data Output||
|15|Rx3n|Receiver Inverted Data Output||
|16|GND|Ground|1|
|17|Rx1p|Receiver Non-Inverted Data Output||
|18|Rx1n|Receiver Inverted Data Output||
|19|GND|Ground|1|
|20|GND|Ground|1|
|21|Rx2n|Receiver Inverted Data Output||
|22|Rx2p|Receiver Non-Inverted Data Output||
|23|GND|Ground|1|
|24|Rx4n|Receiver Inverted Data Output||
|25|Rx4p|Receiver Non-Inverted Data Output||
|26|GND|Ground|1|
|27|ModPrsL|Module Present||
|28|IntL/RxLOS|Interrupt. Optionally configurable as RxLOSL||
|29|VccTx|+3.3 V Power Supply Transmitter|2|
|30|Vcc1|+3.3 V Power Supply|2|
|31|LPMode/Tx|Low Power Mode. Optionallyconfigurable as||
|32|GND|Ground|1|
|33|Tx3p|Transmitter Non-Inverted Data Input||
|34|Tx3n|Transmitter Inverted Data Input||
|35|GND|Ground|1|
|36|Tx1p|Transmitter Non-Inverted Data Input||
|37|Tx1n|Transmitter Inverted Data Input||
|38|GND|Ground|1|



Note: 

1. Circuit ground is internally isolated from chassis ground. GND is the symbol for signal and supply (power) common for the module. All are common within the module and all module voltages are referenced to this 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2022 LINK-PP AlI Rights Reserved 

Page 6 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW200-FR4C Rev1.0- Sep.2022 


potential unless otherwise noted. Connect these directly to the host board signal-common ground plane. 

2. VccRx, Vcc1 and VccTx are applied concurrently and may be internally connected within the module in any combination. Vcc contacts in SFF-8662 and SFF-8672 each have a steady state current rating of 1A. 


Figure 2. Electrical Pin-out Details 

## **Digital Diagnostic Functions** 

|**Performance Item**|**Data Address**|**Data Address**|
|---|---|---|
||Alarm & Warning|Alarm & Warning Thresholds|
|Module temperature|Lower page 9|Page2h (128-135)|
|Module voltage|Lower page 9|Page2h (136-143)|
|Bias current|Page11h (143-146)|Page2h (184-191)|
|Transmitter optical power|Page11h (139-142)|Page2h (176-183)|
|Receiver optical power|Page11h (149-152)|Page2h (192-199)|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2022 LINK-PP AlI Rights Reserved 

Page 7 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW200-FR4C Rev1.0- Sep.2022 


## **Mechanical Dimensions** 



**----- Start of picture text -----**<br>
Figure 3. Mechanical<br>Specifications<br>**----- End of picture text -----**<br>


## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LQ-CW200-FR4C|QSFP56, 200GBASE-FR4 Transceiver,LC, 2km over SMF, PAM4, 0~70℃|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2022 LINK-PP AlI Rights Reserved 

Page 8 of 8 

