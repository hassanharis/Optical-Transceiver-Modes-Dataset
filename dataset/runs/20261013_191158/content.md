
**----- Start of picture text -----**<br>
SFP+ 10GBASE-BX 1330nm-TX/1270nm-RX 40km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **SFP+ 10GBASE-BX 1330nm-TX/1270nm-RX 40km Transceiver** 

## **P/N: BIDI-SFP+-ER-33** 

## **PRODUCT FEATURES** 

- Supports 9.95 to 11.3Gb/s bit rates 

- Simplex LC Connector 

- Hot pluggable SFP+ footprint 

- Uncooled 1330nm DFB transmitter, 1270nm PIN photo-detector 

- Uncooled 1270nm DFB transmitter, 1330nm PIN photo-detector 

- Applicable for 40km SMF connection 

- Low power consumption, < 1.2W 

- Digital Diagnostic Monitor Interface 

- Optical interface compliant to IEEE 802.3ae 10GBASE-ER 

- Electrical interface compliant to SFF-8431 

- Operating case temperature: Commerical:0 to 70 °C 

- Industrial: -40 to 85 °C 

## **APPLICATIONS** 

- 10GBASE-ER at 10.3125Gbps 

- 10GBASE-EW at 9.953Gbps 

- Other optical link 

sales@qsfptek.com 

1/5 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GBASE-BX 1330nm-TX/1270nm-RX 40km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


## **1. Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|
|SupplyVoltage|Vcc|-0.5|4.0|V||
|Storage Temperature|TS|-40|85|°C||
|Relative Humidity|RH|0|85|%||



**Note:** Stress in excess of the maximum absolute ratings can cause permanent damage to the transceiver. 

## **2. General Operating Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Data Rate|DR|9.95||10.3125|Gb/s||
|SupplyVoltage|Vcc|3.13|3.3|3.47|V||
|SupplyCurrent|Icc5|||330|mA||
|Operating Case Temp.|Tc|0||70|°C||
||TI|-40||85|||



## **3. Electrical Characteristics** 

|**. Electrical Characteristics**|||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Typ**|**Max.**|**Unit**|**Note**|
|Transmitter|||||||
|Differential data input swing|VIN,PP|180||700|mVpp|1|
|Transmit Disable Voltage|VD|VCC-0.8||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+0.8|||
|Input differential impedance|Rin||100||Ω||
|Receiver|||||||
|Differential data output swing|Vout,pp|300||850|mVpp|2|
|Output rise time and fall time|Tr,Tf|28|||Ps|3|
|LOS asserted|VLOS_F|VCC-0.8||Vcc|V|4|
|LOS de-asserted|VLOS_N|Vee||Vee+0.8|V|4|



## **Notes:** 

1. Connected directly to TX data input pins. AC coupling from pins into laser driver IC. 

2. Into 100Ωdifferential termination. 

3. 20–80%. Measured with Module Compliance Test Board and OMA test pattern. Use of four 1’s and four 0’s sequence in the PRBS 9 is an acceptable alternative. 

4. LOS is an open collector output. Should be pulled up with 4.7kΩ– 10kΩon the host board. Normal operation is logic 0; loss of signal is logic 1. 

## **4. Optical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|||**Transmitter**|||||
|Operating Wavelength|λ|1320|1330|1340|nm||
|||1260|1270|1280|||
|Ave. output power<br>(Enabled)|PAVE|1||5|dBm|1|



sales@qsfptek.com 

2/5 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GBASE-BX 1330nm-TX/1270nm-RX 40km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


|Side-Mode Suppression<br>Ratio|SMSR|30|||dB||
|---|---|---|---|---|---|---|
|Extinction Ratio|ER|5|||dB||
|RMS spectral width|Δλ|||1|nm||
|Rise/Fall time<br>(20%~80%)|Tr/Tf|||50|ps||
|Dispersionpenalty|TDP|||3.2|dB||
|Relative IntensityNoise|RIN|||-128|dB/Hz||
|Output Optical Eye||Compliant with IEEE 0802.3ae|||||
|||**Receiver**|||||
|Operating Wavelength|λ|1260|1270|1280|nm||
|||1320|1330|1340|||
|Receiver Sensitivity|PSEN2|||-15|dBm|2|
|Average Receive Power|PAVE|||0.5|dBm||
|Receiver Reflectance|Rrx|||-12|dB||
|LOS Assert|Pa|-30|||dBm||
|LOS De-assert|Pd|||-17|dBm||
|LOS Hysteresis|Pd-Pa|0.5|||dB||



## **Notes:** 

1. Average power figures are informative only, per IEEE 802.3ae. 

2. Measured with worst ER=6; BER<10[-12] ; 2[31 – 1 ] PRBS. 

## **5. Pin Definition and Functions** 



|**Pin**|**Symbol**|**Name/Description**|
|---|---|---|
|1|VEET[1]|Transmitter Ground|
|2|Tx_FAULT[2]|Transmitter Fault|
|3|Tx_DIS[3]|Transmitter Disable. Laser output disabled on high or open|
|4|SDA[2]|2-wire Serial Interface Data Line|
|5|SCL[2]|2-wire Serial Interface Clock Line|



sales@qsfptek.com 

3/5 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GBASE-BX 1330nm-TX/1270nm-RX 40km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>


|6|MOD_ABS[4]|Module Absent. Grounded within the module|
|---|---|---|
|7|RS0|Rate Select 0|
|8|RX_LOS[2]|Loss of Signal indication. Logic 0 indicates normal operation|
|9|RS1[5]|Rate Select 1|
|10|VEER[1]|Receiver Ground|
|11|VEER[1]|Receiver Ground|
|12|RD-|Receiver Inverted DATA out. AC Coupled|
|13|RD+|Receiver DATA out. AC Coupled|
|14|VEER[1]|Receiver Ground|
|15|VCCR|Receiver Power Supply|
|16|VCCT|Transmitter Power Supply|
|17|VEET[1]|Transmitter Ground|
|18|TD+|Transmitter DATA in. AC Coupled|
|19|TD-|Transmitter Inverted DATA in. AC Coupled|
|20|VEET[1]|Transmitter Ground|



## **Notes:** 

1. Module circuit ground is isolated from module chassis ground within the module. 

2. should be pulled up with 4.7k – 10k ohms on host board toa voltage between 3.15Vand 3.6V. 

3. Tx_Disable is an input contact with a 4.7 kΩ to 10 kΩ pullup to VccT inside the module. 

4. Mod_ABS is connected to VeeT or VeeR in the SFP+ module. The host may pull this contact up to Vcc_Host with a resistor in the range 4.7 kΩ to10 kΩ.Mod_ABS is asserted “High” when the SFP+ module is physically absent from a host slot. 

## **6. Recommended power supply filter** 


## **Note:** 

Inductors with DC resistance of less than 1Ω should be used in order to maintain the required voltage at the SFP input pin with 3.3V supply voltage. When the recommended supply filtering network is used, hot plugging of the SFP transceiver module will result in an inrush current of no more than 30 mA greater than the steady state value 

sales@qsfptek.com 

4/5 

Rev1.0 


**----- Start of picture text -----**<br>
SFP+ 10GBASE-BX 1330nm-TX/1270nm-RX 40km Transceiver www.qsfptek.com<br>**----- End of picture text -----**<br>



## **Package Dimensions** 

## **7. Ordering Information** 

|**Part Number**|**Description**|
|---|---|
|BIDI-SFP+-ER-33|BIDI SFP+,10 Gb/s, 1330nm,SMF, 40KM ,DDM,LC connector, 0℃~ +70℃|
|BIDI-SFP+-ER-27|BIDI SFP+,10 Gb/s, 1270nm,SMF, 40KM ,DDM,LC connector, 0℃~ +70℃|



sales@qsfptek.com 

5/5 

Rev1.0 

