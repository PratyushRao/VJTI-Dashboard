document.addEventListener('DOMContentLoaded', function() {
  const studentBtn = document.getElementById('student');
  const facultyBtn = document.getElementById('faculty');
  
  function toggleActive(clickedButton: HTMLElement) {
    const buttons = document.querySelectorAll('#toggle button');

    buttons.forEach(button => {
      button.classList.remove('active');
      button.classList.add('inactive');
    });

    const buttonId = clickedButton.id;
    const userInput = document.getElementById('user')

    if(!userInput) return
    if (buttonId === 'student') userInput.setAttribute('placeholder', 'VJTI ID Number');
    if (buttonId === 'faculty') userInput.setAttribute('placeholder', 'VJTI Email Address');
    
    clickedButton.classList.add('active');
    clickedButton.classList.remove('inactive');
  }
  
  if(!studentBtn || !facultyBtn) return
  studentBtn.addEventListener('click', function() { toggleActive(this); });
  facultyBtn.addEventListener('click', function() { toggleActive(this); });
});