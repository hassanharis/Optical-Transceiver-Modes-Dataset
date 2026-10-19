**REV:2.0** 


## **XP-T96-02-2 10GBASE-T Copper SFP+ Transceiver** 

## **PRODUCT FEATURES** 

- Support 10Gbase-T / 5Gbase-T / 2.5Gbase-T / 1000base-T on line port 

- Support 10Gbase-R on host port 

- Hot-pluggable SFP footprint 

- Low power dissipation (Max 3.6W) 

- Compact RJ-45 connector assembly 

- RoHS compliant and lead-free 

- Single +3.3V power supply 

- 10 Gigabit Ethernet over Cat 6a cable 

- Case operating temperature：0°C to +70°C 

## **APPLICATIONS** 

- 10G BASE-T 

- 5G BASE-T 

- 2.5G BASE-T 

- 1000 BASE-T 

**www.xgiga.cn                                           Page 1** 

**REV:2.0** 


## **PRODUCT DESCRIPTION** 

XGIGA’S XP-T96-02-2 10GBASE-T Copper Small Form Pluggable (SFP+) transceivers are based on the SFP Multi Source Agreement (MSA). They are compatible with the 10Gigabit Ethernet and 10GBASE-T/5GBASE-T/2.5GBASE-T/1000BASE-T standards as specified in IEEE Std 802.3. 

SFP+ 10GBASE-T uses the SFP's RX_LOS(must be pulled up on host) pin for link indication. If pull up or open SFP's TX_DISABLE pin,  PHY IC be reset. 

## **Cable Length** 

|**Line Port**|**Cable**|**Reach**|**Host Port**|
|---|---|---|---|
|10Gbase-T|CAT6A|30m|10GBase-R|
|5Gbase-T|CAT5E|100m|10GBase-R|
|2.5Gbase-T|CAT5E|100m|10GBase-R|
|1000base-T|CAT5E|100m|10GBase-R|
|100base-Tx|CAT5E|100m|10GBase-R|



## **I. SFP to Host Connector Pin Out** 


**Figure 1. Diagram of host board connector block pin numbers and names** 

|**Pin**|**Symbol**|**Name/Description**|**Ref.**|
|---|---|---|---|
|1|VEET|Transmitter Ground  (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault. Not supported.||



**www.xgiga.cn                                           Page 2** 

**REV:2.0** 


|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|2|
|---|---|---|---|
|4|MOD_DEF(2)|Module Definition 2. Data line for Serial ID.|3|
|5|MOD_DEF(1)|Module Definition 1. Clock line for Serial ID.|3|
|6|MOD_DEF(0)|Module Definition 0. Grounded within the module.|3|
|7|Rate Select|No connection required||
|8|LOS|High indicates no linked.  low indicates linked.||
|9|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|||||
|10|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|||||
|11|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|||||
|12|RD-|Receiver Inverted DATA out.  AC Coupled||
|13|RD+|Receiver Non-inverted DATA out.  AC Coupled||
|14|VEER|Receiver Ground  (Common with Transmitter Ground)|1|
|15|VCCR|Receiver Power Supply||
|16|VCCT|Transmitter Power Supply||
|17|VEET|Transmitter Ground  (Common with Receiver Ground)|1|
|||||
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in.  AC Coupled.||
|20|VEET|Transmitter Ground  (Common with Receiver Ground)|1|



Notes: 

1. Circuit ground is connected to chassis ground 

2. PHY disabled on TDIS  > 2.0V or open, enabled on TDIS < 0.8V 

3. Should be pulled up with 4.7k - 10k Ohms on host board to a voltage between 2.0 V and 3.6 V. MOD_DEF(0) pulls line low to indicate module is plugged in. 

## **II. +3.3V Volt Electrical Power Interface** 

The XP-T96-02-2 has an input voltage range of 3.3 V +/- 5%. The 4V maximum voltage is not allowed for continuous operation. 

**www.xgiga.cn                                           Page 3** 

**REV:2.0** 


|**+3.3 Volt Electrical Power Interface**|**+3.3 Volt Electrical Power Interface**|**+3.3 Volt Electrical Power Interface**|**+3.3 Volt Electrical Power Interface**|**+3.3 Volt Electrical Power Interface**|**+3.3 Volt Electrical Power Interface**|**+3.3 Volt Electrical Power Interface**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes/Conditions**|
|Supply Current|Is||900|1100|mA|3.6W max power over<br>full range of voltage<br>and temperature.<br>See caution note below|
|Input Voltage|Vcc|3.13|3.3|3.47|V|Referenced to GND|
|Maximum Voltage|Vmax|||4|V||
|Surge Current|Isurge||TBD||mA|Hot plug above steady state<br>current.  See caution note<br>below|



Caution: Power consumption and surge current are higher than the specified values in the SFP MSA 

## **III. Low-Speed Signals** 

MOD_DEF(1)  (SCL)  and  MOD_DEF(2)  (SDA),  are  open  drain  CMOS  signals  (see section VII, "Serial Communication Protocol").   Both MOD_DEF(1) and MOD_DEF(2) must be pulled up to host_Vcc 

|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|**Notes/Conditions**|
|SFP Output LOW|VOL|0|0.5|V|4.7k to 10k pull-up to host_Vcc,<br>measured at host side of connector|
|SFP Output HIGH|VOH|host_Vcc -0.5|host_Vcc + 0.3|V|4.7k to 10k pull-up to host_Vcc,<br>measured at host side of connector|
|SFP Input LOW|VIL|0|0.8|V|4.7k to 10k pull-up to Vcc,<br>measured at SFPside ofconnector|
|SFP Input HIGH|VIH|2|Vcc + 0.3|V|4.7k to 10k pull-up to Vcc,<br>measured at SFP side of connector|



## **IV. High-Speed Electrical Interface** 

All high-speed signals are AC-coupled internally. 

|**High-Speed Electrical Interface, Transmission Line-SFP**|**High-Speed Electrical Interface, Transmission Line-SFP**|**High-Speed Electrical Interface, Transmission Line-SFP**|**High-Speed Electrical Interface, Transmission Line-SFP**|**High-Speed Electrical Interface, Transmission Line-SFP**|**High-Speed Electrical Interface, Transmission Line-SFP**|**High-Speed Electrical Interface, Transmission Line-SFP**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**unit**|**Notes/Conditions**|
|Line Frequency|fL||125||MHz|5-level encoding, per<br>IEEE 802.3|
|Tx Output Impedance|Zout,TX||100||Ohm|Differential, for all<br>frequencies between<br>1MHz and 125MHz|
|Rx Input Impedance|Zin,RX||100||Ohm|Differential, for all<br>frequencies between<br>1MHz and 125MHz|



**www.xgiga.cn                                           Page 4** 

**REV:2.0** 


|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**unit**|**Notes/Conditions**|
|Single ended data input<br>swing|Vinsing|250||1200|mV|Single ended|
|Single ended data output<br>swing|Voutsing|350||800|mV|Single ended|
|Rise/Fall Time|Tr, Tf||175||psec|20%-80%|
|Tx Input Impedance|Zin||50||Ohm|Single ended|
|Rx Output Impedance|Zout||50||Ohm|Single ended|



## **V. General Specifications** 

|**General**|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**unit**|**Notes/Conditions**|
|Data Rate|BR|1||10|Gb/sec|IEEE 802.3 compatible.<br>See Notes 1,2 below|



## **Notes:** 

1. Clock tolerance is +/- 50 ppm 

2. By default, the XP-T96-02-2 is a full duplex device in preferred master mode 

## **VI. Environmental Specifications** 

|**Environmental Specifications**|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**unit**|**Notes/Conditions**|
|Case OperatingTemperature|Tcase|0||70|°C|Case temperature|
|Storage Temperature|Tsto|-40||85|°C|Ambient temperature|



## **VII. Serial Communication Protocol** 

XP-T96-02-2 supports the 2-wire serial communication protocol outlined in the SFP MSA. These SFPs use an MCU, can be accessed with address of A0h. 

|**Serial Bus Timing Requirements**|**Serial Bus Timing Requirements**|**Serial Bus Timing Requirements**|**Serial Bus Timing Requirements**|**Serial Bus Timing Requirements**|**Serial Bus Timing Requirements**|**Serial Bus Timing Requirements**|
|---|---|---|---|---|---|---|
|Parameter|Symbol|Min.|Typ.|Max.|unit|Notes/Conditions|
|I2C Clock Rate||0||200,000|Hz||



**www.xgiga.cn                                           Page 5** 

**REV:2.0** 


## **VIII. Recommended Application Circuit** 


**www.xgiga.cn                                           Page 6** 

**REV:2.0** 


## **IX. Outline Dimensions (mm)** 


## **Appendix A. Document Revision** 

|**Version No. **|**Date **|**Description **|
|---|---|---|
|1.0|2022-04-02|Preliminarydatasheet.|
|2.0|2022-08-17|Update reach from 50m to 100m for 2.5G and 5G.|



**www.xgiga.cn                                           Page 7** 

