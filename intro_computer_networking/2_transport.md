# Transport

## TCP Service Model

When 2 applications use TCP, they establish a 2-way communication channel between the TCP peers at both ends. This is called a **connection**. Both hosts also keep a state machine of the connection. The connection is created via a 3-way handshake. First host A send a SYN (synchronize) message to host B, who then respons with a **SYN + ACK** (acknowledge). Lastly A responds with an ACK to indicate that it is accepting the request from B. The SYN request contains a number that states at which point the byte stream starts.

When TCP segments are sent they only arrive at the destination with a delay. Also they are often sent multiple times, in case something goes wrong with the transmission.

When the connection is closed (called connection **teardown**) the hosts tell each other they are closing the connection and will clean up the state in the state machine. A host tells the other host that it wants to close the connection by sending a **FIN** (finish) message. The other host then replies with an ACK, but can still keep sending data if it wants to (until it sends its own FIN). When a connections is fully closed, the state can be safely removed.

### TCP Model Properties

**Reliable delivery** is guaranteed by the following mechanisms of TCP:

1. TCP layers send an acknowledgement back to the sender when they receive data.
2. Checksums in the header detect corrupt data.
3. Sequence numbers (of the first byte in the segment in the stream of bytes) in the header.
4. Flow control to prevent overflowing receiver. Specifically the receiver keeps telling the sender how much room it has in its buffer to accept new data.

If the TCP segment arrive in an incorrect order, the TCP layer will re-sequence them into the right order using the sequence number. This way data is delivered **in-sequence**.

TCP also has mechanisms for **congestion control**, which is covered extensively later.

### TCP Header Content

The **TCP header** contains the following fields:
- Destination Port: Which application the bytes should be delivered to.
- Source Port: Which port should data be sent back to.
- Sequence Number
- Acknowledgement Sequence Number: Tells other end which byte is expected next. This way TCP acknowledgements piggyback on the data travelling in the other direction.
- 16 bit checksum over data and header.
- Header Length
- TCP Options: Optional new header fields.
- ACK flag: Tells us the acknowledgement sequence number is valid and all data up until this point has been received.
- SYN flag: Indicates this to be a synchronise.
- FIN flag: Signalling closing of connection.
- PSH flag: Tells the other end to send data immediately, instead of waiting for new data.

### Unique ID of a TCP Connection

A TCP connection is uniquely identified internet-wide by 5 fields in the TCP and IP headers:
- IP Source Address
- IP Destination Address
- Transport Layer Protocol IP (TCP)
- TCP Source Port
- TCP Destination Port

This assumes that host A picks a unique source port for each connection with host B. This is ensured by incrementing the port for each new connection. The field is 16-bit, so after 64k new connections the number will wrap around. To mitigate this risk, the first sequence number is picked randomly and sent along with the SYN and SYN+ACK.

## UDP Service Model

UDP is a much simpler service than TCP. It takes data from an application, creates a UDP datagram, then hands it to the network layer.

### UDP Header

The **UDP header** only has 4 header fields and a lenght of 8 bytes:
- Source Port
- Destination Port
- Length: 16-bit, length of the entire datagram (data + header)
- UDP Checksum: Optional for IPv4. All 0s if no checksum. Also includes fields from the IPv4 header in the calculation.

This means it violates the layering principle. This is done so that the UDP layer can detect datagrams sent to the wrong destination.

Ports work exactly the same way as in TCP. UDP can be thought of as just a demultiplexing mechanism to divide up a stream of UDP datagrams and send them to the correct process.

### UDP Model Properties

1. Connection-less datagram service: No connection established, packets may show up in any order
2. Self-contained datagrams: Packets may show up in any order.
3. Unreliable Delivery: No acknowledgments, no mechanism to detect missing or mis-sequenced datagrams.

This sounds very much like the IP layer, because it provides little more on top of it.

### UDP Use Cases

It is used by applications that don't need reliable delivery. E.g. DNS uses UDP because the request is fully contianed in one UDP datagram. DHCP (**Dynamic Host Configuration Protocol**) and NTP (**Network Time Protocol**) also uses UDP for the same reason. Some other apps use UDP because they have special needs with regards to congestion control, retransmission, or in-sequence delivery. E.g. some real-time streaming services use UDP, however most of them are built on top of HTTP these days and therefore use TCP

## ICMP Service Model

**Internet Control Message Protocol** is used to report errors and diagnose problems with the network layer. Besides the IP protocol and routing tables, it is what makes the network layer work.

When end-hosts or routers want to report errors using ICMP they information into an ICMP payload and hands it to IP. E.g. a router might have no information about a the network the host is trying to send something to.

### ICMP Model Properties

1. Self-contained error reporting messages
2. Unreliable: Simple datagram, no retries

### ICMP Message Content

The IDCP message that gets passed to the IP layer contains:
1. IP header of the datagram that caused the error
2. First 8 bytes of IP datagram that caused the error
3. Error Type
4. Error Code

RFC 792 contains the error codes and types.

### Ping Application

The ping app uses ICMP directly. It sends an **ICMP echo request** (type 8, code 0) to the target, which is supposed to send a **ICMP echo reply** (type 0, code 0).

### Traceroute Application

Traceroute actually send UDP messages, the content of which doesn't matter, but the TTL field is set to 1. When this reaches the router, the TTL gets decremented, which leads to the packet being discarded. However the router is also required to send back an ICMP message (TTL expired code/type).

Traceroute then uses the IP datagram header and the time it took to arrive to identify the router and how long the roundtrip took. It continues to do this, increasing the TTL until eventually it gets a response from the target host. Traceroute uses a weird UDP port number that the target host won't know, which leads to a `port unreachable` ICMP message.

## End-to-End Principle

There are many things that the network could be doing to imporve efficiency, but it doesn't (compression, chaching, security, etc.). Why not?

"The function in question can completely and correctly be implemented only with the knowledge and help of the application standing at the end points of the communication system. Therefore providing that questioned function as a feature of the communication system itself is not possible. (Sometimes an incomplete version of the function provided by the communication system may be useful as a performance enhancement.)"

Put in other words, the network can help, but you can't depend on it. E.g. if you want to have a secure app, you need to have end-to-end security, for which you need the app. Making security part of the network so that apps don't have to worry about it is not possible.

E.g. wireless networks often send packets multiple times to increase reliability, which might otherwise only be at 80% (compared with 99.999% for wired connections). However this doesn't absolve the app to check for completeness.

### Strong End-to-End Principle

RFC 1958: "The network's job is to transmit datagrams as efficiently and flexibly as possible. Everything else should be dont at the fringes..."

Put in other words: Don't implement it in the middle, only at the fringes! The reasoning for this is flexibility and simplicity.

E.g. in the reliability improvement example for wireless connections it is assumed that transport layer protocols actually all want higher reliability. If they don't they are stuck with it. This is a problem because it makes innovation and improvements harder. E.g. new transport layers might now assume the described behavior of WiFi, making everything more complex.

In terms of long term design and network evolution the strong end-to-end princicple is extremely valuable. However in terms of shortterm design and performance, network engineers often don't follow it. So over time the network performs better, but becomes harder to change.

## Error Detection

Error detection mechanisms work by appending (ethernet CRC, TLS MAC) or prepending (IP checksum) some error detection bits to the payload. IP checksums are actually put in the header, MAC and CRC are put in the footers of these protocols.

Even though different layers have error detection, applications should still do this as well.

### Checksums

Checksums add up all values in a packet. They are used by IP and TCP for example. They are very cheap to compute, but are not very robust, e.g. two errors could cancel each other out, and were motivated by the early software implementations of the internet. They are good for detecting single bit errors

One's complement algorithm used by IP, UDP, and TCP:
* Set checksum to 0
* Add all 16-bit words in the packet (using one's complement)
* Add any carry bit back in
* Flip all bits unless the result is 0xffff (all 1's), because all 0's means there is no checksum

### Cyclic Redundancy Codes (CRC)

CRCs calculate the remainder of a polynomial. This is not as cheap as checksums, however today it is quite easy to do, esp. in hardware. It is also a lot more robust than checksums are. In fact, TCP and IP can get away with using checksums, because the ethernet and esp. link layers use CRCs.

The algorithm used distills n bits of data down to c bits. E.g. a 1500 bit ethernet package into a 42 bit CRC. It uses polynomial long division to do so. Not going into the mathematical details here. However the creating CRC and checking it can be very efficiently done in hardware.

The chance of collision is 1 in 2 to the power of c, e.g. 1/256 for an 8 bit CRC. They are good for detecting errors bigger errors, esp. bursts or errors shorter than c bits are caught 100%. Burst are of special concern for networks.

### Message Authentication Code (MAC)

MACs are used for cryptographic transmission of data and for example are used in TLS (transport layer security). It prevents malicious modifications, but does not catch errors very well.

Not going into crypto details on MAC algorithm here.

Process:
* 2 parties share secret S (which is random)
* Calculate MAC c by apply the MAC algorithm to the message and S

## Finite State Machines

Finite state machines (**FSM**'s)are composed of a finite number of states, which is a particular configuration of the system. They are often drawn as maps in which the different states are linked by arrows that indicate the event that causes the state transition and the action that should be taken when the state transition occurs (if any).


============    Cause Event        ============
|          |  ----------------     |          |
|  State 1 |   Action to take      |  State 2 |
|          | ====================> |          |
============                       ============

One state can be followed by different other states, but the same event can only lead to one single other state, else it would be ambiguous.

For a clear specification every event that could possibly occur while the machine is in one state should be specified. In practice this can often get messy though.

Good example: FSM of a TCP connection: https://en.wikipedia.org/wiki/Transmission_Control_Protocol#/media/File:Tcp_state_diagram_fixed_new.svg
