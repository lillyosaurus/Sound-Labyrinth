---
layout: page
title: Sound Labyrinth - Implementation
description: A page describing the implementation of the project and the history of the project.
sitemap:
    priority: 0.7
    lastmod: 2017-11-02
    changefreq: weekly
---

## project history.
The project started out as a concept where a user could play the game via audio or visual input and have the same experience out of the box. We were originally considering having a 'chase style game wher the user must escape a maze while they are being chassed by a minotaur-like creature. During our first architecture reviewthe difficulty of audially communicating the position of an object moving around the maze seperate of the player was brought to our attention. the simplest solutions we had involved implementing full 3D sound and realtime audio. This proved to be to ambitious for the time frame of the project and so we pivoted the concept of the game to be more focused on exploring a world and talking to static entities to discover a story. From there we refined our program class structure to reflect the structure necessary for implementing this version of the game.

<span class="image fit"><img src="{{ "/images/footstep_comparason.png" | relative_url }}" alt="An image showing the class structure of the program." /></span>

The inital conception of the project had a flat pixel art style as this was the easiest style to generate with the pygame draw functions. We handdrew some concept images on a whiteboard just to get feedback on if the pixilated look would work well for the image. This resulted in a 'sketched' rendition of pixel art.The students we solicited feedback from really enjoyed the 'sketched' art style of our concept images. This led us to adopt that style as the graphical style for the game itself. 
<span class="image fit"><img src="{{ "/images/footstep_comparason.png" | relative_url }}" alt="An image showing the differnet graphical styles. The inital mate grey graphical style is on the left while the final sketched style is on the right. " /></span>

The shift in graphical design manifested several ways. we pivoted from drawing graphics with the pygame draw functions and started using imported graphics drawin ontop of sprite images. Secondly it caused us to develop a story for the game befiting the new style of the game we had developed. The sketched design felt reminiscent of concept artwork we had seen of souls and spirits. From this arrose the idea that the characters in the world were souls whom the player has to help. When explaining the question of why the player was helping the souls we came up with the idea that the character was cursed to help these souls to repay for what they did in life. From this we developed the story setting and context which is briefly summarized in the introductory video on the home page of this website.

After taking this feedback and generating the story we worked on creating the minimum viable deliverable of this project. An experience where the player can navigate a maze using rudimentary pinging of walls to prode visual and audio cues for navigation.

We then performed another archetecture review where we presented the game experience we had so far. From this testing we realized several issues. Firstly, the game would glitch and display multiple objects if the user pinged the walls too quickly. And secondly that most people had difficulty conceptualizing thir position when they were not given feeback that their character had moved. The playtesters actually requested that we keep the bug in place and that the maze remained shown after they had pinged it once. We decided against taking this feedback because such a method would give sighted players an advantage over non sithted players. Nonsighted players are required to create a mental map of the game world and can't easily perceive locations where they have already been.The other issue about navigation made us realize that we had to iterate the player design and we added footsteps, to display visually and play audially  to signify movemnt and direction of movement.

<span class="image fit"><img src="{{ "/images/visual_comparason.png" | relative_url }}" alt="An image depicting the two options for the visual style of the game. one where the visuals adre displyed once the user pings them, and one where only the current pinged object is displayed. " /></span>

After fixing the issues we discovered, we iterated our navigation systems, and started developing the structure for NPC characters to exist in the world. A summary of the improvements follows:

- Added auomatically pinging obstacles when the player runs into them to provide the user with information that they ran into an obstacle.
- Addied a bootup page with instructions and credits
- Added txext to speach comaptability
- Added back end structure for NPCs and developed the dialogue and story surrounding two NPCs
- Implemented an introductory NPC to explain the situation and goal of the game to the player.

##Implementation
 
Add content here about the evolution of the project
