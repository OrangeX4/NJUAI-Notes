plays(initiator,c). 
+plays(initiator,In)
   :  .my_name(Me)
   <- .send(In,tell,introduction(participant,Me)).

// plan to answer a CFP
+cfp(CNPId,_Service)[source(A)] 
   :   plays(initiator,A)
   <- .send(A,tell,refuse(CNPId)).

