$(document).ready(function() {
	createOptions();
	$('.key').click(function() {
		$('.key').addClass("btn-warning");
		setTimeout(showResults, 600);
	});
	$('.distractor').click(function() {
		$('.distractor').addClass("btn-warning");
		setTimeout(showResults, 600);
	});
});

function createOptions() {
	var ulElement = $(document.createElement('ul'));
	ulElement.addClass('nav nav-pills nav-stacked');
	var options = {};
	options[question.key] = "key";
	for (var i = 0; i < question.distractors.length; i++) {
		options[question.distractors[i]] = "distractor";
	}
	var optionId = 65;
	while (Object.keys(options).length > 0) {
		var i = Math.floor(Math.random()*Object.keys(options).length);
		opt = Object.keys(options)[i];
		var liElement =  $('<li></li>');
		$('<a class="'+options[opt]+'">'+String.fromCharCode(optionId)+'. '+opt+'</a>').appendTo(liElement);
		liElement.appendTo(ulElement);
		delete options[opt];
		optionId += 1;
	}
  	ulElement.appendTo("#options");
}

function showResults() {
	$('.key').removeClass("btn-warning").addClass("btn-success");
	$('.distractor').removeClass("btn-warning").addClass("btn-danger");
}