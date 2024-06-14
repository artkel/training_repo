const options = ['rock', 'paper', 'scissors'];
const score = {
  game_count: 0,
  draw_count: 0,
  victory_count: 0,
  loss_count: 0
};


function updateScoreDisplay() {
  document.getElementById('human-score').textContent = score.victory_count;
  document.getElementById('computer-score').textContent = score.loss_count;
  document.getElementById('draw-score').textContent = score.draw_count;
  document.getElementById('games-played').textContent = `Games played: ${score.game_count}`;
}

function gameRock() {

  let choice_idx = Math.floor(Math.random() * options.length);
  let computer_choice = options[choice_idx];
  

  score.game_count++;
  updateScoreDisplay();

  if (computer_choice === 'rock') {
    score.draw_count++
    document.getElementById('result-message').textContent = "Rock vs Rock!";
    document.getElementById('result-message-final').textContent = "DRAW";
    document.getElementById('result-message-final').className = 'draw';
  } else if (computer_choice === 'scissors') {
    score.victory_count++
    document.getElementById('result-message').textContent = "Rock vs Scissors!";
    document.getElementById('result-message-final').textContent = "WIN";
    document.getElementById('result-message-final').className = 'win';
  } else {
    score.loss_count++
    document.getElementById('result-message').textContent = "Rock vs Paper!";
    document.getElementById('result-message-final').textContent = "LOSS";
    document.getElementById('result-message-final').className = 'loss';
  }

  updateScoreDisplay();
}

function gamePaper() {

  let choice_idx = Math.floor(Math.random() * options.length);
  let computer_choice = options[choice_idx];
  

  score.game_count++;

  if (computer_choice === 'paper') {
    score.draw_count++
    document.getElementById('result-message').textContent = "Paper vs Paper!";
    document.getElementById('result-message-final').textContent = "DRAW";
    document.getElementById('result-message-final').className = 'draw';
  } else if (computer_choice === 'scissors') {
    score.loss_count++
    document.getElementById('result-message').textContent = "Paper vs Scissors!";
    document.getElementById('result-message-final').textContent = "LOSS";
    document.getElementById('result-message-final').className = 'loss';
  } else {
    score.victory_count++
    document.getElementById('result-message').textContent = "Paper vs Rock!";
    document.getElementById('result-message-final').textContent = "WIN";
    document.getElementById('result-message-final').className = 'win';
  }

  updateScoreDisplay();
}

function gameScissors() {

  let choice_idx = Math.floor(Math.random() * options.length);
  let computer_choice = options[choice_idx];
  

  score.game_count++;

  if (computer_choice === 'scissors') {
    score.draw_count++
    document.getElementById('result-message').textContent = "Scissors vs Scissors!";
    document.getElementById('result-message-final').textContent = "DRAW";
    document.getElementById('result-message-final').className = 'draw';
  } else if (computer_choice === 'paper') {
    score.victory_count++
    document.getElementById('result-message').textContent = "Scissors vs Paper!";
    document.getElementById('result-message-final').textContent = "WIN";
    document.getElementById('result-message-final').className = 'win';
  } else {
    score.loss_count++
    document.getElementById('result-message').textContent = "Scissors vs Rock!";
    document.getElementById('result-message-final').textContent = "LOSS";
    document.getElementById('result-message-final').className = 'loss';
  }

  updateScoreDisplay();
}

function resetScore() {
  score.game_count = 0;
  score.victory_count = 0;
  score.loss_count = 0;
  score.draw_count = 0;
  updateScoreDisplay();
  document.getElementById('result-message').textContent = "Good Luck!";
  document.getElementById('result-message-final').textContent = "you've got zero chances, human";
  document.getElementById('result-message-final').className = '';
}

