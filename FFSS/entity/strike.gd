extends Area2D
var bodies = []
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	$StrikeRdy.show()
	$ColorRect.hide()
	$Timer.start()

func _on_timer_timeout() -> void:
	$ColorRect.show()
	$StrikeRdy.hide()
	Global.camera.shake(0.5,7)
	$Timer2.start()

func _on_timer_2_timeout() -> void:
	check_overlap()
	Messenger.strike.emit()
	queue_free()

func check_overlap():
	bodies = get_overlapping_bodies()
	for body in bodies:
		if body.is_in_group("players"):
			body.score = 0
			body.score_label.text = str(body.score)
