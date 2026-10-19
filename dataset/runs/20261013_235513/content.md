LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW100-FR4C Rev1.0- Sep.2016 


## **LQ-CW100-FR4C** 100G QSFP28 CWDM4 2KM Transceiver 

## **Features** 

- 4 CWDM lanes Mux/Demux design 

- CWDM TOSA integrated Driver 

- Build in CDR on both TX and RX 

- Up to 25.78Gbps Data rate per wavelength 

- Up to 2km transmission on SMF 

- Electrically hot-pluggable 

- Digital Diagnostics Monitoring Interface 

- Compliant with QSFP28 MSA with LC connector 

- Case operating temperature range:0°C to 70°C 

- Power dissipation < 3.5 W 

## **Applications** 

- Data Center interconnections 

- 100GBASE Ethernet links 

## **Standard** 

- Compliant to IEEE 802.3ba and 100G CLR4 

- Compliant to SFF-8436 

- RoHS Compliant. 

www.link-pp.com www.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 1 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW100-FR4C Rev1.0- Sep.2016 


## **General Description** 

100G QSFP28 CWDM4 is designed to operate over single-mode fiber system using 4X25 CWDM channel in 1310 band and links up to 2km. The module converts 4 inputs channel of 25Gb/s electrical data to 4 CWDM optical signals, and multiplexes them into a single channel for 100Gb/s optical transmission. Reversely, on the receiver side, the module optically de-multiplexes a 100Gb/s input into 4 CWDM channels signals, and converts them to 4 channel output electrical data. 

The central wavelengths of the 4 CWDM channels are 1271, 1291, 1311 and 1331 nm. It contains a duplex LC connector for the optical interface and a 38-pin connector for the electrical interface. Single-mode fiber (SMF) is applied in this module. This product converts the 4-channel 25Gb/s electrical input data into CWDM optical signals (light), by a 4-wavelength Distributed Feedback Laser (DFB) array. The 4 wavelengths are multiplexed into a single 100Gb/s data, propagating out of the transmitter module via the SMF. The receiver module accepts the 100Gb/s optical signals input, and de-multiplexes it into 4 CWDM 25Gb/s channels. Each wavelength light is collected by a discrete photo diode, and then outputted as electric data after amplified by a TIA. 

The product is designed with form factor, optical/electrical connection and digital diagnostic interface according to the QSFP28 Multi-Source Agreement (MSA) and compliant to IEEE 802.3ba. 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature|Ts|-40|-|85|ºC||
|Relative Humidity|RH|5|-|95|%||
|Power Supply Voltage|VCC|-0.3|-|4|V||
|Signal Input Voltage||Vcc-0.3|-|Vcc+0.3|V||



## **Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Tcase|0|-|70|ºC|Without air<br>flow|
|Power Supply Voltage|VCC|3.13|3.3|3.47|V||
|Power Supply Current|ICC|-||900|mA||
|Data Rate|BR||25.78125||Gbps|Each<br>channel|
|Transmission Distance|TD||-|2|km||
|Coupled fiber|Single mode fiber|||9/125um SMF|||



www.link-pp.com www.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 2 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW100-FR4C Rev1.0- Sep.2016 


## **Electrical Specifications** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.13|3.3|3.47|V||
|Supply Current|Icc|||900|mA||
|**Transmitter**|||||||
|Input differential impedance|Rin||100||Ω|1|
|Differential data input swing|Vin,pp|180||1000|mV||
|Transmit Disable Voltage|VD|Vcc–1.3||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V|2|
|**Receiver**|||||||
|Differential data output swing|Vout,pp|300||850|mV|3|
|Data output rise time|tr|28|||ps|4|
|Data output fall time|tf|28|||ps|4|
|LOS Fault|VLOS fault|Vcc–1.3||VccHOST|V|5|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|5|
|Power Supply Rejection|PSR|100|||mVpp|6|



## **Notes:** 

- 1) Connected directly to TX data input pins. AC coupled thereafter. 

- 2) Or open circuit. 

- 3) Into 100 ohms differential termination. 

- 4) 20 – 80 %. 

- 5) Loss Of Signal is LVTTL. Logic 0 indicates normal operation; logic 1 indicates no signal detected. Receiver sensitivity is compliant with power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specified value applied through the recommended power supply filtering network. 

www.link-pp.com www.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 3 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW100-FR4C Rev1.0- Sep.2016 


## **Optical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Transmitter|||||||
|Wavelength Assignment|λ0|1264.5|1271|1277.5|nm||
||λ1|1284.5|1291|1297.5|nm||
||λ2|1304.5|1311|1317.5|nm||
||λ3|1324.5|1331|1337.5|nm||
|Total Output. Power|POUT|||8.5|dBm||
|Average Launch Power Per lane||-6.5||2.5|dBm||
|Spectral Width (-20dB)|σ|||1|nm||
|SMSR||30|||dB||
|Optical Extinction Ratio|ER|3.5|||dB||
|Average launch Power off per lane|Poff|||-30|dBm||
|Transmitter and Dispersion Penalty per lane|TDP|||3.3|dB||
|RIN|RIN|||-128|dB/Hz||
|Output Eye Mask definition<br>{X1，X2，X3，Y1，Y2，Y3}|{0.25，0.42，0.46，0.28，0.3，0.4}||||||
|Receiver|||||||
|Rx Sensitivity per lane|RSENS|||-10|dBm|1|
|Input Saturation Power (Overload)|Psat|||2.5|dBm||
|Receiver Reflectance|Rr|||-26|dB||



## **Notes:** 

31 -12 Measured with a PRBS 2 -1 test pattern, @25.78Gb/s, BER<10 . 

www.link-pp.com www.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 4 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW100-FR4C Rev1.0- Sep.2016 


## **QSFP28 Edge Connector and Pin out Description** 

The electrical interface to the transceiver is a 38 pins edge connector. The 38 pins provide high speed data, low speed monitoring and control signals, I2C communication, power and ground connectivity. The top and bottom views of the connector are provided below, as well as a table outlining the contact numbering, symbol and full description. 


Figure 1. QSFP28 compliant 38-pin connector 

|**Pin**|**Symbol**|**Name/Description**|**Note**|
|---|---|---|---|
|1|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|2|Tx2n|Transmitter Inverted Data Input||
|3|Tx2p|Transmitter Non-Inverted Data output||
|4|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|5|Tx4n|Transmitter Inverted Data Input||
|6|Tx4p|Transmitter Non-Inverted Data output||
|7|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|8|ModSelL|Module Select||
|9|ResetL|Module Reset||
|10|VccRx|3.3V Power SupplyReceiver|2|
|11|SCL|2-Wire serial Interface Clock||
|12|SDA|2-Wire serial Interface Data||
|13|GND|Transmitter Ground<br>(Common with Receiver Ground)||
|14|Rx3p|Receiver Non-Inverted Data Output||
|15|Rx3n|Receiver Inverted Data Output||
|16|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|17|Rx1p|Receiver Non-Inverted Data Output||
|18|Rx1n|Receiver Inverted Data Output||
|19|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|20|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|21|Rx2n|Receiver Inverted Data Output||



www.link-pp.com www.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 5 of 8 


LINK-PP INT’L TECHNOLOGY CO., LIMITED LQ-CW100-FR4C Rev1.0- Sep.2016 

|22|Rx2p|Receiver Non-Inverted Data Output||
|---|---|---|---|
|23|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|24|Rx4n|Receiver Inverted Data Output|1|
|25|Rx4p|Receiver Non-Inverted Data Output||
|26|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|27|ModPrsl|Module Present||
|28|IntL|Interrupt||
|29|VccTx|3.3Vpower supplytransmitter|2|
|30|Vcc1|3.3Vpower supply|2|
|31|LPMode|Low Power Mode||
|32|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|33|Tx3p|Transmitter Non-Inverted Data Input||
|34|Tx3n|Transmitter Inverted Data Output||
|35|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|36|Tx1p|Transmitter Non-Inverted Data Input||
|37|Tx1n|Transmitter Inverted Data Output||
|38|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|



## Notes: 

1)GND is the symbol for signal and supply (power) common for QSFP28 modules. All are common within the QSFP28 module and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host board signal common ground plane. 

2)VccRx, Vcc1 and VccTx are the receiving and transmission power suppliers and shall be applied concurrently. Recommended host board power supply filtering is shown below. Vcc Rx, Vcc1 and Vcc Tx may be internally connected within the QSFP28 transceiver module in any combination. The connector pins are each rated for a maximum current of 500mA. 

www.link-pp.com www.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 6 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW100-FR4C Rev1.0- Sep.2016 


## **Host - Transceiver Interface Block Diagram** 


www.link-pp.com www.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 7 of 8 

LINK-PP INT’L TECHNOLOGY CO., LIMITED 

LQ-CW100-FR4C Rev1.0- Sep.2016 


**Mechanical Drawings** Unit:mm 


Figure 3. Mechanical Dimensions 

www.link-pp.com www.l-p.com 

Copyright © 2016 LINK-PP AlI Rights Reserved 

Page 8 of 8 

