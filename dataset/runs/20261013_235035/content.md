LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-SFP-TM8C Rev1.0- Sep.2016 


## **LP-SFP-TM8C** Copper SFP RJ45 10/100/1000Mbps 100m Transceiver 

## **Features** 

- Up to 1.25Gb/s bi-directional data links 

- Hot-pluggable SFP footprint 

- Fully metallic enclosure for low EMI 

- Low power dissipation (1.05 W typical) 

- Compact RJ-45 connector assembly 

- Access to physical layer IC via 2-wire serial bus 

- 10/100/1000Mbps compliant in host systems with SGMII interface 

- Operating case temperature: 

   - Commercial : 0 to +70°C 

   - Industrial: -40 to +85°C 

## **Applications** 

- 1.25 Gigabit Ethernet over Cat 5 cable 


## **Description** 

The Copper SFP Transceiver 10/100/1000Base-T or 1000Base-T only SFP Copper Transceiver is high performance, cost effective module, compliant with the Gigabit Ethernet and 1000BASE-T standards as specified in IEEE 802. 3-2002 and IEEE 802.3ab, which supports 1000Mb/s data-rate up to 100 meters reach over twisted-pair category 5 cable. 

The module supports 1000 Mbps full duplex data-links with 5-level Pulse Amplitude Modulation (PAM) signals. All four pairs in the cable are used with symbol rate at 250Mbps on each pair. The module provides standard serial ID information compliant with SFP MSA, which can be accessed with address of A0h via the 2wire serial 

www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-SFP-TM8C Rev1.0- Sep.2016 


CMOS EEPROM protocol. The physical IC can also be accessed via 2wire serial bus at address A0h. 

## **Pin Definitions** 


**Figure 1:Pin Diagram** 

## **Pin Descriptions** 

|**Pin**|**Signal Name**|**Description**|**Plug Seq.**|**Notes**|
|---|---|---|---|---|
|1|VEET|Transmitter Ground|1||
|2|TX FAULT|Transmitter Fault Indication|3|Note1|
|3|TXDISABLE|Transmitter Disable|3|Note2|
|4|MOD_DEF(2)|SDA Serial Data Signal|3|Note3|
|5|MOD_DEF(1)|SCL Serial Clock Signal|3|Note3|
|6|MOD_DEF(0)|TTL Low|3|Note3|
|7|Rate Select|Not Connected|3||
|8|LOS|Loss of Signal|3|Note 4|
|9|VEER|Receiver ground|1||
|10|VEER|Receiver ground|1||
|11|VEER|Receiver ground|1||
|12|RX-|Inv. Received Data Out|3|Note 5|



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-SFP-TM8C Rev1.0- Sep.2016 


|13|RX+|Received Data Out|3|Note 5|
|---|---|---|---|---|
|14|VEER|Receiver ground|1||
|15|VCCR|Receiver Power Supply|2||
|16|VCCT|Transmitter Power Supply|2||
|17|VEET|Transmitter Ground|1||
|18|TX+|Transmit Data In|3|Note 6|
|19|TX-|Inv. Transmit Data In|3|Note 6|
|20|VEET|Transmitter Ground|1||



Notes: 

## Plug Seq.: Pin engagement sequence during hot plugging. 

- 1) TX Fault is an open collector output, which should be pulled up with a 4.7k~10kΩ resistor on the host board to a voltage between 2.0V and Vcc+0.3V. Logic 0 indicates normal operation; logic 1 indicates a laser fault of some kind. In the low state, the output will be pulled to less than 0.8V. 

- 2) TX Disable is an input that is used to shut down the transmitter optical output. It is pulled up within the module with a 4.7 ¨C 10 K resistor. Its states are: 

Low (0 to 0.8V): Transmitter on (>0.8, < 2.0V): Undefined High (2.0 to 3.465V): Transmitter Disabled Open: Transmitter Disabled 

- 3) Mod-Def 0,1,2. These are the module definition pins. They should be pulled up with a 4.7K to 10K resistor on the host board. The pull-up voltage shall be VccT or VccR 

   - Mod-Def 0 is grounded by the module to indicate that the module is present Mod-Def 1 is the clock line of two wire serial interface for serial ID Mod-Def 2 is the data line of two wire serial interface for serial ID 

- 4) LOS (Loss of Signal) is an open collector/drain output, which should be pulled up with a 4.7K to 10K resistor. Pull up voltage between 2.0V and VccT, R+0.3V. When high, this output indicates the received optical power is below the worst-case receiver sensitivity (as defined by the standard in use). Low indicates normal operation. In the low state, the output will be pulled to <0.8V. 

- 5) RD-/+: These are the differential receiver o utputs. They are AC coupled 100 differential lines which should be terminated with 100 (differential) at the user SERDES. 

- 6) TD-/+: These are the differential transmitter inputs. They are AC-coupled, differential lines with 100 differential termination inside the module. 

## **Electrical Power Interface** 

The LP-SFP-xxxx has an input voltage range of +3.3V +/- 5%. The 3.3V maximum voltage is not allowed for continuous operation. 

**Table 1. +3.3V Volt electrical power interface** 

|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Supply Current|Is||320|375|mA|1.2W max power over full range of voltage<br>and temperature.<br>See caution note below|
|Input Voltage|Vcc|3.13|3.3|3.47|V|Referenced to GND|
|Maximum Voltage|Vmax|||4|V||



Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 8 

www.link-pp.com www.l-p.com 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-SFP-TM8C Rev1.0- Sep.2016 


||Surge Current|Isurge|||30|mA|Hot plug above steady state current. See<br>caution note below||
|---|---|---|---|---|---|---|---|---|



Caution: Power consumption and surge current are higher than the specified values in the SFP MSA 

## **Low-Speed Signals** 

MOD_DEF(1) (SCL) and MOD_DEF(2) (SDA), are open drain CMOS signals (see section VII, “Serial Communication Protocol”). Both MOD_DEF(1) and MOD_DEF(2) must be pulled up to host_Vcc 

## **Table 2. Low-speed signals, electronic characteristics** 

|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|**Notes/Conditions**|
|SFP Output LOW|VOL|0|0.5|V|4.7k to 10k pull-up to host_Vcc, measured at host<br>side of connector|
|SFP Output HIGH|VOH|host_Vcc -<br>0.5|host_Vcc +<br>0.3|V|4.7k to 10k pull-up to host_Vcc, measured at host<br>side of connector|
|SFP Input LOW|VIL|0|0.8|V|4.7k to 10k pull-up to Vcc, measured at SFP side of<br>connector|
|SFP Input HIGH|VIH|2|Vcc + 0.3|V|4.7k to 10k pull-up to Vcc, measured at SFP side of<br>connector|



## **High-Speed Electrical Interface** 

## All high-speed signals are AC-coupled internally. 

**Table 3. High-speed electrical interface, transmission line-SFP** 

|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Line Frequency|fL||125||MHz|5-level encoding, per IEEE 802.3|
|Tx Output Impedance|Zout,TX||100||Ohm|Differential, for all Frequencies between<br>1MHz and 125MHz|
|Rx Input Impedance|Zin,RX||100||Ohm|Differential, for all Frequencies between<br>1MHz and 125MHz|



## **High-speed electrical interface, host-SFP** 

**Table 4. High-speed electrical interface, host-SFP** 

|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Single ended data input swing|Vinsing|250||1200|mV|Single ended|
|Single ended data output swing|Voutsing|350||800|mV|Single ended|



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-SFP-TM8C Rev1.0- Sep.2016 


|Rise/Fall Time|Tr,Tf||175||psec|20%-80%|
|---|---|---|---|---|---|---|
|Tx Input Impedance|Zin||50||Ohm|Single ended|
|Rx Output Impedance|Zout||50||Ohm|Single ended|



## **General Specifications** 

**Table 5. General specifications** 

|**General**|**General**|**General**|**General**|**General**|**General**|**General**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Data Rate|BR|10||1,000|Mb/sec|IEEE 802.3 compatible.<br>See Notes 2 through 4 below|
|Cable Length|L|||100|m|Category5 UTP. BER <10-12|



**Notes:** 

1. Clock tolerance is +/- 50 ppm 

2. By default, the LP-SFP-xx is a full duplex device in preferred master mode 

3. Automatic crossover detection is enabled. External crossover cable is not required 

4. 1000 BASE-T operation requires the host system to have an SGMII interface with no clocks, and the module PHY to be configured per Application Note AN-2036. With a SERDES that does not support SGMII, the module will operate at 1000BASE-T only. 

## **Environmental Specifications** 

**Table 6. Environmental specifications** 

||**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Operating Temperature|C|0||70|°C|Commercial Case temperature|
||I|-40||85|°C|Industry Case temperature|
|Storage Temperature|Tsto|-40||85|°C|Ambient<br>temperature|



## **References** 

1. Gigabit Interface Converter (SFP) Transceiver Multi-Source Agreement (MSA), 

2. IEEE Std 802.3, 2002 Edition. IEEE Standards Department, 2002. 

3. “24C01A/02/04/08/16 2-Wire Serial CMOS E2PROM”. 

4. “Alaska Ultra 88E1111 Integrated 10/100/1000M Gigabit Ethernet Transceiver”,Marvell Corporation. 

## **Mechanical Specifications** 

The host-side of the LP-SFP-xx conforms to the mechanical specifications outlined in the SFP MSA1. The front portion of the SFP (part extending beyond the face plate of the host) is larger to accommodate the RJ-45 connector. 

www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-SFP-TM8C Rev1.0- Sep.2016 



**Figure 2. mechanical dimensions** 

## **References** 

1. Small Form Factor Pluggable (SFP) Transceiver Multi-Source Agreement (MSA), 2. IEEE Std 802.3, 2002 Edition. IEEE Standards Department, 2002. 

3. “24C01A/02/04/08/16 2-Wire Serial CMOS E2PROM”. 

## **Ordering information** 

|**Part Number**|**Description**|
|---|---|
|LP-SFP-TMRC|10/100/1000Mbps, SGMII interface, Copper SFP with spring latch, 0~70℃, Realtek<br>RTL8213B|
|LP-SFP-MSRC|1000Mbps only,SERDES interface,Copper SFP with springlatch,0~70℃,Realtek RTL8213B|
|LP-SFP-TM8C|10/100/1000Mbps,SGMII interface,Copper SFP with springlatch,0~70℃,Marvel 88E1111|
|LP-SFP-MS8C|1000Mbps only,SERDES interface,Copper SFP with springlatch,0~70℃,Marvel 88E1111|
|LP-SFP-TMRI|10/100/1000Mbps,SGMII interface,Copper SFP with springlatch,-40~85℃,Realtek RTL8213B|
|LP-SFP-MSRI|1000Mbps only,SERDES interface,Copper SFP with springlatch,-40~85℃,Realtek RTL8213B|
|LP-SFP-TM8I|10/100/1000Mbps,SGMII interface,Copper SFP with springlatch,-40~85℃,Marvel 88E1111|
|LP-SFP-MS8I|1000Mbps only,SERDES interface,Copper SFP with springlatch,-40~85℃,Marvel 88E1111|



**NOT:** All SFP module have Tx-disable and Rx_los function default. 

www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-SFP-TM8C Rev1.0- Sep.2016 


The SFP with Marvel 88E1111 IC may divided into below PN. The module have Tx-disable, Rx_los or not, can be customized. 

|**Part Number**|**Description**|**Speed**|**Tx-disab**<br>**le**|**Rx_LOS**|
|---|---|---|---|---|
|LP-SFP-TM8CNN|10/100/1000Mbps, with SGMII interface, enable the auto-negotiation<br>default, without Tx-disable function, Not support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature 0～70℃.,Marvel 88E1111|10/100/1000<br>Mbps|NO|NO|
|LP-SFP-TM8INN|10/100/1000Mbps, with SGMII interface, enable the auto-negotiation<br>default, without Tx-disable function, Not support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature -40～85℃.,Marvel 88E1111|10/100/1000<br>Mbps|NO|NO|
|LP-SFP-MS8CNY|1000Mbps, with 1Gbps SerDes interface, enable the auto-negotiation<br>default, without Tx-disable function , support Rx-LOS as link indication<br>function,nshielded twisted-pair (UTP) Category 5 Cable ,Transmission<br>Distance 0.1Km,Temperature 0～70℃.,Marvel 88E1111|1000Mbps|NO|YES|
|LP-SFP-MS8INY|1000Mbps, with 1Gbps SerDes interface, enable the auto-negotiation<br>default, without Tx-disable function , support Rx-LOS as link indication<br>function,nshielded twisted-pair (UTP) Category 5 Cable ,Transmission<br>Distance 0.1Km,Temperature -40～85℃.,Marvel 88E1111|1000Mbps|NO|YES|
|LP-SFP-MS8CNN|1000Mbps, with 1Gbps SerDes interface, enable the auto-negotiation<br>default,without Tx_disable function, Not support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature 0～70℃.,Marvel 88E1111|1000Mbps|NO|NO|
|LP-SFP-MS8INN|1000Mbps, with 1Gbps SerDes interface, enable the auto-negotiation<br>default,without Tx_disable function, Not support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature -40～85℃.,Marvel 88E1111|1000Mbps|NO|NO|
|LP-SFP-TM8CNY|10/100/1000Mbps, with SGMII interface, enable the auto-negotiation<br>default, without Tx-disable function, support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature 0～70℃,Marvel 88E1111|10/100/1000<br>Mbps|NO|YES|
|LP-SFP-TM8INY|10/100/1000Mbps, with SGMII interface, enable the auto-negotiation<br>default, without Tx-disable function, support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature -40～85℃,Marvel 88E1111|10/100/1000<br>Mbps|NO|YES|
|LP-SFP-TM8CYN|10/100/1000Mbps, with SGMII interface, enable the auto-negotiation<br>default, with Tx_disable function, not support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature 0～70℃,Marvel 88E1111|10/100/1000<br>Mbps|YES|NO|
|LP-SFP-TM8CYN|10/100/1000Mbps, with SGMII interface, enable the auto-negotiation<br>default, with Tx_disable function, not support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature 0～70℃,Marvel 88E1111|10/100/1000<br>Mbps|YES|NO|
|LP-SFP-MS8CYY|1000Mbps, with 1Gbps SerDes interface, enable the auto-negotiation<br>default,<br>with<br>Tx_disable<br>function,support<br>Rx_LOS<br>as<br>link<br>indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature 0～70℃,Marvel 88E1111|1000Mbps|YES|YES|
|LP-SFP-MS8IYY|1000Mbps, with 1Gbps SerDes interface, enable the auto-negotiation|1000Mbps|YES|YES|



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 7 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-SFP-TM8C Rev1.0- Sep.2016 


||default,<br>with<br>Tx_disable<br>function,support<br>Rx_LOS<br>as<br>link<br>indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature -40～85℃,Marvel 88E1111||||
|---|---|---|---|---|
|LP-SFP-MS8CYN|1000Mbps, with 1Gbps SerDes interface, enable the auto-negotiation<br>default, with Tx_disable function, not support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature 0～70℃,Marvel 88E1111|1000Mbps|YES|NO|
|LP-SFP-MS8CYN|1000Mbps, with 1Gbps SerDes interface, enable the auto-negotiation<br>default, with Tx_disable function, not support Rx_LOS as link indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature 0～70℃,Marvel 88E1111|1000Mbps|YES|NO|
|LP-SFP-TM8CYY|10/100/1000Mbps, with SGMII interface, enable the auto-negotiation<br>default,with<br>Tx_disable<br>function,<br>support<br>Rx_LOS<br>as<br>link<br>indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature 0～70℃,Marvel 88E1111|10/100/1000<br>Mbps|YES|YES|
|LP-SFP-TM8IYY|10/100/1000Mbps, with SGMII interface, enable the auto-negotiation<br>default,with<br>Tx_disable<br>function,<br>support<br>Rx_LOS<br>as<br>link<br>indication<br>function,unshielded<br>twisted-pair<br>(UTP)<br>Category<br>5<br>Cable,Transmission<br>Distance 0.1Km,Temperature -40～85℃,Marvel 88E1111|10/100/1000<br>Mbps|YES|YES|



www.link-pp.com **ww** w.l-p.com **w.l-p.com** 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 8 of 8 

