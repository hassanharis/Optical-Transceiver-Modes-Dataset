DATASHEET 

6.0 

## **TQD014-TUNC-SO** 

QSFP-DD, OpenZR+, Coh Tunable, High-power, CMIS5.1, LC 

## OVERVIEW 

The TQD014-TUNC-SO is an QSFP-DD form-factor (type 2a) DWDM transceiver conforming to the OpenZR+ MSA for 100Gbps to 400Gbps Ethernet application as well as the application 100GBASE-ZR. 

The output power of 0dBm unlocks the potential for the module to transmit 400G signals in already existing, 100GHz spacing, ROADM architectures. 

The OpenZR+ MSA provides a flexible solution for operators having routers that not yet have migrated to 400G services. The TQD014-TUNC-SO can as an example be used in the Smartoptics DCP-404 Muxponder to combine up to 4x 100G flows to a 100G/200G/300G/400G OpenZR+ signal to be transported over an optical network. 


The below table lists the OIF 400ZR and OpenZR+ modes supported by TQD014-TUNC-SO. 

|**CMIS**<br>**Application**<br>**Code**|<br>**Host format**|**Electrical interface**|**Payload**|**FEC**|**Modulation**|<br>**Line Symbol**<br>**Baud Rate**|**MSA format**||
|---|---|---|---|---|---|---|---|---|
|1|400GBASE-R|1x 400GAUI-8 (8x 50G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA||
|2|4x 100GBASE-R|4x 100GAUI-2 (2x 50G)|400G|oFEC|DP-16QAM|60.1GBd|OpenZR+ MSA||
|3|3x 100GBASE-R|3x 100GAUI-2 (2x 50G)|300G|oFEC|DP-8QAM|60.1GBd|OpenZR+ MSA||
|4|2x 100GBASE-R|2x 100GAUI-2 (2x 50G)|200G|oFEC|DP-QPSK|60.1GBd|OpenZR+ MSA||
|5|100GBASE-R|1x 100GAUI-2 (2x 50G)|100G|oFEC|DP-QPSK|30.0GBd|OpenZR+ MSA||
|6|100GBASE-R|1x 100GAUI-2 (2x 50G)|100G|SC-FEC|DP-QPSK|30.0GBd|100GBASE-ZR||




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.0 

## TECHNICAL DATA 

The optical characteristics are into Generic and Application code sections. The _Generic_ section defines the common characteristics, independent of the selected application modes. The _Application_ code section defines application code based optical characteristics. 

The performance is compliant with the respective specifications but can exceed the minimum requirements on some parameters. 

## GENERIC 

|GENERIC||||
|---|---|---|---|
|**Parameter**|**Value**<br>DWDM QSFP-DD type 2a<br>SM (2x LC)<br>191.3 - 196.1THz (tunable) 6.25GHz<br>OpenZR+, 100GBASE-ZR<br>-5OC to +75OC<br>-40OC to +85OC<br>Total received power<br>Coherent channel power<br>OSNR, eSNR, PDL, dispersion, DGD<br>Case temperature|**Parameter**|**Value**|
|Technology||MSA|QSFP-DD MSA’s, CMIS5.1, C-CMIS1.2|
|Transmission media||Power consumption|< 22.5W|
|Nominal wavelengths||Tx Power, configurable range|-6 to +1dBm|
|Interface standards||Tx In-band OSNR|Min 43dB/0.1nm|
|Operating temperature||Tx Out-Of-Band OSNR|Min 40dB/0.1nm|
|Storage temperature||Receiver turn-up|Max 100ms from warm start|
|DDM functions|||Max 150s from cold start|
|||Absolute max conditions|Rx signal input power: +3dBm|
||||Rx total input power: +13dBm|
|||||



**Safety/regulatory compliance:** TUV/UL/FDA (contact Smartoptics for latest certification information) RoHS compliance 


Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.0 

## OPTICAL SPECIFICATION - APPLICATION CODES 

The table below lists the primary optical parameters for each supported application code. 

|**Appl**<br>**mode**|**Line**<br>**rate**|**Host format**|**Tx Power1)**|**Rx sens**<br>**@ OSNR >35dB**|<br>**Rx**<br>**@ OSNR**|**CDC range**<br>**@0.5dB OSNR**<br>**penalty**|
|---|---|---|---|---|---|---|
|1|400G|1x 400GAUI-8|0dBm|-23dBm|23.5dB@-12dBm|12 000 ps/nm|
|2|400G|4x 100GAUI-2|0dBm|-23dBm|23.5dB@-12dBm|12 000 ps/nm|
|3|300G|3x 100GAUI-2|0dBm|-26dBm|20.0dB@-12dBm|18 000 ps/nm|
|4|200G|2x 100GAUI-2|0dBm|-30dBm|15.0dB@-12dBm|24 000 ps/nm|
|5|100G|1x 100GAUI-2|0dBm|-32dBm|12.0dB@-12dBm|48 000 ps/nm|
|6|100G|1x 100GAUI-2|0dBm|--28dBm|15.0dB@-12dBm|40 000 ps/nm|



1) The module transmit power can be provisioned up to the maximum available TX power. 

## ORDERING INFORMATION 

|**Ordering code**|**Item Name**|
|---|---|
|TQD014-TUNC-SO|QSFP-DD OpenZR+ HPow Coh-T SM CMIS5.1|




Subject to change without notice. For more information visit smartoptics.com. 

DATASHEET 

6.0 

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

