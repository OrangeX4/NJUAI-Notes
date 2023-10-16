// the name of the agent playing initiator in the CNP
plays(initiator,c).

// send a message to the initiator introducing myself as a participant
+plays(initiator,In)
   :  .my_name(Me)
   <- .send(In,tell,introduction(participant,Me)).
   
