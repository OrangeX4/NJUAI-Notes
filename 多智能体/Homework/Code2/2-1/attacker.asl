/* Initial goals */

!get(beer).   // initial goal: get a beer
!check_bored. // initial goal: verify whether I am getting bored

+!get(beer) : true
   <- .send(robot, achieve, has(owner,beer)).

