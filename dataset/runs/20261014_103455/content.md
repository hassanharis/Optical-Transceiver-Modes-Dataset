**Rev:3.0** 

## **QXP29B4-10DA-3** 

## **100Gb/s QSFP28 LR4 Transceiver** 

## **PRODUCT FEATURES** 

- Compliant with 100GBASE-LR4 

- Support line rates to 103.125 Gbps 

- Integrated LAN WDM DML TOSA / PIN ROSA for up to 10 km reach over SMF 

- Digital Diagnostics Monitoring Interface 

- Duplex LC optical receptacle 

- No external reference clock 

- Electrically hot-pluggable 

- Compliant with QSFP28 MSA with LC connector 

- Case operating temperature range:-40°C to 85°C 

- Power dissipation < 5.0W 

## **APPLICATIONS** 

- 100G Ethernet 

## **STANDARD** 

- Compliant to IEEE 802.3ba 

- Compliant to SFF-8636 


**Page 1** 

**Rev:3.0** 

## **General Description** 

XGIGA 100G QSFP28 LR4 optical Transceiver integrates receiver and transmitter path on one module. In the transmit side, four lanes of serial data streams are recovered, retimed, and passed to four laser drivers. The laser drivers control 4- Distributed Feedback Laser (DFB) with center wavelength of 1296 nm, 1300nm, 1305nm and 1309 nm. The optical signals are multiplexed to a single –mode fiber through an industry standard LC connector. In the receive side, the four lanes of optical data streams are optically demultiplexed by the integrated optical de-multiplexer. Each data stream is recovered by a PIN photo-detector and trans-impedance amplifier, retimed. This module features a hot-pluggable electrical interface, low power consumption and 2-wire serial interface. 

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
|Case Operating Temperature|Tcase|-40|-|85|ºC||
|Power Supply Voltage|VCC|3.13|3.3|3.47|V||
|Power Supply Current|ICC|-||1515|mA||
|Data Rate|BR||25.78125||Gbps|Each channel|
|Transmission Distance|TD||-|10|km||
|Coupled fiber||Single mode fiber||||9/125um SMF|



## Ⅲ **Optical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||




**Page 2** 

**Rev:3.0** 

|||||||**Rev:3.0**|
|---|---|---|---|---|---|---|
|Signaling Speed per Lane|||25.78125 ± 100 ppm||Gbps||
|Wavelength Assignment|λ0|1294.53|1295.56|1296.59|nm||
||λ1|1299.02|1300.05|1301.09|nm||
||λ2|1303.54|1304.58|1305.63|nm||
||λ3|1308.09|1309.14|1310.19|nm||
|Total Output. Power|POUT|||10.5|dBm||
|Transmit OMA per Lane||-1.3||4.5|dBm||
|Average Launch Power Per lane||-4.3||4.5|dBm||
|SMSR||30|||dB||
|Optical Extinction Ratio|ER|4|||dB||
|Average launch Power off per lane|Poff|||-30|dBm||
|RIN|RIN|||-130|dB/Hz||
|Output Eye Mask definition<br>{X1，X2，X3，Y1，Y2，Y3}||{0.25，0.4，0.45，0.25，0.28，0.4}||||1|
|**Receiver**|||||||
|Signaling Speed per Lane|||25.78125 ± 100 ppm||Gbps||
|Wavelength Assignment||1294.53|1295.56|1296.59|nm||
|||1299.02|1300.05|1301.09|nm||
|||1303.54|1304.58|1305.63|nm||
|||1308.09|1309.14|1310.19|nm||
|Receive Power (OMA) per Lane|ROMA|||4.5|dBm||
|Average Input Power per Channel|RXPx|-10.6||4.5|dBm|2|
|Receiver Sensitivity (OMA) per Lane|Rxsens|||-8.6|dBm||
|LOS De-Assert|LOSD|||-12|dBm||
|LOS Assert|LOSA|-30|||dBm||
|Receiver Reflectance|Rr|||-26|dB||



## **Notes:** 

- -5 

- 1. Hit ratio 5x10 . 

- 31 -12 

- 2. Measured with a PRBS 2 -1 test pattern, @25.78Gb/s, BER<10 . 


**Page 3** 

**Rev:3.0** 

## **IV. Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.13|3.3|3.47|V||
|Supply Current|Icc|||1515|mA||
|**Transmitter**|||||||
|Input differential<br>impedance|Rin||100||Ω|1|
|Differential data input<br>swing|Vin,pp|180||1000|mV||
|Transmit Disable Voltage|VD|Vcc–1.3||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V|2|
|**Receiver**|||||||
|Differential data output<br>swing|Vout,pp|300||850|mV|3|
|LOS Fault|VLOS fault|Vcc–1.3||VccHOST|V|4|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|4|



## **Notes:** 

1. Connected directly to TX data input pins. AC coupled thereafter. 

2. Or open circuit. 

3. Into 100 ohms differential termination. 

4. Loss Of Signal is LVTTL. Logic 0 indicates normal operation; logic 1 indicates no signal detected. 


**Page 4** 

**Rev:3.0** 

## **V. Pin Assignment** 

## **Figure 1---Pin out of Connector Block on Host Board** 


|**Pin**|**Symbol**|**Name/Description**|**NOTE**|
|---|---|---|---|
|1|GND|Transmitter Ground(Common with Receiver Ground)|1|
|2|Tx2n|Transmitter Inverted Data Input||
|3|Tx2p|Transmitter Non-Inverted Data output||
|4|GND|Transmitter Ground(Common with Receiver Ground)|1|
|5|Tx4n|Transmitter Inverted Data Input||
|6|Tx4p|Transmitter Non-Inverted Data output||
|7|GND|Transmitter Ground(Common with Receiver Ground)|1|
|8|ModSelL|Module Select||
|9|ResetL|Module Reset||
|10|VccRx|3.3V Power SupplyReceiver|2|
|11|SCL|2-Wire serial Interface Clock||
|12|SDA|2-Wire serial Interface Data||
|13|GND|Transmitter Ground(Common with Receiver Ground)||
|14|Rx3p|Receiver Non-Inverted Data Output||
|15|Rx3n|Receiver Inverted Data Output||
|16|GND|Transmitter Ground(Common with Receiver Ground)|1|
|17|Rx1p|Receiver Non-Inverted Data Output||
|18|Rx1n|Receiver Inverted Data Output||
|19|GND|Transmitter Ground(Common with Receiver Ground)|1|
|20|GND|Transmitter Ground(Common with Receiver Ground)|1|
|21|Rx2n|Receiver Inverted Data Output||




**Page 5** 

**Rev:3.0** 

||||**Rev:3.0**|
|---|---|---|---|
|22|Rx2p|Receiver Non-Inverted Data Output||
|23|GND|Transmitter Ground(Common with Receiver Ground)|1|
|24|Rx4n|Receiver Inverted Data Output|1|
|25|Rx4p|Receiver Non-Inverted Data Output||
|26|GND|Transmitter Ground(Common with Receiver Ground)|1|
|27|ModPrsl|Module Present||
|28|IntL|Interrupt||
|29|VccTx|3.3Vpower supplytransmitter|2|
|30|Vcc1|3.3Vpower supply|2|
|31|LPMode|Low Power Mode||
|32|GND|Transmitter Ground(Common with Receiver Ground)|1|
|33|Tx3p|Transmitter Non-Inverted Data Input||
|34|Tx3n|Transmitter Inverted Data Output||
|35|GND|Transmitter Ground(Common with Receiver Ground)|1|
|36|Tx1p|Transmitter Non-Inverted Data Input||
|37|Tx1n|Transmitter Inverted Data Output||
|38|GND|Transmitter Ground(Common with Receiver Ground)|1|



**Notes:** 

1. GND is the symbol for signal and supply (power) common for QSFP28 modules. All are common within the QSFP28 module and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host board signal common ground plane. 

2. VccRx, Vcc1 and VccTx are the receiving and transmission power suppliers and shall be applied concurrently. Recommended host board power supply filtering is shown below. Vcc Rx, Vcc1 and Vcc Tx may be internally connected within the QSFP28 transceiver module in any combination. The connector pins are each rated for a maximum current of 500mA. 

## **VI. Digital Diagnostic Functions** 

XGIGA QXP29B4-10D A-3 support the 2-wire serial communication protocol as defined in the QSFP28 MSA. Which allows real-time access to the following operating parameters: 

- Transceiver temperature 

- Laser bias current 

- Transmitted optical power 

- Received optical power 

- Transceiver supply voltage 

It also provides a sophisticated system of alarm and warning flags, which may be used to alert end- 


**Page 6** 

**Rev:3.0** 

users when particular operating parameters are outside of a factory-set normal range. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller inside the transceiver, which is accessed through the 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL pin) is generated by the host. The positive edge clocks data into the QSFP28 transceiver into those segments of its memory map. The negative edge clocks data from the QSFP28 transceiver. The serial data signal (SDA pin) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. The 2-wire serial interface provides sequential or random access to the 8 bit parameters, addressed from 00h to the maximum address of the memory. 

This clause defines the Memory Map for QSFP28 transceiver used for serial ID, digital monitoring and certain control functions. The interface is mandatory for all QSFP28 devices. The memory map has been changed in order to accommodate 4 optical channels and limit the required memory space. The structure of the memory is shown in Figure 2 -QSFP28 Memory Map. The memory space is arranged into a lower, single page, address space of 128 bytes and multiple upper address space pages. This structure permits timely access to addresses in the lower page, e.g. Interrupt Flags and Monitors. Less time critical entries, e.g. serial ID information and threshold settings, are available with the Page Select function. The structure also provides address expansion by adding additional upper pages as needed.  For example, in Figure 2 upper pages 01 and 02 are optional.  Upper page 01 allows implementation of Application Select Table, and upper page 02 provides user read/write space.  The lower page and upper pages 00 and 03 are always implemented. The interface address used is A0xh and is mainly used for time critical data like interrupt handling in order to enable a “one-time-read” for all data related to an interrupt situation. After an Interrupt, IntL, has been asserted, the host can read out the flag field to determine the effected channel and type of flag. 

For more detailed information including memory map definitions, please see the QSFP28 MSA Specification. 


**Page 7** 

**Rev:3.0** 

## **VII. Host - Transceiver Interface Block Diagram** 



**Page 8** 

**Rev:3.0** 

## **VIII. Outline Dimensions** 

## **Appendix A. Document Revision** 

|**VersionNo.**|**Date**|**Description**|
|---|---|---|
|1.0|2019-08-07|Preliminarydatasheet|
|2.0|2021-01-22|Update Power dissipation from 4.5W to 5.0W|
|3.0|2021-03-04|Change PNQXP29B4-10DA toQXP29B4-10DA-3(Generation2)|




**Page 9** 

