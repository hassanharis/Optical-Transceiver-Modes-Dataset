**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


## **Features** 

-  Compliant with 40G Ethernet IEEE802.3ba and 40GBASE-ER4 Standard 


-  QSFP+ MSA compliant 

-  Compliant with QDR/DDR Infiniband data rates 

-  Up to 11.2Gb/s data rate per wavelength 

-  4 CWDM lanes MUX/DEMUX design 

-  Up to 40km transmission on single mode fiber (SMF) 

-  18.5dB link insertion loss budget 

-  Operating case temperature: 0 to 70oC 

-  Maximum power consumption 3.5W 

-  LC duplex connector 

-  RoHS compliant 

## **Applications** 

-  40GBASE-ER4 Ethernet Links 

-  Infiniband QDR and DDR interconnects 

-  Client-side 40G Telecom connections 

## **Absolute Maximum Ratings** 

|**_Parameter_**|**_Symbol_**|**_Min_**|**_Max_**|**_Unit_**|
|---|---|---|---|---|
|Storage Temperature|Ts|-40|85|°C|
|Operating Case Temperature|TOP|0|70|°C|
|Power Supply Voltage|Vcc|-0.5|3.6|V|
|Relative Humidity (non-condensation)|RH|0|85|%|
|Damage Threshold, each Lane|THd|3.8||dBm|



## **Recommended Operating Conditions** 

|**_Parameter_**|**_Symbol_**|**_Min_**|**_Typical_**|**_Max_**|**_Unit_**|
|---|---|---|---|---|---|
|Operating Case Temperature|TOP|0||+70|°C|
|Power Supply Voltage|Vcc|3.135|3.3|3.465|V|
|Data Rate, each Lane|||10.3125|11.2|Gb/s|
|Control Input Voltage High||2||Vcc|V|
|Control Input Voltage Low||0||0.8|V|
|Link Distance with G.652|D|||40|km|



## **Optech Technology Co., Ltd.** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

Version: 18V.A _**Page 1 of**_ **12** 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


## **Electrical Characteristics** 

|**_Parameter_**|**_Symbol_**|**_Min_**|**_Typical_**|**_Max_**|**_Unit_**|**_Notes_**|
|---|---|---|---|---|---|---|
|Power Consumption||||3.5|W||
|Supply Current|Icc|||1.1|A||
|Transceiver Power-on Initialization Time||||2000|ms|1|



Notes: 

1. Power-on Initialization Time is the time from when the power supply voltages reach and remain above the minimum recommended operating supply voltages to the time when the module is fully functional. 

## **Optical Characteristics** 

||**_Parameter_**|**_Symbol_**|**_Min_**|**_Typical_**|**_Max_**|**_Unit_**|**_Notes_**|
|---|---|---|---|---|---|---|---|
|||L0|1264.5|1271|1277.5|nm||
|||L1|1284.5|1291|1297.5|nm||
|Wavelength|Assignment|L2|1304.5|1311|1317.5|nm||
|||L3|1324.5|1331|1337.5|nm||



## **Digital Diagnostic Functions** 

|**_Parameter_**|**_Symbol_**|**_Min_**|**_Max_**|**_Unit_**|**_Notes_**|
|---|---|---|---|---|---|
|Temperature monitor absolute error|DMI_Temp|-3|+3|℃|Over operating<br>temperature range|
|Supply voltage monitor absolute error|DMI_VCC|-0.1|0.1|V|Over full operating range|
|Channel RX power monitor absolute error|DMI_RX_Ch|-2|2|dB|1|
|Channel Bias current monitor|DMI_IBias_Ch|-10%|10%|mA||
|Channel TX power monitor absolute error|DMI_TX_Ch|-2|2|dB|1|



Notes: 

1. Due to measurement accuracy of different single mode fibers, there could be an additional +/-1 dB fluctuation, or a +/- 3 dB total accuracy. 

**Optech Technology Co., Ltd.** 

Version: 18V.A _**Page 2 of**_ **12** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


## **Transmitter Electro-optical Characteristics (each Lane)** 

##   _**Vcc = 3.135 V to 3.465 V, TC = 0 C to 70 C**_ 

|**_Parameter_**|**_Symbol_**|**_Min_**|**_Typical_**|**_Max_**|**_Unit_**|**_Notes_**|
|---|---|---|---|---|---|---|
|||||||Referred to|
|Single-ended Input Voltage Tolerance (Note 1)||-0.3||4.0|V|TP1 signal|
|||||||common|
|AC Common Mode Input Voltage Tolerance||15|||mV|RMS|
|||||||LOSA|
|Differential Input Voltage Swing Threshold||50|||mVpp|Threshold|
|Differential Input Voltage Swing|Vin,pp|190||700|mVpp||
|Differential Input Impedance|Zin|90|100|110|Ohm||
|||||||10MHz-|
|Differential Input Return Loss||See IEEE 802.3ba||86A.4.11|dB|11.1GHz|
|J2 Jitter Tolerance|Jt2|0.17|||UI||
|J9 Jitter Tolerance|Jt9|0.29|||UI||
|Data Dependent Pulse Width Shrinkage||0.07|||UI||
|(DDPWS)Tolerance|||||||
|Eye Mask Coordinates<br>{X1, X2<br>Y1, Y2}||0.11, 0.31<br>95, 350|||UI<br>mV|Hit Ratio =<br>5x10-5|
|Side Mode Suppression Ratio|SMSR|30|||dB||
|Total Average Launch Power|PT|||10.5|dBm||
|Average Launch Power, each Lane|PAVG|-2.7||4.5|dBm||
|Optical Modulation Amplitude<br>(OMA), each Lane|POMA|0.3||5.0|dBm|2|
|Difference in Launch Power between any Two<br>Lanes(OMA)|<br>Ptx,diff|||4.7|dB||
|Launch Power in OMA minus Transmitter and<br>Dispersion Penalty (TDP), each Lane||-0.5|||dBm||
|TDP, each Lane|TDP|||2.6|dB||
|Extinction Ratio|ER|5.5|||dB||
|Relative Intensity Noise|RIN|||-128|dB/Hz|12dB<br>reflection|
|Optical Return Loss Tolerance|TOL|||20|dB||
|Transmitter Reflectance|RT|||-12|dB||
|Transmitter Eye Mask Definition<br>{X1, X2, X3, Y1, Y2, Y3}||{0.25,0.4,0.45,0.25,0.28,0.4}|||||



**Optech Technology Co., Ltd.** 

Version: 18V.A _**Page 3 of**_ **12** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 


## **40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 

|**_Parameter_**|**_Symbol_**|**_Min_**|**_Typical_**|**_Max_**|**_Unit_**|**_Notes_**|
|---|---|---|---|---|---|---|
|Average Launch Power OFF Transmitter,|Poff|||-30|dBm||
|each Lane|||||||



Notes: 

1. The single ended input voltage tolerance is the allowable range of the instantaneous input signals. 

2. Even if the TDP < 0.8 dB, the OMA min must exceed the minimum value specified here. 

**Optech Technology Co., Ltd.** 

Version: 18V.A _**Page 4 of**_ **12** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


## **Receiver Electro-optical Characteristics (each Lane)** 

|**_Vcc= 3.135 V to 3.465 V, TC = 0_**<br>|**_C to 70_**<br>|**_C_**||||||||
|---|---|---|---|---|---|---|---|---|---|
|**_Parameter_**|||**_Symbol_**|**_Min_**|**_Typical_**|<br>**_Max_**|**_Unit_**|**_Notes_**||
|||||||||Referred to||
|Single-ended Output Voltage||||-0.3||4.0|V|signal||
|||||||||common||
|AC Common Mode Output Voltage||||||7.5|mV|RMS||
|Differential Output Voltage Swing|||Vout,pp|300||850|mVpp|||
|Differential Output Impedance|||Zout|90|100|110|Ohm|||
|Termination Mismatch at 1MHz||||||5|%|||
|||||||||10MHz-||
|Differential Output Return Loss||||See IEEE|802.3ba|86A.4.2.1|dB|11.1GHz||
|||||||||10MHz-||
|Common Mode Output Return Loss||||See IEEE|802.3ba|86A.4.2.2|dB|11.1GHz||
|Output Transition Time||||28|||ps|20% to 80%||
|J2 Jitter Output|||Jo2|||0.42|UI|||
|J9 Jitter Output|||Jo9|||0.65|UI|||
|Eye Mask Coordinates<br>{X1, X2<br>Y1, Y2}|||||0.29, 0.5<br>150, 425|<br>|UI<br>mV|Hit Ratio =<br>5x10-5||
|Damage Threshold, each Lane|||THd|3.8|||dBm|2||
|Average Receive Power, each Lane||||-21.2||-4.5|dBm|||
|Receiver Reflectance|||RR|||-26|dB|||
|Receive Power (OMA), each Lane||||||-4|dBm|||
|Receiver Sensitivity (OMA), each|Lane||SEN|||-19|dBm|||
|Stressed Receiver Sensitivity||||||-16.8|dBm|2||
|(OMA), each Lane||||||||||
|Difference in Receive Power||||||||||
|between anyTwo Lanes(OMA)|||Prx,diff|||7|dB|||
|LOS Assert|||LOSA|-35|||dBm|||
|LOS Deassert|||LOSD|||-20|dBm|||
|LOS Hysteresis|||LOSH|0.5|||dB|||
|Receiver Electrical 3 dB upper|||Fc|||12.3|GHz|||
|Cutoff Frequency, each Lane||||||||||
|||||||||||



**Optech Technology Co., Ltd.** 

Version: 18V.A _**Page 5 of**_ **12** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


|**_Parameter_**|**_Symbol_**|**_Min_**|**_Typical_**|**_Max_**|**_Unit_**|**_Notes_**|
|---|---|---|---|---|---|---|
|**Conditions of**|**Stress Receiver Sensitivity Test (Note 3)**||||||
|Vertical Eye Closure Penalty, each Lane|||2.2||dB||
|Stressed Eye J2 Jitter, each Lane|||0.3||UI||
|Stressed Eye J9 Jitter, each Lane|||0.47||UI||



## Notes: 

1. The receiver shall be able to tolerate, without damage, continuous exposure to a modulated optical input signal having this power level on one lane. The receiver does not have to operate correctly at this input power. 

2. Measured with conformance test signal at receiver input for BER = 1x10[-12] . 

3. Vertical eye closure penalty and stressed eye jitter are test conditions for measuring stressed receiver sensitivity. They are not characteristics of the receiver. 

**Optech Technology Co., Ltd.** 

Version: 18V.A _**Page 6 of**_ **12** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


**Block Diagram of Transceiver** 


## **Figure 1. Transceiver Block Diagram** 

This product converts the 4-channel 10Gb/s electrical input data into CWDM optical signals (light), by a driven 4- wavelength Distributed Feedback Laser (DFB) array. The light is combined by the MUX parts as a 40Gb/s data, propagating out of the transmitter module from the SMF. The receiver module accepts the 40Gb/s CWDM optical signals input, and de-multiplexes it into 4 individual 10Gb/s channels with different wavelength. Each wavelength light is collected by a discrete avalanche photodiode (APD), and then outputted as electric data after amplified first by a TIA and then by a post amplifier. Figure 1 shows the functional block diagram of this product. 

A single +3.3V power supply is required to power up this product. Both power supply pins VccTx and VccRx are internally connected and should be applied concurrently. As per MSA specifications the module offers 7 low speed hardware control pins (including the 2-wire serial interface): ModSelL, SCL, SDA, ResetL, LPMode, ModPrsL and IntL. 

Module Select (ModSelL) is an input pin. When held low by the host, this product responds to 2-wire serial communication commands. The ModSelL allows the use of this product on a single 2-wire interface bus – individual ModSelL lines must be used. 

Serial Clock (SCL) and Serial Data (SDA) are required for the 2-wire serial bus communication interface and enable the host to access the QSFP+ memory map. 

The ResetL pin enables a complete reset, returning the settings to their default state, when a low level on the ResetL pin is held for longer than the minimum pulse length. During the execution of a reset the host shall disregard all status bits until it indicates a completion of the reset interrupt. The product indicates this by posting an IntL (Interrupt) signal with the Data_Not_Ready bit negated in the memory map. Note that on power up (including hot insertion) the module should post this completion of reset interrupt without requiring a reset. 

Low Power Mode (LPMode) pin is used to set the maximum power consumption for the product in order to protect hosts that are not capable of cooling higher power modules, should such modules be accidentally inserted. 

Module Present (ModPrsL) is a signal local to the host board which, in the absence of a product, is normally pulled up to the host Vcc. When the product is inserted into the connector, it completes the path to ground though a resistor on the host board and asserts the signal. ModPrsL then indicates its present by setting ModPrsL to a “Low” state. 

Interrupt (IntL) is an output pin. “Low” indicates a possible operational fault or a status critical to the host system. The host identifies the source of the interrupt using the 2-wire serial interface. The IntL pin is an open collector output and must be pulled to the Host Vcc voltage on the Host board. 

## **Optech Technology Co., Ltd.** 

Version: 18V.A _**Page 7 of**_ **12** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


## **Pin Assignment** 


**Figure 2.  MSA compliant Connector** 

|**PIN**|**Logic**|**Symbol**|**Name/Description**|**Note**|
|---|---|---|---|---|
|1||GND|Ground|1|
|2|CML-I|Tx2n|Transmitter Inverted Data Input||
|3|CML-I|Tx2p|Transmitter Non-Inverted Data output||
|4||GND|Ground|1|
|5|CML-I|Tx4n|Transmitter inverted Data Input||
|6|CML-I|Tx4p|Transmitter Non-Inverted Data output||
|7||GND|Ground|1|
|8|LVTLL-I|ModSeIL|Module Select||
|9|LVTLL-I|ResetL|Module Reset||
|10||VccRx|+3.3V Power SupplyReceiver|2|
|11|LVCMOS-I/O|SCL|2-Wire Serial Interface Clock||
|12|LVCMOS-I/O|SDA|2-Wire Serial Interface Data||
|13||GNC|Ground||
|14|CML-O|Rx3p|Receiver Non-Inverted Data output||
|15|CML-O|Rx3n|Receiver Inverted Data output||
|16||GND|Ground|1|
|17|CML-O|Rx1p|Receiver Non-Inverted Data Output||
|18|CML-O|Rx1n|Receiver Inverted Data Output||
|19||GND|Ground|1|
|20||GND|Ground|1|
|21|CML-O|Rx2n|Receiver Inverted Data output||
|22|CML-O|Rx2p|Receiver Non-Inverted Data output||
|23||GND|Ground|1|



## **Optech Technology Co., Ltd.** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

Version: 18V.A _**Page 8 of**_ **12** 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


|24|CML-O|Rx4n|Receiver Inverted Data output|1|
|---|---|---|---|---|
|25|CML-O|Rx4p|Receiver Non-Inverted Data output||
|26||GND|Ground|1|
|27|LVTTL-O|ModPrsL|Module Present||
|28|LVTTL-O|IntL|Interrupt||
|29||VccTx|+3.3V Power Supplytransmitter|2|
|30||Vcc1|+3.3V Power Supply|2|
|31|LVTTL-I|LPMode|Low Power Mode||
|32||GND|Ground|1|
|33|CML-I|Tx3p|Transmitter Non-Inverted Data Input||
|34|CML-I|Tx3n|Transmitter Inverted Data Output||
|35||GND|Ground|1|
|36|CML-I|Tx1p|Transmitter Non-Inverted Data Input||
|37|CML-I|Tx1n|Transmitter Inverted Data Output||
|38||GND|Ground|1|
||||||



Notes: 

1. GND is the symbol for signal and supply (power) common for QSFP+ modules. All are common within the QSFP+ module and all module voltages are referenced to this potential unless otherwise noted. Connect these directly to the host board signal common ground plane. 

2. VccRx, Vcc1 and VccTx are the receiving and transmission power suppliers and shall be applied concurrently. Vcc Rx, Vcc1 and Vcc Tx may be internally connected within the QSFP+ transceiver module in any combination. The connector pins are each rated for a maximum current of 500mA. 

**Optech Technology Co., Ltd.** 

Version: 18V.A _**Page 9 of**_ **12** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


**Dimensions** 


**Optech Technology Co., Ltd.** 

Version: 18V.A _**Page 10 of**_ **12** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


## **Optical Receptacle Cleaning Recommendations:** 

All fiber stubs inside the receptacle portions were cleaned before shipment.  In the event of contamination of the optical ports, the recommended cleaning process is the use of forced nitrogen.  If contamination is thought to have remained, the optical ports can be cleaned using a NTT international Cletop®  stick type and HFE7100 cleaning fluid.  Before the mating of patch-cord, the fiber end should be cleaned up by using Cletop®  cleaning cassette. 


**Optech Technology Co., Ltd.** 2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

Version: 18V.A _**Page 11 of**_ **12** 

**40Gbps QSFP ER4 Optical Transceiver Module OPCS-S40-13-CB datasheet** 


## **Ordering Information** 

## **OP     CA S -     S 40 - 13 - C B** 

**Product Code: Data Rate: Type:** S=Single- **Reach: Wavelength: Operating Temperature: For Optech Internal Ref.** 5=GBIC; A=155Mb/s; mode; M=MultiNormal: Normal: C=Commercial Purpose 6=SFP-LC; B=622Mb/s; mode; W=BWDM; X1=Under 150m; 85=850nm; (0~70 ℃ ); 7=XFP; C=1.25Gb/s; B=DUAL-BWDM; X2=220m; 13=1310nm; I= Industrial Purpose C=CWDM; 15=1550nm; 8=XENPAK; D=2.125Gb/s; X3=300m; (Extended Range) D=DWDM; 00=Copper T (RJ-45) 9=X2; E=2.5Gb/s; X5=550m; T=Copper-T (RJ-45) A=SFP+ (SFP28); F=4.25Gb/s; 02=2km, CWDM: E=GEPON ONU; 27=1270nm; C=QSFP+ (QSFP28); G=3.1Gb/s; F=GEPON OLT; 10=10km; 47=1470nm; F=CFP; J=2.97G G=GPON ONU; 70=70km; 61=1610nm G=CFP2; P=6.144G: H=GPON OLT A0=100km; H=CFP4; Q=7.37G; X=MMF/SMF C0=120km BWDM: B3=Tx1310/Rx1550; B5=Tx1550/Rx1310; P=SFP-SC; Q=SFPH=8.5Gb/s; CWDM: B4=Tx1310/Rx1490; B9=Tx1490/Rx1310; MTRJ K=10Gb/s; 20=20dB; 51=Tx1510/Rx1570; 57=Tx1570/Rx1510; T=1/10Gb/s 24=24dB; 27=Tx1270/Rx1330; 33=Tx1330/Rx1270; L=16Gb/s; 28=28dB B2=Tx1270/Rx1577; B7=Tx1577/Rx1270 R=20Gb/s; T2=2TX1310nm; T3=TX1310nm; X=25Gb/s; T5=TX1550nm S=40Gb/s; W=100Gb/s (4x25G or 10x10G); DWDM: M=100Base-X SGMII; 17=Channel 17 N=100/1000Base-X SGMII; 34= Channel 34 00=Channel 17~61 Tunable 

|**_Model Number_**|**_Part Number_**|**_Voltage_**|**_Temperature_**|
|---|---|---|---|
|QSFP-40G-ER4|OPCS-S40-13-CB|3.3V|0C to 70 C|



**Note: All information contained in this document is subject to change without notice.** 

Version: 18V.A _**Page 12 of**_ **12** 

**Optech Technology Co., Ltd.** 

2F., No.41, Ln. 221, Gangqian Rd., Neihu Dist., Taipei City 114, Taiwan, R.O.C. Tel: +886-2-2656-0588          Fax: +886-2-2656-0599 http://www.optech.com.tw e-m ail: sales@optech.com.tw 

