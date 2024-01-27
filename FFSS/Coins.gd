extends Node2D

var coin = preload("res://entity/coin.tscn")
var spawn_area = Rect2(Vector2(30, 30), Vector2(1100, 750))  # Adjust to your game area

func _ready():
	Messenger.connect("coin_collected", _on_coin_collect)
	spawn_coin()

func spawn_coin():
	var instance = coin.instantiate()
	var spawn_position = Vector2(
		randf_range(spawn_area.position.x, spawn_area.end.x),
		randf_range(spawn_area.position.y, spawn_area.end.y)
	)
	instance.position = spawn_position
	add_child.call_deferred(instance)

func _on_coin_collect():
	spawn_coin()

