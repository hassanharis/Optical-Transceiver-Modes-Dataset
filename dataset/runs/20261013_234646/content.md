LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ45TGE-3YC Rev1.0- Sep.2020 


## **LP-RJ45TGE-3YC** 

## 10GBase-T Copper SFP+ RJ45 30m Transceiver 

## **Product Features** 

- Supports 10G Ethernet transmission up to 30 meters via Cat6A and above twisted pair cables 

- Complies with SFF-8431 and SFF-8432 MSA standard protocols 

- Adheres to IEEE 802.3az and 802.3an protocols 

- Complies with 2.5G and 5G Ethernet IEEE 802.3bz standards 

- Hot-swappable SFP+ package 

- TX Disable and RX Los functions 

- Full metal shell packaging with low electromagnetic interference emissions 

- +3.3V single power supply 

- Low power consumption (maximum power of 2.5W for 30m transmission) 

- Compact RJ45 connector for cost-effective twisted pair copper cabling 

- Access to physical layer chip via 2-wire serial bus 

- Automatic negotiation for XFI/5GBASE-R/2500BASE-X on SGMII interface host systems 

- Automatic negotiation with other 10GBASE-T PHYs 

- Supports 100/1000M rate transmission over Cat5E cables 

- MDI/MDIX conversion 

- Multiple loopback modes for testing and fault diagnosis 

- Built-in cable monitoring and link diagnostics 

- Supports both unshielded and shielded cables 

- Operating temperature range: 0°C to +70°C 

## **Applications** 

- Supports 10G Ethernet over Cat 6A/7 cables 


- Supports 5G Ethernet over Cat 6A/7 cables 

- Supports 2.5G Ethernet over Cat 6A/7 cables 

- Supports 1G Ethernet over Cat 5e cables 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 1 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ45TGE-3YC Rev1.0- Sep.2020 


## **Description** 

The LP-RJ45TGE-3YC small form-factor pluggable 10GBASE-T SFP+ electrical module is a high-performance, high-reliability, and cost-effective 10G connectivity solution. It is compatible with the 10G Ethernet and 10GBASE-T/5GBASE-T/2.5GBASE-T/1000BASE-T standards specified by IEEE 802.3az-2015 and 802.3a, supporting 30 meters of data rate transmission at 10Gbps over shielded twisted pair Cat 6A cables. It supports 10Gbps full-duplex data links with 16-level pulse amplitude modulation (PAM) signals. The module provides serial ID information compliant with the SFP+ MSA standard, accessible via a 2-wire serial bus at address A0h. The physical chip is accessed via the 2-wire serial bus at address ACh. 

## **Pin Descriptions** 


|**Pin**|**Signal Name**|**Description**|**Notes**|
|---|---|---|---|
|1|VEET|Transmitter Ground|1|
|2|TX FAULT|Transmitter Fault Indication|2|
|3|TXDISABLE|Transmitter Disable|3|
|4|Mod_DEF(2)/SDA|SDA Serial Data Signal|4|
|5|Mod_DEF(1)/SCL|SCL Serial Clock Signal|4|
|6|Mod_DEF(0)/MOD_ABS|Module Absent. Grounded within the module|4|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 2 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 


LP-RJ45TGE-3YC Rev1.0- Sep.2020 

||7|RS0|Not Connected|||
|---|---|---|---|---|---|
||8|LOS|Loss of Signal|2||
||9|RS1|Not Connected|1||
||10|VEER|Receiver ground|1||
||11|VEER|Receiver ground|1||
||12|RD-|Inv. Received Data Out|||
||13|RD+|Received Data Out|||
||14|VEER|Receiver ground|1||
||15|VCCR|Receiver Power Supply|||
||16|VCCT|Transmitter Power Supply|||
||17|VEET|Transmitter Ground|1||
||18|TD+|Transmit Data In|||
||19|TD-|Inv. Transmit Data In|||
||20|VEET|Transmitter Ground|1||



Notes: 

- 1.The module signal ground pins VeeR and VeeT should be isolated from the module casing. 

- 2.This pin is an open-collector/drain output contact that can be pulled up to any power supply potential of the host. 

- 3.Tx_Disable is a pin that is pulled up to the internal VccT pin of the module through a current-limiting resistor of 4.7kΩ to 10kΩ. 

- 4.The voltage at the end of the 4.7kΩ to 10kΩ resistor on the host board should be pulled down to 2.0V-3.6V, and Mod_DEF(0) pulled low indicates that the module is inserted. 

## **+3.3V Volt Electrical Power Interface** 

**Table 1. +3.3V Volt electrical power interface** 

|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Supply Current|Is||500|750|mA|2.5W max power over full range of voltage<br>and temperature.<br>See caution note below|
|Input Voltage|Vcc|3.13|3.3|3.47|V|Referenced to GND|
|Maximum Voltage|Vmax|||3.6|V||



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 3 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ45TGE-3YC Rev1.0- Sep.2020 


**Table 2. Low-speed signals, electrical characteristics** 

|**Low-speed signals, electrical characteristics**|**Low-speed signals, electrical characteristics**|**Low-speed signals, electrical characteristics**|**Low-speed signals, electrical characteristics**|**Low-speed signals, electrical characteristics**|**Low-speed signals, electrical characteristics**|
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**<br>**s**|**Notes/Conditions**|
|SFP+ Output Low Level|VOL|0|0.5|V|Pulled up to host_Vcc with 4.7k to 10k, measured<br>on the host side of the connector|
|SFP+ Output High Level|VOH|host_Vcc-<br>0.5|host_Vcc+0.<br>3|V|Pulled up to host_Vcc with 4.7k to 10k, measured<br>on the host side of the connector|
|SFP+ Input Low Level|VIL|0|0.8|V|Pulled up to Vcc with 4.7k to 10k, measured on the<br>SFP side of the connector|
|SFP+ Input High Level|VIH|2|Vcc+0.3|V|Pulled up to Vcc with 4.7k to 10k, measured on the<br>SFP side of the connector|



Notes:MOD_DEF(1) (SCL) and MOD_DEF(2) (SDA) are open-drain CMOS signals and must be pulled up to the host side Vcc (host_Vcc). 

**Table 3. High-Speed Electrical Interface, Transmission Line - SFP+** 

|**High-Speed Electrical Interface, Transmission Line - SFP+**|**High-Speed Electrical Interface, Transmission Line - SFP+**|**High-Speed Electrical Interface, Transmission Line - SFP+**|**High-Speed Electrical Interface, Transmission Line - SFP+**|**High-Speed Electrical Interface, Transmission Line - SFP+**|**High-Speed Electrical Interface, Transmission Line - SFP+**|**High-Speed Electrical Interface, Transmission Line - SFP+**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Line Frequency|FL||800||MHz|16-level encoding, compliant with IEEE 802.3|
|Tx Output<br>Impedance|ZOUT,TX||100||Ω|Differential, applicable for all frequencies<br>between 1MHz and 800MHz|
|Rx Input<br>Impedance|ZIN,RX||100||Ω|Differential, applicable for all frequencies<br>between 1MHz and 800MHz|



Notes:All high-speed signals are internally AC coupled. 

**Table 4. High-Speed Electrical Interface, Host - SFP** 

|**High-Speed Electrical Interface, Host - SFP**|**High-Speed Electrical Interface, Host - SFP**|**High-Speed Electrical Interface, Host - SFP**|**High-Speed Electrical Interface, Host - SFP**|**High-Speed Electrical Interface, Host - SFP**|**High-Speed Electrical Interface, Host - SFP**|**High-Speed Electrical Interface, Host - SFP**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Single-ended Data Input Swing|Input|500|800|1100|mV|Differential|
|Single-ended Data Output Swing|Output|500|800|1100|mV|Differential|
|Rise/Fall Time|Tr|20||47|ps|20% to 80%|
|Tx Input Impedance|Zin||100||Ω|Differential|
|Rx Output Impedance|Zout||100||Ω|Differential|



Notes:All high-speed signals are internally AC coupled. 

www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 4 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ45TGE-3YC Rev1.0- Sep.2020 


## **General Specifications** 

## **Table 5. General specifications** 

|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|---|---|---|---|---|---|
|BR|1||10|Gb/sec|IEEE 802.3 compatible.|
|L|||30|m|Category 6a/7 UTP. BER <10-12|



Notes: 

1. The clock tolerance is +/-50 ppm. 

2. By default, the LP-RJ45TGE-3YC is a full-duplex module in preferred master mode. 

3. Automatic crossover detection, no external crossover cable is required. 

## **Environmental Specifications** 

## **Table 6. Environmental specifications** 

|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Operating Temperature|Top|0||70|°C|Case temperature|
|Storage Temperature|Tsto|-40||85|°C|Ambient temperature|



## **Serial Communication Protocol** 

## **Table 7. Serial Communication Protocol** 

All SFPs support the 2-wire serial communication protocol outlined in the SFP MSA, and these SFPs can be accessed via the MCU's I2C bus at address A0h. 

|**Serial Clock Bus Requirements**|**Serial Clock Bus Requirements**|**Serial Clock Bus Requirements**|**Serial Clock Bus Requirements**|**Serial Clock Bus Requirements**|**Serial Clock Bus Requirements**|**Serial Clock Bus Requirements**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|I2C Clock Rate|Top|0||200,000|Hz||



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 5 of 6 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LP-RJ45TGE-3YC Rev1.0- Sep.2020 


## **Mechanical Specifications** 

## **Mechanical Appearance and Dimensions (Unit: mm):** 

The LP-RJ45TGE-3YC product complies with the mechanical specifications in the SFP MSA1, with the front part of the SFP (the portion extending beyond the host panel) being larger to accommodate the RJ-45 connector. 


## **Ordering information** 

|**Part Number**|**Tx_DIS**|**Link Indicator**<br>**on Rx_LOS Pin**|**Data rate**|**Distance(Max)**|**Temp.**|
|---|---|---|---|---|---|
|LP-RJ45TGE-3YC|Yes|Yes|10M/100M/1.25G<br>/2.5G/5G/10G|30m|0~70°C|



www.link-pp.com **ww** w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 6 of 6 

