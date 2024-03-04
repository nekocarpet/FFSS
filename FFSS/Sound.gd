extends Node2D
var count = 0
func _ready():
	Messenger.connect("coin_collected", _on_coin_collect)
	Messenger.connect("new_player", _on_new_player)
	Messenger.connect("despawn_player", _on_despawn_player)
	Messenger.connect("player_moved", _on_player_move)
	Messenger.connect("strike", _on_strike)
	
func _on_coin_collect():
	$Score.play()
func _on_new_player():
	$NewPlayer.play()
func _on_despawn_player():
	$DespawnPlayer.play()
func _on_player_move():
	$PlayerMove.play()
func _on_strike():
	$Strike.play()
