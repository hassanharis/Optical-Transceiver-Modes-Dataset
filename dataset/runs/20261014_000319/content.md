LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


## **LQ-LW100-LR4C** 

## 100G QSFP28 LR4 10KM Optical Transceiver 

## **Features** 

- Compliant with the QSFP28 MSA Technical Specifications. 

- Supports operation for a data rate of 103.1Gb/s. 

- Maximum link length of 10km on Single Mode Fiber (SMF). 

- Optical specifications are compliant with IEEE802.3ba 100GBASE-LR4. 

- Low speed electrical signal is compliant with SFF-8679. 

- High speed electrical signal is compliant with 802.3bm CAUI-4. 

- Digital diagnostic functions are available via the I2C interface, as specified by SFF-8636. 

- 4x25Gb/s DFB-based LAN-WDM transmitter with central wavelengths of 4 channels 1295.56, 1300.05, 1304.58 and 1309.14 nm. 

- Supports operation for a case temperature of 0°C to +70 °C. 

- Duplex LC receptacles. 

- Single 3.3V Power Supply. 

- ROHS Compliant. 

## **Applications** 

- 100GBASE-LR4 Ethernet Links 

- Infiniband QDR and DDR interconnects 

- Client-side 100G Telecom connections 

## **Description** 

This product is a 100Gb/s transceiver module designed for optical communication applications compliant to 100GBASE-LR4 of the IEEE P802.3ba standard. The module converts 4 input channels of 25Gb/s electrical data to 4 channels of LAN WDM optical signals and then multiplexes them into a single channel for 100Gb/s optical transmission. Reversely on the receiver side, the module de-multiplexes a 100Gb/s optical input into 4 channels of LAN WDM optical signals and then converts them to 4 output channels of electrical data. 

The central wavelengths of the 4 LAN WDM channels are 1295.56, 1300.05, 1304.58 and 1309.14 nm as members of the LAN WDM wavelength grid defined in IEEE 802.3ba. The high performance cooled LAN WDM EA-DFB transmitters and high sensitivity PIN receivers provide superior performance for 100Gigabit Ethernet 

www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 1 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


applications up to 10km links and compliant to optical interface with IEEE802.3ba Clause 88 100GBASE-LR4 requirements. 

The product is designed with form factor, optical/electrical connection and digital diagnostic interface according to the QSFP+ Multi-Source Agreement (MSA). It has been designed to meet the harshest external operating conditions including temperature, humidity and EMI interference. 

## **Functional Description** 

The transceiver module receives 4 channels of 25Gb/s electrical data, which are processed by a 4-channel Clock and Data Recovery (CDR) IC that reshapes and reduces the jitter of each electrical signal. Subsequently, each of 4 EML laser driver IC's converts one of the 4 channels of electrical signals to an optical signal that is transmitted from one of the 4 cooled EML lasers which are packaged in the Transmitter Optical Sub-Assembly (TOSA). Each laser launches the optical signal in specific wavelength specified in IEEE802.3ba 100GBASE-LR4 requirements. These 4-lane optical signals will be optically multiplexed into a single fiber by a 4-to-1 optical WDM MUX. The optical output power of each channel is maintained constant by an automatic power control (APC) circuit. The transmitter output can be turned off by TX_DIS hardware signal and/or 2-wire serial interface. 

The receiver receives 4-lane LAN WDM optical signals. The optical signals are de-multiplexed by a 1-to-4 optical DEMUX and each of the resulting 4 channels of optical signals is fed into one of the 4 receivers that are packaged into the Receiver Optical Sub-Assembly (ROSA). Each receiver converts the optical signal to an electrical signal. The regenerated electrical signals are retimed and de-jittered and amplified by the RX portion of the 4-channel CDR. The retimed 4-lane output electrical signals are compliant with IEEE CAUI-4 interface requirements. In addition, each received optical signal is monitored by the DOM section. The monitored value is reported through the 2-wire serial interface. If one or more received optical signal is weaker than the threshold level, RX_LOS hardware alarm will be triggered. 

A single +3.3V power supply is required to power up this product. Both power supply pins VccTx and VccRx are internally connected and should be applied concurrently. As per MSA specifications the module offers 7 low speed hardware control pins (including the 2-wire serial interface): ModSelL, SCL, SDA, ResetL, LPMode, ModPrsL and IntL. 

Module Select (ModSelL) is an input pin. When held low by the host, this product responds to 2-wire serial communication commands. The ModSelL allows the use of this product on a single 2-wire interface bus – individual ModSelL lines must be used. 

Serial Clock (SCL) and Serial Data (SDA) are required for the 2-wire serial bus communication interface and enable the host to access the QSFP28 memory map. 

The ResetL pin enables a complete reset, returning the settings to their default state, when a low level on the ResetL pin is held for longer than the minimum pulse length. During the execution of a reset the host shall disregard all status bits until it indicates a completion of the reset interrupt. The product indicates this by posting an IntL (Interrupt) signal with the Data_Not_Ready bit negated in the memory map. Note that on power up (including hot insertion) the module should post this completion of reset interrupt without requiring 

www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 2 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


## a reset. 

Low Power Mode (LPMode) pin is used to set the maximum power consumption for the product in order to protect hosts that are not capable of cooling higher power modules, should such modules be accidentally inserted. 

Module Present (ModPrsL) is a signal local to the host board which, in the absence of a product, is normally pulled up to the host Vcc. When the product is inserted into the connector, it completes the path to ground through a resistor on the host board and asserts the signal. ModPrsL then indicates its present by setting ModPrsL to a “Low” state. 

Interrupt (IntL) is an output pin. “Low” indicates a possible operational fault or a status critical to the host system. The host identifies the source of the interrupt using the 2-wire serial interface. The IntL pin is an open collector output and must be pulled to the Host Vcc voltage on the Host board. 

## **Transceiver Block Diagram** 


**Figure 1. Transceiver Block Diagram** 

www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 3 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


## **Absolute Maximum Ratings** 

It has to be noted that the operation in excess of any individual absolute maximum ratings might cause permanent damage to this module. 

|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Storage Temperature|TS|-40|85|degC||
|OperatingCase Temperature|TOP|0|70|degC||
|Power Supply Voltage|VCC|-0.5|3.6|V||
|Relative Humidity (non-condensation)|RH|0|85|%||
|Damage Threshold, each Lane|THd|5.5||dBm||



## **Recommended Operating Conditions and Power Supply Requirements** 

|**Parameter**<br>Operating Case Temperature<br>Power Supply Voltage<br>Data Rate, each Lane<br>Control Input Voltage High<br>Control Input Voltage Low<br>Link Distance with G.652|**Symbol**|**Min**|**Typical**|**Max**|**Units**|
|---|---|---|---|---|---|
||TOP|0||70|degC|
||VCC|3.135|3.3|3.465|V|
||||25.78125||Gb/s|
|||2||Vcc|V|
|||0||0.8|V|
||D|0.002||10|km|



## **Electrical Characteristics** 

The following electrical characteristics are defined over the Recommended Operating Environment unless otherwise specified. 

|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Units**|**Notes**|
|---|---|---|---|---|---|---|
|Power Consumption||||4.0|W||
|Supply Current|Icc|||1.21|A||



www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 4 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


|Transceiver Power-on Initialization<br>Time||||2000|ms|1|
|---|---|---|---|---|---|---|
|**Transmitter (each Lane)**|||||||
|Single-ended<br>Input<br>Voltage<br>Tolerance (Note 2)||-0.3||4.0|V|Referred<br>to TP1<br>signal<br>common|
|AC Common Mode Input<br>Voltage Tolerance||15|||mV|RMS|
|Differential<br>Input<br>Voltage<br>Swing Threshold||50|||mVpp|LOSA<br>Threshold|
|Differential Input Voltage Swing|Vin,pp|190||700|mVpp||
|Differential Input Impedance|Zin|90|100|110|Ohm||
|**Receiver (each Lane)**|||||||
|Single-ended Output Voltage||-0.3||4.0|V|Referred to<br>signal<br>common|
|AC Common Mode Output<br>Voltage||||7.5|mV|RMS|
|Differential Output Voltage Swing|Vout,pp|300||850|mVpp||
|Differential Output Impedance|Zout|90|100|110|Ohm||



Notes: 

- 1.Power-on Initialization Time is the time from when the power supply voltages reach and remain above the 

minimum recommended operating supply voltages to the time when the module is fully functional. 

- 2.The single ended input voltage tolerance is the allowable range of the instantaneous input signals. 

www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 5 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


## **Optical Characteristics** 

||**QSFP28 100GBASE-LR4**|**QSFP28 100GBASE-LR4**|**QSFP28 100GBASE-LR4**|**QSFP28 100GBASE-LR4**|**QSFP28 100GBASE-LR4**|**QSFP28 100GBASE-LR4**|
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typical**|**Max**|**Unit**|**Notes**|
|Lane Wavelength|L0|1294.53|1295.56|1296.59|nm||
||L1|1299.02|1300.05|1301.09|nm||
||L2|1303.54|1304.58|1305.63|nm||
||L3|1308.09|1309.14|1310.19|nm||
||**Transmitter**||||||
|Side Mode Suppression Ratio|SMSR|30|||dB||
|Total Average Launch Power|PT|||10.5|dBm||
|Average Launch Power, each<br>Lane|PAVG|-4.3||4.5|dBm||
|OMA, each Lane|POMA|-1.3||4.5|dBm|1|
|Difference<br>in<br>Launch<br>Power<br>between anyTwo Lanes(OMA)|Ptx,diff|||5|dB||
|Launch<br>Power<br>in<br>OMA<br>minus<br>Transmitter<br>and<br>Dispersion||-2.3|||dBm||
|Penalty (TDP),each Lane|||||||
|TDP,each Lane|TDP|||2.2|dB||
|Extinction Ratio|ER|4|||dB||
|RIN20OMA|RIN|||-130|dB/Hz||
|Optical Return Loss Tolerance|TOL|||20|dB||
|Transmitter Reflectance|RT|||-12|dB||
|Eye Mask{X1, X2, X3, Y1, Y2, Y3}||{0.25, 0.4, 0.45, 0.25, 0.28, 0.4}||||2|
|Average<br>Launch<br>Power<br>OFF<br>Transmitter,each Lane|Poff|||-30|dBm||
||**Receiver**||||||
|Damage Threshold,each Lane|THd|5.5|||dBm|3|
|Total Average Receive Power||||10.5|dBm||
|Average Receive Power, each Lane||-10.6||4.5|dBm||



www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 6 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


|Receive<br>Power<br>(OMA), each<br>Lane||||4.5|dBm||
|---|---|---|---|---|---|---|
|Receiver Sensitivity (OMA), each Lane|SEN|||-8.6|dBm||
|Stressed<br>Receiver<br>Sensitivity<br>(OMA),each Lane||||-6.8|dBm|4|
|Receiver Reflectance|RR|||-26|dB||
|Difference<br>in<br>Receive Power<br>between anyTwo Lanes(OMA)|Prx,diff|||5.5|dB||
|LOS Assert|LOSA||-18||dBm||
|LOS Deassert|LOSD||-15||dBm||
|LOS Hysteresis|LOSH|0.5|||dB||
|Receiver Electrical 3 dB upper Cutoff<br>Frequency,each Lane|Fc|||31|GHz||
|**Conditions of Stress Receiver Sensitivity Test(Note 5)**|||||||
|Vertical Eye Closure Penalty, each<br>Lane|||1.8||dB||
|Stressed Eye J2 Jitter,each Lane|||0.3||UI||
|Stressed Eye J9 Jitter,each Lane|||0.47||UI||



Notes: 

- 1.Even if the TDP < 1 dB, the OMA min must exceed the minimum value specified here. 

## 2.See Figure 2 below. 

- 3.The receiver shall be able to tolerate, without damage, continuous exposure to a modulated optical input signal having this power level on one lane. The receiver does not have to operate correctly at this input power. 

4.Measured with conformance test signal at receiver input for BER = 1x10-12. 

5.Vertical eye closure penalty and stressed eye jitter are test conditions for measuring stressed receiver sensitivity. They are not characteristics of the receiver. 

www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 7 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 



**Figure 4. Eye Mask Definition** 

## **Digital Diagnostic Functions** 

The following digital diagnostic characteristics are defined over the normal operating conditions unless otherwise specified. 

|**Parameter**|**Symbol**|**Min**|**Max**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Temperature<br>monitor<br>absolute error|DMI_Temp|-3|+3|degC|Over<br>operating<br>temperature range|
|Supply voltage monitor<br>absolute error|DMI _VCC|-0.1|0.1|V|Over full operating<br>range|
|Channel<br>RX<br>power<br>monitor absolute error|DMI_RX_Ch|-2|2|dB|1|
|Channel<br>Bias<br>current<br>monitor|DMI_Ibias_Ch|-10%|10%|mA||
|Channel<br>TX<br>power<br>monitor absolute error|DMI_TX_Ch|-2|2|dB|1|



Notes: 

Due to measurement accuracy of different single mode fibers, there could be an additional +/-1 dB fluctuation, or a +/- 3 dB total accuracy. 

www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 8 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


## **QSFP28 Connector and Pinout Description** 

The electrical interface to the transceiver is a 38 pins edge connector. The 38 pins provide high speed data, low speed monitoring and control signals, I2C communication, power and ground connectivity. The top and bottom views of the connector are provided below, as well as a table outlining the contact numbering, symbol and full description. 


Figure 3. QSFP28-compliant 38-pin connector 

|**PIN**|**Logic**|**Symbol**|**Name/Description**|**Notes**|
|---|---|---|---|---|
|1||GND|Ground|1|
|2|CML-I|Tx2n|Transmitter Inverted Data Input||
|3|CML-I|Tx2p|Transmitter Non-Inverted Data output||
|4||GND|Ground|1|
|5|CML-I|Tx4n|Transmitter Inverted Data Input||
|6|CML-I|Tx4p|Transmitter Non-Inverted Data output||
|7||GND|Ground|1|
|8|LVTLL-I|ModSelL|Module Select||



www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 9 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


|9|LVTLL-I|ResetL|Module Reset||
|---|---|---|---|---|
|10||VccRx|+3.3V Power SupplyReceiver|2|
|11|LVCMOS-I/O|SCL|2-Wire Serial Interface Clock||
|12|LVCMOS-I/O|SDA|2-Wire Serial Interface Data||
|13||GND|Ground||
|14|CML-O|Rx3p|Receiver Non-Inverted Data Output||
|15|CML-O|Rx3n|Receiver Inverted Data Output||
|16||GND|Ground|1|
|17|CML-O|Rx1p|Receiver Non-Inverted Data Output||
|18|CML-O|Rx1n|Receiver Inverted Data Output||
|19||GND|Ground|1|
|20||GND|Ground|1|
|21|CML-O|Rx2n|Receiver Inverted Data Output||
|22|CML-O|Rx2p|Receiver Non-Inverted Data Output||
|23||GND|Ground|1|
|24|CML-O|Rx4n|Receiver Inverted Data Output|1|
|25|CML-O|Rx4p|Receiver Non-Inverted Data Output||
|26||GND|Ground|1|
|27|LVTTL-O|ModPrsL|Module Present||
|28|LVTTL-O|IntL|Interrupt||
|29||VccTx|+3.3 V Power Supplytransmitter|2|
|30||Vcc1|+3.3 V Power Supply|2|
|31|LVTTL-I|LPMode|Low Power Mode||
|32||GND|Ground|1|
|33|CML-I|Tx3p|Transmitter Non-Inverted Data Input||
|34|CML-I|Tx3n|Transmitter Inverted Data Output||
|35||GND|Ground|1|
|36|CML-I|Tx1p|Transmitter Non-Inverted Data Input||
|37|CML-I|Tx1n|Transmitter Inverted Data Output||
|38||GND|Ground|1|



## Notes: 

1. GND is the symbol for signal and supply (power) common for the QSFP28 module. All are common within the module 

www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 10 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host 

board signal common ground plane. 

- 2.VccRx, Vcc1 and VccTx are the receiving and transmission power suppliers and shall be applied concurrently. 

Recommended host board power supply filtering is shown in Figure 3 below. Vcc Rx, Vcc1 and Vcc Tx may be internally 

connected within the module in any combination. The connector pins are each rated for a maximum current of 

1000mA. 

## **Recommended Power Supply Filter** 


**Figure 4. Recommended Power Supply Filter** 

www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 11 of 12 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-LW100-LR4C Rev1.0- Sep.2020 


## **Mechanical Specifications** 

Unit: mm 


Figure 3. Mechanical Dimensions 

www.link-pp.com www.l-p.com 

Copyright © 2020 LINK-PP AlI Rights Reserved 

Page 12 of 12 

