DATASHEET 

5.7 

## **SO-TQSFP-DD-4CC-ZR** 

QSFP-DD OIF 400G-ZR Ethernet Coh Tunable Flexgrid 120km LC D9128-D9612 

## OVERVIEW 

The SO-TQSFP-DD-4CC-ZR is an QSFP-DD form-factor (type 2) DWDM transceiver for 400 Gbps Ethernet applications. The transceiver is intended for use in interconnect applications between data centers with switches, routers etc. 

SO-TQSFP-DD-4CC-ZR supports both the amplified (Application Code 0x01) and the un-amplified (Application Code 0x02) use cases as defined in the OIF 400ZR specification. 

The dispersion performance is in accordance with OIF 400ZR for distances up to 120km over a SingleMode (SM) fiber using a single optical carrier at 60Gbaud and 16QAM coherent modulation. The transmitter is tunable over the ITU C-Band at 100 GHz grid (75 GHz grid is optional). 

The electrical interface is according to IEEE 802.3bs 400GAUI-8 enabling SO-TQSFP-DD-4CC-ZR to support 400G transport according to OIF-ZR specification. The 400GAUI-8 client/electrical interface is compatible with IEEE P802.3bs 8 lane 56G PAM-4, as used for “grey” datacenter optical transceivers, for example 400GBASE-DR4. 

This transceiver provides digital diagnostic functions via a 2-wire serial interface and a management interface according to CMIS4.0. 

The transceiver supports the commercial temperature range (C-temp): 0°C to 70°C (32°F to 158°F). 

## TECHNICAL DATA 

|**Parameter**<br>**Value**|**Parameter**|**Value**|
|---|---|---|
|Technology<br>DWDM QSFP-DD type 2|**Transmitter data:**||
|Transmission media<br>SM (2x LC)|Output power|Min: -10.0dBm|
|Typical reach<br>120km||Max: -6.0dBm|
|Nominal wavelengths<br>191.28 - 196.12THz (Tunable) 6.25GHz|Transmit wavelengths|191.28 - 196.12THz|
|Interface standards<br>400GBASE-ZR||in 100 (75) GHz steps|
|Protocol support<br>400GbE||(G.694.1)|
|4x 100GbE|**Receiver data:**||
|Power consumption<br>< 20 W (Class 8)|Minimum input power|-20.0dBm1)|
|Operating temperature<br>0°C to +70°C||-12.0dBm2)|
|Storage temperature<br>-40°C to +85°C|Input sensitivity|-12.0dBm3)|
|Latency<br>8µs|Overload (max power)|0 dBm2)|
|1)Receiver sensitivity at unamplified configurations|OSNR tolerance|Max: 26dB/0.1nm4)|
|2)Signal power of the channel at the OSNR performance value|CD tolerance|Min: 2400ps/nm|
|3)Input power needed to achieve post FEC BER|Optical path OSNR penalty<br>tolerance|Max: 0.5dB5)|
|4)At CFEC threshold|PMD tolerance|Min: 10 ps6)|
|5)OSNR tolerance penalty over OSNR Tolerance due to reflections and dispersion|Pre-FEC BER|1.25x10-2|
|6)Tolerance to PMD with <0.5 dB penalty to OSNR sensitivity.|Rx_LOS Assert|-28.0dBm7)|
|7)Set to comply with 400G modes. Can be changed on individual modules to fully support<br>other modes.|DDM|Yes|
|**Safety/regulatory compliance:**|MSA compliance|QSFP-DD MSA|
|TUV/UL/FDA (contact Smartoptics for latest certification information)||CMIS4.0, OIF400ZR|



7) Set to comply with 400G modes. Can be changed on individual modules to fully support other modes. **Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. 

For more information visit smartoptics.com. 

DATASHEET 

5.7 

## ORDERING INFORMATION 

|**Ordering code**|**Description**|
|---|---|
|SO-TQSFP-DD-4CC-ZR|QSFP-DD OIF 400GZR Ethernet Coh Tunable Flexgrid 120km LC|



## GENERAL DEFINITIONS 

|**Parameter**|**Description**||
|---|---|---|
||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
|Technology|DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
||AOC: Active Optical Cable. Optical cable with attached connectors.||
|Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
|Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.||
|Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
|Protocols|Protocols within supported bit rate range.||
|Nominal wavelength|Typical wavelength(s) from transmitter.||
|Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
|Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
|Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.||
||Max operating case temperature range.||
|Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
||Industrial temperature range (I-temp):-40°C to +85°C (-40°F to +185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

