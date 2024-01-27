extends Node2D

@onready var main: Node2D = $".."
var player = preload("res://entity/player.tscn")
var mouse_pos = Vector2()
var characters = []
var target_positions = []

func _ready():
	target_positions = [Vector2(800,500),Vector2(550,500)]

func inst(pos):
	var instance = player.instantiate()
	instance.position= pos
	add_child(instance)

func _physics_process(delta: float) -> void:
	Global.player_count = get_child_count()
	update_character_targets(target_positions)
	mouse_pos = get_global_mouse_position()
	# receives target_position here
	target_positions = [Vector2(800,500), Vector2(550,500), mouse_pos, Vector2(550,150)]

func update_character_targets(received_targets):
	# Create new instances or update existing ones
	for i in range(received_targets.size()):
		if i < get_child_count():
			# Update existing character's target position
			var character = get_child(i)
			if character.has_method("update_target_pos"):
				character.update_target_pos(received_targets[i])
		else:
			# Create a new character
			inst(received_targets[i])

# ... rest of your players script ...

	# Remove extra characters
	while get_child_count() > received_targets.size():
		var last_child = get_child(get_child_count() - 1)
		last_child.score = 0
		remove_child(last_child)
		last_child.queue_free()


# Process position data received from Python here
#func update_character_targets(received_targets):
	#characters = get_children()
	#for i in range(characters.size()):
		#var character = characters[i]
		#if character.has_method("update_target_pos"):
			#character.update_target_pos(target_positions[i])
