const stylesheet = document.querySelector('link');
// Check if user has a preferred style stored in localStorage
var preferredStyle = localStorage.getItem('preferredStyle');
if (preferredStyle) {
  stylesheet.setAttribute('href', '/playground/static/Main' + preferredStyle + '.css');
}

function toggleMode() {
  if (stylesheet.getAttribute('href') === '/playground/static/MainLight.css') {
    stylesheet.setAttribute('href', '/playground/static/MainDark.css');
    localStorage.setItem('preferredStyle', 'Dark');
    console.log(stylesheet.href);
  } else {
    stylesheet.setAttribute('href', '/playground/static/MainLight.css');
    localStorage.setItem('preferredStyle', 'Light');
    console.log(stylesheet.href);
  }
}