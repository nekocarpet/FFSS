extends CanvasLayer
class_name UI

@onready var count_label = %Count
@onready var ppos_label = %P_Pos
@onready var t_score = %TScore #Total Score
@onready var players: Node2D = $"../Players"


func _ready():
	update_pos_label()
	update_count_label()
	update_score_label()
	Messenger.connect("coin_collected", _on_coin_collect)

func _process(delta: float) -> void:
	update_pos_label()
	update_count_label()

func update_pos_label():
	var pos_strings = []
	for id in players.players.keys():
		var player_info = players.players[id]
		var pos = player_info["pos"]
		# Format each player's info into 'id: (x, y)' string
		var pos_string = "%s: (%s, %s)" % [id, pos.x, pos.y]
		pos_strings.append(pos_string)
	# Join all formatted strings with a newline to separate entries
	ppos_label.text = "\n".join(pos_strings)


func update_count_label():
	var count_str = "Count: " + str(players.players.size())
	count_label.text = count_str

func update_score_label():
	var score_str = "Score: " + str(Global.score)
	t_score.text = score_str

func _on_coin_collect():
	Global.score += 1
	update_score_label()
