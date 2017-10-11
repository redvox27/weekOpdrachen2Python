with open('packets.txt', 'r') as f:
    packet_stream = str(f.read())

packet_list = []
packet_start = 0

while packet_start < len(packet_stream):
    tempList = []

    len_MAC_address = 12
    len_id = 3

    MAC_address = packet_stream[:len_MAC_address]
    tempList.append(MAC_address)
    print(MAC_address)

    hexPacketLength = int(packet_stream[len_MAC_address: len_MAC_address+len_id])
    packet_length = int(packet_stream[len_MAC_address : len_MAC_address+len_id], 16)
    tempList.append(hexPacketLength)

    print(packet_length)

    packContent = packet_stream[len_MAC_address+len_id+1: packet_length]
    tempList.append(packContent)
    packet_list.append(tuple(tempList))

    packet_stream = packet_stream[len_MAC_address + len_id + packet_length +1:]
# print the tuples
for packet in packet_list:
    print(packet)
