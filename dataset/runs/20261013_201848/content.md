
## **160-9116-900-C** 

Ciena® 160-9116-900 Compatible 10GBase-SR SFP+ Transceiver (MMF, 850nm, 300m, LC, DOM) 

## **Features:** 

- SFF-8432 and SFF-8472 Compliance 

- Duplex LC Connector 

- VCSEL transmitter and PIN receiver 

- Multi-mode Fiber 

- Commercial Temperature 0 to 70 Celsius 

- Hot Pluggable 

- Metal with Lower EMI 

- Excellent ESD Protection 

- RoHS Compliant and Lead Free 


## **Applications:** 

- 10GBase-SR Ethernet 

- 8x/10x Fibre Channel 

- Access, Datacenter and Enterprise 

- Mobile Fronthaul CPRI/OBSAI 

## **Product Description** 

This Ciena® 160-9116-900 compatible SFP+ transceiver provides 10GBase-SR throughput up to 300m over multi-mode fiber (MMF) using a wavelength of 850nm via an LC connector. Our transceiver is built to meet or exceed OEM specifications and is guaranteed to be 100% compatible with Ciena®. It has been programmed, uniquely serialized, and tested for data-traffic and application to ensure that it will initialize and perform identically. All of our transceivers comply with Multi-Source Agreement (MSA) standards to provide seamless network integration. Additional product features include Digital Optical Monitoring (DOM) support which allows access to real-time operating parameters. We stand behind the quality of our products and proudly offer a limited lifetime warranty. 

## ProLabs’ transceivers are RoHS compliant and lead-free. 

TAA refers to the Trade Agreements Act (19 U.S.C. & 2501-2581), which is intended to foster fair and open international trade. TAA requires that the U.S. Government may acquire only "U.S.-made or designated country end products.") 


**Rev. 011926** 

## **Absolute Maximum Ratings** 

|**Parameter**|**Symbol**|**Min.**|**Max.**|**Unit**|
|---|---|---|---|---|
|**Maximum Supply Voltage**|Vcc|-0.5|4.0|V|
|**Storage Temperature**|TS|-40|85|°C|
|**Operating Case Temperature**|Tc|0|70|°C|
|**Operating Humidity**|RH|5|85|%|
|**Receiver Power**|RMAX||-1|dBm|
|**Maximum Bitrate**|Bmax||11.3|Gbps|



## **Electrical Characteristics** (TOP=25°C, Vcc=3.3Volts) 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|**Power Supply Voltage**|Vcc|3.15|3.30|3.43|V||
|**Power Supply Current**|Icc|||303|mA||
|**Power Consumption**|PDISS|||1|W||
|**Transmitter**|||||||
||||||||
|**Differential data input swing**|Vin,pp|120||850|mV||
|**Input differential impedance**|Zin|80|100|120|Ω||
|**Receiver**|||||||
||||||||
|**Differential data output swing**|Vout, pp|300||850|mV||
|**Output differential impedance**|Zin|80|100|120|Ω||



## **Optical Characteristics** 

|**Parameter**|**Symbol**|**Min.**|**Typ.**|**Max.**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|**Transmitter**|||||||
||||||||
|**Optical Power (average)**|PAVE|-7.3||-1.2|dBm|1|
|**Optical Modulation amplitude (OMA)**|POMA|-1.5|||dBm|2|
|**Optical Extinction Ratio**|ER|3|||dB||
|**Optical Wavelength**|Tλ|840|850|860|nm||
|**Insertion loss**|IL||2||||
|**Receiver**|||||||
||||||||
|**Receiver Sensitivity (average)**|RAVE|||-9.9|dBm|3|
|**Receiver Sensitivity (OMA)**|ROMA|||-11.1||2|
|**Receiver overload**|Pmax|-1|||dBm|4|
|**Receiver wavelength**|Rλ|840||860|nm||



## **Notes:** 

1. Coupled into a Multi-mode fibre 

2. Per IEEE 802.3ae specification 

3. Average power, back-to-back, @10.31Gbps, BER 1E-12, PRBS 231-1. 

4. Exceeding the Receiver overload can physically damage the module. Please use appropriate attenuation. 

## **Pin Descriptions** 

|**Pin**|**Symbol**|**Name/Descriptions**|**Ref.**|
|---|---|---|---|
|**1**|VeeT|Transmitter Ground (Common with Receiver Ground).|1|
|**2**|TX Fault|Transmitter Fault. LVTTL-O|2|
|**3**|TX Disable|Transmitter Disable. Laser output disabled on high or open. LVTT-I.|3|
|**4**|SDA|2-Wire Serial Interface Data Line (Same as MOD-DEF2 in INF-8074i). LVTTL-<br>I/O.||
|**5**|SCL|2-Wire Serial Interface Data Line (Same as MOD-DEF2 in INF-8074i). LVTTL-I.||
|**6**|MOD_ABS|Module Absent, Connect to VeeT or VeeR in Module.|4|
|**7**|RS0|Rate Select 0. Not used|5|
|**8**|LOS|Loss of Signal indication. Logic 0 indicates normal operation. LVTTL-O.|2|
|**9**|RS1|Rate Select 1. Not used|5|
|**10**|VeeR|Receiver Ground (Common with Transmitter Ground).|1|
|**11**|VeeR|Receiver Ground (Common with Transmitter Ground).|1|
|**12**|RD-|Receiver Inverted DATA out. AC Coupled. CML-O.||
|**13**|RD+|Receiver Non-inverted DATA out. AC Coupled. CML-O.||
|**14**|VeeR|Receiver Ground (Common with Transmitter Ground).|1|
|**15**|VccR|Receiver Power Supply.||
|**16**|VccT|Transmitter Power Supply.||
|**17**|VeeT|Transmitter Ground (Common with Receiver Ground).|1|
|**18**|TD+|Transmitter Non-Inverted DATA in. AC Coupled. CML-I.||
|**19**|TD-|Transmitter Inverted DATA in. AC Coupled. CML-O.||
|**20**|VeeT|Transmitter Ground (Common with Receiver Ground).|1|



## **Notes:** 

1. The module signal ground contacts, VeeR and VeeT, should be isolated from the module case. 

2. This contact is an open collector/drain output and should be pulled up to the Vcc_Host with resister in the range 4.7KΩ to 10KΩ. Pull ups can be connected to one or several power supplies, however the host board design shall ensure that no module contract has voltage exceeding module VccT/R +0.5.V. 

3. Tx_Disable is an input contact with a 4.7KΩ to 10KΩ pull-up resistor to VccT inside module. 

4. Mod_ABS is connected to VeeT or VeeR in the SFP+ module. The host may pull the contract up to Vcc_Host with a resistor in the range from 4.7KΩ to 10KΩ. Mod_ABS is asserted “High” when the SFP+ module is physically absent from a host slot. 

5. Internally pulled down per SFF-8431 


Pin-out of connector Block on Host board 

## **Recommended Circuit Schematic** 


## **Mechanical Specifications** 

Small Form Factor Pluggable (SFP) transceivers are compatible with the dimensions defined by the SFP MultiSourcing Agreement (MSA). 


## **EEPROM Information** 

EEPROM memory map specific data field description is as below: 


## **About ProLabs** 

Our extensive experience comes as standard. For over 20 years ProLabs has delivered optical connectivity solutions that give our customers freedom and choice through our ability to provide seamless interoperability. At the heart of our company is the ability to provide state-of-the-art optical transport and connectivity solutions that are compatible with more than 100 optical switching and transport platforms. 

## **A Complete Portfolio of Network Solutions** 

ProLabs is focused on innovations in optical transport and connectivity. The combination of our knowledge of optics and networking equipment enables ProLabs to be your single source for optical transport and connectivity solutions from 100Mb to 1.6T while providing innovative solutions that increase network efficiency. We provide the optical connectivity expertise that is compatible with and enhances your switching and transport equipment. 

## **The Trusted Partner** 

Customer service is our number one value. ProLabs has invested in people, labs and manufacturing capacity to ensure compatible products, and immediate answers to your questions. With Engineering and Manufacturing offices in the U.K. and U.S. augmented by field offices throughout the U.S., U.K. and Asia, ProLabs is able to be our customers best advocate 24 hours a day. 


## **Contact Information** 

ProLabs US 

Email: sales@prolabs.com Telephone:  952-852-0252 

ProLabs UK 

Email: salessupport@prolabs.com Telephone: +44 1285 719 600 

