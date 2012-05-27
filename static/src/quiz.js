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
	$('<h2 style="text-align:center">Correct Answer:'+question.key+'</h2>').appendTo("#question_or_answer")
	$('<br>').appendTo("#question_or_answer")
	$('<p>'+question.explanation+'</p>').appendTo("#question_or_answer")
	$('<br>').appendTo("#question_or_answer")
	$('<div class="verdict alert alert-success">CORRECT</div>').appendTo("#question_or_answer")
	$('<br>').appendTo("#question_or_answer")
	$('<a class="btn btn-large btn-primary" href="/quiz/'+tag+'">Next question</a>').appendTo("#question_or_answer")
	$('<a class="btn btn-large" href="/category">Change settings</a>').appendTo("#question_or_answer")
}

function displayResultAnswerWrong() {
	$("#question_or_answer").children().remove();
	$('<h2 style="text-align:center">Correct Answer:'+question.key+'</h2>').appendTo("#question_or_answer")
	$('<br>').appendTo("#question_or_answer")
	$('<p>'+question.explanation+'</p>').appendTo("#question_or_answer")
	$('<br>').appendTo("#question_or_answer")
	$('<div class="verdict alert alert-error">INCORRECT</div>').appendTo("#question_or_answer")
	$('<br>').appendTo("#question_or_answer")
	$('<a class="btn btn-large btn-primary" href="/quiz/'+tag+'">Next question</a>').appendTo("#question_or_answer")
	$('<a class="btn btn-large" href="/category">Change settings</a>').appendTo("#question_or_answer")
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