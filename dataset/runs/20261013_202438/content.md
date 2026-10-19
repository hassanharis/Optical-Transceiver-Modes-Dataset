
## **SFP-1G-13-80K-D** 

## **1.25Gb/s 1550nm Single-mode SFP Transceiver** 

## **PRODUCT FEATURES** 


Up to 1.25Gb/s data links with DDM 


DFB laser transmitter and PIN photo-detector 


Up to 80km on 9/125µm SMF 


- Hot-pluggable SFP footprint 


Duplex LC/UPC type pluggable optical interface 


- Low power dissipation 


Metal enclosure, for lower EMI 


RoHS compliant and lead-free 


Support Digital Diagnostic Monitoring interface 


Single +3.3V power supply 


Compliant with SFF-8472 


Case operating temperature range: Commercial: 0°C to +70°C 

Industrial: -40°C to +85° 

## **APPLICATIONS** 


Switch to Switch Interface 


Gigabit Ethernet 


Switched Backplane Applications 


Router/Server Interface 


Other Optical Links 



## **PRODUCT DESCRIPTION** 

Cloudtron SFP-1G-13-80-D Small Form Factor Pluggable (SFP) transceivers are compatible with the Small Form Factor Pluggable Multi-Sourcing Agreement (MSA). The transceiver consists of five sections: the LD driver, the limiting amplifier, the digital diagnostic monitor, the DFB laser and the PIN photo-detector. The module data link up to 80KM in 9/125um single mode fibre. 

The optical output can be disabled by a TTL logic high-level input of Tx Disable, and the system also can disable the module via I2C. Tx Fault is provided to indicate that degradation of the laser. Loss of signal (LOS) output is provided to indicate the loss of an input optical signal of receiver or the link status with partner. The system can also get the LOS (or Link)/Disable/Fault information via I2C register access. 

## **Ordering information** 

|Product Part<br>Number|Data Rate||Wavelength|Transmission|Temperature Range<br>`（`Tcase`）（`℃`）`|Temperature Range<br>`（`Tcase`）（`℃`）`|
|---|---|---|---|---|---|---|
||(Mbps)|Media|(nm)|Distance(km)|||
|**SFP-1G-13-80K-D**|1250|Single mode<br>fibre|1310|80|0~70|Commercial|
|**SFP-1G-13-80K-DI**|1250|Single mode<br>fibre|1310|80|-40~85|Industrial|





## **I.       Pin Descriptions** 

|**Pin**|**Symbol**|**Name/Description**|**Ref.**|
|---|---|---|---|
|1|VEET|Transmitter Ground(Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.||
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|2|
|4|MOD_DEF(2)|Module Definition 2. Data line for Serial ID.|3|
|5|MOD_DEF(1)|Module Definition 1. Clock line for Serial ID.|3|
|6|MOD_DEF(0)|Module Definition 0. Grounded within the module.|3|
|7|Rate Select|No connection required|4|
|8|LOS|Loss of Signal indication.    Logic 0 indicates normal operation.|5|
|9|VEER|Receiver Ground(Common with Transmitter Ground)|1|
|10|VEER|Receiver Ground(Common with Transmitter Ground)|1|
|11|VEER|Receiver Ground(Common with Transmitter Ground)|1|
|12|RD-|Receiver Inverted DATA out.    AC Coupled||
|13|RD+|Receiver Non-inverted DATA out.    AC Coupled||
|14|VEER|Receiver Ground(Common with Transmitter Ground)|1|
|15|VCCR|Receiver Power Supply||
|16|VCCT|Transmitter Power Supply||
|17|VEET|Transmitter Ground(Common with Receiver Ground)|1|
|18|TD+|Transmitter Non-Inverted DATA in. AC Coupled.||
|19|TD-|Transmitter Inverted DATA in.    AC Coupled.||
|20|VEET|Transmitter Ground(Common with Receiver Ground)|1|



Note: 

1.   Circuit ground is internally isolated from chassis ground. 

2.   Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

3.   Should be pulled up with 4.7k - 10kohms on host board to a voltage between 2.0V and 3.6V.MOD_DEF (0) pulls line low to indicate module is plugged in. 

4.   This is an optional input used to control the receiver bandwidth for compatibility with multiple data rates (most likely Fibre Channel 1x and 2x Rates). If implemented, the input will be internally pulled down with > 30kΩ resistor. The input states are: 

Low (0 – 0.8V):             Reduced Bandwidth 

- (>0.8, < 2.0V):              Undefined 

High (2.0 – 3.465V):     Full Bandwidth 

   - Open:                             Reduced Bandwidth 

5.   LOS is open collector output should be pulled up with 4.7k - 10kohms on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal 


. 



**Figure2. Pin out of Connector Block on Host Board** 

## **II.      Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Storage Temperature|Ts|-40||85|ºC||
|Storage Ambient Humidity|HA|5||95|%||
|Power Supply Voltage|VCC|-0.5||4|V||
|Signal Input Voltage||-0.3||Vcc+0.3|V||
|Receiver Damage Threshold||5|||dBm||



## **III.    Recommended Operating Conditions** 

|Parameter|Symbol|Min.<br>Typ.<br>Max.<br>Unit|Min.<br>Typ.<br>Max.<br>Unit|Min.<br>Typ.<br>Max.<br>Unit|Min.<br>Typ.<br>Max.<br>Unit|Note|
|---|---|---|---|---|---|---|
|Case Operating Temperature|Tcase|0||70|º|SFP-1G-13-80K-D|
|||-40||85|C|SFP-1G-13-80K-DI|
|Ambient Humidity|HA|5||70|%|Non-condensing|
|Power SupplyVoltage|VCC|3.13|3.3|3.47|V||
|Power SupplyCurrent|ICC|||300|mA||
|Power SupplyNoise Rejection||||100|mVp-p|100Hz to 1MHz|
|Data Rate|||1250/1250||Mbps|TX Rate/RX Rate|
|Transmission Distance||||80|KM||
|Coupled Fibre||Single mode fibre||||9/125um SMF|





## **IV.    Specification of Transmitter** 

|**Parameter**|**Symbol**<br>**Min.**<br>**Typ. **<br>**Max.**|**Symbol**<br>**Min.**<br>**Typ. **<br>**Max.**|**Symbol**<br>**Min.**<br>**Typ. **<br>**Max.**|**Symbol**<br>**Min.**<br>**Typ. **<br>**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Average Output Power|POUT|0||5|dBm||
|Extinction Ratio|ER|9|||dB||
|Centre Wavelength|λC|1530|1550|1570|nm|DFB Laser|
|Side Mode Suppression Ratio|SMSR|30|||dB||
|Spectrum Bandwidth(-20dB)|σ|||1|nm||
|Transmitter OFF Output Power|POff|||-45|dBm||
|Differential Line Input Impedance|RIN|90|100|110|Ohm||
|Jitter P-P|tJ|||0.1|UI|Note (1)|
|Output Eye Mask|Compliant with    IEEE802.3 z<br>(class 1 laser safety)|||||Note (2)|



Note (1): Measure at 2^7-1 NRZ PRBS pattern. 

Note (2): Transmitter eye mask definition. 


## **V.    Specification of Receiver** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|Input Optical Wavelength|λIN|1270||1610|nm|PIN-TIA|
|Receiver Sensitivity|PIN|||-26|dBm|Note(1)|
|Input Saturation Power(Overload)|PSAT|-3|||dBm||
|Los Of Signal Assert|PA|-38|||dBm||
|Los Of Signal De-assert|PD|||-27|dBm|Note(2)|
|LOS Hysteresis|PA-PD|0.5|2|6|dB||



Note 

(1): Measured with Light source 1550nm, ER=9dB; BER =<10^-12 @PRBS=2^7-1 NRZ Note 

(2): When LOS de-asserted, the RX data+/- output is signal output. 



## **VI.    Electrical Interface Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ. **|**Max.**|**Unit**|**Note**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
|Total SupplyCurrent|ICC|||A|mA|Note(1)|
|Transmitter Disable Input-High|VDISH|2||Vcc+0.3|V||
|Transmitter Disable Input-Low|VDISL|0||0.8|V||
|Transmitter Fault Input-High|VDISL|2||Vcc+0.3|V||
|Transmitter Fault Input-Low|VTxFH|0||0.8|V||
|**Receiver**|||||||
|Total SupplyCurrent|ICC|||B|mA|Note(1)|
|LOSS Output Voltage-High|VLOSH|2||Vcc+0.3|V|LVTTL|
|LOSS Output Voltage-Low|VLOSL|0||0.8|V||



Note (1): A (TX) + B (RX) = 300mA (Not include termination circuit) 

## **VII.   Digital Diagnostic Functions** 

Cloudtron SFP-1G-13-80K-D transceivers support the 2-wire serial communication protocol as defined in the SFP MSA. It is very closely related to the E2PROM defined in the GBIC standard, with the same electrical specifications. The standard SFP serial ID provides access to identification information that describes the transceiver’s capabilities, standard interfaces, manufacturer, and other information. 

Additionally, Cloudtron SFP transceivers provide a unique enhanced digital diagnostic monitoring interface, which allows real-time access to device operating parameters such as transceiver temperature, laser bias current, transmitted optical power, received optical power and transceiver supply voltage. It also defines a sophisticated system of alarm and warning flags, which alerts end-users when particular operating parameters are outside of a factory set normal range. 

The SFP MSA defines a 256-byte memory map in E2PROM that is accessible over a 2-wire serial interface at the 8bit address 1010000X (A0h). The digital diagnostic monitoring interface makes use of the 8bit address 1010001X (A2h), so the originally defined serial ID memory map remains unchanged. The interface is identical to, and is thus fully backward compatible with both the GBIC Specification and the SFP Multi Source Agreement. 

The operating and diagnostics information is monitored and reported by a Digital Diagnostics Transceiver Controller (DDTC) inside the transceiver, which is accessed through a 2-wire serial interface. When the serial protocol is activated, the serial clock signal (SCL, Mod Def 1) is generated by the host. The positive edge clocks data into the SFP transceiver into those segments of the E2PROM that are not write-protected. The negative edge clocks data from the SFP transceiver. The serial data signal (SDA, Mod Def 2) is bi-directional for serial data transfer. The host uses SDA in conjunction with SCL to mark the start and end of serial protocol activation. The memories are organized as a series of 8-bit data words that can be addressed individually or sequentially. 

Digital diagnostics for the SFP-1G-13-80K-D are internally calibrated by default. 



## **VIII. Recommend Circuit Schematic** 


**IX.    Mechanical Specifications** (Unit: mm) 





**SFP-1G-13-80K-D** 



## **X.      Regulatory Compliance** 

|**Feature**|**Reference**|**Performance**|
|---|---|---|
|Electrostatic discharge<br>(ESD`）`|IEC/EN 61000-4-2|Compatible with standards|
|Electromagnetic<br>Interference(EMI)|FCC Part 15 Class B EN  55022 Class B (CISPR<br>22A)|Compatible with standards|
|Laser Eye Safety|FDA   21CFR    1040.10,1040.11<br>IEC/EN60825-1，2|Class 1 laser product|
|Component Recognition|IEC/EN 60950, UL|Compatible with standards|
|ROHS|2002/95/EC|Compatible with standards|
|EMC|EN61000-3|Compatible with standards|




