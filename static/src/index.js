$(document).ready(function() {
	displayQuestion();
	createOptions();
	$('.key').click(function() {
		$('.key').addClass("btn-success");
		displayResultAnswerCorrect();
	});
	$('.distractor').click(function() {
		$('.distractor').addClass("btn-danger");
		displayResultAnswerWrong()
	});
});

function displayResultAnswerCorrect() {
	$("#question_or_answer").children().remove();
	$('<h2 style="text-align:center">Correct Answer:</h2>').appendTo("#question_or_answer")
	$('<h2 style="text-align:center">'+question.key+'</h2>').appendTo("#question_or_answer")
	$('<p>'+question.explanation+'</p>').appendTo("#question_or_answer")
	$('<div style="display:block;width:5em;margin-left:auto;margin-right:auto" class="alert alert-success">CORRECT!</div>').appendTo("#question_or_answer")
}

function displayResultAnswerWrong() {
	$("#question_or_answer").children().remove();
	$('<h2 style="text-align:center">Correct Answer:</h2>').appendTo("#question_or_answer")
	$('<h2 style="text-align:center">'+question.key+'</h2>').appendTo("#question_or_answer")
	$('<p>'+question.explanation+'</p>').appendTo("#question_or_answer")
	$('<div style="display:block;width:5em;margin-left:auto;margin-right:auto" class="alert alert-error">INCORRET!</div>').appendTo("#question_or_answer")
}

function displayQuestion() {
  	$("#question_or_answer").children().remove();
	$('<p>'+question.stem+'</p>').appendTo("#question_or_answer")
}

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
  	ulElement.appendTo("#question_or_answer");
}

function showResults() {
	$('.key').removeClass("btn-warning").addClass("btn-success");
	$('.distractor').removeClass("btn-warning").addClass("btn-danger");
}