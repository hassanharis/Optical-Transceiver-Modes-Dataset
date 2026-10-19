DATASHEET 

6.2 

## **OSFP 800G AEC, CMIS 5.2** 

OSFP800 – OSFP800 Active Electrical Cable (AEC) 800GbE, AWG32, CMIS5.2, 1.0-3m 

## DOC001-xxxC-SO 

DOC001-xxxC-SO is an Active Electrical Cable (AEC) solution of Twinax type, i.e. a copper cable similar to coaxial cable, but with two inner conductors instead of one. DOC001-xxxC-SO is a solution for 800Gbps connections within racks and across adjacent racks where the interconnected equipment uses OSFP800 interfaces. It provides a cost-efficient solution as compared to using optical transceivers and it simplifies the patching since no separate transmit/receive direction has to be taken into account. 

DOC001-xxxC-SO incorporates a data-signal processor (DSP) in each end to enhance the performance of the electrical characteristics. The electrical interfaces of the module are compliant with 800GAUI-8, 400GAUI-4, 200GAUI-2, 100GAUI-2, 100GAUI-1 and 50GAUI-1 as well as the OSFP800 MSA. 

DOC001-xxxC-SO integrates eight data lanes (50Gbd) in each direction using PAM4 modulation with 800Gbps aggregate bandwidth. 

DOC001-xxxC-SO cables have an I2C interface with Integrated Digital Diagnostic Monitoring according to the Common Management Interface Specification CMIS 5.2. 

The DOC001-xxxC-SO is provided in lengths from 1 to 3 meters (3.3 to 9.8 ft). 

## PRODUCT FEATURES 

- 800G to 800G interconnect 

- OSFP800 compliant connectors 

- 800GAUI-8, 400GAUI-4, 200GAUI-2, 100GAUI-2, 100GAUI-1, 50GAUI-1 electrical interface 

- Thin and flexible cables (AWG32) 

- CMIS5.2 compliant I[2] C management interface 

- BER < 10[-8] (pre-FEC), BER < 10[-15] (post FEC) 

- 1 to 3 meters (3.3 to 9.8 ft) 

- Low power consumption; <10.0W per side 

- Operating temperature 0[o] C to +70[o] C (32°F to +158°F) 

- Storage temperature -40[o] C to +85[o] C (-40°F to +185°F) 

## APPLICATIONS 

- Data Center cabling infrastructure 

- Storage Area Network (SAN) 

- Network Attached Storage (NAS) 

- Hub, switches, routers, servers 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.2 

## ORDERING INFORMATION 

|**Parameter**|**Description, long**|
|---|---|
|DOC001-001C-SO|OSFP800 Active Electrical Cable (AEC), 800G Ethernet, AWG32, CMIS5.2 1m|
|DOC001-1M5C-SO|OSFP800 Active Electrical Cable (AEC), 800G Ethernet, AWG32, CMIS5.2 1.5m|
|DOC001-002C-SO|OSFP800 Active Electrical Cable (AEC), 800G Ethernet, AWG32, CMIS5.2 2m|
|DOC001-2M5C-SO|OSFP800 Active Electrical Cable (AEC), 800G Ethernet, AWG32, CMIS5.2 2.5m|
|DOC001-003C-SO|OSFP800 Active Electrical Cable (AEC), 800G Ethernet, AWG32, CMIS5.2 3m|



## APPLICATION CODE LIST 

|**CMIS**|**Application**|**Code**|<br>**Host format**|**Electrical interface**|**Host**<br>**Electrical ID**|**Payload**|**FEC**|**MSA**|**Media ID**||
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||Active Cable|||
||1||1x 800GBASE-R|1x 800GAUI-8-S C2M|0x51|800G|RS-FEC|assembly with|0x03||
|||||||||BER<2.6e-4|||
|||||||||Active Cable|||
||2||2 x 400GBASE-R|2x 400GAUI-4-S C2M|0x4F|2x 400G|RS-FEC|assembly with|0x03||
|||||||||BER<2.6e-4|||
|||||||||Active Cable|||
||3||8 x 100GBASE-R|8x 100GAUI-1-S C2M|0x4B|8x 100G|RS-FEC|assembly with|0x03||
|||||||||BER<2.6e-4|||
|||||||||Active Cable|||
||4||1x 400GBASE-R|1x 400GAUI-8 C2M|0x11|1x 400G|RS-FEC|assembly with|0x04||
|||||||||BER<1.0e-6|||
|||||||||Active Cable|||
||5||4 x 200GBASE-R|2x 200GAUI-1-S C2M|0x4D|4x 200G|RS-FEC|assembly with|0x03||
|||||||||BER<2.6e-4|||
|||||||||Active Cable|||
||6||2x 200GBASE-R|2x 200GAUI-4 C2M|0x0F|2x 200G|RS-FEC|assembly with|0x04||
|||||||||BER<1.0e-6|||
|||||||||Active Cable|||
||7||2x 100GBASE-R|2x 100GAUI-2 C2M|0x0D|2x 100G|RS-FEC|assembly with|0x04||
|||||||||BER<1.0e-6|||
|||||||||Active Cable|||
||8||8 x 50GBASE-R|8x 50GAUI-1 C2M|0x4F|8x 50G|RS-FEC|assembly with|0x02||
|||||||||BER<1.0e-6|||



## 



Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.2 

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
||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)||
|Power consumption|Worst case power consumption. Will vary over temperature.||
|Transmitter Output power|Average output power. Provided in min and max values.||
|Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
|Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
|DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

