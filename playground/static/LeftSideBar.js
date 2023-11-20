// Function to open the options frame
function openOptionsFrame() {
    document.getElementById('options-frame').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
  }

  // Function to close the options frame
  function closeOptionsFrame() {
    document.getElementById('options-frame').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
  }

  // Event listener to open the options frame when the trigger is clicked
  document.getElementById('options-trigger').addEventListener('click', openOptionsFrame);

  // Event listener to close the options frame when clicking away from it
  document.getElementById('overlay').addEventListener('click', closeOptionsFrame);