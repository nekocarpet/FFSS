extends CharacterBody2D

@onready var players: Node2D = $".."
@onready var score_label = $Control/ScoreLabel
@export var speed = 600
var target_pos = Vector2()
var score = 0  #own score

func _ready():
	add_to_group("players")
	score_label.text = str(self.score)

func _physics_process(delta: float) -> void:
	move_to_target(delta)

func move_to_target(delta):
	if position.distance_to(target_pos) > 30:
		var direction = (target_pos - position).normalized()
		velocity = (direction * speed)
		move_and_slide()

func update_target_pos(new_target_pos: Vector2):
	target_pos = new_target_pos


