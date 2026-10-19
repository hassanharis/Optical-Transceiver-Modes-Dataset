DATASHEET 

6.3 

## **TQD027-S55C-SO** 

QSFP-DD, 400G Ethernet Coherent 193.7THz, 40km, CMIS 5.0. 

## OVERVIEW 

The TQD027-S55C-SO is an QSFP-DD form-factor (type 2a) coherent transceiver intended for 400Gbps Ethernet applications over 40km without amplifiers. TQD027-S55C-SO is fixed to the frequency of 193.7THz. 

The TQD027-S55C-SO is a flexible module with application codes that is compatible with asynchronous 100G/200G electrical streams 4x100GAUI-2 or 2x200GAUI-4 or the 400G electrical stream 400GAUI-8 stream. This makes the module compatible with a variety of hosts, including 400G Transponder and 4x100G or 2x200G Muxponder solutions to carry the optical 400G signal. 


The below table lists the OIF 400ZR and OpenZR+ modes supported by TQD027-S55C-SO. 

|**CMIS**<br>**Application**<br>**Code**|<br>**Host format**|**Electrical interface**|**Payload**|**FEC**|**Modulation**|<br>**Line Symbol**<br>**Baud Rate**|**MSA format**||
|---|---|---|---|---|---|---|---|---|
|1|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA, extended||
|2|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|CFEC|DP-16QAM|59.8GBd|OIF 400ZR, app code 0x02||
|3|2 x 200GBASE-R|2x 200GAUI-4 (4x 50G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA, extended||
|4|4 × 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA, extended||



TQD027-S55C-SO will automatically configure the above via the Application modes. For 400G applications, the TQD027-TUNCSO asynchronously (GMP) maps an Ethernet signal from a switch/router to an intermediate 400ZR frame structure, then adapts the frame structure to the selected FEC engine. The encoded signal is subsequently DSP framed and modulated for transmission as a coherent Dual Polarity signal. 

Note! CMIS application codes 1, 3 and 4 are not interoperable with the OpenZR+ MSA. These modes have been enhanced in to increase the optical performance on the Media side. 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.3 

## TECHNICAL DATA 

The optical characteristics are into Generic and Application code sections. The _Generic_ section defines the common characteristics, independent of the selected application modes. The _Application_ code section defines application code based optical characteristics. 

The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|**Parameter**|**Value**|
|---|---|
|Technology|DWDM QSFP-DD type 2a|
|Transmission media|SM (2x LC)|
|Nominal wavelength|193.7 THz|
|Interface standards|OIF 400ZR / OpenZR+ (extended)|
|Operating temperature|+15OC to +75OC1)|
|Storage temperature|-40OC to +85OC|
|DDM functions|Total received power|
||Coherent channel power|
||OSNR, eSNR, PDL, dispersion, DGD|
||Case temperature|



- 1) The module will turn up from cold start at ambient temperature as low as 

- -5C and will reach specifications after self-heating up to min temperature. 

- 2) The module transmit power can be provisioned up to the maximum available TX power. 

|**Parameter**|**Value**|
|---|---|
|MSA|QSFP-DD MSA’s, CMIS5.0|
|Misc|Sync-E support, LLDP, MLG 2.0 & 3.0|
|Power consumption, EOL|20.0W|
|Tx Power|Min -9dBm2)|
||Max -4dBm2)|
|Tx In-band OSNR|Min 34dB/0.1nm|
|Tx Out-Of-Band OSNR|Min 30dB/0.1nm|
|Rx_LOS Assert|-28.0dBm3)|
|Receiver turn-up|Max 30ms from warm start|
||Max 120s from cold start|
|Absolute max conditions|Rx signal input power: +13dBm|
||Rx total input power: +15dBm|



If the TX power is not provisioned by the host, the module TX power will default to the maximum available power, which can be any power level in the specified 10dB range. 

- 4) Set to comply with 400G modes. Can be changed on individual modules to fully support other modes. 

**Safety/regulatory compliance:** 

TUV/UL/FDA (contact Smartoptics for latest certification information) 

RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.3 

## OPTICAL SPECIFICATION - APPLICATION CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Appl**<br>**mode**||**Line rate**|**Host format**|**Tx Power1)**|**Rx sensitivity**|**CDC range**|
|---|---|---|---|---|---|---|
||1|400G|1x 400GAUI-8|-9 to -4dBm|-22dBm|2 400 ps/nm|
||2|400G|1x 400GAUI-8|-9 to -4dBm|-20dBm|2 400 ps/nm|
||3|400G|2x 200GAUI-4|-9 to -4dBm|-22dBm|2 400 ps/nm|
||4|400G|4x 100GAUI-2|-9 to -4dBm|-22dBm|2 400 ps/nm|



1) The module transmit power can be provisioned up to the maximum available TX power. If the TX power is not provisioned by the host, the module TX power will default to the maximum available power, which can be any power level in the specified 10dB range. 

|ORDERING|INFORMATION|||
|---|---|---|---|
|**Ordering code**|**Item Name**|**Latency:**||
|||400G CFEC:|8us|
|TQD027-S55C-SO|QSFP-DD 400G-ER Coh 193.7THz SM 40km CMIS5.0|400G OFEC:|5us|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.3 

## GENERAL DEFINITIONS 

|**Parameter**|**Description**||
|---|---|---|
||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
|Technology|CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.<br>DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.||
||BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
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

