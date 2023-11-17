// Get the element
var text = document.getElementById('movingText');

// Set the initial position
var position = 0;

// Update the position every 100 milliseconds
setInterval(function() {
    // Increase the position by 1
    position++;

    // Apply the new position to the element
    text.style.left = position + 'px';
}, 100);

// Get the Lottie player element
var player = document.querySelector('dotlottie-player');

// Add a click event listener
player.addEventListener('click', function() {
    // Check if the animation is currently playing
    if (player.isPlaying) {
        // If it's playing, pause it
        player.pause();
    } else {
        // If it's not playing, play it
        player.play();
    }
});
