Data Classification: Confidential DATASHEET 

6.1 

## **QSFP-DD 400G DAC PASSIVE, CMIS 4.0** 

QSFP-DD to QSFP-DD Direct Attach Cable (DAC), 400G Ethernet, 0.5-2.5m, passive 

## DQD003-xxxC-SO 

The DQD003-xxxC-SO is an active Direct Attach Cable (DAC) solution of Twinax type, i.e. a copper cable similar to coaxial cable, but with two inner conductors instead of one. DQD003-xxxC-SO is a solution for 400Gbps connections within racks and across adjacent racks where the interconnected equipment uses QSFP-DD interfaces. It provides a cost-efficient solution as compared to using optical transceivers and it simplifies the patching since no separate transmit/receive direction has to be taken into account. 

The electrical interface of the module is compliant with the electrical interfaces 4x100GAUI-2 and 400GAUI-8 as well as the QSFPDD MSA. 

DQD003-xxxC-SO integrates eight data lanes (25Gbd) in each direction using PAM4 modulation with 400Gbps aggregate bandwidth. 

The DQD003-xxxC-SO cables have an I2C interface with Integrated Digital Diagnostic Monitoring according to the Common Management Interface Specification CMIS 4.0. 

The DQD003-xxxC-SO is provided in lengths from 0.5 to 2.5 meters (1.6 to 8.2 ft). 

## PRODUCT FEATURES 

- QSFP-DD to QSFP-DD 400G connectivity 

- 8x 26.5625GBd (PAM4) Electrical Interface (400GAUI-8) 

- Digital diagnostics functions via the I2C interface CMIS 4.0 

- 0.5 to 2.5 meters (1.6 to 8.2ft) 

- AWG26/30 (cable thickness) 

- Operating temperature 0[o] C to +70[o] C (32°F to +158°F) 

- Storage temperature -40[o] C to +85[o] C (-40°F to +185°F) 

## APPLICATIONS 

- Data Center cabling infrastructure 

- Storage Area Network (SAN) 

- Network Attached Storage (NAS) 

- Hub, switches, routers, servers 

## ORDERING INFORMATION 

||**Parameter**|**Value**||||
|---|---|---|---|---|---|
||DQD003-0M5C-SO|QSFP-DD to QSFP-DD Direct Attach Cable (DAC),|400G Ethernet, AWG30,|0.5m, passive||
||DQD003-001C-SO|QSFP-DD to QSFP-DD Direct Attach Cable (DAC),|400G Ethernet, AWG30,|1m, passive||
||DQD003-1M5C-SO|QSFP-DD to QSFP-DD Direct Attach Cable (DAC),|400G Ethernet, AWG30,|1.5m, passive||
||DQD003-002C-SO|QSFP-DD to QSFP-DD Direct Attach Cable (DAC),|400G Ethernet, AWG26,|2m, passive||
||DQD003-2M5C-SO|QSFP-DD to QSFP-DD Direct Attach Cable (DAC),|400G Ethernet, AWG26,|2.5m, passive||




Subject to change without notice. For more information visit smartoptics.com. 

Data Classification: Confidential DATASHEET 

6.1 

## APPLICATION CODE LIST 

||**CMIS Application Code**|**Host format**|**Electrical interface**|**Payload**|**FEC**||
|---|---|---|---|---|---|---|
||1|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|RS-FEC1)||
||2|2x 100GBASE-R|2x 100GBASE-CR4 (Clause 136) (4x25G)|200G|RS-FEC1)||
||3|2x 100GBASE-R|2x 100GBASE-CR4 (Clause 92) (4x25G)|200G|RS-FEC1)||
||4|8x 50GBASE-R|8x 50GBASE-CR (Clause 126) (1x50G)|200G|RS-FEC1)||
||5|IB HDR|IB HDR (Arch.Spec.Vol.2)|400G|RS-FEC1)||
||6|8x 25GBASE-R|25GBASE-CR CA-25G-L (Clause 110) (1x25G)|400G|RS-FEC1)||
||7|IB EDR|IB EDR (Arch.Spec.Vol.2)|400G|RS-FEC1)||
||8|4 x 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|RS-FEC1)||



- 1) FEC is provided by the host. 

## 


## GENERAL DEFINITIONS 

||**Parameter**|**Description**||
|---|---|---|---|
|||Grey; Transceiver type for non-WDM applications. Electrical or optical.||
|||CWDM; Transceiver type for CWDM applications using G.694.2 channel grid.||
||Technology|DWDM; Transceiver type for DWDM applications using G.694.1 channel grid.<br>BiDi; Transceiver pair using two different wavelength channels operating on a single-fiber.||
|||DAC: Direct Attach Cable. Electrical cable with attached connectors.||
|||AOC: Active Optical Cable. Optical cable with attached connectors.||
||Transmission Media|Type of fiber, e.g. Multimode (MM) or Singlemode (SM). Number of and connector type within brackets (e.g. 2x LC, 1x MPO).||
||Typical reach|Nominal distance performance based on typical fiber dispersion, fiber loss and power budget properties, i.e. w/o dispersion<br>compensation and optical amplification. Actual distance is dependent on actual optical path loss and dispersion properties.||
||Bit rate range|Supported bit rate range in Gigabit or Megabit per second (Gbps or Mbps).||
||Protocols|Protocols within supported bit rate range.||
||Nominal wavelength|Typical wavelength(s) from transmitter.||
||Interface standards|Referenced interface standards or MSA’s, e.g. IEEE 802.3 standard for 10GbE services or 100G 4WDM-10 etc.||
||Power budget|Min and max power budget between Transmitter and Receiver w/o optical path penalties.||
||Dispersion tolerance/penalty|Maximum amount of tolerated dispersion and required reduction of power budget to maintain stipulated Bit Error Rate (BER) and at<br>a given bit rate.||
|||Max operating case temperature range.||
||Temperature range|Standard temperature range (C-temp): 0°C to +70°C (32°F to +158°F)<br>Extended temperature range (E-temp): typically -20°C to +75°C (-4°F to +167°F)||
|||Industrial temperature range (I-temp):-40°C to+85°C (-40°F to+185°F)||
||Power consumption|Worst case power consumption. Will vary over temperature.||
||Transmitter Output power|Average output power. Provided in min and max values.||
||Receiver minimum input power|Minimum average input power at specified BER, normally 1E-12. Note that some protocols require FEC to achieve sufficient BER.||
||Receiver max input power|Maximum average input power giving a BER, normally 1E-12.||
||DDM|Digital Diagnostic Monitoring functionality as defined in e.g. SFF-8472 MSA.||



Smartoptics makes no warranties or representations, expressed or implied, of any kind relative to the information or any portion thereof contained in this document or its adaptation or use, and assumes no responsibility or liability of any kind, including, but not limited to, indirect, special, consequential or incidental damages, for any errors or inaccuracies contained in the information or arising from the adaptation or use of the information or any portion thereof. The information in this document is subject to change without notice. 


Subject to change without notice. For more information visit smartoptics.com. 

