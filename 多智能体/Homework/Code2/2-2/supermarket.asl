last_order_id(1). // initial belief
// 库存为 100
stock(beer, 8). // initial belief
// stock(beer, 100). // initial belief

// 在家政机器人实例中, 对超市 Agent 进行修改, 使得超市在
// 商品啤酒上具有一定的库存, 每次完成订单时打印当前的
// 库存量, 当库存不足以满足订单要求时, 打印相关的失败
// 信息.
// 提交修改后的超市Agent代码, 并在初始啤酒库存分别为
// 100和8时, 给出程序的运行结果.

// plan to achieve the goal "order" for agent Ag
+!order(Product,Qtd)[source(Ag)] : stock(beer, X) & X >= Qtd
  <- ?last_order_id(N);
     OrderId = N + 1;
     -+last_order_id(OrderId);
     deliver(Product,Qtd);
     -stock(beer, X);
     +stock(beer, X - Qtd);
     .print("Stock of ", Product, " is ", X - Qtd);
     .send(Ag, tell, delivered(Product,Qtd,OrderId)).

+!order(Product,Qtd)[source(Ag)] : stock(beer, X) & X < Qtd
   <- .concat("There is no enough ", Product, ", only ", X, " but need ", Qtd, M);
      .print(M);
      .send(Ag,tell,msg(M)).
