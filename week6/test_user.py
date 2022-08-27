from user import User
from item import ItemBox, Accessories
from monster import Monster

test_user = User(2, 2)

# Test 1 :  'take_monster_exp' function and 'level_up'
for i in range(10):
    test_user.take_monster_exp(i * 5)
    assert(test_user.level == (i + 1))

# Test 2 : equip item test
itembox_weapon = ItemBox(0, 0, 'W', 3)
itembox_armor = ItemBox(0, 0, 'A', 3)
itembox_acc = ItemBox(0, 0, 'O', 'HU')

pre_attack = test_user.attack
pre_defense = test_user.defense

test_user.equip_item(itembox_weapon)
assert(test_user.attack == pre_attack + int(itembox_weapon.data))
assert(test_user.weapon is not None)

test_user.equip_item(itembox_armor)
assert(test_user.defense == pre_defense + int(itembox_armor.data))

test_user.equip_item(itembox_acc)
assert(test_user.effect_flag['HU'] == True)

# Test 3 : Fight Monster
# Lv.10 User Data
# HP : 65
# EXP : 0
# ATK : 20 + 3
# DEF : 20 + 3

# Test 3 - 1 : One Shot One Kill Monster
monster_osok = Monster(0, 0, 'OSOK', 1, 1, 1, 1)
assert(test_user.fight_monster(monster_osok) == False)
assert(test_user.hp == 65)
assert(test_user.exp == 1)
assert(monster_osok.hp <= 0)

# Test 3 - 2 : Easy Monster
monster_easy = Monster(0, 0, 'EASY', 3, 2, 40, 5)
assert(test_user.fight_monster(monster_easy) == False)
assert(test_user.hp == 64)
assert(test_user.exp == 6)
assert(monster_easy.hp <= 0)

# Test 3 - 3 : Boss Monster and 'HU' Test
boss = Monster(0, 0, 'BOSS', 1000, 0, 24, 10)
assert(test_user.fight_monster(boss, True) == False)
# HU -> Full Hp : 65 -> Only 1 damage from Boss -> 64
assert(test_user.hp == 64)
assert(test_user.exp == 16)

# Test 3 - 4 : Strong Monster
monster_strong = Monster(0, 0, 'STRONG', 60, 100, 100, 10)
assert(test_user.fight_monster(monster_strong) == True)
assert(test_user.hp <= 0)
assert(monster_strong.hp == 98)

# Test 4 : Step on The Trap
test_user2 = User(0, 0)

for i in range(10):
    test_user2.take_monster_exp(i * 5)

assert(test_user2.step_on_the_trap() == False)
assert(test_user2.hp == 60)

dx_acc = Accessories('DX')
test_user2.equip_accessories(dx_acc)
assert(test_user2.step_on_the_trap() == False)
assert(test_user2.hp == 59)

# Test 5 : Reincarnation

re_acc = Accessories('RE')
test_user2.equip_accessories(re_acc)
assert(test_user2.fight_monster(monster_strong) == False)
assert(test_user2.position == (0, 0))
assert(test_user2.hp == test_user2.max_hp)
assert(test_user2.effect_flag['RE'] == False)
assert(test_user2.accessories_num == 1)
assert(monster_strong.hp == monster_strong.max_hp)
