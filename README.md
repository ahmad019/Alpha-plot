# Alpha-plot
Image-processing-project//Physics 

Code for the ball motion tracking project

<h1>Introduction:</h1>

<p>The aim of this project is to use computer vision technique to identify an object and detect its motion and calculating the value of 'g' using the collected data. The code of this project is written in python.</p>

<h1>Elements:</h1>

<p>The following are the elements for this project, the video and code is set to work, but if anyone want to run their own video should know this:
>The camera used to make the video had 240fps
>This code only detects red colored ball (can be easily modified)
>The conversion from pixel to cm is totally based on the scale of the video


<h1>Calculations</h1>

<p>
>Diameter of the ball used = 6.8cm
>Diameter in pixels = 32px

Which gives us,
> 1 pixel = 0.212 cm

Projectile equation used: 

![equation](http://www.mathwords.com/p/p_assets/p108.gif)

27 px - (4.32 x 10^3)t -  (4.05 x 10^-2)t^2

<i>using regression for second degree polynomial</i>

0.5(g) = -4.051 x 10^-2 px/f^2 				<i>such that; 1frame = 1/240s </i>

<b>gives</b> 

g = -991.7 cm/s^2 with 1.1% uncertainity!!






