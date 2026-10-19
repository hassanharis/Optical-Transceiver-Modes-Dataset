Optical Transceivers 

## FTLF8519F2XNL 

## **2.125 Gb/s RoHS Compliant Short Wavelength 2x5 SFF Transceiver** 

FTLF8519F2xNL Small Form Factor (SFF) transceivers comply with the 2x5 standard package defined by the Small Form Factor Multi-Sourcing Agreement (MSA)[1] . They are simultaneously compatible with Gigabit Ethernet as specified in IEEE Std 802.32 and Fibre Channel FC-PI-2 10.03. They are RoHS compliant and lead-free per Directive 2002/95/EC[4] and Finisar Application Note AN-2038. 


## FEATURES 

## APPLICATIONS 

- Up to 2.125 Gb/s bi-directionaldata links 

- Standard 2x5 pin SFF footprint(MSA compliant) 

   - 1.25 Gb/s 1000Base-SX Ethernet 

   - Dual Rate 1.063/2.125 Gb/s FibreChannel 

- 850nm Oxide VCSEL lasertransmitter 

- Duplex LC connector 

- RoHS compliant and Lead Free 

- Up to 500m on 50/125μm MMF,300m on 62.5/125μm MMF 

- Metal enclosure, for lower EMI 

- Single 3.3V power supply 

- Low power dissipation <750mW 

- Extended operating temperaturerange: -10°C to 85°C 

**FTLF8519F2xNL** 

## **Product Selection** 

## **FTLF8519F2xNL** 

G 2 Grounding Pins, Short EMI shield M 6 Grounding Pins, Short EMI shield K 2 Grounding Pins, Long EMI shield H 6 Grounding Pins, Long EMI shield 

## **I. Pin Descriptions** 


**----- Start of picture text -----**<br>
Pin Symbol Name/Description Notes<br>**----- End of picture text -----**<br>


|Pin|Symbol|Name/Description|Notes|
|---|---|---|---|
|||||
|MS|MS|Mounting Studs are for mechanical attachment and are<br>connected to chassis ground. Chassis ground is inter-<br>nally isolated from circuit grounds. Connection to user’s<br>ground plane is recommended.|NA|
|1|VEER|Receiver Ground (Common with Transmitter Ground)|NA|
|2|VCCR|Receiver Power Supply|NA|
|3|SD|Signal Detect. Logic 1 indicates normal operation.|LVTTL|
|4|RD-|Receiver Inverted DATA out. AC Coupled|See Rx spec.|
|5|RD+|Receiver Non-inverted DATA out. AC Coupled|See Rx spec.|
|6|VCCT|Transmitter Power Supply|NA|
|7|VEET|Transmitter Ground (Common with Receiver Ground)|NA|
|8|TDIS|Transmitter Disable|LVTTL|
|9|TD+|Transmitter Non-Inverted DATA in. AC Coupled.|See Tx spec.|
|10|TD-|Transmitter Inverted DATA in. AC Coupled|See Tx spec.|




2 

**FTLF8519F2xNL** 

## **II. Absolute Maximum Ratings** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ Max Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Maximum Supply Voltage|Vcc|-0.5||4.0|V||
|Storage Temperature|TS|-40||85|°C||
|Case Operating Temperature|TOP|-10||85|°C||
|Relative Humidity|RH|0||85|%|1|
|Hand Lead Soldering Temperature/Time||||260/10|°C/s||
|Wave Lead Soldering Temperature/Time||||260/10|°C/s||



Notes: 

Non-condensing. 

## **III. Electrical Characteristics (TOP = -10 to 85 °C, VCC = 3.0 to 3.6 Volts)** 

|Parameter|Symbol|Min|Typ|Max|Unit|Ref.|
|---|---|---|---|---|---|---|
|SupplyVoltage|Vcc|3.0||3.6|V||
|SupplyCurrent|Icc||180|240|mA||
|Transmitter|||||||
|Input diferential impedance|Rin||100||Ω|1|
|Single ended data input swing|Vin,pp|250||1200|mV||
|Transmit Disable Voltage|VD|2||Vcc|V||
|Transmit Enable Voltage|VEN|Vee||Vee+ 0.8|V|2|
|Receiver|||||||
|Output diferential impedance|Rout||100||Ω|1|
|Single ended data output swing|Vout,pp|250|350|550|mV|3|
|Data output rise/fall time|tr/ tf|||170|ps|4|
|Mask Margin|||45%||||
|Signal Detect Normal|SDnormal|||VccHOST|V|5|
|Signal Detect Fault|SDfault|Vee||Vee+0.5|V|5|
|Power SupplyRejection|PSR|||100|mVpp|6|
|Deterministic Jitter Contribution (p-p)|RX ∆ DJ|||51.7|ps|7|
|Total Jitter Contribution (p-p)|RX ∆ TJ|||123|ps|8|



Notes: 

1. AC coupled. 

2. Or open circuit. 

3. Into 100 Ω differential termination. Data pattern is PRBS 2[7] -1. 

4. 20 – 80 %. 

5. Signal detect is LVTTL. Logic 1 indicates normal operation; logic 0 indicates no signal detected. 

6. All transceiver specifications are compliant with a power supply sinusoidal modulation of 20 Hz to 1.5 MHz up to specified value applied through the power supply filtering network shown on page 23 of the Small Form-factor Pluggable (SFP) Transceiver MultiSource Agreement (MSA), September 14, 2000[5] . 

7. Measured with DJ-free data input signal. In actual application, output DJ will be the sum of input DJ and ∆ DJ. 

8. If measured with TJ-free data input signal. In actual application, output TJ will be given by 

TJOUT = DJIN + ΔDJ + ~~√~~ (TJIN - DJIN)[2] + (ΔTJ - ΔDJ)[2] 

3 

**FTLF8519F2xNL** 

## **Optical Characteristics (TOP = 0 to 70°C, VCC = 3.0 to 3.6 Volts)** 


**----- Start of picture text -----**<br>
Parameter Symbol Min Typ 7BMax Unit Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|7BMax|Unit|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Transmitter|||||||
|Output Opt. Pwr: 50 or 62.5 MMF|POUT|-9||-3|dBm|1|
|Optical Wavelength|λ|830||860|nm||
|Spectral Width|δ|||0.85|nm||
|Optical Modulation Amplitude|OMATx|196|||μW|2|
|Optical Rise/Fall Time|tr/ tf|||150|ps|3|
|Relative Intensity Noise|RIN|||-120|dB/Hz||
|Deterministic Jitter Contribution (p-p)|TX Δ DJ||20|56.5|ps|4|
|Total Jitter Contribution (p-p)|TX Δ TJ|||119|ps|4|
|Extinction Ratio @ 1.25 Gb/s|ER|9|||dB||
|Mask Margin|||45%||||
|Receiver|||||||
|Receiver Sensitivity = 1.0625 Gb/s|RxSENS|||-20|dBm|5|
|Receiver Sensitivity = 2.125 Gb/s|RxSENS|||-18|dBm|5|
|Receiver Sensitivity = 1.25 Gb/s|RxSENS|||-20|dBm|6|
|Stressed RX sens. = 1.0625 Gb/s||0.055|||mW|7|
|Stressed RX sens. = 2.125 Gb/s||0.096|||mW|7|
|Stressed RX sens = 1.25 Gb/s||||-13.5|dBm|8|
|Average Received Power|RxMAX|||0|dBm||
|Receiver Elec. 3 dB cutof freq.||||1500|MHz||
|Optical Center Wavelength|λC|770||860|nm||
|Return Loss|RL|12|||dB||
|Signal Detect Normal|SDnormal|||-20|dBm||
|Signal Detect Fault|SDfault|-30|||dBm||
|Signal Detect Hysteresis||0.5|||dB||



Notes: 

1. Class 1 Laser Safety per FDA/CDRH, EN (IEC) 60825 laser safety regulations. 

2. Equivalent extinction ratio specification for Fibre Channel. Allows smaller ER at higher average power. 

3. Unfiltered, 20-80%. Complies with FC 1x and 2x eye mask when filtered. 

4. Measured with DJ-free data input signal. In actual application, output DJ will be the sum of input DJ and Δ DJ. 

5. If measured with TJ-free data input signal. In actual application, output TJ will be given by: 

TJOUT = DJIN + ΔDJ +   √ (TJIN - DJIN)[2] + (ΔTJ - ΔDJ)[2] 

6. Specifications are for 50 micro-meter or 62.5 micro-meter fiber 

7. As measured with 9dB extinction ratio. 

8. Measured with conformance signals defined in FC-PI-2 10.0 specifications. 

9. Measured with conformance signals defined in IEEE 802.3 specifications. 

4 

**FTLF8519F2xNL** 

## **V. General Specifications** 


**----- Start of picture text -----**<br>
Parameter Symbol  Min  Typ Max  Units  Ref.<br>**----- End of picture text -----**<br>


|Parameter|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
||||||||
|Data Rate|BR||1.062,<br>1.25<br>2.125|10500|Gb/sec|1|
|Bit Error Rate|BER|||10-12||4|
|Fiber Length on 50/125μm MMF|L|||500<br>300|meters|2<br>3|
|Fiber Length on 62.5/125μm MMF|L|||300<br>150|meters|2<br>3|



Notes: 

1. Gigabit Ethernet and 1x, 2x Fibre Channel compatible per IEEE 802.3 and FC-PI-2 10.0 respectively. Typical maximum data rate extends to 2.5Gb/s. 

2. At 1.0625 Gb/s Fibre Channel and 1.25 Gb/s Gigabit Ethernet data rates. 

3. At 2.125 Gb/s Fibre Channel data rate. 

4. At 1.0625, 1.25, and 2.125Gb/s with PRBS 2[7] -1. 

## **VI. Environmental Specifications** 

FTLF8519F2xNL SFF transceivers have an extended operating temperature range from-10°C to +85°C case temperature. 

|Parameter|Symbol|Min|Typ|Max|Units|Ref.|
|---|---|---|---|---|---|---|
|Case OperatingTemperature|Top|-10||85|°C||
|Storage Temperature|Tsto|-40||85|°C||



Notes: 

1. SFF transceivers may be water washed. However, the process must be followed by a baking step at 80°C for one hour, to ensure the drying of any water which may be trapped inside then shells of the modules. 

## **VII. Regulatory Compliance** 

Finisar transceivers are Class 1 Laser Products and comply with US FDA regulations. These products are certified by TÜV and CSA to meet the Class 1 eye safety requirements of EN (IEC) 60825 and the electrical safety requirements of EN (IEC) 60950. Copies of certificates are available at Finisar Corporation upon request. 

## **VIII. Mechanical Specifications** 

Finisar’s Small Form Factor (SFF) transceivers comply with the standard dimensions defined by the Small Form Factor Multi-Sourcing Agreement (MSA). 

5 

**FTLF8519F2xNL** 


FTLF8519F2GNL 

6 

**FTLF8519F2xNL** 



**----- Start of picture text -----**<br>
FTLF8519F2KNL<br>**----- End of picture text -----**<br>



FTLF8519F2HNL 

7 

**FTLF8519F2xNL** 

## **Ix. PCB Layout and Bezel Recommendations** 



Minimum Recommended Pitch is 0.600” 

8 

**FTLF8519F2xNL** 

## **x. References** 

1. Small Form Factor (SFF) Transceiver Multi-source Agreement (MSA). July 5, 2000. 

2. IEEE Std 802.3, 2002 Edition, Clause 38, PMD Type 1000BASE-SX. IEEE Standards Department, 2002. 

3. “Fibre Channel Draft Physical Interface Specification (FC-PI-2 10.0)”. American National Standard for Information Systems. 

4. Directive 2002/95/EC of the European Council Parliament and of the Council, “on the restriction of the use of certain hazardous substances in electrical and electronic equipment.” January 27, 2003. 

5. Small Form-factor Pluggable (SFP) Transceiver Multi-source Agreement (MSA), September 14, 2000. 

© 2023 Coherent Corp. Legal notices : coherent.com/legal 

photonics.sales@coherent.com www.coherent.com 

