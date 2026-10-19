DATASHEET 

5.3 

## **SO-SFP-1000BASE-TX & -TX-I** 

SFP, 10/100/1000Base-T SERDES/SGMII Interface, 100m, RJ45 

## OVERVIEW 

The SO-SFP-1000BASE-TX is a transceiver with a high-performance integrated duplex data link for bidirectional communication over copper cable. It is specifically designed for high speed communication links that require 1Gbps Ethernet (GbE) over LAN cable. 

SO-SFP-1000BASE-T supports 10/100/1000BASE-T Operation in Host Systems with SGMII interface. SGMII is a serial connection bus for Ethernet MACs and PHYs defined by Cisco Systems. SGMII runs its physical layer at 1.25Gb/s, 8B10B encoded at all times, regardless of the negotiated data rate. If the rate is 100Mbps it will repeat the same symbol ten times or one hundred times for 10Mbps. 

This transceiver provides a 2-wire serial interface as defined by the SFF-8472 specification. The transceiver module is compliant to RoHS-6/6. 

The transceiver is available in two temperature range options, one being the Industrial temperature range (I-temp): -40°C to +85°C (-40°F to +185°F). 

## TECHNICAL DATA 

|**Parameter**|**Value**||**Parameter**|**Value**|
|---|---|---|---|---|
|Technology|Grey SFP (copper)||Sync on line side|Preferred slave2)|
|Transmission media|Electrical (1x RJ45)||Auto- negotiation|Yes, SGMII auto-neg|
|Typical reach|100m1)||Rx LOS|No|
|Interface standards|1000BASE-T IEEE 802.3||MSA compliance|SFP MSA|
||100BASE-T IEEE 802.3|||SFF-8472|
||10BASE-T IEEE 802.3||||
|Protocol support|1Gbps Ethernet (GbE)||||
||100Mbps Ethernet (FE)||||
||10Mbps Ethernet||||
|Operating temperature|0°C to +70°C (-TX)||||
||-40°C to +85°C (-TX-I)||||
|Power consumption|< 1.2W||||
|Storage temperature|-40°C to +85°C||||
|1)Using CAT5e cable or better|||||
|2)Slave mode means it uses|the recovered clock from its link partner.||||
|**Safety/regulatory compliance:**|||||
|TUV/UL/FDA (contact Smartoptics for latest certification information)|||||
|RoHS compliance|||||



10/100/1000 BASE-T operation requires an SGMII interface with no clocks in the host system, and the module will operate as 1000BASE-T when the host system uses SERDES interface. It depends on the module PHY configuration 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.3 

## ORDERING INFORMATION 

|**Ordering number**|**Description**|
|---|---|
|SO-SFP-1000Base-TX|SFP, 10/100/1000Base-T SERDES/SGMII Interface, 100m, RJ45|
|SO-SFP-1000Base-TX-I|SFP, 10/100/1000Base-T SERDES/SGMII Interface, 100m, RJ45, I-temp|



## RECOMMENDED SW CONFIGURATION 

SO-SFP-1000BASE-TX supports 10/100/1000Mbps full duplex SGMII interface default. But it also can operate with 1000Mbps of SERDES operation. Please refer the following steps to configure: 

Step 1: Access the PHY at 0Xac via two-wire serial interface. Step 2: Configure 0Xac as below table 

||**Register address**|**Write Data**|**Description**||
|---|---|---|---|---|
||0x16|0x0001|Select page 1||
||0x1B|0x9088|Enable SerDes mode||
||0x00|0x9140|Software reset to allow changes to take effect||
||0x16|0x0000|Select page 0||



SO-SFP-1000BASE-TX operate at mode of “Auto-negotiation enable” by default. But it also can operate with “Auto-negotiation disable”. Please refer the following steps to configure: 

Step 1: Access the PHY at 0Xac via two-wire serial interface. Step 2: Configure 0Xac as below table 

||**Register address**|**Write Data**|**Description**||
|---|---|---|---|---|
||0x16|0x0001h|Select page 1||
||0x00h|0x8140h|Disable Auto-negotiation||
||0x16h|0x0000h|Select page 0||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

5.3 

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

