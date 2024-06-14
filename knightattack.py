while True:
    print("当前请输出攻防和")
    total_abb = int(input())
    print("请输入怪物攻击力")
    knight_attack = int(input())
    print("请输入怪物防御力")
    knight_defense = int(input())
    print("请输入怪物血量")
    knight_hp = int(input())
    print("是否双倍攻击(输入Y代表是/输入其他代表否)")
    att_double = input() == "Y"
    print("是否先攻击")
    att_first = input() == "Y"
    INT_MAX = 2**31-1
    def fight(att,defense):
        hp = knight_hp
        total_consume = 0
        if att_double:
            att = att *2
        if att <= knight_defense:
            return INT_MAX
        if att_first:
            total_consume = total_consume + knight_attack - defense
        while True:
            hp = hp - att + knight_defense
            if hp > 0:
                total_consume = total_consume + knight_attack - defense

            else:
                break

        return total_consume



    min_consume = INT_MAX
    min_att = 0
    min_defense = 0
    for att in range(total_abb):
        defense = total_abb - att
        consume = fight(att, defense)
        if consume < min_consume:
            min_consume = consume
            min_att = att
            min_defense = defense
    if min_consume == INT_MAX:
        print("无法击败")
    elif min_consume < 0:
        print("att:", min_att, "defense:", min_defense, "consume:", 0)
    else:
        print("att:", min_att, "defense:", min_defense, "consume:", min_consume)
    input("任意键继续")