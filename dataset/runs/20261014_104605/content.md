Finisar[®] Transceiver 


## **Product Specification 10Gb/s SFPwire[®] SFP+ Active Optical Cable FCBG110SD1Cxx-WX** 

## **PRODUCT FEATURES** 

- Hot-pluggable SFP+ cable ends 

- Supports 10.3125 Gb/s bit rate 

- RoHS-6 compliant (lead-free) 

- Available in lengths up to 20m 

- SFI Limiting interface 

- Single 3.3V power supply 

- Low power dissipation 

- Commercial temperature range: 0°C to 70°C 

- Rigid pull-tab for improved highdensity installations 


## **APPLICATIONS** 

- 10G Ethernet Datacenter Intra-Rack and Inter-Rack links 

FCBG110SD1Cxx-WX 10Gb/s SFPwire® SFP+ active optical cables are designed for use in 10-Gigabit Ethernet links.  They are electrically compliant with SFF-8431[1] , and the mechanical SFP+ plug is compatible with SFF-8432[2] . SFPwire is SFI limiting.  No host electrical transmitter pre-emphasis is required.  No host electrical receiver linear equalization is required.   Host board designers using an EDC PHY IC should follow the IC manufacturer’s recommended settings for interoperating the host-board EDC PHY with a limiting receiver. SFPwire is RoHS compliant as described in Application Note AN-2038[3,4] . 

## **PRODUCT SELECTION** 

## 16B **FCBG110SD1Cxx-WX** 

|XX|Cable Length||XX|Cable Length|
|---|---|---|---|---|
|01|1 meter||20|20 meters|
|02|2 meters||30|30 meters|
|03|3 meters||Z5|0.5 meter|
|07|7 meters||A5|1.5 meters|
|10|10 meters||B5|2.5 meters|
|15|15 meters||C5|3.5 meters|



© Coherent Corp. June 2023 RevD2 

Page 1 

FCBG110SD1Cxx-WX Product Specification                                                           Finisar[®] Transceiver 

## **I. Pin Descriptions** 

|**Pin**|**Symbol**|**Name/Description**|**Ref.**|
|---|---|---|---|
|1|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|2|TFAULT|Transmitter Fault.|2|
|3|TDIS|Transmitter Disable. Laser output disabled on high or open.|3|
|4|SDA|2-wire Serial Interface Data Line|4|
|5|SCL|2-wire Serial Interface Clock Line|4|
|6|MOD_ABS|Module Absent. Grounded within the module|4|
|7|RS0|No connection required||
|8|RX_LOS|Loss of Signal indication.  Logic 0 indicates normal operation.|5|
|9|RS1|No connection required||
|10|VEER|Receiver Ground (Common with Transmitter Ground)|1|
|11|VEER|Receiver Ground (Common with Transmitter Ground)|1|
|12|RD-|Receiver Inverted DATA out.  AC Coupled||
|13|RD+|Receiver Non-inverted DATA out.  AC Coupled||
|14|VEER|Receiver Ground (Common with Transmitter Ground)|1|
|15|VCCR|Receiver Power Supply||
|16|VCCT|Transmitter Power Supply||
|17|VEET|Transmitter Ground (Common with Receiver Ground)|1|
|18|TD+|Transmitter Non-Inverted DATA in.  AC Coupled.||
|19|TD-|Transmitter Inverted DATA in.  AC Coupled.||
|20|VEET|Transmitter Ground (Common with Receiver Ground)|1|



Notes: 

1. Circuit ground is internally isolated from chassis ground. 

2. TFAULT is an open collector/drain output, which is pulled up with a 4.7k  – 10k  resistor on the host board, but is grounded inside the SFP+ cable plug. 

3. Laser output disabled on TDIS >2.0V or open, enabled on TDIS <0.8V. 

4. Should be pulled up with 4.7k  – 10k  on host board to a voltage between 2.0V and 3.6V. MOD_ABS pulls line low to indicate module is plugged in. 

5. LOS is open collector output.  Should be pulled up with 4.7k  – 10k  on host board to a voltage between 2.0V and 3.6V. Logic 0 indicates normal operation; logic 1 indicates loss of signal. 


**----- Start of picture text -----**<br>
VeeT 20<br>1 VeeT<br>TD- 19<br>2 TX_Fault<br>TD+ 18<br>3 TX_Disable<br>VeeT 17<br>4 SDA<br>VccT 16<br>Towards 5 SCL VccR 15 Towards<br>Bezel 6 MOD_ABS ASIC<br>VeeR 14<br>7 RS0<br>RD+ 13<br>8 RX_LOS<br>RD- 12<br>9 RS1<br>VeeR 11<br>10 VeeR<br>**----- End of picture text -----**<br>


**Figure 1.  Diagram of Host Board Connector Block Pin Numbers and Names.** 

© Coherent Corp. June 2023 RevD2 

Page 2 

FCBG110SD1Cxx-WX Product Specification                                                                Finisar[®] Transceiver 

## **II. Absolute Maximum Ratings** 

Exceeding the limits below may damage the active optical cable permanently. 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Ref.**|
|---|---|---|---|---|---|---|
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|C|1|
|Case OperatingTemperature|TA|0||70|C||
|RelativeHumidity|RH|0||85|%|2|



## Notes: 

1. Assumes no mechanical load force on the unit.  Ensuring no mechanical load force requires a cable bend radius >70 mm.  Otherwise, the storage temperature range is -20 to 75°C. 

2. Non-condensing. 

## **III. Electrical Characteristics (each cable end, TOP = 0 to 70**  **C, VCC = 3.14 to 3.46 Volts)** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Ref.**|
|---|---|---|---|---|---|---|
|Supply Voltage|Vcc|3.14||3.46|V||
|Supply Current|Icc|||250|mA||
|**Transmitter**|||||||
|Input differential impedance|Rin||100|||1|
|Differential data input swing|Vin,pp|180||700|mV||
|Transmit Disable Voltage|VD|2||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V||
|**Receiver**|||||||
|Differential data output swing|Vout,pp|300||850|mV|2,6|
|Data output rise time, fall time|tr|28|||ps|3|
|LOS Fault|VLOS fault|2||VccHOST|V|4|
|LOS Normal|VLOS norm|Vee||Vee+0.8|V|4|
|Power Supply Noise Tolerance|VccT/VccR|Per SFF-8431 Rev 4.1|||mVpp|5|



## Notes: 

1. Connected directly to TX data input pins.  AC coupling from pins into laser driver IC. 2. Into 100  differential termination. 

3. 20 – 80%. Measured with Module Compliance Test Board and OMA test pattern. Use of four 1’s and four 0’s in sequence in the PRBS^9 is an acceptable alternative. SFF-8431 Rev 4.1 

4. LOS is an open collector output.  Should be pulled up with 4.7k  – 10k  on the host board. Normal operation is logic 0; loss of signal is logic 1. Maximum pull-up voltage is 5.5V. 

5. Testing methodology per SFF-8431. Rev 4.1 

6. The FCBG110SD1Cxx-WX is SFI Limiting.  Host board designers using an EDC PHY IC should follow the IC manufacturer’s recommended settings for interoperating the host-board EDC PHY with a limiting receiver. 

## **IV.  General Specifications** 

|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Ref.**|
|---|---|---|---|---|---|
|BR||10.3||Gb/s||
|BER|||10-15||1|



Notes: 

1. Tested with a 2[31] – 1 PRBS 

© Coherent Corp. June 2023 RevD2 

Page 3 

FCBG110SD1Cxx-WX Product Specification                                                                Finisar[®] Transceiver 

## **V. Environmental Specifications** 

The FCBG110SD1Cxx-WX SFPwire has a commercial operating temperature range from 0°C to 70°C case temperature. 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Units**|**Ref.**|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|0||70|°C||
|Storage Temperature|Tsto|-40||85|°C|1|



Notes: 

1. Assumes no mechanical load force on the unit.  Ensuring no mechanical load force requires a cable bend radius of >70 mm.  Otherwise, the storage temperature range is -20 to 75°C. 

## **VI. Regulatory Compliance** 

The FCBG110SD1Cxx-WX SFPwire, which contains laser devices, is a Class 1 laser product and complies with 21CFR 1040.10 and 1040.11 except for deviations pursuant to Laser Notice No. 50, dated June 24, 2007, and it complies with EN(IEC) 60825 Edition 1.2 regulations. The FCBG110SD1Cxx-WX is also RoHS Compliant. 

Copies of certificates are available at Coherent upon request. 

© Coherent Corp. June 2023 RevD2 

Page 4 

FCBG110SD1Cxx-WX Product Specification                                                                Finisar[®] Transceiver 

## **VII.  Mechanical Specifications** 

The FCBG110SD1Cxx-WX SFPwire SFP+ cable ends are compatible with the SFF-8432 specification for improved pluggable form factor.  The color of rigid pull-tab is black and the color of cable jacket is orange. 


|Length tolerance X|1 m ≤length ≤ 4.5 m:     +15 / -0|cm|
|---|---|---|
||5 m ≤length ≤ 14.5 m:    +30 / -0|cm|
||Length≥15.0 m            +2% / -0|m|



**Figure 2.  FCBG110SD1Cxx-WX Mechanical Dimensions.** 

## **FCBG110SD1Cxx-WX SFPwire® cable details** 

|**Description**|**Min**|**Typ**|**Max**|**Units**|**Notes**|
|---|---|---|---|---|---|
|Cable JacketMaterial|||||PVC|
|CableFlammabilityRating|||||OFNR|
|Cable Outer Diameter|2.8|3.0|3.2|mm||
|CableTensileLoad (ShortTerm)|||200|Newtons||
|CableTensileLoad (LongTerm)|||100|Newtons||
|Crush Resistance|10|||Newtons/mm|FOTP-41|
|ImpactResistance|0.5|||Newton·m|FOTP-25|
|Flexing|300|||Cycles|FOTP-104|
|TwistBend|||||ExceedsFOTP-85|
|Cable to SFP+ Plug Connection|||90|Newtons||
|BendRadius (ShortTerm)|25|||mm||
|BendRadius (LongTerm)|30|||mm||
|Durability|100|||Cycle Min||



Page 5 

© Coherent Corp. June 2023 RevD2 

Finisar[®] Transceiver 

FCBG110SD1Cxx-WX Product Sp 

## **VIII.  PCB Layout and Bezel Recommendations** 


**Figure 3.** 

Page 6 

© Coherent Corp. June 2023 RevD2 

Finisar[®] Transceiver 

FCBG110SD1Cxx-WX Product Sp 



**Figure 4.** 

© Coherent Corp. June 2023 RevD2 

Page 7 

FCBG110SD1Cxx-WX Product Specification                                                                Finisar[®] Transceiver 

## **IX.     Host - Active optical cable end Interface Block Diagram** 


**Figure 5.** 

© Coherent Corp. June 2023 RevD2 

Page 8 

FCBG110SD1Cxx-WX Product Specification                                                                Finisar[®] Transceiver 

## **X. References** 

1. “Specifications for Enhanced 8.5 and 10 Gigabit Small Form Factor Pluggable Module ‘SFP+ ‘”, SFF Document Number SFF-8431, Revision 4.1. 

2. “Improved Pluggable Formfactor”, SFF Document Number SFF-8432, Revision 4.2, April 18, 2007. 

3. Directive 2011/65/EU of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment”. Certain products may use one or more exemptions as allowed by the Directive. 

4. “Application Note AN-2038: Finisar Implementation of RoHS Compliant Transceivers” 

## **XI. For More Information** 

Coherent Corp. 375 Saxonburg Boulevard Saxonburg, PA  16056 photonics.sales@coherent.com H www.coherent.com U 

© Coherent Corp. June 2023 RevD2 

Page 9 

