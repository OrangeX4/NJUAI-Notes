/* Initial beliefs and rules */

// initially, I believe that there is some beer in the fridge
available(beer,fridge).

// my owner should not consume more than 10 beers a day :-)
limit(beer,10).

too_much(B) :-
   .date(YY,MM,DD) &
   .count(consumed(YY,MM,DD,_,_,_,B),QtdB) &
   limit(B,Limit) &
   QtdB > Limit.


/* Plans */

// 在家政机器人实例中, 机器人 Agent 为完成目标
// !has(owner,beer) 制定了三个规划 (在课件中的标签为 h1,
// h2, h3), 但是此处的限制不够严格,因为机器人在执行规
// 划时没有确认目标来源是否来自于主人owner Agent (或是
// 其他合理的来源).
// 请为相应的代码 (课件中的robot Agent的h1, h2, h3三个规
// 划)添加上合适的条件, 使得在不影响执行结果的情况下
// 执行该目标时限制更为严格. 给出修改后的代码和修改的
// 理由.

@h1
+!has(owner,beer)[source(S)]
   :  (S == self | S == owner) & available(beer,fridge) & not too_much(beer)
   <- !at(robot,fridge);
      open(fridge);
      get(beer);
      close(fridge);
      !at(robot,owner);
      hand_in(beer);
      ?has(owner,beer);
      // remember that another beer has been consumed
      .date(YY,MM,DD); .time(HH,NN,SS);
      +consumed(YY,MM,DD,HH,NN,SS,beer).

@h2
+!has(owner,beer)[source(S)]
   :  (S == self | S == owner) & not available(beer,fridge)
   <- .send(supermarket, achieve, order(beer,5));
      !at(robot,fridge). // go to fridge and wait there.

@h3
+!has(owner,beer)[source(S)]
   :  (S == self | S == owner) & too_much(beer) & limit(beer,L)
   <- .concat("The Department of Health does not allow me to give you more than ", L,
              " beers a day! I am very sorry about that!",M);
      .send(owner,tell,msg(M)).


-!has(_,_)
   :  true
   <- .current_intention(I);
      .print("Failed to achieve goal '!has(_,_)'. Current intention is: ",I).

@m1
+!at(robot,P) : at(robot,P) <- true.
@m2
+!at(robot,P) : not at(robot,P)
  <- move_towards(P);
     !at(robot,P).

// when the supermarket makes a delivery, try the 'has' goal again
@a1
+delivered(beer,_Qtd,_OrderId)[source(supermarket)]
  :  true
  <- +available(beer,fridge);
     !has(owner,beer).

// when the fridge is opened, the beer stock is perceived
// and thus the available belief is updated
@a2
+stock(beer,0)
   :  available(beer,fridge)
   <- -available(beer,fridge).
@a3
+stock(beer,N)
   :  N > 0 & not available(beer,fridge)
   <- -+available(beer,fridge).

+?time(T) : true
  <-  time.check(T).

