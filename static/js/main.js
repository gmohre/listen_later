//Initialize players

$('audio').mediaelementplayer({
	features: ['playpause', 'duration']
	});

//Delete Functions

var deleteAudio = function(id) {
	$.post("list/delete", { id : id } );
	$('.clip'+ id).fadeOut();
}