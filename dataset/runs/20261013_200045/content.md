**FN-TRAN-GC-COM** 1000BASE-T, Category 5, 100m, RJ-45 for Fortinet 


## **FN-TRAN-GC-COM** 

## Copper SFP Transceiver 

## **Features** 

- Up to 1.25Gb/s bi-directional data links 

- Hot-pluggable SFP footprint 

- Extended case temperature range (0°C to +70°C ) 

- Fully metallic enclosure for low EMI 

- Low power dissipation (1.05 W typical) 

- Compact RJ-45 connector assembly 

- Access to physical layer IC via 2-wire serial bus 

- 1000 BASE-T operation in host systems with SERDES interface 

- 10/100/1000Mbps compliant in host systems with SGMII interface 

## **Applications** 

- 1.25 Gigabit Ethernet over Cat 5 cable 

## **Description** 

**FN-TRAN-GC-COM** Copper Small Form Pluggable (SFP) transceivers are high performance, cost effective module compliant with the Gigabit Ethernet and 10/100/1000BASE-T standards as specified in IEEE 802. 3-2002 and IEEE 802.3ab, which supporting 10/100/1000Mbps data- rate up to 100 meters reach over unshielded twisted-pair category 5 cables. The module supports 10/100/1000Mbps full duplex data-links with 5-level Pulse Amplitude Modulation (PAM) signals. All four pairs in the cable are used with symbol rate at 250Mbps on each pair. The module provides standard serial ID information compliant with SFP MSA, which can be accessed with address of A0h via the 2wire serial CMOS EEPROM protocol. The physical IC can also be accessed via 2wire serial bus at address ACh. 

**FN-TRAN-GC-COM** 1000BASE-T, Category 5, 100m, RJ-45 for Fortinet 



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




## **FN-TRAN-GC-COM** 

1000BASE-T, Category 5, 100m, RJ-45 for Fortinet 

||8|LOS|Loss of Signal|3|Note 4||
|---|---|---|---|---|---|---|
||9|VEER|Receiverground|1|||
||10|VEER|Receiverground|1|||
||11|VEER|Receiverground|1|||
||12|RX-|Inv. Received Data Out|3|Note 5||
||13|RX+|Received Data Out|3|Note 5||
||14|VEER|Receiverground|1|||
||15|VCCR|Receiver Power Supply|2|||
||16|VCCT|Transmitter Power Supply|2|||
||17|VEET|Transmitter Ground|1|||
||18|TX+|Transmit Data In|3|Note 6||
||19|TX-|Inv. Transmit Data In|3|Note 6||
||20|VEET|Transmitter Ground|1|||



Notes: 

Plug Seq.: Pin engagement sequence during hot plugging. 

- 1) TX Fault is is not supported and is always connected to ground. 

- 2) TX Disable is not supported. 

resistor on the host board. The pull-up voltage shall be VccT or VccR 

Mod-Def 0 is grounded by the module to indicate that the module is present 

- Mod-Def 1 is the clock line of two wire serial 

- interface for serial ID Mod-Def 2 is the data line of 

two wire serial interface for serial ID 

4) RX_LOS (Loss of Signal): LVTTL compatible with a maximum voltage of Host_Vcc. RX_LOS can enabled or disabled (Refer to Ordering information),RX_LOS is not used and is always tied to ground via 100-ohm resistor 

- 5) RD-/+: These are the differential receiver outputs. They are AC coupled 100 differential lines which should be terminated with 100 (differential) at the user SERDES. 

- 6) TD-/+: These are the differential transmitter inputs. They are AC-coupled, differential lines with 100 differential terminations inside the module. 

## **+3.3V Volt Electrical Power Interface** 

The FN-TRAN-GC-COM has an input voltage range of +5V +/- 5%. The 3.3V maximum voltage is not allowed for continuous operation. 

||**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|**+3.3V volt Electrical Power Interface**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Supply Current|Is||320|375|mA|1.2W max power over full<br>range of voltage and<br>temperature.<br>See caution note below|



**FN-TRAN-GC-COM** 1000BASE-T, Category 5, 100m, RJ-45 for Fortinet 


||Input Voltage|Vcc|3.13|3.3|3.47|V|Referenced to GND||
|---|---|---|---|---|---|---|---|---|
||Maximum Voltage|Vmax|||4|V|||
||Surge Current|Isurge|||30|mA|Hot plug above steady state<br>current. See caution note<br>below||



Caution: Power consumption and surge current are higher than the specified values in the SFP MSA 

## **Low-Speed Signals** 

MOD_ DEF(1) (SCL) and MOD_DEF(2) (SDA), are open drain CMOS signals (see section VII, “Serial Communication Protocol”). Both MOD_ DEF(1) and MOD_DEF(2) must be pulled up to host_Vcc. 

||**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|**Low-Speed Signals, Electronic Characteristics**|
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|**Notes/Conditions**|
|SFP Output<br>LOW|VOL|0|0.5|V|4.7k to 10k pull-up to host_Vcc,<br>measured at host side of connector|
|SFP Output<br>HIGH|VOH|host_Vcc<br>- 0.5|host_Vcc<br>+ 0.3|V|4.7k to 10k pull-up to host_Vcc,<br>measured at host side of connector|
|SFP Input LOW|VIL|0|0.8|V|4.7k to 10k pull-up to Vcc, measured<br>at SFP side of connector|
|SFP Input HIGH|VIH|2|Vcc + 0.3|V|4.7k to 10k pull-up to Vcc, measured<br>at SFP side of connector|



## **High-Speed Electrical Interface** 

All high-speed signals are AC-coupled internally. 

||**High-Speed Electrical Interface**|**High-Speed Electrical Interface**|**High-Speed Electrical Interface**|**High-Speed Electrical Interface**|**Transmission Line-SFP**|**Transmission Line-SFP**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Line Frequency|fL||125||MHz|5-level encoding, per IEEE 802.3|
|Tx Output<br>Impedance|Zout,TX||100||Ohm|Differential, for all Frequencies<br>between 1MHz and 125MHz|
|Rx Input<br>Impedance|Zin,RX||100||Ohm|Differential, for all Frequencies<br>between 1MHz and 125MHz|



## **High-speed electrical interface, host-SFP** 

||**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**|**High-Speed Electrical Interface, Host-SFP**||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Single ended data input<br>swing|Vinsing|250||1200|mV|Single ended|
|Single ended data output<br>swing|Voutsing|350||800|mV|Single ended|
|Rise/Fall Time|Tr,Tf||175||psec|20%-80%|
|Tx Input Impedance|Zin||50||Ohm|Single ended|




## **FN-TRAN-GC-COM** 

1000BASE-T, Category 5, 100m, RJ-45 for Fortinet 

Rx Output Impedance Zout 50 Ohm Single ended 

## **General Specifications** 

|**Parameter**||||**General**|**General**||
|---|---|---|---|---|---|---|
||**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Data Rate<br>Cable Length|BR|10||1,000|Mb/sec|IEEE 802.3 compatible.<br>See Notes 2 through 4 below|
||L|||100|m|Category5 UTP. BER <10-12|



Notes: 

1. Clock tolerance is +/- 50 ppm. 

2. By default, the **FN-TRAN-GC-COM** 

is a full duplex device in preferred master mode. 

3. Automatic crossover detection is enabled. External crossover cable is not required. 

## **Environmental Specifications** 

||**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**|**Environmental Specifications**||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Notes/Conditions**|
|Operating<br>Temperature|Top|0||70|°C|Case temperature|
|Storage Temperature|Tsto|-40||85|°C|Ambient temperature|



## **Mechanical Specifications** 

## The host-side of the **FN-TRAN-GC-COM** 

conforms to the mechanical specifications outlined in the SFP MSA1. The front portion of the SFP (part extending beyond the face plate of the host) is larger to accommodate the RJ-45 connector. 

**FN-TRAN-GC-COM** 1000BASE-T, Category 5, 100m, RJ-45 for Fortinet 



Figure2. GLC-T mechanical dimensions 

## **References** 

1. Small Form Factor Pluggable (SFP) Transceiver Multi-Source Agreement (MSA). 

2. IEEE Std 802.3, 2002 Edition. IEEE Standards Department, 2002. 

3. “AT24C01A/02/04/08/16 2-Wire Serial CMOS E2PROM”, Atmel Corporation. 

## **Ordering information** 

**Part number Operating Case temperature FN-TRAN-GC-COM** 1000Mbps only, SERDES interface, Copper SFP with spring latch 

