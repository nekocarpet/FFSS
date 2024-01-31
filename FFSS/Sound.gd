extends Node2D
var count = 0
func _ready():
	Messenger.connect("coin_collected", _on_coin_collect)
	Messenger.connect("new_player", _on_new_player)
	Messenger.connect("despawn_player", _on_despawn_player)
func _on_coin_collect():
	$Score.play()
func _on_new_player():
	$NewPlayer.play()
func _on_despawn_player():
	$DespawnPlayer.play()
