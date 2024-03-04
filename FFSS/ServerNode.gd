class_name ServerNode
extends Node

signal player_data_parsed(player_data)
var server := UDPServer.new()
var port := 4242
var ip := "127.0.0.1"
var peers = []
var msg

func _ready():
	var result = server.listen(port, ip)
	if result == OK:
		print("UDP server started on port %d" % port)
	else:
		print("Failed to start server")

func _process(delta):
	server.poll() 
	if server.is_connection_available():
		var peer: PacketPeerUDP = server.take_connection()
		var packet = peer.get_packet()
		msg = packet.get_string_from_utf8()
		#print("Accepted peer: %s:%s" % [peer.get_packet_ip(), peer.get_packet_port()])
		#print("Received data: %s" % [msg])
		parse_data()
		# Reply so it knows we received the message.
		#peer.put_packet(packet)
		# Keep a reference so we can keep contacting the remote peer.
		#peers.append(peer)

	for i in range(0, peers.size()):
		pass # Do something with the connected peers.

func parse_data():
	var parsed_data = {}
	var player_segments = msg.split("|", true, 0)
	for segment in player_segments:
		var details = segment.split(",", true, 0)
		if details.size() == 3:
			var id = details[0]
			var pos =  Vector2(float(details[1]), float(details[2]))
			parsed_data[id] = {"pos": pos}
	emit_signal("player_data_parsed", parsed_data)
	return parsed_data
