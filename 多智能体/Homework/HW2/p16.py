# 攻击列表
# attacks = {('A', 'B'), ('C', 'A'), ('B', 'E'), ('E', 'C'), ('C', 'D'), ('D', 'E'), ('D', 'B')}
attacks = {('c', 'b'), ('d', 'c'), ('d', 'e'), ('e', 'd'), ('d', 'g'), ('e', 'g'), ('g', 'h'), ('e', 'f')}

def get_attackers(target):
    attackers = []
    for attack in attacks:
        if attack[1] == target:
            attackers.append(attack[0])
    return attackers

# 找出可采纳的立场
def is_acceptable_stance(stance):
    # 首先判断是否无冲突
    for i in range(len(stance)):
        for j in range(i + 1, len(stance)):
            if (stance[i], stance[j]) in attacks or (stance[j], stance[i]) in attacks:
                return False
    # 再判断是否互相辩护
    # 对于 stance 中每一个论证, 找出其攻击者
    for arg in stance:
        attackers = get_attackers(arg)
        # 对于每一个攻击者, 寻找辩护
        for attacker in attackers:
            is_defended = False
            defenders = get_attackers(attacker)
            for defender in defenders:
                if defender in stance:
                    is_defended = True
                    break
            if not is_defended:
                return False
    return True


# 遍历 b - f 中的每个立场, 即 b - f 的幂集
for i in range(1, 2 ** 7):
    stance = []
    for j in range(7):
        if i & (1 << j):
            # stance.append(chr(ord('A') + j))
            stance.append(chr(ord('b') + j))
    if is_acceptable_stance(stance):
        print(stance)

