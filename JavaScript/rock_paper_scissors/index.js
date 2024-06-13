const options = ['rock', 'paper', 'scissors'];

// if user selects something, computer also selects; then winner is defined; then score is updated
let game_count = 0;
let draw_count = 0;
let victory_count = 0;
let loss_count = 0;

function updateScoreDisplay() {
  document.getElementById('human-score').textContent = `Human - ${victory_count}`;
  document.getElementById('computer-score').textContent = `Computer - ${loss_count}`;
  document.getElementById('draw-score').textContent = `Draw - ${draw_count}`;
  document.getElementById('games-played').textContent = `Games played: ${game_count}`;
}

function gameRock() {

  let choice_idx = Math.floor(Math.random() * options.length);
  let computer_choice = options[choice_idx];
  

  game_count++;
  updateScoreDisplay();

  if (computer_choice === 'rock') {
    draw_count++
    document.getElementById('result-message').textContent = "Rock vs Rock!";
    document.getElementById('result-message-final').textContent = "DRAW";
    document.getElementById('result-message-final').className = 'draw';
  } else if (computer_choice === 'scissors') {
    victory_count++
    document.getElementById('result-message').textContent = "Rock vs Scissors!";
    document.getElementById('result-message-final').textContent = "WIN";
    document.getElementById('result-message-final').className = 'win';
  } else {
    loss_count++
    document.getElementById('result-message').textContent = "Rock vs Paper!";
    document.getElementById('result-message-final').textContent = "LOSS";
    document.getElementById('result-message-final').className = 'loss';
  }

  updateScoreDisplay();
}

function gamePaper() {

  let choice_idx = Math.floor(Math.random() * options.length);
  let computer_choice = options[choice_idx];
  

  game_count++;

  if (computer_choice === 'paper') {
    draw_count++
    document.getElementById('result-message').textContent = "Paper vs Paper!";
    document.getElementById('result-message-final').textContent = "DRAW";
    document.getElementById('result-message-final').className = 'draw';
  } else if (computer_choice === 'scissors') {
    loss_count++
    document.getElementById('result-message').textContent = "Paper vs Scissors!";
    document.getElementById('result-message-final').textContent = "LOSS";
    document.getElementById('result-message-final').className = 'loss';
  } else {
    victory_count++
    document.getElementById('result-message').textContent = "Paper vs Rock!";
    document.getElementById('result-message-final').textContent = "WIN";
    document.getElementById('result-message-final').className = 'win';
  }

  updateScoreDisplay();
}

function gameScissors() {

  let choice_idx = Math.floor(Math.random() * options.length);
  let computer_choice = options[choice_idx];
  

  game_count++;

  if (computer_choice === 'scissors') {
    draw_count++
    document.getElementById('result-message').textContent = "Scissors vs Scissors!";
    document.getElementById('result-message-final').textContent = "DRAW";
    document.getElementById('result-message-final').className = 'draw';
  } else if (computer_choice === 'paper') {
    victory_count++
    document.getElementById('result-message').textContent = "Scissors vs Paper!";
    document.getElementById('result-message-final').textContent = "WIN";
    document.getElementById('result-message-final').className = 'win';
  } else {
    loss_count++
    document.getElementById('result-message').textContent = "Scissors vs Rock!";
    document.getElementById('result-message-final').textContent = "LOSS";
    document.getElementById('result-message-final').className = 'loss';
  }

  updateScoreDisplay();
}

function resetScore() {
  game_count = 0;
  victory_count = 0;
  loss_count = 0;
  draw_count = 0;
  updateScoreDisplay();
  document.getElementById('result-message').textContent = "Good Luck!";
  document.getElementById('result-message-final').textContent = "";
  document.getElementById('result-message-final').className = '';
}

