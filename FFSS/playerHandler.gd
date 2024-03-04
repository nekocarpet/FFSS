extends Node2D

@onready var server_node: ServerNode = $"../ServerNode"
var player = preload("res://entity/player.tscn")
var players = {}   # Master dictionary
var life = 25

func _ready():
	server_node.connect("player_data_parsed", _on_player_data_parsed)   #receive parsed data

func _on_player_data_parsed(parsed_data):
	# Decrement life or update player target_pos
	for id in players.keys():
		if id in parsed_data:
			var pos = parsed_data[id]["pos"]
			players[id]["pos"] = pos  # Update position in the dictionary
			players[id].node.target_pos = players[id]["pos"]  # Move player
			Messenger.player_moved.emit()
		else:
			players[id]["life"] -= 1
			if players[id]["life"] < 0:
				despawn_player(id)
	
	# Spawn New Players
	for id in parsed_data.keys():
		if not players.has(id):
			var pos = parsed_data[id]["pos"]
			spawn_player(id, pos)

func spawn_player(id, pos):
	var player_instance = player.instantiate()
	player_instance.position = pos
	player_instance.target_pos = pos
	player_instance.name = "%s" % id
	add_child(player_instance)
	players[id] = {"node": player_instance, "pos": pos, "life": life}
	print("New player:", id)
	Messenger.new_player.emit()

func despawn_player(id):
	var player_instance = players[id]["node"]
	remove_child(player_instance)
	player_instance.queue_free()
	players.erase(id)
	Messenger.despawn_player.emit()
	print("Removed player", id)

