
Nokia Coherent Module 6 (CHM6) – The Industry’s Best-performing 800G Xponder Lower the Cost per Bit per km, Power, and Footprint of 100 GbE, 400 GbE, and OTU4 Services 

## Leveraging Industry-leading Optical Engine Technology 

Nokia’s Coherent Module 6 (CHM6) coherent channel module leverages Infinite Capacity Engine 6 (ICE6) high-performance coherent optics, the sixth generation of Nokia‘s vertically integrated optical engines, and combines 2 x 800 Gb/s wavelengths with 16 client ports into a single module providing up to 1.6T of line capacity and up to 1.6T of client capacity. The CHM6 is designed to be operated over Nokia or thirdparty line systems, and with the flexibility to tune its baud rate from 31 to 100+ Gbaud with 400+ supported line modes, the CHM6 can be deployed in both fixed-grid and flexible-grid networks. 

Each of its two carriers can be arbitrarily tuned with 0.05 GHz granularity to any frequency within the extended C-band or the extended L-band to support more than 80 Tb/s of capacity over a single fiber pair. The CHM6 utilizes methods such as second-generation Nyquist subcarriers, long-codeword probabilistic constellation shaping (LC-PCS), dynamic bandwidth allocation (DBA), high-gain soft decision-forward error correction (SD-FEC), and SD-FEC gain sharing to maximize capacity-reach and spectral efficiency/fiber capacity in any network scenario. The CHM6 supports flexible transport of 100 GbE, 400 GbE, and OTU4 clients and is deployed within the Nokia 1830 Global Express (GX) G42 compact modular transport platform with total power consumption of around 0.2 W/G/s. In addition, 10 GbE, OTU2, OTU2e, and OC192/ STM64 services can be supported utilizing the 1830 GX G42’s UCM4 sled. 

## Benefits of the CHM6 

- Maximize spectral efficiency and wavelength capacity-reach with industry-leading ICE6 optical engine technology 

- Optimize performance in metro, DCI, long-haul, and subsea scenarios with over 400 supported line modes, specialized subsea capabilities, and advanced features for challenging terrestrial conditions 

- Deliver 100 GbE, OTU4, and 400 GbE client services cost-effectively with bandwidth visualization over two wavelengths and fully flexible client-toline mapping 

- Protect your services with resiliency mechanisms including SNCP and Y-cable and with wire-speed AES-256 encryption 

- Minimize operational costs with integrated PRBS test and loopback, ZTP, and automation tools leveraging RESTCONF/NETCONF open APIs, OpenConfig/YANG data models, and gRPC streaming telemetry 

- Deploy the CHM6 over a wide variety of Nokia and third-party optical line systems, leveraging its tuneable baud rate and transmit power 


Figure 1: CHM6 sled with two line interfaces and 16 clients 

The Nokia CHM6 is built with Nokia’s ICE6 advanced optical engine technology leveraging a 7-nm CMOS process node digital ASIC/DSP, a highly integrated indium phosphide (InP) photonic integrated circuit (PIC), high-performance analog electronics, and advanced packaging. ICE6 benefits from holistic co-design, with all the components and packaging designed in-house. This enables high modem signal-tonoise ratio (SNR), minimizing the noise and distortions inside the optical engine, which is a key enabler for market-leading 800 Gb/s performance. 


Nokia 1830 GX G42 with redundant controllers and 4 x CHM6 sleds 

The images shown are for illustration purposes only and may not be an exact representation of the product. 

Data sheet 

Nokia Coherent Module 6 (CHM6) – The Industry’s Best-performing 800G Xponder 



Figure 2: ICE6 industry-leading optical engine technology 

The CHM6 supports bandwidth virtualization, shown in Figure 3, which enables highly flexible mapping of client interface to line interface. Bandwidth virtualization provides operators the freedom and flexibility of client service mapping and enables very cost-efficient transport networking deployment. For example, three 400 GbE client services can be transported over two 600 Gb/s line interfaces on a single CHM6 module. This feature is also a key enabler for delivering 400 GbE services over networks that are not able to support a single 400G+ wavelength. 


Figure 3: CHM6 bandwidth virtualization 

The CHM6 sled is ideally suited to support the current growth of 400 GbE service demands and can support up to 4 x 400 GbE services on a single sled, as well as any mix of 100 GbE and 400 GbE services in high-speed networking connectivity applications, including data center interconnect (DCI). A few example configurations: 


Figure 4: Example Configurations 

Data sheet 

2 

Nokia Coherent Module 6 (CHM6) – The Industry’s Best-performing 800G Xponder 


## 1830 GX G42 CHM6 in Terrestrial Networks 

Leveraging ultra-high baud rates of up to 100+ Gbaud, high modem SNR, and advanced features including LC-PCS and Nyquist subcarriers, the CHM6 has been able to deliver stellar performance under favorable terrestrial conditions. Wavelength distances can exceed 1,000 km at 800 Gb/s per wavelength, 3,000 km at 600 Gb/s per wavelength, and 7,500 km at 400 Gb/s per wavelength. 

With the ability to select from over 400 line modes, the CHM6 can also maximize performance under more challenging terrestrial conditions, such as high-loss spans, G.655 fiber with low chromatic dispersion, high ROADM cascades, and aerial fiber in regions prone to frequent lightning strikes. Specialized features for challenging terrestrial conditions include a high-gain 33% overhead FEC option, SDFEC gain sharing, a tight roll-off, DBA, PDL mitigation, and high state-of-polarization (SOP) rotation tolerance of up to 6+ Mrad/s. 

## 1830 GX G42 CHM6 in Subsea Networks 

The CHM6 also provides a comprehensive toolkit for submarine applications. These tools include tuneable ultra-high baud rates, LC-PCS with a super-Gaussian PCS distribution option, Nyquist subcarriers, specialized 4D and 8D modulations, SD-FEC gain sharing, extensive programmability including 400+ line modes, bandwidth virtualization, PDL mitigation, and multiple additional features that help to maximize spectral efficiency. Submarine network operators can pick and mix from this toolkit to maximize performance for any submarine cable type, including dispersion managed, uncompensated, SDM, and unrepeatered/festoon. 

## Protection Options 

The CHM6 module supports Y-cable client layer protection, providing resiliency options that can address client interface failures, line interface failures, CHM6 module failures, and fiber cuts. The client signal is split and sent to two line interface ports. At the other end, the CHM6, or two CHM6s paired via the backplane, forwards the best signal to the client, with a protection switching time of under 50 ms, as shown below. Both revertive and non-revertive modes are supported. 


Figure 5: CHM6 protection options 

Leveraging an optical protection switch in the line system, such as the OPSW-2 in the Nokia 1830 Flexible Intelligent Line System (FlexILS), the CHM6 can also support cost-effective line interface (OCh) protection with 50-ms switching times even with colorless add/ drop. The CHM6 also supports client layer protection and SNCP, where a single client signal is sent across two different line interface wavelengths (λ1 and λ2) within the same CHM6. 

Data sheet 

3 

Nokia Coherent Module 6 (CHM6) – The Industry’s Best-performing 800G Xponder 


## Pseudorandom Binary Sequence Testing 

A pseudorandom binary sequence (PRBS) test is an IEEE 802.3 82.2.11 standard feature. It provides a test signal to verify link quality and error-free traffic flow of network links. PRBS simplifies turn-up and commissioning procedures and is valuable for troubleshooting purposes. Nokia’s 1830 GX G42 CHM6 provides comprehensive end-to-end testing of the entire signal path from the client system to the remote client system and back via the CHM6’s built-in PRBS tester. Testing can be executed completely from end to end or stepwise to verify each connectivity segment. 


Figure 6: PRBS test and loopback 

## Security and Encryption 

The 1830 GX G42 and CHM6 provide comprehensive security mechanisms, including access management through local authentication, authorization, and accounting (AAA) and remote authentication, which includes RADIUS and TACACS+ protocols, Secure Shell (SSH v2) protection of management traffic secure protocols, and NTP server authentication to prevent the tampering of timestamps. Furthermore, the solution supports secure boot with signed images to provide integrity and authenticity of the 1830 GX COS software during software downloads and system boot-up via Nokia digital signatures based on ECDSA-P521 and SHA2-512 algorithms. The 1830 GX G42 and CHM6 support integrated AES-256-GCM in-flight encryption with hitless key rotation and Elliptic-curve Diffie-Hellman key exchange and are currently being FIPS140-3 Level 2 certified. 

## Automation Enabled by Open APIs and Streaming Telemetry 

The 1830 GX G40 Series and CHM6 support management, automation, and streaming telemetry via open interfaces. Both the 1830 GX G42 chassis and the CHM6 sled support WebGUI, CLI, SNMP, TACACS+, syslog, OpenConfig YANG-modeled NETCONF and RESTCONF APIs, and gNMI/gRPC streaming telemetry. In-band management is supported via GCC0 on the line interfaces, out-of-band management via Ethernet interfaces, and commissioning via the 1830 GX G42’s console interface. An OSPF-based DCN is supported. Additional manageability features include zero-touch commissioning, RMON, LLDP, and PRBS test generation and loopbacks. The 1830 GX G40 Series is supported under Nokia’s Transcend Network Management System and Transcend Controller. 

Data sheet 

4 

Nokia Coherent Module 6 (CHM6) – The Industry’s Best-performing 800G Xponder 


## Technical Specifications 

## **Applications** 

- Transponder 

- Ethernet transponder 

- OTN transponder 

- Muxponder 

- OTN muxponder 

- Ethernet muxponder 

- Mix of 100G and 400G service transport 

- OEO 3R regenerator (including regen without clients) 

- Add/drop multiplexer (ADM) 

- Client hairpin 

## **Physical Interface** 

- 2 x embedded line interfaces 

- 16 x pluggable client interfaces 

## **Line Interfaces** 

- Data rate tuneability: 100 Gb/s to 800 Gb/s in 50G increments 

- Baud rate tuneability: 31 to 96 Gbaud (ICE6)/100.4 Gbaud (ICE6 Turbo) 

- C-band tuneability: 191.325 THz to 196.125 THz (CHM6) 

- L-band tuneability: 186.05 THz to 191.050 THz (CHM6L) 

- TX optical output power: -6 dBm to +9 dBm 

- Modulation options: 

- Probabilistic constellation shaping (PCS) 

- 64QAM 

- Long codeword (LC-PCS) 

- 12 to 4 bits per symbol 

- Gaussian and super-Gaussian distribution options 

- Conventional modulation: 64QAM, 32QAM, 16QAM, 8QAM, QPSK 

- Time-domain hybrid modulation (e.g., 64/32QAM, 4/3QAM) 

- Specialized 4D/8D modulation formats for dispersion-managed subsea 

- High-gain soft-decision forward error correction (SD-FEC) with 20% or 33% overhead options 

- Second-generation Nyquist subcarriers (8 subcarriers per wave) 

- Dynamic bandwidth allocation (persubcarrier PCS) 

- SD-FEC gain sharing (over two waves) 

- Bandwidth virtualization over two wavelengths (e.g., 3 x 400 GbE over 2 x 600G wavelengths) 

- Chromatic dispersion tolerance: 150,000 ps/nm to 400,000 ps/nm (depending on line mode) 

- Max DGD: ~100-160 ps (depending on line mode) 

- SOP rotation tolerance: up to 6 Mrad/s (depending on line mode) 

- Interworking with 1830 FlexILS, 1830 GX G30, 1830 Express Transport Metro (XTM) Series, 7300 multi-haul transport platform, and third-party line systems 

## **Client Interfaces** 

- 8 x QSFP28 

- 4 x QSFP28/56 

- 4 x QSFP28/56/DD 

- 400G: AOC, FR4, SR8, LR4, DR4, SR4.2, DAC, XDR4 

- 100G: LR4, FR1, SR4, CWDM4, DR, ER, CR4, LR1, ER4 

## **Operational Features** 

- Performance monitoring: line interfaces • Chromatic dispersion (CD) 

- Differential group delay (DGD) 

- Polarization-dependent loss (PDL) 

- Q-factor 

- Pre-FEC BER 

- Post-FEC errors 

- Latency 

- SNR 

- OSNR 

- Channel power 

- Wavelength 

- OTU-level PM 

- Performance monitoring: client interfaces 

- Physical coding sublayer: errors 

- PHY: FEC, BER, synch 

- MAC: packets, errors, CRC 

- OTN: FEC, errors, synch 

- Zero-touch provisioning (ZTP) 

- PRBS test and loopback (facility and terminal loopbacks ) 

- LLDP snooping on each 400 GbE/100 GbE client port 

- RMON and test signal 

- TCM 

## **Management** 

- Management and control platforms: 

- Nokia Transcend Controller 

- Nokia Transcend Network Management System 

- Command line interface 

- Zero-touch commissioning 

- Syslog 

- SNMP, WebGUI 

- NETCONF 

- RESTCONF 

- Native YANG data models 

- OpenConfig 

- gNMI/gRPC 

- SNMP fault and performance management 

- Generic Communication Channel (GCC0) in-band management on the line port OTUk 

- OSPF-based DCN 

## **Protection** 

- Y-cable 

- SNCP 

- 50-ms OCh protection 

- Including coherent colorless add/ drop 

- With line system optical protection switch 

## **Security** 

- Wire-speed ODUk AES-256 encryption for 100G and 400G clients 

- TACACS+ 

- RADIUS 

- SSH v2 

- Secure boot 

Data sheet 

5 

Nokia Coherent Module 6 (CHM6) – The Industry’s Best-performing 800G Xponder 


## Technical Specifications 

## **Environmental** 

- Power dissipation: 213 to 445 W depending on configuration 

- Operating temperature: -5° C to 55° C/23° F to 131° F 

- Transport and storage: -40° C to 70° C/-40°F to 158° F/40° C + 93% RH 

- Humidity: 5% to 93% maximum 

## **Regulatory and Compliance** 

- RoHS-6 compliant and lead-free per Directive 2002/95/EC 

- GR-3160-Core Generic Requirements for Telecommunications Data Center Equipment and Spaces 

- Telcordia GR-326-Core Generic Requirements for Single-Mode Optical Connectors and Jumper Assemblies 

- Telcordia GR-1435-Core Generic Requirements for Multi-Fiber Optical Connectors 

- Emissions: FCC Part 15 Class A, EN55022/CISPR Class A Compliant, CE Laser Safety: ANSI Class 1M, IEC Class 1M, EN 60825-1/2, 21 CFR 1040 US FDA CDR, Class 1 

- Electrical safety: UL 60950, CSA22.2 60950 and IEC 60950 

## **About Nokia** 

At Nokia, we create technology that helps the world act together. 

As a B2B technology innovation leader, we are pioneering networks that sense, think and act by leveraging our work across mobile, fixed and cloud networks. In addition, we create value with intellectual property and long-term research, led by the award-winning Nokia Bell Labs. 

With truly open architectures that seamlessly integrate into any ecosystem, our high-performance networks create new opportunities for monetization and scale. Service providers, enterprises and partners worldwide trust Nokia to deliver secure, reliable and sustainable networks today – and work with us to create the digital services and applications of the future. 

© 2025 Nokia 

Nokia OYJ 

Karakaari 7 02610 Espoo Finland 

Tel. +358 (0) 10 44 88 000 

Document code: (March) CID214588 

