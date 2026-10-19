LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ452G-TC Rev1.0- Sep.2016 


## **LP-RJ452G-TC** 

## 2.5GBASE-T SFP Copper Transceiver 

## **Features** 

- Up to 2.5Gb/s bi-directional data links 

- Support Links up to 100m using Cat 6a Cable 

- Compliant with SFF-8431 and SFF-8432 MSA 

- Compliant with IEEE 802.3az and 802.3an 

- Compliant with IEEE 802.3bz (2.5GBASE-T) 

- Hot-pluggable SFP+ footprint 

- Support TX Disable and RX Los 

- Fully metallic enclosure for low EMI 

- +3.3V single power supply 

- Low power dissipation（max 2.5W） 

- Compact RJ-45 connector assembly 

- Access to physical layer IC via 2-wire serial bus 

- Support 100/1000M Ethernet over Cat 5e cable 

- Operating temperature range: 0°C to 70°C 

## **Applications** 

- 2.5 Gigabit Ethernet over Cat 6A/7cable 

- Gigabit Ethernet over Cat 5e cable 

## **Description** 

2.5GBASE-T Copper Small Form Pluggable transceivers are based on the SFP Multi Source Agreement (MSA). They are compatible with the 2.5Gbase-T and 1000BASE-T standards as specified in IEEE Std 802.3. They are RoHS compliant and per Directive 2011/65/EU. 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ452G-TC Rev1.0- Sep.2016 


## **Pin Definitions** 

Pin Diagram 


## **Pin Descriptions** 

|**Pin**|**Signal Name**|**Description**|**Plug Seq.**|**Notes**|
|---|---|---|---|---|
|1|VEET|Transmitter Ground|1||
|2|TX FAULT|Transmitter Fault Indication|3|Note1|
|3|TX DISABLE|Transmitter Disable|3|Note2|
|4|MOD_DEF(2)|SDA Serial Data Signal|3|Note3|
|5|MOD_DEF(1)|SCL Serial Clock Signal|3|Note3|
|6|MOD_DEF(0)|TTL Low|3|Note3|
|7|Rate Select|Not Connected|3||
|8|LOS|Loss of Signal|3|Note 4|
|9|VEER|Receiverground|1||
|10|VEER|Receiverground|1||
|11|VEER|Receiverground|1||
|12|RX-|Inv. Received Data Out|3|Note 5|
|13|RX+|Received Data Out|3|Note 5|
|14|VEER|Receiverground|1||
|15|VCCR|Receiver Power Supply|2||



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ452G-TC Rev1.0- Sep.2016 


|16|VCCT|Transmitter Power Supply|2||
|---|---|---|---|---|
|17|VEET|Transmitter Ground|1||
|18|TX+|Transmit Data In|3|Note 6|
|19|TX-|Inv. Transmit Data In|3|Note 6|
|20|VEET|Transmitter Ground|1||



Notes: 

Plug Seq.: Pin engagement sequence during hot plugging. 

- 1) TX Fault is an open collector output, which should be pulled up with a 4.7k~10kΩ resistor on the host board to a voltage between 2.0V and Vcc+0.3V. Logic 0 indicates normal operation; logic 1 indicates a laser fault of some kind. In the low state, the output will be pulled to less than 0.8V. 

- 2) TX Disable is an input that is used to shut down the transmitter optical output. It is pulled up within the module with a 4.7 ¨C 10 K resistor. Its states are: 

   - Low (0 to 0.8V): Transmitter on 

   - (>0.8, < 2.0V): Undefined 

   - High (2.0 to 3.465V): Transmitter Disabled Open: Transmitter Disabled 

- 3) Mod-Def 0,1,2. These are the module definition pins. They should be pulled up with a 4.7K to 10K resistor on the host board. The pull-up voltage shall be VccT or VccR 

   - Mod-Def 0 is grounded by the module to indicate that the module is present Mod-Def 1 is the clock line of two wire serial interface for serial ID 

   - Mod-Def 2 is the data line of two wire serial interface for serial ID 

- 4) LOS (Loss of Signal) is an open collector/drain output, which should be pulled up with a 4.7K to 10K resistor. Pull up voltage between 2.0V and VccT, R+0.3V. When high, this output indicates the received optical power is below the worst-case receiver sensitivity (as defined by the standard in use). Low indicates normal operation. In the low state, the output will be pulled to <0.8V. 

- 5) RD-/+: These are the differential receiver outputs. They are AC coupled 100 differential lines which should be terminated with 100 (differential) at the user SERDES. 

- 6) TD-/+: These are the differential transmitter inputs. They are AC-coupled, differential lines with 100 differential termination inside the module. 

## **+3.3V Volt Electrical Power Interface** 

The LP-RJ452G-TC has an input voltage range of +5V +/- 5%. The 3.3V maximum voltage is not allowed for continuous operation. 

## **Table 1. +3.3V Volt electrical power interface** 

|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Supply Current|Is||320|375|mA|1.2W max power over full range of voltage<br>and temperature.<br>See caution note below|
|Input Voltage|Vcc|3.13|3.3|3.47|V|Referenced to GND|
|Maximum Voltage|Vmax|||4|V||
|Surge Current|Isurge|||30|mA|Hot plug above steady state current. See<br>caution note below|



Caution: Power consumption and surge current are higher than the specified values in the SFP MSA 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ452G-TC Rev1.0- Sep.2016 


## **Low-Speed Signals** 

MOD_DEF(1) (SCL) and MOD_DEF(2) (SDA), are open drain CMOS signals (see section VII, “Serial Communication Protocol”). Both MOD_DEF(1) and MOD_DEF(2) must be pulled up to host_Vcc 

**Table 2. Low-speed signals, electronic characteristics** 

|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|**Notes/Conditions**|
|SFP Output LOW|VOL|0|0.5|V|4.7k to 10k pull-up to host_Vcc, measured at host<br>side of connector|
|SFP Output HIGH|VOH|host_Vcc -<br>0.5|host_Vcc +<br>0.3|V|4.7k to 10k pull-up to host_Vcc, measured at host<br>side of connector|
|SFP Input LOW|VIL|0|0.8|V|4.7k to 10k pull-up to Vcc, measured at SFP side of<br>connector|
|SFP Input HIGH|VIH|2|Vcc + 0.3|V|4.7k to 10k pull-up to Vcc, measured at SFP side of<br>connector|



## **High-Speed Electrical Interface** 

All high-speed signals are AC-coupled internally. 

**Table 3. High-speed electrical interface,transmission line-SFP** 

|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|**High-Speed Electrical Interface Transmission Line-SFP**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Line Frequency|fL||800||MHz|5-level encoding, per IEEE 802.3|
|Tx Output Impedance|Zout,TX||100||Ohm|Differential, for all Frequencies between<br>1MHz and 125MHz|
|Rx Input Impedance|Zin,RX||100||Ohm|Differential, for all Frequencies between<br>1MHz and 125MHz|



## **High-speed electrical interface, host-SFP** 

**Table 4. High-speed electrical interface, host-SFP** 

|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Single ended data input swing|Vinsing|250||1200|mV|Single ended|
|Single ended data output swing|Voutsing|350||800|mV|Single ended|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ452G-TC Rev1.0- Sep.2016 


|Rise/Fall Time|Tr,Tf|20||47|psec|20%-80%|
|---|---|---|---|---|---|---|
|Tx Input Impedance|Zin||50||Ohm|Single ended|
|Rx Output Impedance|Zout||50||Ohm|Single ended|



## **General Specifications** 

**Table 5. General specifications** 

|**General**|**General**|**General**|**General**|**General**|**General**|**General**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Data Rate|BR|1000||2500|Mb/sec|IEEE 802.3 compatible.|
|Cable Length|L|||100|m||



## **Notes:** 

1. Clock tolerance is +/- 50 ppm 

2. 2.By default, the module is a full duplex device in preferred master mode. 

3. Automatic crossover detection is enabled. External crossover cable is not required 

## **Environmental Specifications** 

**Table 6. Environmental specifications** 

|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Operating Temperature|Top|0||70|°C|Case temperature|
|Storage Temperature|Tsto|-40||85|°C|Ambient temperature|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ452G-TC Rev1.0- Sep.2016 


## **Mechanical Specifications** 

The host-side of the LP-RJ452G-TC conforms to the mechanical specifications outlined in the SFP MSA1. The front portion of the SFP (part extending beyond the face plate of the host) is larger to accommodate the RJ-45 connector. 


**Figure 2. LP-RJ452G-TC mechanical dimensions** 

## **References** 

1. Small Form Factor Pluggable (SFP) Transceiver Multi-Source Agreement (MSA), 

2. IEEE Std 802.3, 2002 Edition. IEEE Standards Department, 2002. 

3. “AT24C01A/02/04/08/16 2-Wire Serial CMOS E2PROM”. 

## **Ordering information** 

|**Part Number**|**Description**|
|---|---|
|LP-RJ452G-TC|2.5G BASE-T,Copper SFP with springlatch,0-70℃|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 6 

