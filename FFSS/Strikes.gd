extends Node2D

var strike = load("res://entity/strike.tscn")

func _ready():
	set_process_input(true)

func _input(event):
	if event is InputEventMouseButton and event.pressed:
		var mouse_pos = get_global_mouse_position()
		var strike_instance = strike.instantiate()
		strike_instance.position = mouse_pos
		add_child(strike_instance)
