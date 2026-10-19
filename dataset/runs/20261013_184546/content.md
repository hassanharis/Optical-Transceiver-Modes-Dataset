
**----- Start of picture text -----**<br>
40GBASE-LR4 QSFP+ 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **40GBASE-LR4 QSFP+ 1310nm 10km DDM SMF Transceiver** 

## **P/N: QT-QSFP+-LR4** 

## **PRODUCT FEATURES** 

- 4 CWDM lanes Mux/Demux design 

- Up to 11.1Gbps Data rate per wavelength 

- Up to 10km transmission on SMF 

- Electrically hot-pluggable 

- Digital Diagnostics Monitoring Interface 

- Compliant with QSFP+ MSA with LC connector 

- Case operating temperature range:0°C to 70°C 

- Power dissipation < 2.5 W 

- Compliant to IEEE 802.3ba 

- RoHS Compliant. 

## **APPLICATIONS** 

- 40G Ethernet 

- Data Center and LAN 

## **1. Absolute Maximum Ratings** 

|**Absolute Maximum Ratings**|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|Storage Temperature|Ts|-40|-|85|ºC||
|Relative Humidity|RH|5|-|95|%||
|Power SupplyVoltage|VCC|-0.3|-|4|V||
|Signal Input Voltage||Vcc-0.3|-|Vcc+0.3|V||




**----- Start of picture text -----**<br>
40GBASE-LR4 QSFP+ 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **2. Recommended Operating Conditions** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Tcase|0|-|70|ºC|Without air flow|
|Power SupplyVoltage|VCC|3.13|3.3|3.47|V||
|Power Supply Current|ICC|-||760|mA||
|Data Rate|BR||10.3125||Gbps|Each channel|
|Transmission Distance|TD||-|10|km||
|Coupled fiber|Single mode fiber|||||9/125um SMF|



## **3. Optical Characteristics** 

|**Optical Characteristics**|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|Transmitter|||||||
|Wavelength Assignment|λ0|1264.5|1271|1277.5|nm||
||λ1|1284.5|1291|1297.5|nm||
||λ2|1304.5|1311|1317.5|nm||
||λ3|1324.5|1331|1337.5|nm||
|Total Output. Power|POUT|||8.3|dBm||
|Average Launch Power Per lane||-7||2.3|dBm||
|Spectral Width(-20dB)|σ|||1|nm||
|SMSR||30|||dB||
|Optical Extinction Ratio|ER|3.5|||dB||
|Average launch Power offper lane|Poff|||-30|dBm||
|RIN|RIN|||-128|dB/Hz||
|Output Eye Mask|Compliant with IEEE 802.3ba||||||
|Receiver|||||||
|Rx Sensitivity per lane（OMA）|RSENS|||-13.7|dBm|1|
|Input Saturation Power(Overload)|Psat|2.3|||dBm||
|Receiver Reflectance|Rr|||-26|dB||



## **Notes:** 

1. Measured with a PRBS 2[31] -1 test pattern, @10.325Gb/s, BER<10[-12] 

## **4. Electrical Characteristics** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**NOTE**|
|---|---|---|---|---|---|---|
|SupplyVoltage|Vcc|3.13|3.3|3.47|V||
|SupplyCurrent|Icc|||760|mA||
|Transmitter|||||||
|Input differential impedance|Rin||100||Ω|1|
|Differential data input swing|Vin,pp|180||1000|mV||
|Transmit Disable Voltage|VD|Vcc–1.3||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V|2|
|Transmit Disable Assert Time||||10|us||




**----- Start of picture text -----**<br>
40GBASE-LR4 QSFP+ 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


|Receiver|||||||
|---|---|---|---|---|---|---|
|Differential data output swing|Vout,pp|300||850|mV|3|
|Data output rise time|tr|28|||ps|4|
|Data output fall time|tf|28|||ps|4|
|LOS Fault|VLOS fault|Vcc–1.3||VccHOST|V|5|
|LOS Normal|VLOS<br>norm|Vee||Vee+0.8|V|5|



## **Notes:** 

1. Connected directly to TX data input pins. AC coupled thereafter. 

2. Or open circuit. 

3. Into 100 ohms differential termination. 

4. 20 -80 %. 

5. Loss Of Signal is LVTTL. Logic 0 indicates normal operation; logic 1 indicates no signal detected. 

## **5. Pin Assignment** 


**Figure 1---Pin out of Connector Block on Host Board** 


**----- Start of picture text -----**<br>
40GBASE-LR4 QSFP+ 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


|**Pin**|**Symbol**|**Name/Description**|**NOTE**|
|---|---|---|---|
|1|GND|TransmitterGround<br>(Common with Receiver Ground)|1|
|2|Tx2n|Transmitter InvertedDataInput||
|3|Tx2p|Transmitter Non-Inverted Data output||
|4|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|5|Tx4n|Transmitter InvertedDataInput||
|6|Tx4p|Transmitter Non-InvertedData output||
|7|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|8|ModSelL|Module Select||
|9|ResetL|ModuleReset||
|10|VccRx|3.3V Power Supply Receiver|2|
|11|SCL|2-Wire serial Interface Clock||
|12|SDA|2-Wire serial InterfaceData||
|13|GND|TransmitterGround<br>(Common with Receiver Ground)||
|14|Rx3p|Receiver Non-InvertedData Output||
|15|Rx3n|Receiver InvertedData Output||
|16|GND|TransmitterGround<br>(Common with Receiver Ground)|1|
|17|Rx1p|Receiver Non-InvertedData Output||
|18|Rx1n|Receiver InvertedData Output||
|19|GND|TransmitterGround<br>(Common with ReceiverGround)|1|
|20|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|21|Rx2n|Receiver InvertedData Output||
|22|Rx2p|Receiver Non-InvertedData Output||
|23|GND|TransmitterGround<br>(Common with Receiver Ground)|1|
|24|Rx4n|Receiver InvertedData Output|1|
|25|Rx4p|Receiver Non-InvertedData Output||
|26|GND|Transmitter Ground<br>(Common with Receiver Ground)|1|
|27|ModPrsl|ModulePresent||
|28|IntL|Interrupt||
|29|VccTx|3.3V power supply transmitter|2|
|30|Vcc1|3.3V power supply|2|
|31|LPMode|Low Power Mode||
|32|GND|TransmitterGround<br>(Common with Receiver Ground)|1|
|33|Tx3p|Transmitter Non-Inverted Data Input||
|34|Tx3n|Transmitter InvertedData Output||
|35|GND|TransmitterGround<br>(Common with Receiver Ground)|1|
|36|Tx1p|Transmitter Non-Inverted Data Input||
|37|Tx1n|Transmitter Inverted Data Output||
|38|GND|TransmitterGround<br>(Common with Receiver Ground)|1|



## **Notes:** 

1. GND is the symbol for signal and supply (power) common for QSFP+ modules. All are common within the QSFP+ module and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host board signal common ground plane. 

2. VccRx, Vcc1 and VccTx are the receiving and transmission power suppliers and shall be applied concurrently. Recommended host board power supply filtering is shown below. Vcc Rx, Vcc1 and Vcc Txmay be internally connected within the QSFP+ transceiver module in any combination. The connector pins are each rated for a maximum current of 500mA. 


**----- Start of picture text -----**<br>
40GBASE-LR4 QSFP+ 1310nm 10km DDM SMF Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **6. Outline Dimensions** 


**----- Start of picture text -----**<br>
3.8<br>27.2 12.2 Units in mm<br>D R0<br>.3 R<br>0<br>.2 DETAIL A<br>SCALE 2:1<br>2<br>2-C0.35X45° 2.55<br>Label<br>29.6± 0.1<br>SEE DETAIL A<br>2<br>72<br>48.4<br>4.2 6.25± 0.05<br>16.7<br>3<br>5.2 1<br> 0.1<br>15.4 13.68 ±<br>16.4<br>0.6 2.25<br>3<br> 0.1<br>8.5±<br>2.15 5.85<br>1.4<br>1<br>**----- End of picture text -----**<br>


## **7. Ordering information** 

|**Part Number**|**Product Description**|
|---|---|
|QT-QSFP+-LR4|QSFP+,40Gb/s,1271~1331nm,SMF,10KM,DDM,LC connector,0°C to 70°C|
|QT-QSFP+-SR4|QSFP+,40Gb/s,850nm,MMF,300m,DDM,MPO,0°C to 70°C|
|QT-QSFP+-LH4|QSFP+,40Gb/s,1271~1331nm,SMF,20KM,DDM,LC connector,0°C to 70°C|
|QT-QSFP+-ER4|QSFP+,40Gb/s,1271~1331nm,SMF,40KM,DDM,LC connector,0°C to 70°C|



