# Space Rock
## CS110 Final Project  << Fall, 2024 >>

## Team Members

Jake Edelstein

***

## Project Description

My project consists of a ship sprite which is controlled by the player, with the goal of avoiding the falling space rocks and make it out of their own personal 'meteor storm'. The player gains points by surviving, but the asteroids fall faster and more frequently as time progresses. The game ends when the player is hit.

***    
## Additional modules

* pygame
* sys
* random
* math
* time

## GUI Design

### Initial Design

![initial gui](assets/gui/gui.jpg)

### Final Design

![final gui](assets/gui/finalgui1.jpg)
![final gui](assets/gui/finalgui2.jpg)
![final gui](assets/gui/finalgui3.jpg)
![final gui](assets/gui/finalgui4.jpg)
![final gui](assets/gui/finalgui5.jpg)
![final gui](assets/gui/finalgui6.jpg)
![final gui](assets/gui/finalgui7.jpg)

## Program Design

### Features

1. Different game states and corresponding screens
2. Moveable character
3. Score and timer which reset after each playthrough
4. List of 5 highest scores since launching the program
5. Interactive buttons
6. Pause menu
7. WASD and arrow key functionality for movement
8. Toggle for SFX and music

### Classes
* Ship(pygame.sprite.Sprite)
     * Creates a ship to be controlled by the player
     * Allows user to move up, down, left, right and diagonally using both WASD and arrow keys.
 
 * Asteroid(pygame.sprite.Sprite)
     * Creates asteroids which spawn across the screen and fall downwards
     * Asteroids are removed once they fall beneath the bottom of the screen

 * Time (not the existing python module)
    * Creates a Time object which manages the time-based information for the game using the existing python time module.
    * Contains methods to start, stop and reset game time, as well as return the current game time in both raw and formatted forms.

 * Textbox (pygame.sprite.Sprite)
    * Creates a text box to be displayed on a pygame Surface.
    * Has methods to change the font size, text and text color. The draw method defined for Textbox objects has optional parameters;for text color and box color, as well as a bool parameter for if the text box should have a background box (default = False). 

 * Counter(Textbox)
    * Creates a modified Textbox object which contains a Time() object and uses it to manage the game time and game score.
    * Has methods to calculate the score by adding a certain number of points per update. The number of points is calculated using the current game time, in such a way that the player gains less points per update as the game continues.
    * Has a 'type' parameter in the constructor to determine if the counter is for the timer or for the score.

 * Button(Textbox)
    * Creates a modified Textbox object which functions as a pressable button.
    * Has a method which determines whether the player's mouse is hovered over it and updates the button accordingly. When the button is hovered over, its text color changes and it plays a sound. The sound plays only once untless the mouse is removed and hovers the button again.
    * Has a method which determines whether the button has been clicked. When it is clicked, a sound is played and the method returns True. This method exists to reduce repetitiveness in the controller.

 * Sound
    * Creates a personalized library of named sounds from the assets folder, as well as named pygame mixer channels as constants.
    * Has methods to toggle sound effects and music. Mainly serves as a helper class for organizing the controller and reducing repetitiveness.

 * Game
    * Controller class which manages the different game states/loops and game logic
    * Besides the loop functions, also has a helper function to re-initialize the game state.

## ATP

### Test Case 1: Player Movement

Description: Confirm that the player is able to move in all 4 directions, as well as diagonally, and that the player cannot move past the expected boundaries.
    
    Step 0: Launch the program.
    Step 1: Press the START button to start the game.
    Step 2: Press the W key.
    Step 3: Confirm that the player moves up.
    Step 4: Press the up arrow key.
    Step 5: Confirm that the player moves up.
    Step 6. Press and hold either the W or up arrow key.
    Step 7: Confirm that the player stops moving upwards once the ship sprite has moved halfway up the screen.
    Step 8: Press the W/up arrow and A/left arrow keys at the same time.
    Step 9: Confirm that the player moves diagonally upwards and to the left without moving vertically past the aforementioned boundary or past the left border of the screen.

Expected Outcome: The ship sprite should move in the corresponding direction of the WASD/arrow key inputs without moving off the screen or crossing the vertical halfway point.

|Step |                    Procedure                      |                                                         Expected Results |
|-----|:-------------------------------------------------:|:------------------------------------------------------------------------:|
|  0  | Launch the program.                               |           GUI window appears with start menu (see Final Design image 1). |
|  1  | Click the START button to start the game.         |        GUI window updates to the game screen (see Final Design image 5). |
|  2  | Press and hold the W or up arrow key.             |               Player moves upwards until reaching halfway up the screen. |
|  3  | Press and hold the A or left arrow key.           |            Player moves left until reaching the left side of the screen. |
|  4  | Press and hold the D or right arrow key.          |          Player moves right until reaching the right side of the screen. |
|  5  | Press and hold the S or down arrow key.           |          Player moves downwards until reaching the bottom of the screen. |
|  6  | Press and hold the W and A keys at the same time. |                         The player moves diagonally upwards to the left. |

### Test Case 2: 

Description: Confirm that upon collision with an enemy, the collision sound effect is played and the game is stopped for 2 seconds, after which the game over screen is displayed.

|Step |                    Procedure                      |                                                         Expected Results |
|-----|:-------------------------------------------------:|:------------------------------------------------------------------------:|
|  0  | Launch the program.                               |           GUI window appears with start menu (see Final Design image 1). |
|  1  | Click the START button to start the game.         |        GUI window updates to the game screen (see Final Design image 5). |
|  2  | Move the player to collide with an asteroid.      |                  Collision sound effect plays, game stops for 3 seconds, |
|  3  | Wait for 2 seconds.                               |   GUI window updates to the game over screen (see Final Design image 7). |

### Test Case 3:

Description: Confirm that pressing the escape key while playing will open and close the pause menu. Also confirm that the pause menu buttons are functional.

|Step |                    Procedure                      |                                                         Expected Results |
|-----|:-------------------------------------------------:|:------------------------------------------------------------------------:|
|  0  | Launch the program.                               |           GUI window appears with start menu (see Final Design image 1). |
|  1  | Click the START button to start the game.         |        GUI window updates to the game screen (see Final Design image 5). |
|  2  | Press the ESC key.                                |       GUI window updates to the pause screen (see Final Design image 6). |
|  3  | Click the SFX button.                             |      SFX button text changes to SFX: OFF and sound effects are disabled. |
|  4  | Click the SFX button again.                       |        SFX button text changes to SFX: ON and sound effects are enabled. |
|  5  | Click the MUSIC button.                           |           MUSIC button text changes to MUSIC: OFF and music is disabled. |
|  6  | Click the MUSIC button again.                     |             MUSIC button text changes to MUSIC: ON and music is enabled. |
|  7  | Click the BACK TO MENU button.                    |                             GUI window updates to the start menu screen. |
|  8  | Click the START button to start the game.         |                                   GUI window updates to the game screen. |
|  9  | Press the ESC key (take note of game screen).     |                                  GUI window updates to the pause screen. |
|  10 | Press the ESC key again.                          |  GUI window updates to the same game screen as before the pause occured. |

### Test Case 4:

Description: Test if highscores are saved and updated in the highscore menu.

|Step |                    Procedure                    |                                                           Expected Results |
|-----|:-----------------------------------------------:|:--------------------------------------------------------------------------:|
|  0  | Launch the program.                             |             GUI window appears with start menu (see Final Design image 1). |
|  1  | Click the HIGHSCORES button (top left).         |  GUI window updates to empty highscores screen (see Final Design image 2). |
|  2  | Confirm that there are no recorded high scores. |        GUI window should only display the background, HIGHSCORES and BACK. |
|  3  | Click the BACK button.                          |                               GUI window updates to the start menu screen. |
|  4  | Complete steps 1-3 from Test Case 2.            |                                      See Test Case 2 for expected results. |
|  5  | Click the BACK TO MENU button.                  |    GUI window updates to the start menu screen (see Final Design image 1). |
|  6  | Click the HIGHSCORES button again.              |  GUI window updates to highscores screen with last score as 1st highscore. |
|  7  | Repeat steps 3-6 at least five times.           |               Highscores screen displays 5 highest scores since launching. |

When this test case is completed, the highscore screen should resemble Final Design image 3.