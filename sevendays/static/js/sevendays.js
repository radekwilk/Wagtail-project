// HAMBURGER MENU FUNCTIONALITY
const $menu = document.querySelector('.hamburger-menu')
const $body = document.querySelector('body')
const $closeBtn = document.querySelector('.responsive-nav-close')

$menu.addEventListener('click',()=> {
  $body.classList.add('change')
})

$closeBtn.addEventListener('click',()=> {
  $body.classList.remove('change')
})



// THIS IS TO RUN ANALOG WATCH IN MATCHES DASHBOARD
const deg = 6;
const hr = document.querySelector('.tip-handle-hr');
const mn = document.querySelector('.tip-handle-min');
const sc = document.querySelector('.tip-handle-sec');
setInterval(() => {
	let day = new Date();
	let hh = day.getHours() * 30;
	let mm = day.getMinutes() * deg;
	let ss = day.getSeconds() * deg;
	hr.style.transform = `rotateZ(${hh+(mm/12)}deg)`;
    mn.style.transform = `rotateZ(${mm}deg)`;
    sc.style.transform = `rotateZ(${ss}deg)`;
})

// COUNT DOWN TO NEAREST MATCH
// Set the date we're counting down to
let matchDate = document.querySelector('#js-next-game-date').value
matchDate = moment(matchDate, "MMMM Do YYYY h:mm:ss a").toDate();
const countDownDate = new Date(matchDate).getTime();
const nowDate = new Date()
console.log('Match date:',matchDate)
console.log('CountDown date:',countDownDate)
console.log('System date:',nowDate)

// Update the count down every 1 second
const x = setInterval(function() {
  //Get names of spans holding date
  const $days = document.querySelector('.counter-days');
  const $hours = document.querySelector('.counter-hours');
  const $minutes = document.querySelector('.counter-minutes');
  const $seconds = document.querySelector('.counter-seconds');

  // Get today's date and time
  const now = new Date().getTime();

  // Find the distance between now and the count down date
  const distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
//   document.getElementById("demo").innerHTML = days + "d " + hours + "h "
//   + minutes + "m " + seconds + "s ";
  $days.innerText = days;
  $hours.innerText = hours;
  $minutes.innerText = minutes;
  $seconds.innerText = seconds;

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.querySelector(".counter").innerHTML = "MATCH FINISHED";
  }
}, 1000);