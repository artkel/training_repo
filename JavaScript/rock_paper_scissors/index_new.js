const options = ['rock', 'paper', 'scissors'];
const score = JSON.parse(localStorage.getItem('score')) || {
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

  localStorage.setItem('score', JSON.stringify(score));

}

function playGame(playerChoice) {
  const computerChoice = options[Math.floor(Math.random() * options.length)];

  score.game_count++;

  if (playerChoice === computerChoice) {
    score.draw_count++;
    document.getElementById('result-message').textContent = `${playerChoice.charAt(0).toUpperCase() + playerChoice.slice(1)} vs ${computerChoice.charAt(0).toUpperCase() + computerChoice.slice(1)}!`;
    document.getElementById('result-message-final').textContent = "DRAW";
    document.getElementById('result-message-final').className = 'draw';
  } else if (
    (playerChoice === 'rock' && computerChoice === 'scissors') ||
    (playerChoice === 'paper' && computerChoice === 'rock') ||
    (playerChoice === 'scissors' && computerChoice === 'paper')
  ) {
    score.victory_count++;
    document.getElementById('result-message').textContent = `${playerChoice.charAt(0).toUpperCase() + playerChoice.slice(1)} vs ${computerChoice.charAt(0).toUpperCase() + computerChoice.slice(1)}!`;
    document.getElementById('result-message-final').textContent = "WIN";
    document.getElementById('result-message-final').className = 'win';
  } else {
    score.loss_count++;
    document.getElementById('result-message').textContent = `${playerChoice.charAt(0).toUpperCase() + playerChoice.slice(1)} vs ${computerChoice.charAt(0).toUpperCase() + computerChoice.slice(1)}!`;
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


// Event listeners for buttons
document.getElementById('rock').addEventListener('click', () => playGame('rock'));
document.getElementById('paper').addEventListener('click', () => playGame('paper'));
document.getElementById('scissors').addEventListener('click', () => playGame('scissors'));
document.getElementById('reset').addEventListener('click', resetScore);

updateScoreDisplay();
