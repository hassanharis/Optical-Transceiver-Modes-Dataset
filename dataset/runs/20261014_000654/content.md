LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-CW400-LR4C Rev1.0- Sep.2021 


## **LQD-CW400-LR4C** 

## 400G QSFP-DD LR4 Transceiver 

## **Product Features** 

- Compliant with IEEE Std 802.3bs 

- Compliant with 400G-LR4 optical specifications 

- Compliant with QSFP-DD MSA 

- Compliant with CMIS4.0 Management interface specifications 

- 8x53.125Gb/s electrical interface (400GAUI-8) 

- Up to 10km transmission on single mode fiber (SMF) with FEC 

- Single +3.3V power supply 

- Case temperature range: 0 ~ +70℃ 

- Maximum power consumption 9.5W 

- RoHS complaint 

## **Applications** 

- 400G Ethernet 

- Data Center Interconnect 

- Infiniband Interconnect 

- Enterprise Networking 

## **Standards** 

- IEEE 802.3cd 

- QSFP-DD MSA 

- CMIS4.0 


## **Descriptions** 

LQD-CW400-LR4C is a transceiver module designed for 10km optical communication applications, and it is compliant to 100G Lambda MSA standard. This module can convert 8-channel 53.125Gb/s electrical data to 4- channel 106.25Gb/s optical signals, and multiplex them into a single channel for 425Gb/s optical transmission. Similarly, it optically de-multiplexes a 425Gb/s input into 4-channel signals, and converts them to 8-channel output electrical data on the receiver side. It has been designed to meet the harshest external operating conditions including temperature, humidity and EMI interference. The module offers very high functionality and feature integration, accessible via a two-wire serial interface. 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 1 of 10 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-CW400-LR4C Rev1.0- Sep.2021 


## **Absolute Maximum Ratings** 

It has to be noted that the operation in excess of any individual absolute maximum ratings might cause permanent damage to this module. 

|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|
|---|---|---|---|---|
|Storage Temperature Range|TSTG|-40|+85|⁰C|
|SupplyVoltage|VCC|0|4|V|
|Relative Humidity|RH|10% to 90% non-condensing|||



## **Operating Conditions** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|
|---|---|---|---|---|
|Case Temperature- Operating|TCASE|0|70|⁰C|
|Supply Voltage|Vcc|3.14|3.46|V|
|Power Consumption|PDISS||12|W|
|Pre-FEC Bit Error Ratio|||2.4x10-4||
|Link Distance|2||10000|M|



## **Optical Characteristics** 

|**Transmitter Parameter**|**Lane**|**Min**|**Typical**|**Max**|**Units**|
|---|---|---|---|---|---|
|Lane Wavelength Range|Lane 0|1264.5|1271|1277.5|nm|
||Lane 1|1284.5|1291|1297.5|nm|
||Lane 2|1304.5|1311|1317.5|nm|
||Lane 3|1324.5|1331|1337.5|nm|
|Signal rateper lane|||53.125||GBd|
|Average launch Powerper lane||-2.7||5.1|dBm|
|Total Average launchpower||||11.1|dBm|
|Outer Optical Modulation Amplitude<br>(OMAouter), each lane for TDECQ<1.4 dB<br>for 1.4dB<=TDECQ<=3.9dB||0.3-<br>1.1+TDEC<br>Q||4.4|dBm|
|Difference in launch power between any two lanes<br>(OMAouter)||||4|dB|
|Average Launch Powerper Lane@TX Off State||||-16|dBm|
|Transmitter Eye Closure for PAM4(TECQ),each Lane||||3.9|dB|
|Transmitter and dispersion Eye Closure for PAM4(TDECQ),<br>each Lane||||3.9|dB|
||TDECQ– TECQ|||||2.5|dB|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 2 of 10 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LQD-CW400-LR4C Rev1.0- Sep.2021 

||Extinction Ratio||3.5|||dB||
|---|---|---|---|---|---|---|---|
||Relative IntensityNoise(OMA)||||-136|dB/Hz||
||Side-Mode Suppression Ration(SMSR)||30|||dB||
||Optical Return Loss Tolerance||||15.6|dB||
||Transmitter Reflectance||||-26|dB||
||Transmitter over/under-shoot||||25|%||
||Transmitterpeak-to-peakpower||||5.2|dBm||
||Transmitter transition time||||17|ps||



## **Receiver Optical Specifications** 

|**Receiver Parameter**|**Lane**|**Min**|**Typical**|**Max**|**Units**|
|---|---|---|---|---|---|
|Lane Wavelength Range|Lane 0|1264.5|1271|1277.5|nm|
||Lane 1|1284.5|1291|1297.5|nm|
||Lane 2|1304.5|1311|1317.5|nm|
||Lane 3|1324.5|1331|1337.5|nm|
|Signal rateper lane|||53.125||GBd|
|Damage Threshold||6.1|||dBm|
|Average Receive Power,each lane||-9||5.1|dBm|
|Receiver Power,each lane(OMA)||||4.4|dBm|
|Receiver Reflectance||||-26|dB|
|Difference in receive Power between any Two<br>Lanes(OMAouter)||||4.3|dBm|
|Receiver Sensitivity each lane (OMAouter) for TECQ<1.4dB<br>for 1.4dB<=TECQ<=3.9dB||||-6.8<br>-8.2+TECQ|dBm|
|Stressed Receiver Sensitivity (OMAouter),each||||-4.3|dBm|
|Stressed Conditions for Stress Receiver Sensitivity||||||
|Stressed Eye Closure for PAM4(SECQ),Lane under Test|||3.9||dB|
|OMAouter of each Aggressor Lane|||-0.4||dBm|



## **Electrical Characteristics** 

|**Parameter**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|
|**Receiver electrical output characteristics at TP4**||||||
|Signalingrateper lane||26.5625||GBd||
|AC common-mode output voltage(RMS)||-|17.5|mV||
|Differentialpeak-to-peak output voltage|||900|mV||
|Near-end ESMW (Eye symmetry mask<br>width)||0.265||UI||
|Near-end Eye height, differential|7<br>0|||mV||
|Near-end vertical eye closure|||7.5|dB||



**ww** www.link-pp.com w.l-p.com **w.l-p.com** Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 3 of 10 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-CW400-LR4C Rev1.0- Sep.2021 


|Far-end ESMW(Eye symmetrymask width)||0.20||UI||
|---|---|---|---|---|---|
|Far-end Eye height, differential|3<br>0|||mV||
|Far-end vertical eye closure|||7.5|dB||
|Far-endpre-cursor ISI ratio|-4.5||2.5|%||
|Common mode to differential conversion<br>return<br>loss|802.3 Equation(83E-3)|||dB||
|Differential output return loss|802.3 Equation(83E-2)|||dB||
|Differential termination mismatch|||10|%||
|Transition time(min,20% to 80%)||9.5||ps||
|DC common mode voltage|-350||2850|mV||
|**Transmitter electrical input characteristics at TP1**||||||
|Signalingrate, per lane||26.5625||GBd||
|Differential peak-to-peak input voltage<br>tolerance|900|||mV||
|Differential input return loss|802.3 Equation(83E-5)|||||
|Differential to common mode input return<br>loss|802.3 Equation(83E-6)|||mV||
|AC common-mode output voltage(RMS)|||17.5|mV||
|Single-ended voltage tolerance range|-0.4||3.3|V||
|Module stressed input|802.3 120E.3.4.1|||UI||
|Differential termination mismatch|||10|%||
|DC common mode voltage|-350|||mV||



## **Receiver Output Power Thresholds for Loss of Signal(LOS)** 

|**Parameter**|**Min**|**Typical**|**Max**|**Unit**|
|---|---|---|---|---|
|RX_LOS_Assert Min/Max|-20.0|||dBm|
|RX_LOS_De-Assert Min/Max|||-12.2|dBm|
|RX_LOS_Hysteresis|0.5|||dB|



## **Digital Diagnostic Monitoring Specifications** 

|**Parameters**|**Unit**|**Specification**|
|---|---|---|
|Temperature Monitor absolute error|°C|±3|
|SupplyVoltage Monitor absolute error|%|±5|
|I_bias Monitor absolute error|%|±10|
|Received Power(Rx)Monitor absolute error|dB|±3.0|
|Transmit Power(Tx)Monitor absolute error|dB|±3.0|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 4 of 10 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-CW400-LR4C Rev1.0- Sep.2021 


## **High Speed Electrical Specifications** 

|**Parameter**|**Min**|**Min**|**Min**|**Typical**|**Typical**|**Max**|**Max**|**Max**|**Unit**<br>**s**|**Note**<br>**s**|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receiver**||**electrical**|**output**||**characteristics**||**at**|**TP4**|||
|Signaling rate per lane||||26.5625|||||GBd||
|AC common-mode output voltage(RMS)||||-||17.5|||mV||
|Differential peak-to-peak output voltage||||||900|||mV||
|Near-end ESMW (Eye symmetry mask<br>width)||||0.265|||||UI||
|Near-end Eye height, differential|70||||||||mV||
|Far-end ESMW (Eye symmetry mask width)||||0.2|||||UI||
|Far-end Eye height, differential|30||||||||mV||
|Far-end pre-cursor ISI ratio|-4.5|||||2.5|||%||
|Differential output return loss|9.5 - 0.37f||||||||dB|0.01 – 8 GHz|
||4.75 -7.4log 10<br>(f/14)||||||||dB|8 – 19 GHz|
|Common to differential mode conversion<br>return loss|22-20(f/25.78)||||||||dB|0.01 -12.89GHz|
||15 -6log 10<br>(f/25.78)||||||||dB|12.89 – 19 GHz|
|Differential termination mismatch||||||10|||%||
|Transition time (min, 20% to 80%)|9.5||||||||ps||
|DC common mode voltage|-350|||||2850|||mV||
|**Transmitter electrical input characteristics at TP1**|||||||||||
|Signaling rate, per lane||||26.5625|||||GBd||
|Differential pk-pk input voltage tolerance|900||||||||mV||
|Differential input return loss|9.5 - 0.37f||||||||dB|0.01 – 8 GHz|
||4.75 -7.4log 10<br>(f/14)||||||||dB|8 – 19 GHz|
|Differential to common mode input return<br>loss|22-20(f/25.78)||||||||dB|0.01 -12.89GHz|
||15 -6log 10<br>(f/25.78)||||||||dB|12.89 – 19 GHz|
|Differential termination mismatch||||||10|||%||
|Module stressed input test|Per Section<br>120E.3.4.1,<br>IEEE802.3bs||||||||||
|Single-ended voltage tolerance range|-0.4|||||3.3|||V||
|Common-mode voltage|-350|||||2850|||mV||



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 5 of 10 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-CW400-LR4C Rev1.0- Sep.2021 


## **Receiver Output Power Thresholds for Loss of Signal (LOS)** 

|**Parameter**|**Min**|**Typical**<br>**Max**|**Typical**<br>**Max**|**Units**|
|---|---|---|---|---|
|RX_LOS_Assert Min/Max|-20.0|||dBm|
|RX_LOS_De-Assert Min/Max|||-10.3|dBm|
|RX_LOS_Hysteresis|0.5|||dB|



## **Digital Diagnostic Monitoring Specifications** 

|**Parameter**|**Unit**|**Specification**|
|---|---|---|
|Temperature Monitor absolute error|degC|± 3|
|Voltage Monitor absolute error|%|± 5|
|I_bias Monitor absolute error|%|± 10|
|Transmit Power (Tx) Monitor absolute error|dB|± 3.0|
|Received Power (Rx) Monitor absolute error|dB|± 3.0|



## **QSFP-DD Edge Connector and Pinout Description** 

The electrical pinout of the QSFP-DD module is shown in Figure 1 below. 


**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 6 of 10 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-CW400-LR4C Rev1.0- Sep.2021 



Figure 1. Host PCB QSFP-DD pad assignment top view 

|**Pin No.**|**Symbol**|**Description**|**Note**|
|---|---|---|---|
|1|GND|Ground|1|
|2|Tx2n|Transmitter Inverted Data Input||
|3|Tx2p|Transmitter Non-Inverted Data outpu|t|
|4|GND|Ground|1|
|5|Tx4n|Transmitter Inverted Data Input||
|6|Tx4p|Transmitter Non-Inverted Data outpu|t|
|7|GND|Ground|1|
|8|ModSelL|Module Select||
|9|ResetL|Module Reset||
|10|VccRx|3.3V Power Supply Receiver|2|
|11|SCL|2-Wire serial Interface Clock||
|12|SDA|2-Wire serial Interface Data||
|13|GND|Ground|1|
|14|Rx3p|Receiver Non-Inverted Data Output||
|15|Rx3n|Receiver Inverted Data Output||
|16|GND|Ground|1|
|17|Rx1p|Receiver Non-Inverted Data Output||
|18|Rx1n|Receiver Inverted Data Output||
|19|GND|Ground|1|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 7 of 10 


LINK-PP INT’L TECHNOLOGY CO., LIMITED LQD-CW400-LR4C Rev1.0- Sep.2021 

||20|GND|Ground|1||
|---|---|---|---|---|---|
||21|Rx2n|Receiver Inverted Data Output|||
||22|Rx2p|Receiver Non-Inverted Data Output|||
||23|GND|Ground|1||
||24|Rx4n|Receiver Inverted Data Output|||
||25|Rx4p|Receiver Non-Inverted Data Output|||
||26|GND|Ground|1||
||27|ModPrsL|Module Present|||
||28|IntL|Interrupt|||
||29|VccTx|3.3V power supply transmitter|2||
||30|Vcc1|3.3V power supply|2||
||31|Init Mode|Initialization mode|||
||32|GND|Ground|1||
||33|Tx3p|Transmitter Non-Inverted Data Input|||
||34|Tx3n|Transmitter Inverted Data Output|||
||35|GND|Ground|1||
||36|Tx1p|Transmitter Non-Inverted Data Input|||
||37|Tx1n|Transmitter Inverted Data Output|||
||38|GND|Ground|1||
||39|GND|Ground|1||
||40|Tx6n|Transmitter Inverted Data Input|||
||41|Tx6p|Transmitter Non-Inverted Data output|||
||42|GND|Ground|1||
||43|Tx8n|Transmitter Inverted Data Input|||
||44|Tx8p|Transmitter Non-Inverted Data output|||
||45|GND|Ground|1||
||46|Reserved|For Future Use|3||
||47|VS1|Module Vendor Specific 1|3||
||48|VccRx1|3.3V Power Supply|2||
||49|VS2|Module Vendor Specific 2|3||
||50|VS3|Module Vendor Specific 3|3||
||51|GND|Ground|1||
||52|Rx7p|Receiver Non-Inverted Data Output|||
||53|Rx7n|Receiver Inverted Data Output|||
||54|GND|Ground|1||
||55|Rx5p|Receiver Non-Inverted Data Output|||
||56|Rx5n|Receiver Inverted Data Output|||
||57|GND|Ground|1||
||58|GND|Ground|1||



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 8 of 10 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-CW400-LR4C Rev1.0- Sep.2021 


|59|Rx6n|Receiver Inverted Data Output||
|---|---|---|---|
|60|Rx6p|Receiver Non-Inverted Data Output||
|61|GND|Ground|1|
|62|Rx8n|Receiver Inverted Data Output||
|63|Rx8p|Receiver Non-Inverted Data Output||
|64|GND|Ground|1|
|65|NC|No Connect|3|
|66|Reserved|For Future Use|3|
|67|VccTx1|3.3V power supply|2|
|68|Vcc2|3.3V power supply|2|
|69|Reserved|For Future Use|3|
|70|GND|Ground|1|
|71|Tx7p|Transmitter Non-Inverted Data Input||
|72|Tx7n|Transmitter Inverted Data Output||
|73|GND|Ground|1|
|74|Tx5p|Transmitter Non-Inverted Data Input||
|75|Tx5n|Transmitter Inverted Data Output||
|76|GND|Ground|1|



## **Module Block Diagram** 


Figure 2. Module Block Diagram 

**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 9 of 10 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQD-CW400-LR4C Rev1.0- Sep.2021 


## **Memory map** 

Compatible with CMIS 5.0 

## **Mechanical Specifications** 


## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LQD-CW400-LR4C|400Gbps，QSFP-DD，LR4，10km，0°C~+70°C，with DDM|



**ww** www.link-pp.com w.l-p.com **w.l-p.com** 

Copyright © 2021 LINK-PP AlI Rights Reserved 

Page 10 of 10 

