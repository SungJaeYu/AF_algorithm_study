from game import Game



game = Game()
# Test 1 : Trap Area
game.N = 5
game.M = 5
game.user = User(2, 2)
game.area_dict['^']
assert(game.user.hp == 15)

# Test 2 : Monster Area
game.area_dict['&']

