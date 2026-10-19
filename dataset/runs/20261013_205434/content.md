## **Stratos H2-TR4-Sxxx** 

## **Hybrid Technology Quad Optical Transceiver** 

## Four Ports, 2.125 Gbps, 3.3V, 850nm VCSEL, Multimode, Up to 700M Link Distance 

## Key Features & Benefits 

- Four independent TX and RX ports at 2.125 Gbps each 

- Small footprint 1.00 inch square 

- Low height, less than 0.285 inches max 

- Fiber Flex with custom lengths and termini 

- BGA socket surface mount, no through holes required 

- Removable device (from BGA socket) for IR reflow 

- Industrial temp range, vibration tolerant design 

- SPI control interface for software control and status 

- Control for RX Data Squelch on Loss of Signal 

- Control for TX optical Enable/Disable 

- Status for RX Signal Detect and Signal Strength 

- 3.3V Power, 1.6W max 


Ordering Information H2 - TR4 - Sxxx The –Sxxx suffix represents unique part numbering for fiber route and termini options. See page 22 or consult the factory for details and for custom part numbering for your application. 

## Applications 

The H2-TR4-Sxxx Quad Port Hybrid Transceiver provides a highly ruggedized, small footprint, cost effective solution for 1 to 2.5Gbps multimode optical data links. The device includes an integrated Fiber Flex cable terminated into an industry standard 1x12 MT connector. The device may be customized to have different Fiber Flex lengths, custom fiber flex routing, or use alternate types of fiber termini such as ST, SC, or MIL-T-29504. A complete list is provided in the Ordering Options section of this data sheet. These transceivers are designed to operate for 1x/2x Fiber Channel Links, but can be used for any other data communications purpose within their operating parameters, up to 2.5 Gbps per port. 

## Product Overview 

The Emerson Network Power Connectivity Solutions H2-TR4-Sxxx Quad Port Hybrid Transceiver consists of a VCSEL and PIN Diode Array, Laser Driver, Post Amp circuits, a microcontroller, and integrated fiber flex with MT termination. The electrical signals are routed through a BGA surface mount pin/socket connector to allow easy removal of the entire assembly and to support BGA reflow thermal profiles for ease of PCB assembly. The transmitter accepts four sets of differential data and drives a quad 850nm VCSEL array. The VCSEL drive circuit includes a temperature sensor circuit to 

drive temperature compensation of the optical output level in order to maintain stable output power level over the thermal range. The internal microprocessor provides software control for each individual transmit port for TX Enable/Disable and TX diagnostics. The receiver uses a quad 850nm GaAs PIN array, post amplifier, and outputs four sets of differential data. The internal microprocessor enables software control or read for individual port RX Signal Detect, RX Squelch enable/disable, and Receive Signal Strength Indicators (RSSI). The data interface for the device is a 100  differential pair, 50  impedance per line, and is CML compliant. Individual LVTTL hardware status pins are provided for RX Signal Detect, RX Enable, TX Enable, and TX Fault. The hardware control allows an FPGA or other hardware device to control and monitor the main functions of the Hybrid Transceiver. Software control is provided using a Serial Peripheral Interface (SPI) 4-wire bus. The SPI bus operates in a bit-serial fashion at clock rates up to 2MHz. The internal registers are addressed through a 3 byte read or write sequence. The control and status of the device via software is not required for operation, and is provided purely as an enhancement to operation. The Power Up default SPI register values are all configured for normal operation on all channels, thereby allowing the transceiver’s control pins to configure the device without any SPI activity. 




Please read our datasheet & drawing disclaimer here. 

## Stratos 

## H2-TR4-Sxxx 

## Hybrid Technology Quad Optical Transceiver 

## Ordering Options 

|Part Number|Name|Description|
|---|---|---|
|H2-TR4-SKT-R3|BGASocket|16x16BGAsurfacemount socket,no clip|
|H2-TR4-CLP-R3|BGA Socket with Clip|16x16 BGA surface mount socket with integrated clip|
|H2-TR4-S001|Standard Hybrid Transceiver –<br>Option001|Hybrid Transceiver, 1” fiber length from feedthrough exit, straight fiber<br>route configuration.|
||||
|H2-TR4-S002|Standard Hybrid Transceiver –<br>Option002|Hybrid Transceiver, 6” fiber length from feedthrough exit, straight fiber<br>route configuration.|
||||
|H2-TR4-Sxxx|Hybrid Transceiver|The –Sxxx suffix represents unique part numbering for fiber route and<br>termini options. Consult the factory for details and for custom part<br>numberingforyourapplication.|
||||
|H2-TR4-PULL|Extraction Tool|Tool to aid in removingthe Hybrid Transceiver from the BGA socket.|
|H2-TR4-PIN|PinStraighteningTool|Toolto aidinstraightening the pins oftheHybridTransceiver.|
|H2-TR4-EVAL|HTP EVAL Card|Demonstration and evaluation card, includes support hardware, BGA<br>Socket, and theHybridTransceiver.|
||||



## H2-TR4-Sxxx Hybrid Transceiver Label 


For a complete datasheet, contact your RSM or Duane Teachout at duane.teachout@emerson.com 

## IMPORTANT NOTICE 

Emerson Connectivity Solutions product line, Stratos reserves the right to make changes to or discontinue any optical link product or service identified in this publication, without notice. Stratos recommends that its customers obtain the latest version of the publications to verify, before placing orders, that the information being relied on is current. Stratos warrants performance of its optical link products to current specifications in accordance with the Stratos standard warranty. Testing and other quality control techniques are utilized to the extent that Stratos has determined it to be necessary to support this warranty. Specific testing of all parameters of each optical link product is not necessarily performed on all optical link products. Stratos products are not designed for use in life support appliances, devices, or systems where malfunction of a Stratos International, Inc. product can reasonably be expected to result in a personal injury. Stratos customers using or selling optical link products for use in such applications do so at their own risk and agree to fully indemnify Stratos for any damages resulting from such improper use or sale. Stratos assumes no liability for Stratos applications assistance, customer product design, software performance, or infringement of patents or services described here in. Nor does Stratos warrant or represent that a license, either expressed or implied is granted under any patent right, copyright, or intellectual property right, and makes no representations or warranties that these products are free from patent, copyright, or intellectual property rights. Applications that are described herein for any of the optical link products are for illustrative purposes only. Stratos makes no representation or warranty that such applications will be suitable for the specified use without further testing or modification. 

||Emerson Network Power<br>The leader in enabling<br>Business-Critical Continuity.||AC Power Systems<br> Connectivity<br>DC Power Systems||Embedded Power<br>Inbound Power<br>Integrated Cabinet Solutions||Outside Plant<br>Precision Cooling<br>Site Monitoring and Services||
|---|---|---|---|---|---|---|---|---|
||Emerson Network Power||Emerson Network Power|||Emerson Network Power and the|||
||Connectivity Solutions||Connectivity Solutions|||Network Power logos are|||
||Stratos||USA Headquarters|||service marks of Emerson Electric|||
||1333 Gateway Dr., Ste 107||3000 Lakeside Dr, Ste 308N|||©2011 Emerson Electric|||
||Melbourne, FL 32901||Bannockburn, IL 60015||||||
||For product Information:||For product Information:||||||
||www.EmersonConnectivity.com||call 507.833.8822 or||||||
||or call 321.308.4100||800.247.8256||||||



