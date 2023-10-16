// gets the price for the product,
// a random value between 100 and 110.
price(_Service,X) :- .random(R) & X = (10*R)+100.

plays(initiator,c). 

// randomly cancel a CNP
!randomlyCancel(1, 0.5, 3000).
// !randomlyCancel(1, 0.5, 7000).

/* Plans */

+!randomlyCancel(CNPId, Prob, Delay)
   <- .wait(Delay); // wait 3 seconds
      .random(R);
      if (R < Prob) {
        +cancel(CNPId);
      } else {
        .print("I don't want to cancel ",CNPId,".");
      }.

// send a message to the initiator introducing myself as a participant
+plays(initiator,In)
   :  .my_name(Me)
   <- .send(In,tell,introduction(participant,Me)).

// answer to Call For Proposal   
@c1 +cfp(CNPId,Task)[source(A)]
   :  plays(initiator,A) & price(Task,Offer)
   <- +proposal(CNPId,Task,Offer); // remember my proposal
      .send(A,tell,propose(CNPId,Offer)).

// answer to Abort Call For Proposal
@c2 -cfp(CNPId,Task)[source(A)]
   :  plays(initiator,A)
   <- .print("CNP ",CNPId," for ",Task," aborted.").
      -proposal(CNPId,_,_). // clear memory

@r1 +accept_proposal(CNPId)
   :  proposal(CNPId,Task,Offer)
   <- .print("My proposal '",Offer,"' won CNP ",CNPId,
             " for ",Task,"!").
      // do the task and report to initiator
      
@r2 +reject_proposal(CNPId)
   <- .print("I lost CNP ",CNPId, ".");
      -proposal(CNPId,_,_). // clear memory

// handle cancel
@r3 +cancel(CNPId)
   :  plays(initiator,A)
   <- .print("I want to cancel ",CNPId);
      .send(A,tell,cancel(CNPId)).

@r4 +cancel_succeeded(CNPId)
   <- .print("I successfully canceled ",CNPId,".");
      -proposal(CNPId,_,_). // clear memory

@r5 +cancel_failed(CNPId)
   <- .print("I failed to cancel ",CNPId,".").