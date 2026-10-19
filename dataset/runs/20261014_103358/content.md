**REV:1.0** 


## **100Gb/s QSFP28 LR4 Receiver** 

## **PRODUCT FEATURES** 

- ⚫ Compliant with 100GBASE-LR4 and ITU-T G.959.1 

- ⚫ Support line rates from 103.125 Gbps to 111.81 Gbps 

- ⚫ Integrated LAN WDM ROSA for up to 10 km reach over SMF 

- ⚫ Digital Diagnostics Monitoring Interface 

- ⚫ Duplex LC optical receptacle 

- ⚫ No external reference clock 

- ⚫ Electrically hot-pluggable 

- ⚫ Compliant with QSFP28 MSA with LC connector 

- ⚫ Case operating temperature range:0°C to 70°C 

- ⚫ Power dissipation < 2 W 

## **APPLICATIONS** 

- ⚫ 100G Ethernet 

- ⚫ ITU-T OTU4 

## **STANDARD** 

- ⚫ Compliant to IEEE 802.3ba, IEEE 802.3bm and ITU-T G959.1 

- ⚫ Compliant to SFF-8636 

- ⚫ RoHS Compliant. 

**www.xgiga.cn                                           Page 1** 

**REV:1.0** 


## **General Description** 

XGIGA 100G QSFP28 LR4 receiver integrates receiver on one module. In the receive side, the four lanes of optical data streams are optically de-multiplexed by the integrated optical de-multiplexer. Each data stream is recovered by a PIN photo-detector and trans-impedance amplifier, retimed. This module features a hot-pluggable electrical interface, low power consumption and 2-wire serial interface. 

The product is designed with form factor, optical/electrical connection and digital diagnostic interface according to the QSFP28 Multi-Source Agreement (MSA) and compliant to IEEE 802.3ba. 

## Ⅰ **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature|Ts|-40|-|85|ºC||
|Relative Humidity|RH|5|-|95|%||
|Power SupplyVoltage|VCC|-0.3|-|4|V||
|Signal Input Voltage||Vcc-0.3|-|Vcc+0.3|V||



## Ⅱ **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Tcase|0|-|70|ºC|Without air flow|
|Power SupplyVoltage|VCC|3.13|3.3|3.47|V||
|Power SupplyCurrent|ICC|-||600|mA||
|Data Rate|BR||25.78125/27.9525||Gbps|Each channel|
|Transmission Distance|TD||-|10|km||
|Coupled fiber|Single mode fiber|||||9/125um SMF|



## Ⅲ **Optical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|**Receiver**|||||||
|Rx Sensitivity per lane|RSENS|||-10.6|dBm|1|
|LOS De-Assert|LOSD|||-12|dBm||
|LOS Assert|LOSA|-30|||dBm||
|Input Saturation Power (Overload)|Psat|||4.5|dBm||
|Receiver Reflectance|Rr|||-26|dB||



**www.xgiga.cn                                           Page 2** 

**REV:1.0** 


## **Notes:** 

- 31 -12 

- 1. Measured with a PRBS 2 -1 test pattern, @25.78Gb/s, BER<10 . 

## **IV. Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.13|3.3|3.47|V||
|Supply Current|Icc|||600|mA||
|**Receiver**|||||||
|Differential data output swing|Vout,pp|300||850|mV|3|
|LOS Fault|VLOS fault|Vcc–1.3||VccHOST|V|4|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|4|



## **Notes:** 

1. Connected directly to TX data input pins. AC coupled thereafter. 

2. Or open circuit. 

3. Into 100 ohms differential termination. 

4. Loss Of Signal is LVTTL. Logic 0 indicates normal operation; logic 1 indicates no signal detected. 

## **V. Pin Assignment** 

**Figure 1---Pin out of Connector Block on Host Board** 


**www.xgiga.cn                                           Page 3** 

**REV:1.0** 


|**Pin**|**Symbol**|**Name/Description**|**NOTE**|
|---|---|---|---|
|1|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|2|Tx2n|Transmitter Inverted Data Input||
|3|Tx2p|Transmitter Non-Inverted Data output||
|4|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|5|Tx4n|Transmitter Inverted Data Input||
|6|Tx4p|Transmitter Non-Inverted Data output||
|7|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|8|ModSelL|ModuleSelect||
|9|ResetL|Module Reset||
|10|VccRx|3.3V PowerSupplyReceiver|2|
|11|SCL|2-Wire serial InterfaceClock||
|12|SDA|2-Wire serial Interface Data||
|13|GND|TransmitterGround(Commonwith ReceiverGround)||
|14|Rx3p|Receiver Non-Inverted DataOutput||
|15|Rx3n|Receiver Inverted DataOutput||
|16|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|17|Rx1p|Receiver Non-Inverted DataOutput||
|18|Rx1n|Receiver Inverted DataOutput||
|19|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|20|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|21|Rx2n|Receiver Inverted DataOutput||
|22|Rx2p|Receiver Non-Inverted DataOutput||
|23|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|24|Rx4n|Receiver Inverted DataOutput|1|
|25|Rx4p|Receiver Non-Inverted DataOutput||
|26|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|27|ModPrsl|Module Present||
|28|IntL|Interrupt||
|29|VccTx|3.3Vpower supplytransmitter|2|
|30|Vcc1|3.3Vpower supply|2|
|31|LPMode|LowPower Mode||
|32|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|33|Tx3p|Transmitter Non-Inverted Data Input||
|34|Tx3n|Transmitter Inverted DataOutput||
|35|GND|TransmitterGround(Commonwith ReceiverGround)|1|
|36|Tx1p|Transmitter Non-Inverted Data Input||
|37|Tx1n|Transmitter Inverted DataOutput||
|38|GND|TransmitterGround(Commonwith ReceiverGround)|1|



**Notes:** 

1. GND is the symbol for signal and supply (power) common for QSFP28 modules. All are common within the QSFP28 module and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host board signal common ground plane. 

2. VccRx, Vcc1 and VccTx are the receiving and transmission power suppliers and shall be applied concurrently. Recommended host board power supply filtering is shown below. Vcc Rx, Vcc1 and Vcc Tx may be internally connected within the QSFP28 transceiver module in any combination. The connector 

**www.xgiga.cn                                           Page 4** 

**REV:1.0** 


pins are each rated for a maximum current of 500mA. 

## **VI. Digital Diagnostic Functions** 

XGIGA QXP29B4-10D-RX support the 2-wire serial communication protocol as defined in the QSFP28 MSA. Which allows real-time access to the following operating parameters: 

- Transceiver temperature 

- Received optical power 

- Transceiver supply voltage 

It also provides a sophisticated system of alarm and warning flags, which may be used to alert end-users when particular operating parameters are outside of a factory-set normal range. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller inside the transceiver, which is accessed through the 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL pin) is generated by the host. The positive edge clocks data into the QSFP28 transceiver into those segments of its memory map that are not write-protected. The negative edge clocks data from the QSFP28 transceiver. The serial data signal (SDA pin) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. The 2-wire serial interface provides sequential or random access to the 8 bit parameters, addressed from 00h to the maximum address of the memory. 

This clause defines the Memory Map for QSFP28 transceiver used for serial ID, digital monitoring and certain control functions. The interface is mandatory for all QSFP28 devices. The memory map has been changed in order to accommodate 4 optical channels and limit the required memory space. The structure of the memory is shown in Figure 2 -QSFP28 Memory Map. The memory space is arranged into a lower, single page, address space of 128 bytes and multiple upper address space pages. This structure permits timely access to addresses in the lower page, e.g. Interrupt Flags and Monitors. Less time critical entries, e.g. serial ID information and threshold settings, are available with the Page Select function. The structure also provides address expansion by adding additional upper pages as needed.  For example, in Figure 2 upper pages 01 and 02 are optional.  Upper page 01 allows implementation of Application Select Table, and upper page 02 provides user read/write space.  The lower page and upper pages 00 and 03 are always implemented. The interface address used is A0xh and is mainly used for time critical data like interrupt handling in order to enable a “one-time-read” for all data related to an interrupt situation. After an Interrupt, IntL, has been asserted, the host can read out the flag field to determine the effected channel and type of flag. 

**www.xgiga.cn                                           Page 5** 

**REV:1.0** 


For more detailed information including memory map definitions, please see the QSFP28 MSA Specification. 

## **VII. Host - Transceiver Interface Block Diagram** 


**www.xgiga.cn                                           Page 6** 

**REV:1.0** 


## **VIII. Outline Dimensions** 

## **Appendix A. Document Revision** 

|**Version No.**|**Date**|**Description**|
|---|---|---|
|Preliminary|2016-8-10|Preliminarydatasheet|



**www.xgiga.cn                                           Page 7** 

