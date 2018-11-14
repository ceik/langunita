# The Internet and IP

## Networked Applications & Byte Stream Model

Connectivity: 2 Computers in different parts of the world can connect to each other and exchange data.

Networked applications can exchange data across the world. Most common communication model used for this: `Bidirectional, reliable stream of bytes`, aka `byte stream model`. HTTP is a document-centric example of this: Client send a request by writing to the connection, server reads the request, processes it, writes a response to the connection, and the client then reads the response.

There are more complicated examples that are also based on a bidirectional, reliable bytestreams, like BitTorrent and Sykpe.

Note that this abstracts away the entire network.

## The 4 Layer Internet Model

Source End-Host
===============
| Application |
===============
|  Transport  |
===============
|   Network   |
===============
|     Link    |
===============

4 Layer Internet Model invented so that apps can reuse the same building block. Each layer has a different responsibility and builds a service on top of the one below.

The bidirectional, reliable byte stream is what happens between applications, using all the other layers.

Internet is made up of `end-hosts`, `links`, and `routers`. Data is delivered in packets, hop-by-hop over each link. A `packet` consists of the data and a `header`.

Simple example Packet:

===================================
| Data     | Source | Destination |
===================================


### Link Layer

The link layer is supposed to carry the data one hop at a time.

Ethernet and WiFi are two examples.

### Network Layer

The network layer is supposed to deliver packets end-to-end across the internet from source to destination.

Network layer packets are called datagrams. The data is broken into packets/datagrams in the network layer.

The network layer of the source end-host hands a datagram to the link layer, which then hands it to the router at the end of the first link. The router then examines the destination and is responsible for routing it over the next hop, to the next router. This continues until the network layer at the destination is reached.


Source End-Host                          Dest End-Host
===============                         ===============
| Application |                         | Application |
===============                         ===============
|  Transport  |   Router      Router    |  Transport  |
=============== =========== =========== ===============
|   Network   | | Network | | Network | |   Network   |
=============== =========== =========== ===============
|     Link    | |  Link   | |  Link   | |     Link    |
=============== =========== =========== ===============
       |____________| |________|  |____________|

The Network layer does not know/care how the link layer sends the datagram. This is called `Separation of Concern`. This also means that one network layer has a common way to talk to many different link layers, simply by handing them datagrams. This is possible because each layer has a common, well-defined API to the layer below.

### Internet Protocol

In the case of the internet, the network layer is special. Only the `Internet Protocal` (IP) can be used. It is sometimes referred to as the 'thin waist'.

The IP makes a best-effort attempt to deliver the datagram, but no promises.

IP datagrams can get lost, delivered out of order, or corrupted.

### Transport Layer

The transport layer can use protocols that guarantee that data is redelivered when lost, in the right order, and without corruption. This protocol is called `Transmission Control Portocl` (TCP).

Not all applications need this guarantee though (e.g. video call app). The simpler `User Datagram Protocal` (UDP) can then be used.

### Application Layer

Application typically want a bidirectional, reliable bytestream between two end points. They use their own protocols to communicate with each other. E.g. in the case of http, a GET request is sent directly to the application at the destination as far as the application is concerned. It does not need to know how this happens and instead just hands the request to the TCP layer, which ensures it is delivered.

It is as if each layer is only communication with it's 'peer' layer.

### 7 Layer OSI Model

Old model created by ISO, has been replaced by 4 layer model. It is basically a more granular look at the same model.

Because of this the network layer is sometimes called layer 3, Ethernet as layer 2, and applications as layer 7.

## The Internet Protocol (IP)

The data handed down by the transport layer is in a `transport segment`, which has data and a header. The netwok layer puts the transport segment inside a new `IP datagram` (it becomes the data) and adds a header. IP then sends the datagram to the link layer, which puts it into a `link frame` and ships it off to the first router.

### IP Service Model Properties

Datagram: Individually routed packets (based on the info in its header), hop-by-hop. Datagram header contains destination IP, upon which later routing descision are based.

Unreliable: No guarantee that packets will arrive, on time, or in sequence. They can also be duplicated.

Best Effort: Will only drop packets if necessary. Doesn't even tell source that packet was dropped.

Connectionless: It maintains no state related to a communication. As a result packets might be mis-sequenced.

### IP Model Simplicity

Simpler network can be made to run faster at lower cost and are easier to maintain.

`End-to-end Principle`: Where possible implement features in the end hosts (via software instead of the network hardware). This makes them easier to maintain and evolve.

If the model is simple, a wide variety of reliable or unreliable services can be run on top (e.g. image forcing retransmitting old data for video call applications).

IP makes barely any assumptions about link layer. In fact it was designed to connect many different networks, which is why it is called internet.

### IP Service Model

1. IP tries to catch and delete packets that are stuck in a loop via `time-to-live` field in the datagram headers.

2. IP will fragment packets if they are too long. Not all links have the same allowed packet size. Routers will segment the datagrams and provide info to reassemble them again (via headers).

3. Header contains a checksum to reduce chances of delivery to the wrong destination.

4. Allows for new versions of IP. E.g. gradual switch to IPv6

5. Allows new fields to be added to header. This can be helpful, but changes would need to also be processed by routers. So this might require hardware upgrades.

### IPv4 Datagram fields:

- Destination IP Address
- Source IP Address
- Protocol ID (identifying what is in the data field, e.g. TCP). There are more than 140 different ones
- Version (4 or 6)
- Total packet length (incl. header).
- Time to Live (TTL). Every router decrements this field. When it reaches 0, the packet is dropped.
- Packet ID: Helps to fragment
- Flags: Helps to fragment
- Fragment Offset: Helps to fragment
- Type of Service: Hints how important the packet is
- Header Length: Sometimes headers have extra fields
- Checksum: Over the whole header
- Lots of data

## Life of a Packet

### Transport Layer

Almost all web traffic is via TCP.

In a typical client-server operation, a `3-way handshake` happens:
1. Client to Server: Synchronize (`SYN`)
2. Server to Client: Synchronize / Acknowledge (`SYN/ACK`)
3. Client to Server: Acknowledge (`ACK`)

### IP Address & Ports

Transport layer is responsible to deliver data to application. Network layer is responsible to deliver data to computers. Therefore to deliver a packet to an application we need both an `IP address`, which specifies which computer to deliver the packet to, and a `TCP port`, which specify which application to deliver it to.

### Hops between Routers

Routing decisions are made via routing tables. These consist of IP address patterns and the link a packet with that patterns should be sent to.

The routing to a specific address can be traced via `tracert`. `* * *` means that the router is hidden and doesn't give any info back to tracert.

## Packet Switching

A `packet` is a self-contained unit of data that carries information necessary for it to reach its destination.

`Packet Switching` is the idea that a router picks its outgoing link independently for each arriving packet. If the link is free, the packet is sent. Else the packet is held for later.

### Source Routing

`Source Routing` is a form of packet switching. In this case each packet contains an explicit route, specifying each packet switch along the way.

The internet supports source routing, however it is generally disabled, because it raises big security issues.

The alternative (and what mostly happens today) is for the switch to decide on the next hop, based on the routing table and for the packet to contain only the destination.

### Consequences of Packet Switching

**Simplicity**: The switch doesn't care about the content, source, etc. of a packet and can treat every packet individually.

A `flow` is a collection of datagrams belonging to the same end-to-end communication, e.g. a TCP connection. Because every packet is independet, a switch does not need to know about flows. Remember, IP is connectionless and no per-flow state is required.

Advantages are:
1. No state needs to be established on each router along the connection, before sending data. This would take a lot of time.
2. Per-flow states don't need to be stored.
3. No implications if something fails (e.g. a host or switch going down).

**Efficiency**: Because packets are independent and the switch doesn't care about the source or destination, the same link can be used simultaneously by two people.

Internet traffic is very bursty on a low level. The bandwidth of a link that is available to a single user depends on how much other users are using that same link. This is called `statistical multiplexing`.

## Layering

**Layering** means organizing a system into a number of separate functional components, or layers, that communicate sequentially. I.e. each layer has an interface only to the layer directly above or below.

Each layer provides a well-defined service to the layer above, using the services by the layers below and it's own processing.

This separation of concern allows each layer in the hierarchy to focus on it's own job and provide a well defined service to the layer above.

Layering is a very common principle. It can be found everywhere, e.g. booking a plane ticket (aggregator, merchant, airline, airport), sending mail, or writing code (editing source code, compiler, linker, cpu).

### 5 Reasons for Layering

1. Modularity: Breaking down the system into smaller, more managable modules.
2. Well defined services: Each layer provides a well defined service to the layer above.
3. Reuse: A layer above can rely on the layer below.
4. Separation of concerns: Each layer can focus on its own job
5. Continuous improvement
6. Peer-to-peer communication: This refers to layers communicating directly with each other (not peer-to-peer networks). This advantage is specific to the internet.

## Encapsulation

Encapsulation is achieved by combining layering and packet switching. Information is organized in packets so that layers can be maintained: E.g. TCP segment inside IP packet inside Ethernet frame.

Encapsulation allows you to layer recursively. E.g. in case of a VPN, the packet looks like this:

======================================================
| Eth | IP | TCP | TLS | IP | TCP | HTTP | | | | | | |
======================================================

## Memory, Byte Order, and Packet Formats

When generating a message, software typically creates it in memory first. Only then is it passed to the networking card. The same happens in reverse when receiving a message: It is put into memory by the networking card.

In most computers memory is organized in `bytes`, which are 8-bit chunks of memory. Each byte has an `address` and most modern computers are 64-bit, meaning addresses are 64 bits long, resulting in 2 to the power of 64 (18 sextillion) potential bytes.

Software can also access memory in groups, e.g. a 64-bit integer from 8 continuous byte cells.

### Endianness

If you want to represent a value in memory you need to decide in which order they appear in memory. E.g. the number 1024 in hexadecimal is `0x0400`. This requires 16 bits, or 2 bytes, because each hexadecimal position is 4 bits long (4 bits are needed to represent 16 options). The 2 bytes are `0x04` and `0x40`.

**Little Endian** means that the `least significant byte` (`0x00`) is at the lowest address: `0x00``0x40` (writing the lowest address first). This makes most sense from a computational and architectual standpoint. **Big Endian**, the other way around, makes more sense to human readers.

Different processors use different endianness. E.g. x86 by Intel & AMD uses little endian, where as ARM processors (e.g. in iPhones). We don't want computers to have to care which approach the other side uses. So protocol specifications typically pick one and stick with it. In the case of the Internet protocol this is big endian.

When programmatically accessing a packet you need to know which approach is used and how your computer stores data. In order to simplify this, programming languages like C have helper functions for conversion. E.g. `htons()` (host to network short) or 'long' alternatives for 32-bit values.

## IPv4 Addresses

The aim of the internet was to stitch many different networks (e.g. already existing company/university networks) together. For this to work, every computer needs an address that is unique across all networks.

Technicaly IPv4 addresses today are not totally unique because of some special cases, but for explanations sake let assume they are.

IPv4 addresses are 32 bits long and often written as 4 octets, e.g. `a.b.c.d` or `171.64.64.64`. The values of each octet is between 0 and 255, which means 256 possibilities, which means 8 bits are required to represent this.

Every device connected through IPv4 has and IP address. The IP layer delivers packets to the device with the destination address.

### Netmask

A **netmask** tells a device which IP addresses are local (meaning on the same link) and which ones require going through an IP router. E.g. two devices that are in the same WiFi network can communicate directly because they are on the same link.

Netmasks are best imagined as a series of 0s and 1s. E.g. `255.255.255.0` means `1111.1111.1111.0000`. This example means that an IP address that matches the first 3 octets, or 24 bits, is on the same network. `255.255.252.0` means it needs to match the first 22 bits.

### Old Address Structure

Class A/B/C (in that order)

==================================================
|0| network(7)  |            host(24)            |
==================================================
==================================================
|1|0|    network(14)    |       host(16)         |
==================================================
==================================================
|1|1|0|      network(21)       |     host(8)     |
==================================================

The network part of the address denotes an administrative domain, e.g. Stanford University. The host part denotes a specific device on that network. Note the leading 1s and 0s of the addresses.

The problem with this approach is that the classes are too coarsely grained, leading to a lot of wasted addresses.

### Classless Inter-Domain Routing

Today **Classless Inter-Domain Routing** (CIDR) is used so solve this. CIDR allows prefixes to be any number of bits. Address blocks are made up of address/count, e.g. `171.64.0.0/16` which means any address between `171.64.0.0` and `171.64.255.255`. The number after the `/` is the netmask length.

### ICANN & IANA

The `Internet Corporation for Assignment of Names and Numbers` (ICANN) is ultimately responsible for allocating CIDR blocks, but delegates this work to the `Internet Assigned Numbers Authority`.

IANA gives out /8s (16 mio) to Regional Internet Registries (RIRs). They then break them up into smaller blocks and assign them according to their own policy.

## Hops & LPM

Which link to forward a packet to is determined by an algorithm called **Longest Prefix Match** (LPM). This operates based on the destination address and a **forwarding table**, which look like the one below.

 destination  | link
===================
0.0.0.0/0     |  1
171.33.x.x/16 |  5
23.x.x.x/8    |  2
28.33.5.x/24  |  4
171.32.x.x/16 |  2
67.x.x.x/6    |  6
216.x.x.x/8   |  1

With LPM the packet is forwarded to the most specific match, which is picked by looking at the length of the prefix, e.g. 16 in the first case.

## Address Resolution Protocol

ARP allows the network layer to discover the link address associated with a network address it is connected to.

Each protocol layer has their own names and addresses. E.g. an IP address describes a host, a unique destination at the network layer. A link address describes a particular network card, a unique device that sends and receives link layer frames.

It is common for a single host to have multiple IP addresses, one for each interface. This is because one IP address can really only be in one network as determined by the netmask.

 _____                   _____                   _____
 |   |===================|   |===================|   |
 |   |   0:18:e7:f3:ce:1a|   |0:18:e7:f3:ce:1a   |   |
 |___|        192.168.0.1|___|171.43.22.8        |___|
   A                    gateway                    B
192.168.0.5                                  171.43.22.5
00:13:72:4c:d9:6a                            9:9:9:9:9:9

This setup is in large part a historical artifact because the internet was trying to connect many networks (link layers) which weren't simple going to stop using their addresses.

A packet sent by host A to host B in the example above would have the network layer destination of B, but the link layer destination of the gateway. Host A knows it needs to do this because it's netmask tells it that B is not on the same network. When the packet arrives at the gateway, the IP packet will be repackaged into a new link layer frame with a new link layer address.

ARP allows host A to find out what the link layer address of the gateway is. It requires every node to keep a cache of mappings from IP addresses on its network to link layer addresses. If a node needs to send a packet to an IP address it does not have a mapping for it sends a request to a link layer broadcast address, which all nodes in the network will hear. Nodes that have the desired IP address mapped will respond (and include the link layer address).

Mappings are generated only from packets sent and nodes only reply for themselves to broadcasts. The mappings stay in the cache for a limited amout of time (minutes or hours) depending on the device. They don't share mappings. This ensures that dead clients automatically leave the mapping after some time.

### ARP Packet Format

ARP packets contain the following fields (stored in big endian):
1. Hardware: What link layer this request is for
2. Protocol: Network protocol this request is for
3. Hardware Length: Length in bytes of the link layer address
3. Protocol Length: Length in bytes of the network layer address
4. Opcode: States whether packet is request or response
5. Source Hardware Address
6. Source Protocol Address
7. Destination Hardware Address
8. Destination Protocol Address
9. Data

The broadcast address is `ff:ff:ff:ff:ff:ff` (all 1s), which is used as the destination hardware address.

Originally replies to broadcasts were send to the sender of the broadcast (called `unicast`). Today however they are also often broadcasted, which speeds up the replacement of cache entries.

Nodes also send `gratuitous ARP packets`, requesting non-existing mappings, to advertise themselves on a network.