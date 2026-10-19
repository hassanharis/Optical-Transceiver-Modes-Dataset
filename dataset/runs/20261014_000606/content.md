LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-M8540-SR4C Rev1.0- Sep.2020 


## **LQ-M8540-SR4C** 

## 40Gbps 850nm QSFP+ SR4 300m Transceiver 

## **Product Features** 

- 4 independent full-duplex channels 

- High Channel Capacity: 40Gbps per module 

- Up to 11.2Gbps Data rate per channel 

- MTP/MPO optical connector 

- High Reliability 850nm VCSEL technology 

- Maximum link length of 100m links on OM3 multimode fiber or 300m links on OM4 multimode fiber 

- Hot Pluggable 

- Power dissipation﹤1.5W 

- Real Time Digital Diagnostic Monitoring 

- Operating case temperature: 0 to +70°C 

## **Applications** 

- 40 Ethernet links 

- Infiniband QDR, DDR and SDR 

- 40G Telecom connections 


## **Standard** 

- Compliant to IEEE 802.3ba 

- Compliant with QSFP+ MSA 

- Compliant to SFF-8436 

**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 1 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-M8540-SR4C Rev1.0- Sep.2020 


## **Description** 

LQ-M8540-SR4C are designed for use in 40 Gigabit per second links over multimode fiber. They are compliant with the QSFP+ MSA and IEEE 802.3ba 40GBASE-SR4.The optical transmitter portion of the transceiver incorporates a 4-channel VCSEL (Vertical Cavity Surface Emitting Laser) array, a 4-channel input buffer and laser driver, diagnostic monitors, control and bias blocks. For module control, the control interface incorporates a Two Wire Serial interface of clock and data signals. Diagnostic monitors for VCSEL bias, module temperature, received optical power and supply voltage are implemented and results are available through the TWS interface. Alarm and warning thresholds are established for the monitored attributes. Flags are set and interrupts generated when the attributes are outside the thresholds. Flags are also set and interrupts generated for loss of input signal (LOS) and transmitter fault conditions. All flags are latched and will remain set even if the condition initiating the latch clears and operation resumes. All interrupts can be masked and flags are reset by reading the appropriate flag register. The optical output will squelch for loss of input signal unless squelch is disabled. Fault detection or channel deactivation through the TWS interface will disable the channel. Status, alarm/warning and fault information are available via the TWS interface. 

The optical receiver portion of the transceiver incorporates a 4-channel PIN photodiode array, a 4-channel TIA array, a 4 channel output buffer, diagnostic monitors, and control and bias blocks. Diagnostic monitors for optical input power are implemented and results are available through the TWS interface. Alarm and warning thresholds are established for the monitored attributes. Flags are set and interrupts generated when the attributes are outside the thresholds. Flags are also set and interrupts generated for loss of optical input signal (LOS). All flags are latched and will remain set even if the condition initiating the flag clears and operation resumes. All interrupts can be masked and flags are reset upon reading the appropriate flag register. The electrical output will squelch for loss of input signal (unless squelch is disabled) and channel de-activation through TWS interface. Status and alarm/warning information are available via the TWS interface. 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|Storage Ambient Temperature|TSTG|-40|85|℃|
|Operating Humidity|HO|5|95|%|
|Power Supply Voltage|Vcc|-0.5|3.6|V|



**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 2 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-M8540-SR4C Rev1.0- Sep.2020 


## **Recommended Operating Conditions** 

|**Recommended Operating Conditions**|**Recommended Operating Conditions**|**Recommended Operating Conditions**|**Recommended Operating Conditions**|**Recommended Operating Conditions**|**Recommended Operating Conditions**|
|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|
|Operating Case Temperature|Tc|0||70|℃|
|Power Supply Voltage|Vcc|3.135|3.3|3.465|V|
|Power Supply Current|ICC|||200|mA|
|Aggregate Bit Rate|BRAVE||41.25||Gbps|
|Data Rate,each Lane|BRAVE||10.3125|11.2|Gbps|
|Transmission Distance|TD:OM3|-|100|-|m|
|Transmission Distance|TD:OM4||300||m|



## **Electrical transmitter Characteristics** 

|**Parameter**|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|
|Input Impedance (Differential)||Zin|85|100|115|ohms|Rin > 100 kohms<br>@DC|
|Differential data input swing||Vin,pp|180||1000|mV||
|TX Disable|Disable|VIH|2||Vcc+0.3|V||
||Enable|VIL|0||0.8|||
|TX FAULT|Fault|VOH|2.4||Vcc+0.3|V||
||Normal|VOL|0||0.8|||



## **Electrical receiver Characteristics** 

|**Parameter**|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|---|
|Input Impedance (Differential)||Zin|85|100|115|ohms||
|Differential data output swing||Vout,pp|300||850|mV||
|RX_LOS|LOS|VoH|2.4||Vcc+0.3|V||
||Normal|VoL|0||0.8|||
|Rise Time||tr|||30|ps|10%~90%|
|Fall Time||tf|||30|ps|10%~90%|



**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 3 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-M8540-SR4C Rev1.0- Sep.2020 


## **Optical Characteristics** 

|**Transmitter**|**Transmitter**|**Transmitter**|**Transmitter**|**Transmitter**|**Transmitter**|**Transmitter**|**Transmitter**|**Transmitter**|**Transmitter**|**Transmitter**||
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Parameter**||**Symbol**||**Min**||**Typical**||**Max**||**Unit**|**Notes**|
|Average Launch Power each lane||Pavg||-7.6||||1||dBm||
|Per Lane Bit Rate||Er||||3||||dB||
|Center Wavelength||λ0||840||850||860||nm||
|Spectral Width(-20dB)||∆λ||||||0.65||nm||
|Average launch Power off each<br>lane||Poff||||||-30||dBm||
|Transmitter and Dispersion<br>Penaltyeach lane||TDP||||||3.5||dB||
|Optical Return Loss Tolerance||ORL||||||12||dB||
|Output Eye Diagram||IEEE 802.3ba-2010 Compliant||||||||||
|**Treceiver**||||||||||||
|**Parameter**|||**Symbol**||**Min**||**Typical**||**Max**|**Unit**|**Notes**|
|Receiver Wavelength|||λin||840||850||860|nm||
|Receiver sensitivity in OMA, each<br>lane|||Pmins||||||-9.5|dBm||
|Input Saturation Power (Overload)|||Psat||2.4|||||dBm||
|Receiver reflectance|||Rr||||||-12|dB||
|LOS|Optical De-assert||LOSD||||||-12|dBm||
||Optical Assert||LOSA||-30|||||||



## **Digital Diagnostic Monitoring Information** 

Link-pp LQ-M8540-SR4C support the 2-wire serial communication protocol as defined in the QSFP+ MSA, which allows real-time access to the following operating parameters: 

- Transceiver temperature 

- Laser bias current 

- Transmitted optical power 

- Received optical power 

- Transceiver supply voltage 

It also provides a sophisticated system of alarm and warning flags, which may be used to alert end-users when particular operating parameters are outside of a factory-set normal range.The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller inside the transceiver, 

**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 4 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-M8540-SR4C Rev1.0- Sep.2020 


which is accessed through the 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL pin) is generated by the host. The positive edge clocks data into the QSFP+ transceiver into those segments of its memory map that are not write-protected. The negative edge clocks data from the QSFP+ transceiver. The serial data signal (SDA pin) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. The 2-wire serial interface provides sequential or random access to the 8 bit parameters, addressed from 00h to the maximum address of the memory. 

This clause defines the Memory Map for QSFP+ transceiver used for serial ID, digital monitoring and certain control functions. The interface is mandatory for all QSFP+ devices. The memory map has been changed in order to accommodate 4 optical channels and limit the required memory space. The structure of the memory is shown in Figure 2 -QSFP+ Memory Map. The memory space is arranged into a lower, single page, address space of 128 bytes and multiple upper address space pages. This structure permits timely access to addresses in the lower page, e.g. Interrupt Flags and Monitors. Less time critical entries, e.g. serial ID information and threshold settings, are available with the Page Select function. The structure also provides address expansion by adding additional upper pages as needed. For example, in Figure 2 upper pages 01 and 02 are optional. Upper page 01 allows implementation of Application Select Table, and upper page 02 provides user read/write space. The lower page and upper pages 00 and 03 are always implemented. The interface address used is A0xh and is mainly used for time critical data like interrupt handling in order to enable a “one-time-read” for all data related to an interrupt situation. After an Interrupt, IntL, has been asserted, the host can read out the flag field to determine the effected channel and type of flag.For more detailed information including memory map definitions, please see the QSFP+ MSA Specification. 

## **Pin Definition** 


Figure1 QSFP MSA-compliant 38-pin connector 

**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 5 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-M8540-SR4C Rev1.0- Sep.2020 


|**Pin**|**Symbol**|**Name/Description**|**Notes**|
|---|---|---|---|
|1|GND|Transmitter Ground(Common with Receiver Ground)|1|
|2|TX2N|Transmitter Inverted Data Input||
|3|TX2P|Transmitter Non-Inverted Data Input||
|4|GND|Ground|1|
|5|TX4N|Transmitter Inverted Data Input||
|6|TX4P|Transmitter Non-Inverted Data Input||
|7|GND|Ground|1|
|8|ModSelL|Module Select||
|9|ResetL|Module Reset||
|10|Vcc Rx|+3.3 V Power supply receiver|2|
|11|SCL|2-wire serial interface clock||
|12|SDA|2-wire serial interface data||
|13|GND|Ground||
|14|RX3P|Receiver Non-Inverted Data Output||
|15|RX3N|Receiver Inverted Data Output||
|16|GND|Ground|1|
|17|RX1P|Receiver Non-Inverted Data Output||
|18|RX1N|Receiver Inverted Data Output||
|19|GND|Ground|1|
|20|GND|Ground|1|
|21|RX2N|Receiver Inverted Data Output||
|22|RX2P|Receiver Non-Inverted Data Output||
|23|GND|Ground|1|
|24|RX4N|Receiver Inverted Data Output|1|
|25|RX4P|Receiver Non-Inverted Data Output||
|26|GND|Ground|1|
|27|ModPrsL|Module Present||
|28|IntL|Interrupt||
|29|Vcc Tx|+3.3 V Power supply transmitter|2|
|30|Vcc1|+3.3 V Power Supply|2|
|31|LPMode|Low Power Mode||
|32|GND|Ground|1|
|33|TX3P|Transmitter Non-Inverted Data Input||



**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 6 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-M8540-SR4C Rev1.0- Sep.2020 


|34|TX3N|Transmitter Inverted Data input||
|---|---|---|---|
|35|GND|Ground|1|
|36|TX1P|Transmitter Non-Inverted Data Input||
|37|TX1N|Transmitter Inverted Data input||
|38|GND|Ground|1|



Table 1: QSFP Module PIN Definition 

## **Notes** ： 

1. All Ground (GND) are common within the QSFP+ module and all module voltages are referenced to this potential unless noted otherwise. Connect these directly to the host board signal common ground plane. 2. VccRx, Vcc1 and VccTx are the receiving and transmission power suppliers and shall be applied concurrently. The connector pins are each rated for a maximum current of 500mA. 

## **Package Outline** 

Dimensions are in millimeters. All dimensions are ±0.1mm unless otherwise specified. (Unit: mm) 


**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 7 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-M8540-SR4C Rev1.0- Sep.2020 


## **Regulatory Compliance** 

|**Feature**|**Test**|**Method**|
|---|---|---|
|Electrostatic Discharge<br>(ESD) to the Electrical Pins|MIL-STD-883E<br>Method 3015.7|Class 1(>1000V for SFI<br>pins, >2000Vfor other pins.)|
|Electrostatic Discharge<br>(ESD)Immunity|IEC61000-4-2|Class 2(>4.0kV)|
|Electromagnetic<br>Interference (EMI)|CISPR22 ITE Class B<br>FCC Class B<br>CENELEC EN55022<br>VCCI Class 1|Comply with standard|
|Immunity|IEC61000-4-3|Comply with standard|
|Eye Safety|FDA 21CFR 1040.10 and<br>1040.11<br>EN(IEC)60825-1,2|Compatible with Class I laser<br>Product|



## **Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|LQ-M8540-SR4C|QSFP+ 850nm,40Gbps,MTP/MPO,300m,0°C~+70°C,with DDM|



**ww** www.link-pp.com w.l-p.comw.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 8 of 8 

