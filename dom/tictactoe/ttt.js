// Restart Game Button
var restart = document.querySelector('#button');

// Grab all the squares
var squares = document.querySelectorAll("td");


// Clear Squares Function
function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
  }

}
restart.addEventListener('click',clearBoard)




// Create a function that will check the square marker
function changeMarker(){
    if(this.textContent === ''){
      this.textContent = 'X';
      // console.log(marker)
    }else if (this.textContent === 'X') {
      this.textContent = 'O';
    }else {
      this.textContent = '';
    }
};

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changeMarker);
}

// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
// color changer

// var body = document.querySelector("body")
// body.style.color = "#56505f";
//
// function getRandomColor(){
//   var letters = "0123456789ABCDEF";
//   var color = '#';
//   for (var i = 0; i < 6; i++) {
//     color += letters[Math.floor(Math.random()*16)];
//   }
//   return color
// }
//
// // Simple function for clarity
// function changeHeaderColor(){
//   colorInput = getRandomColor()
//   body.style.color = colorInput;
//   body.style.background = colorInput;
// }
//
// // Now perform the action over intervals (milliseocnds):
// setInterval("changeHeaderColor()",2000);

// >>>>>>>>>>>>>>>>>>>>>
// https://www.w3schools.com/jsref/prop_style_background.asp
// Definition and Usage
// The background property sets or returns up to eight separate background properties, in a shorthand form.
//
// With this property, you can set/return one or more of the following (in any order):
//
// background-color
// background-image
// background-repeat
// background-attachment
// background-position
// background-size
// background-origin
// background-clip
