# tictactoe-terminal-3d
it is 1d but work like 3d

well this is a terminal 3d game which could be played by the two players.
according to me and the aspects of the 3d tic tac toe the winning conditions are little 
different than normal tic tac toe

let me show you all
here i will use 'o' to demonstrate all the win conditions
1st (horizontal) condition
----------------
o| o| o|         .| .| .|         .| .| .|
.| .| .|         o| o| o|         .| .| .|
.| .| .|         .| .| .|         o| o| o|
-----------------
------------------

2nd (vertical) condition
---------------------
o| .| .|        .| o| .|         .| .| o|
o| .| .|        .| o| .|         .| .| o|
o| .| .|        .| o| .|         .| .| o|
--------------------
-------------------

3rd (diagonal) condition
------------------
o| .| .|        .| .| o|
.| o| .|        .| o| .|
.| .| o|        o| .| .|
--------------------
--------------------

4th (3d straight) condition
--------------------
o| .| .|          .| .| .|          .| .| .|        .| o| .|
.| .| .|          o| .| .|          .| .| .|        .| .| .|
.| .| .|          .| .| .|          o| .| .|        .| .| .| 

o| .| .|          .| .| .|          .| .| .|        .| o| .|
.| .| .|          o| .| .|          .| .| .|        .| .| .|
.| .| .|          .| .| .|          o| .| .|        .| .| .|

o| .| .|          .| .| .|          .| .| .|        .| o| .|
.| .| .|          o| .| .|          .| .| .|        .| .| .|  
.| .| .|          .| .| .|          o| .| .|        .| .| .|  and so on..
--------------------
--------------------

5th (3d vertical diagonal-part1) condition
--------------------------
o| .| .|         .| o| .|           .| .| o|   
.| .| .|         .| .| .|           .| .| .|       
.| .| .|         .| .| .|           .| .| .|       

.| .| .|         .| .| .|           .| .| .|  
o| .| .|         .| o| .|           .| .| o|       
.| .| .|         .| .| .|           .| .| .|

.| .| .|         .| .| .|           .| .| .|
.| .| .|         .| .| .|           .| .| .|
o| .| .|         .| o| .|           .| .| o|
-------------------------
-------------------------

6th (3d vertical diagonal-part2) condition
------------------
.| .| .|         .| .| .|           .| .| .|   
.| .| .|         .| .| .|           .| .| .|       
o| .| .|         .| o| .|           .| .| o|       

.| .| .|         .| .| .|           .| .| .|  
o| .| .|         .| o| .|           .| .| o|       
.| .| .|         .| .| .|           .| .| .|

o| .| .|         .| o| .|           .| .| o|
.| .| .|         .| .| .|           .| .| .|
.| .| .|         .| .| .|           .| .| .|
----------------------
----------------------

7th (3d horizontal diagonal-part1) condition
---------------------
o| .| .|         .| .| .|           .| .| .|   
.| .| .|         o| .| .|           .| .| .|       
.| .| .|         .| .| .|           o| .| .|       

.| o| .|         .| .| .|           .| .| .|  
.| .| .|         .| o| .|           .| .| .|       
.| .| .|         .| .| .|           .| o| .|

.| .| o|         .| .| .|           .| .| .|
.| .| .|         .| .| o|           .| .| .|
.| .| .|         .| .| .|           .| .| o|
-----------------------
-----------------------

8th (3d horizontal diagonal-part2) condition
---------------------
.| .| o|         .| .| .|           .| .| .|   
.| .| .|         .| .| o|           .| .| .|       
.| .| .|         .| .| .|           .| .| o|       

.| o| .|         .| .| .|           .| .| .|  
.| .| .|         .| o| .|           .| .| .|       
.| .| .|         .| .| .|           .| o| .|

o| .| .|         .| .| .|           .| .| .|
.| .| .|         o| .| .|           .| .| .|
.| .| .|         .| .| .|           o| .| .|
-----------------------
-----------------------

final condition
9th (3d diagonal) condition
---------------------
o| .| .|         .| .| o|      
.| .| .|         .| .| .|               
.| .| .|         .| .| .|             

.| .| .|         .| .| .|         
.| o| .|         .| o| .|           
.| .| .|         .| .| .|          

.| .| .|         .| .| .|         
.| .| .|         o| .| .|        
.| .| o|         .| .| .|           
-----------------------
-----------------------

so these are the conditions to increase the score by 1
it is a very simple game to understand