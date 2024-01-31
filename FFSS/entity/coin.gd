extends Area2D


func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("players"):
		Messenger.coin_collected.emit()
		body.score += 1
		body.score_label.text = str(body.score)
		queue_free()
