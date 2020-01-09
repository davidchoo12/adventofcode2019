import heapq

maze = '''                                     V       Z       Q         X         Z Q     J     C                                         
                                     O       B       F         W         Z H     M     A                                         
  ###################################.#######.#######.#########.#########.#.#####.#####.#######################################  
  #...#...#.#.#...................#.....#...........#...#.....#...#.#...#.....#.....#...........#.......#.#...................#  
  ###.###.#.#.#####.#.###.###.#########.###########.###.#.#.###.###.###.#.#.#.###.#.#.###.#.###.###.#####.#.#########.#########  
  #...#.....#.#.....#.#.#.#...#.#.........#.........#...#.#.#...#.....#...#.#.#.#.#.#...#.#.#.#.#.....#.........#...#.....#.#.#  
  #.#.#####.#.###.#####.#####.#.#######.###.#.#######.###.#.#.#.#.#.#####.#####.###.###.#####.###.###.#####.#####.#.#######.#.#  
  #.#...#...#.#...#...#.....#.....#.#.....#.#...#...#.....#.#.#.#.#.......#.....#.#.#.#...#...#.....#...#.#...#...#.....#...#.#  
  #####.###.#.#######.#####.###.###.###.#######.#.#.#######.#.#######.#.#.#.#.###.#.#.#.###.#####.#######.#.###.#######.#.###.#  
  #.#.....#.....#.....#.................#.#.......#.#.....#.#...#...#.#.#...#.....#.#.........#.#...........#.#.......#.#...#.#  
  #.#.###.###.#######.###.###.#.###.#.#.#.#.#######.#.###.#.#.#.#.###.#############.#######.###.#.#######.###.#.#########.###.#  
  #...#...................#.#.#.#...#.#.#.....#.....#...#...#.#...#...........#.....#.................#.......#...............#  
  ###.#.#.#.#####.###.#.###.#####.#.###.#########.#####.###.###.#########.###.###.#.###.#####.#.#.#.###.#.#.#.#.#.###.#.#####.#  
  #.#.#.#.#...#.#...#.#.#.........#.#.#.......#.....#...#.....#...#.#.......#.#...#.#.......#.#.#.#.#.#.#.#.#...#...#.#.#.#.#.#  
  #.###########.#####.#.#.#.#.#######.#.#.#####.#.###.#####.###.#.#.#.#.###.#######.#.#.###.###.#.###.#.#.###.###.#######.#.###  
  #.#...#.........#...#.#.#.#.#.#.#...#.#...#...#.#.......#.#...#.#.#.#...#.#.......#.#.#...#...#...#.#.#.#.#.#.#.#.....#.#...#  
  #.#.###########.#.###.#######.#.###.#####.#.#########.###.#.###.#.#.#####.#####.#########.#####.###.###.#.#.#.###.#####.#.###  
  #.#.#.....#.........#.#.......#.#.........#.....#.......#.#...#.#.....#...#...........#.....#.#.#.....#.#.............#.....#  
  #.#.#####.#####.#####.#######.#.###.#######.#######.#######.###.###.#############.#######.###.#####.#############.#####.###.#  
  #...#.#.#.....#.....#.#...................#.......#.#.........#.#...#.#.#.....#.#.....#.......#.#.....#...#.#.#.....#.#.#...#  
  #.#.#.#.#.#################.#.###.#.###.###.#######.#########.#####.#.#.###.###.#.#####.#.#####.###.###.###.#.#######.#####.#  
  #.#.#.....#...#.#...#.......#.#...#...#.#...#.#.#.......#...#...#.....#.#...........#.#.#...#.#...#.#...#.....#.#.....#.#...#  
  #.#######.###.#.#.#################.###.#.#.#.#.###.#.#####.#.#####.###.###.#########.#.#.###.#.###.#.#####.###.#.#.###.###.#  
  #.#.#...........#.#.....#.....#.#.#...#.#.#.#.#...#.#...#...#...#.......#.#...#.......#.#...#.....#...#.#.......#.#.....#.#.#  
  #.#.###.###.#.###.#####.#####.#.#.#.#######.#.#.###.#######.#.#######.###.###.#.#.#.#####.#####.###.###.###.#########.###.#.#  
  #.#.#.#...#.#.#...#.#.......#.#...#.....#.....#.#.....#.......#...#.....#.....#.#.#...#.............#...#.......#.#...#...#.#  
  #.#.#.#######.###.#.###.#.#.#.#.#.#.###.###.###.###.#.#####.###.#.#.#######.###.#.#######.###.#.#.###.#.#.#.#.###.###.###.#.#  
  #.#.#.#.#.#.....#.#.#...#.#.....#...#.#...#.#.....#.#.#...#.....#.#...#...#.#...#.....#.#.#.#.#.#...#.#.#.#.#.#.#...#.#.#...#  
  #.#.#.#.#.###.###.#.#######.#.#.###.#.#.###.#.#.###.###.###.#####.###.###.#.#.###.#####.#.#.#########.#####.###.#.###.#.#.###  
  #...#...#...#...#...#.......#.#.#.....#.#.#...#.#.......#.....#...#...#.....#.#...#...#...#.#.#...#.....#.#.....#...#...#...#  
  #.#.###.###.#.###.#####.###########.#####.#####.#####.###.#####.###.#######.#.#.#####.#.###.#.###.#.#####.###.#####.###.###.#  
  #.#.#...#...........#.#...#.#...#...#.#...#.#...#.#...#...#...#...#.....#.#.#.#...#...........#.......#...#.#.#.#...#.#.#.#.#  
  #.#####.###.###.#####.#####.###.###.#.###.#.#.###.#.#########.###.###.###.#.#.###.#######.###.###.###.#.###.#.#.###.#.#.#.#.#  
  #.#.#.#.#...#.#.#...#.#.#.............#.........#.....#.............#...#.....#...#.......#.....#.#.#...#.....#...#.#.#.#...#  
  #.#.#.#.###.#.###.###.#.###.#.#######.#######.#######.#####.#########.###########.###.#############.#.#####.###.###.#.#.#.###  
  #...#.............#.#...#.#.#...#    R       N       E     F         H           K   X      #.#.#.....#.......#.#...#...#.#.#  
  #.###########.#####.###.#.#######    H       K       K     J         Q           R   W      #.#.#.#########.###.###.###.#.#.#  
  #...#.#...#...#.#.#...#.#.....#.#                                                           #.#.....#...#...#...#.#.#.#...#.#  
  #.###.###.###.#.#.#.###.#.#####.#                                                           #.#.#####.###.#####.#.#.#.#.###.#  
BI..#...#...#.#.......#.....#.....#                                                         MX....#.........#...#.#.#...#......MG
  #.#.#####.#.#.#########.#####.###                                                           #.#.#.#.#####.###.#.#.###.#.###.#  
  #.......#.........#.#.#.#...#....ZN                                                         #.#...#.#.........#...#.....#....KR
  ###.###.#.#.#######.#.#.#.#####.#                                                           #.#.#.###.#####.#.#.#.#.###.#.#.#  
  #.....#...#.#.#...#.#...#...#.#.#                                                         BQ..#.#.#...#.#...#.#.#.#.#...#.#.#  
  #.#########.#.#.###.###.#.#.#.#.#                                                           #.#########.#####.#.#.#.###.#.#.#  
  #...#.#...................#.....#                                                           #.#...#...#.#...#...#...#.#.#.#.#  
  #.###.#########################.#                                                           #####.###.#.#.###########.#######  
  #.#.........#...........#.....#.#                                                           #...#...#.....................#.#  
  #.###.#####.###.#######.#.###.###                                                           #.#####.###.#.#####.#.#######.#.#  
  #.#...#...#...#.#...#.....#.....#                                                         QX....#...#...#.#.#...#.....#.....#  
  #####.#.#####.#.#############.###                                                           #.#####.#.#####.#######.#.#.###.#  
  #.#.....#.....#...#...#.#.....#.#                                                           #.#.....#.#...#...#.....#.#.#....EK
  #.#####.#.#######.#.###.###.#.#.#                                                           #.#.###.#.#.#.###.###############  
MX........#.............#.#.#.#....LV                                                         #.....#...#.#.#...#.#.....#...#.#  
  ###.#####.#####.#.#####.#.#.###.#                                                           #.###########.#.###.###.#####.#.#  
  #.#.#.........#.#.#.......#.#...#                                                           #.#.................#.#.#.#.....#  
  #.#.###.###.###.###.###.#.#######                                                           ###.#.###.###.###.#.#.#.#.###.#.#  
VL..#.#.#...#.#.#.#...#...#.#.#...#                                                           #...#...#...#...#.#.......#...#..SX
  #.###.#######.#####.#.#####.#.###                                                           #.#.#.###.###.#####.#####.#.###.#  
AA..#.........#.#.....#.........#..ZK                                                         #.#.#.#.....#.#.......#...#...#.#  
  #.#.#####.###.###.###.###.###.#.#                                                           #.#######.###########.#.###.#.###  
  #.....#.............#...#.#.#...#                                                         ZB....#.#.....#...#...#.#.....#...#  
  #########.###.#.###.#######.#.#.#                                                           #.###.#######.###.#####.#########  
  #.....#.#.#...#.#.....#.#.....#.#                                                           #.#.......#.#.......#.#.#...#....QX
  ###.#.#.###.#######.###.#########                                                           ###.###.#.#.#.#.#.###.#####.#.#.#  
  #...#...#.#.#.....#.#...#.#...#.#                                                           #.....#.#.....#.#.....#...#...#.#  
  #.#####.#.#######.###.###.#.###.#                                                           #.#####.#.#######.#.###.###.#####  
  #...#.#.#.........#.#.#.#.....#..MG                                                         #.#.#.#.#.#...#...#.#.....#.....#  
  ###.#.#.#.#.#.#.#.#.#.#.###.#.#.#                                                           #.#.#.#####.#######.#.#.#######.#  
RH....#.#...#.#.#.#...........#...#                                                         CA..#.#.#.#...#.........#.........#  
  #####.#######.#####.#.#####.#.###                                                           ###.#.#.###.#######.###.#####.#.#  
  #.#.#.......#.....#.#...#...#.#.#                                                           #.#.#.....#.....#...#...#...#.#.#  
  #.#.###.###.#.#.###.###########.#                                                           #.#.#.#.###.###.#.#.#######.###.#  
LV..#.....#...#.#.#.#.#...#.#......NU                                                         #.#...#.....#.#.#.#.#.#.#.....#.#  
  #.#.#####.#######.###.###.###.#.#                                                           #.#.#####.###.#######.#.#.#######  
  #...#.#...#...#.#.#.....#.#.#.#.#                                                           #.......#.#.#...#.#.#...#.#.#...#  
  #.###.#.###.#.#.#.###.#.#.#.###.#                                                           #.#.#.###.#.#.###.#.#.###.#.#.###  
  #.#.#.#.....#.........#.........#                                                         VO..#.#.#.#........................DV
  ###.#.###.###.#.#.###.#.#.#######                                                           #######.#######.#.#.#############  
  #.#.#...#.#...#.#.#...#.#.....#..VL                                                         #.....#.#.....#.#.#.#............BQ
  #.#.#.#####.#.#########.#.#####.#                                                           #.###.#.#.#############.###.#.###  
  #.......#.#.#.....#.#...#.#.....#                                                           #.#.....#...#.#.....#.....#.#...#  
  #.#####.#.#########.#########.###                                                           #.#####.###.#.###.#.#####.#.#.###  
MF....#...#...#...#.....#.....#...#                                                         BI....#...#.#...#...#.#.....#.#.#.#  
  #####.###.#.###.###.#.#.#######.#                                                           #.###.###.#.#####.#.###.#######.#  
  #.........#.........#...........#                                                           #...#.............#.........#...#  
  ###.###.###.#.#####.###.###.###.#          J       D   S         M   Q       Q       X      #####.###.###.#.###.#.#.#.#.###.#  
  #...#...#...#...#...#.#.#.#.#...#          M       V   X         F   F       H       I      #.#...#.....#.#...#.#.#.#.#.....#  
  #.#.###.###.#.#######.#.#.#.###.###########.#######.###.#########.###.#######.#######.#######.###.#######.###.###.###.#.#.###  
  #.#.#.#...#.#.#...........#...#.#.#.#.....#.#.........#.....#.....#.#...#.......#.#.............#.#.........#.#.....#.#.#.#.#  
  ###.#.#.#.###.#####.###.#.#######.#.#.###.#.#.#.#.#.###.#.#######.#.#.#####.#####.###.#.#.###.###.###.#.#.#.#####.#####.###.#  
  #.....#.#.#...#.....#...#.....#.......#.....#.#.#.#...#.#.....#...#.#.....#.......#...#.#...#.#.....#.#.#.#.#.........#.....#  
  #.###.#######.#####.###.#.#######.#.#.#.#####.#####.#####.#####.#.#.###.#.#####.#####.###.#####.#######.###.###.###.#####.###  
  #...#...#.......#.#...#.#...#.....#.#.#.#...#.....#.#.....#...#.#.....#.#.#.....#.#.....#...#.#.....#...#.#.#.....#...#.....#  
  #####.#####.###.#.#.#.#.#######.#.###.###.#.#.#.#########.#.###.###.###.#####.#.#.#.###.#####.###.#######.###.###.#.#####.#.#  
  #.....#.#...#.....#.#.#...#.....#.#...#...#.#.#...#.....#.....#.#...#.#.#.#...#.#...#.#.#.......#...#.#.....#...#.#...#...#.#  
  #####.#.#.#####.#####################.#.###.#.#.#####.#.#.#.#####.###.#.#.###.###.#.#.#####.#.#######.#.###.#.###.#.#.#.#.###  
  #...#.#.....#.....#...#.#...#.#.#.#.....#...#.#.#.#...#.#.#.#...#.#.#.#.....#...#.#.#...#.#.#.#.#.#.....#.....#.#.#.#.#.#...#  
  ###.###.#.###.#.###.###.###.#.#.#.#.#.###.###.###.###.#.###.#.#.#.#.#.#.#.#####.###.#.###.#.###.#.#########.###.###.#####.#.#  
  #.......#...#.#...#...#...#.........#.#...#.#.....#.#.#.#...#.#.#...#...#...#.....#.....#.............#.........#...#.....#.#  
  ###.###.#.#.#.#######.#.###########.#####.#.###.#.#.#.#.#.###.#.#.#######.#######.###.###.#.#.#.#.#######.#.#######.#####.###  
  #.....#.#.#.#...#.....#.#...#.#.....#.......#...#.#...#.....#.#.....#.#...#.....#.#.......#.#.#.#...#.#...#.......#.#.......#  
  ###.###.#.###########.#.###.#.#.###########.#.#######.#######.#####.#.###.#.#####.#.###.#.#####.#####.###.#.###.#.#.#.###.###  
  #...#...#.#.......................#.#.....#.#.#...#.....#.........#.#.........#...#...#.#.#...#.#.#.....#.#.#...#.#.#.#.....#  
  ###.###############.###.#.###.#.###.#####.#.#.#.#####.#######.#.#.#####.###.###.#.#.#######.###.#.#.#######.#.#.#.#.#####.###  
  #...#.........#.....#...#.#...#.#...........#...#.#...#.#.....#.#.#.#.....#.#.#.#.#.#.........#.#.....#.#...#.#.#.#.#.......#  
  ###.#######.#############.#.#######.#.#.#.#.#.###.###.#.#####.###.#.#.#.#.###.###.#.###.#.#.#######.###.###.###.#.###.###.#.#  
  #.....#.............#.#.#.#.#...#...#.#.#.#.#.#...#.#...#.......#.#.#.#.#.#.......#.....#.#...#.#.#...#.#.#...#.#...#.#...#.#  
  ###.#####.#.#######.#.#.#.#.###.#########.###.###.#.#.#####.###.###.#.###.#####.#########.#####.#.###.#.#.###.###.###.#.###.#  
  #.......#.#.#...#.#.......#.#...............#.......#.#...#.#.......#.#...#.#.#...#.....#.........#.#.......#...#.#...#.#...#  
  ###.#####.#.###.#.#.#.#.#.###.#####.#.#.#.#########.#.###.###.#.#.#######.#.#.#.#.#.###.#.###.#.###.#.#.#########.###.###.###  
  #...#.....#.#.......#.#.#.#.#.#.....#.#.#...#.....#.#.#.#.#...#.#.....#.#...#.#.#.#...#.#...#.#.#.....#.......#.....#...#...#  
  ###.###.#.#.###.###.#####.#.#######.#######.###.###.#.#.#.###.#.#.#####.#.###.###.#.###.#.#########.#.###.#.###.#.###.#.###.#  
  #.....#.#.#.#...#.#.#.........#.....#.#.#...#...#...#.......#.#.#.#.......#.#.....#.#...#...........#...#.#.#...#.#...#...#.#  
  ###.###.#####.#.#.#.###.#.#####.#####.#.#.#.###.###.#####.#.#.###.#.###.###.#####.#.#.###.#.#.#.#######.###########.###.#.###  
  #.....#...#.#.#...#.#...#.#.#.#.#.#.....#.#.#.......#.....#.#.#.#.#.#.........#...#.#.....#.#.#.......#.#.#...#...#...#.#...#  
  #.#.#####.#.###.#########.#.#.###.#.#.#.###.###.#.###.#######.#.#########.#.#####.#.#######.###.#######.#.#.###.#########.###  
  #.#.#.......#.......#.....#.#.#.....#.#.....#.#.#.#.......#.........#.....#.#.#.#.#.......#...#...#...#.............#.#.#.#.#  
  ###.#####.#.###.#.#########.#.#.###########.#.#.#####.#.#####.#.#.###.###.###.#.#.#.###.#######.#####.###.#.#.#####.#.#.###.#  
  #.......#.#.#...#.#.............#.............#...#...#.#.....#.#...#.#.....#.....#.#.........#.........#.#.#.....#.........#  
  #########################################.#######.#####.#####.###########.###.#########.#####################################  
                                           Z       X     Z     N           H   N         F                                       
                                           K       I     N     U           Q   K         J                                       '''
# adj list for maze below {'AA': 0, 'BC': 4, 'DE': 11, 'FG': 16, 'ZZ': 23}
# maze = '''         A           
#          A           
#   #######.#########  
#   #######.........#  
#   #######.#######.#  
#   #######.#######.#  
#   #######.#######.#  
#   #####  B    ###.#  
# BC...##  C    ###.#  
#   ##.##       ###.#  
#   ##...DE  F  ###.#  
#   #####    G  ###.#  
#   #########.#####.#  
# DE..#######...###.#  
#   #.#########.###.#  
# FG..#########.....#  
#   ###########.#####  
#              Z       
#              Z       '''
# maze 3
# maze = '''             Z L X W       C                 
#              Z P Q B       K                 
#   ###########.#.#.#.#######.###############  
#   #...#.......#.#.......#.#.......#.#.#...#  
#   ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  
#   #.#...#.#.#...#.#.#...#...#...#.#.......#  
#   #.###.#######.###.###.#.###.###.#.#######  
#   #...#.......#.#...#...#.............#...#  
#   #.#########.#######.#.#######.#######.###  
#   #...#.#    F       R I       Z    #.#.#.#  
#   #.###.#    D       E C       H    #.#.#.#  
#   #.#...#                           #...#.#  
#   #.###.#                           #.###.#  
#   #.#....OA                       WB..#.#..ZH
#   #.###.#                           #.#.#.#  
# CJ......#                           #.....#  
#   #######                           #######  
#   #.#....CK                         #......IC
#   #.###.#                           #.###.#  
#   #.....#                           #...#.#  
#   ###.###                           #.#.#.#  
# XF....#.#                         RF..#.#.#  
#   #####.#                           #######  
#   #......CJ                       NM..#...#  
#   ###.#.#                           #.###.#  
# RE....#.#                           #......RF
#   ###.###        X   X       L      #.#.#.#  
#   #.....#        F   Q       P      #.#.#.#  
#   ###.###########.###.#######.#########.###  
#   #.....#...#.....#.......#...#.....#.#...#  
#   #####.#.###.#######.#######.###.###.#.#.#  
#   #.......#.......#.#.#.#.#...#...#...#.#.#  
#   #####.###.#####.#.#.#.#.###.###.#.###.###  
#   #.......#.....#.#...#...............#...#  
#   #############.#.#.###.###################  
#                A O F   N                     
#                A A D   M                     '''
maze_lines = maze.splitlines()
height = len(maze_lines)
width = len(maze_lines[0])
portal_name_len = 2
# edges = {} # 0: outer top, 1: outer bottom, 2: outer left, 3: outer right, 4: inner top, 5: inner bottom, 6: inner left, 7: inner right
outer_edge_top = portal_name_len
outer_edge_left = portal_name_len
outer_edge_right = width - portal_name_len - 1
outer_edge_bottom = height - portal_name_len - 1
inner_edge_top = -1
inner_edge_left = -1
inner_edge_right = -1
inner_edge_bottom = -1
inner_edge_start = False
outer_top = {} # indexed by col
outer_left = {}
outer_right = {}
outer_bottom = {}
inner_top = {}
inner_left = {}
inner_right = {}
inner_bottom = {}
for i, line in enumerate(maze_lines):
  for j, char in enumerate(line):
    if char == ' ' or char == '.' or char == '#':
      if char == ' ' and inner_edge_top == -1 and portal_name_len < i < width - portal_name_len and portal_name_len < j < width - portal_name_len:
        inner_edge_start = True
        inner_edge_top = i - 1
        inner_edge_left = j - 1
      elif inner_edge_top != -1 and inner_edge_right == -1 and char == '#':
        inner_edge_right = j
      elif inner_edge_start and j == inner_edge_left + 1 and char == '#':
        inner_edge_bottom = i
        inner_edge_start = False
      continue
    if i < outer_edge_top: # outer top
      outer_top.setdefault(j, '')
      outer_top[j] += char
    elif j < outer_edge_left: # outer left
      outer_left.setdefault(i, '')
      outer_left[i] += char
    elif j > outer_edge_right: # outer right
      outer_right.setdefault(i, '')
      outer_right[i] += char
    elif i > outer_edge_bottom: # outer bottom
      outer_bottom.setdefault(j, '')
      outer_bottom[j] += char
    elif i <= inner_edge_top + portal_name_len: # inner top
      inner_top.setdefault(j, '')
      inner_top[j] += char
    elif j <= inner_edge_left + portal_name_len: # inner left
      inner_left.setdefault(i, '')
      inner_left[i] += char
    elif j >= inner_edge_right - portal_name_len: # inner right
      inner_right.setdefault(i, '')
      inner_right[i] += char
    else: # inner bottom
      inner_bottom.setdefault(j, '')
      inner_bottom[j] += char
locs_portals = {} # {y1: {x1: 'AB0', ...}, y2: {x2: 'AB1', ...}, ...} (suffix 0 for outer, 1 for inner)
portals_locs = {} # {'AB0': [y1, x1], 'AB1': [y2, x2], ...}
for j, v in outer_top.items():
  portals_locs[v + '0'] = [outer_edge_top, j]
locs_portals[outer_edge_top] = {k: v + '0' for k, v in outer_top.items()}
for i, v in outer_left.items():
  portals_locs[v + '0'] = [i, outer_edge_left]
  locs_portals.setdefault(i, {})
  locs_portals[i][outer_edge_left] = v + '0'
for i, v in outer_right.items():
  portals_locs[v + '0'] = [i, outer_edge_right]
  locs_portals.setdefault(i, {})
  locs_portals[i][outer_edge_right] = v + '0'
for j, v in outer_bottom.items():
  portals_locs[v + '0'] = [outer_edge_bottom, j]
locs_portals[outer_edge_bottom] = {k: v + '0' for k, v in outer_bottom.items()}
for j, v in inner_top.items():
  portals_locs[v + '1'] = [inner_edge_top, j]
locs_portals[inner_edge_top] = {k: v + '1' for k, v in inner_top.items()}
for i, v in inner_left.items():
  portals_locs[v + '1'] = [i, inner_edge_left]
  locs_portals.setdefault(i, {})
  locs_portals[i][inner_edge_left] = v + '1'
for i, v in inner_right.items():
  portals_locs[v + '1'] = [i, inner_edge_right]
  locs_portals.setdefault(i, {})
  locs_portals[i][inner_edge_right] = v + '1'
for j, v in inner_bottom.items():
  portals_locs[v + '1'] = [inner_edge_bottom, j]
locs_portals[inner_edge_bottom] = {k: v + '1' for k, v in inner_bottom.items()}
# print(portals_locs)
# print(locs_portals)

def bfs(start_portal):
  adj_list = {}
  maze_spaces = [[char == '.' for char in line] for line in maze_lines]
  start_portal_y = portals_locs[start_portal][0]
  start_portal_x = portals_locs[start_portal][1]
  visiting_queue = [[start_portal_y, start_portal_x, 0]] # (y, x, step)
  def process_adj(y, x, step):
    target = maze_lines[y][x]
    if maze_spaces[y][x]:
      visiting_queue.append([y, x, step])
  while visiting_queue:
    # print(visiting_queue)
    front = visiting_queue.pop(0)
    y = front[0]
    x = front[1]
    step = front[2]
    maze_spaces[y][x] = False
    # top
    if y > outer_edge_top:
      process_adj(y - 1, x, step + 1)
    if y < outer_edge_bottom:
      process_adj(y + 1, x, step + 1)
    if x > outer_edge_left:
      process_adj(y, x - 1, step + 1)
    if x < outer_edge_right:
      process_adj(y, x + 1, step + 1)
    if y in locs_portals and x in locs_portals[y] and (y != start_portal_y or x != start_portal_x):
      portal = locs_portals[y][x]
      # print(f'found {portal}')
      if portal not in adj_list:
        adj_list[portal] = step
      # locs = portals_locs[portal].copy()
      # locs.remove([y, x])
      # if locs:
      #   exit = locs[0]
      #   process_adj(exit[0], exit[1], step + 1)
  return adj_list

adj_matrix = {}
for portal in portals_locs:
  adj_matrix[portal] = bfs(portal)
print({k: v for k,v  in sorted(adj_matrix.items())})

def bfs_levels(adj_matrix, start_portal, start_level, dest_portal, dest_level):
  i = 0
  sum_steps = 0
  visiting_heap = [(0, start_portal, start_level, start_portal)] # (step, portal, level, path)
  portal = start_portal
  level = 0
  while True:
    nearest = heapq.heappop(visiting_heap)
    # print(nearest)
    sum_steps = nearest[0]
    portal = nearest[1]
    level = nearest[2]
    path = nearest[3]
    # if portal == dest_portal and level == dest_level:
    #   i += 1
    #   if i == 1:
    #     return nearest
    # if portal != start_portal and portal != dest_portal:
    #   portal_isinner = portal[-1] == '1'
    #   sum_steps += 1
    #   portal = portal[0:-1] + ('0' if portal_isinner else '1') # name of opposite of portal
    #   level += 1 if portal_isinner else -1 # +1 if enter inner portal else -1
    #   path += ' ' + portal
    for adj_portal, steps in adj_matrix[portal].items():
      adj_isinner = adj_portal[-1] == '1'
      adj_opp_portal = adj_portal[0:-1] + ('0' if adj_isinner else '1') # name of opposite of portal
      adj_visit = (sum_steps + steps, adj_portal, level, path + ' ' + adj_portal)
      adj_opp_visit = (sum_steps + steps + 1, adj_opp_portal, level + (1 if adj_isinner else -1), path + ' ' + adj_portal + ' ' + adj_opp_portal)
      if level == dest_level and adj_portal == dest_portal:
        return adj_visit
      elif (level == 0 and not adj_isinner) or adj_portal == start_portal or (level != dest_level and adj_portal == dest_portal):
        continue
      heapq.heappush(visiting_heap, adj_opp_visit)
        # heapq.heappush(visiting_heap, (sum_steps + steps, adj_portal, level))
    # print(sorted(visiting_heap))
  return sum_steps

nearest = bfs_levels(adj_matrix, "AA0", 0, "ZZ0", 0)
print(f'ans {nearest}')
path = nearest[3].split(' ')
steps_sum = 0
level = 0
# print(path)
for i in range(len(path)):
  if i % 2 == 0:
    steps_sum += adj_matrix[path[i]][path[i + 1]] + 1
    level += 0 if path[i + 1] == 'ZZ0' else 1 if path[i + 1][-1] == '1' else -1
    print(f'p[i] {path[i]} p[i+1] {path[i+1]} dist {adj_matrix[path[i]][path[i + 1]]} steps {steps_sum} level {level}')
# ans 7162
# output
# {'AA0': {'VL0': 4, 'ZK1': 56}, 'BI0': {'ZN1': 50}, 'BI1': {'BQ0': 64}, 'BQ0': {'BI1': 64}, 'BQ1': {'MX1': 6, 'MG0': 60, 'KR0': 62}, 'CA0': {'XW1': 56}, 'CA1': {'QX0': 66}, 'DV0': {'VO1': 44}, 'DV1': {'XI0': 54}, 'EK0': {'QX1': 50}, 'EK1': {'QF0': 74}, 'FJ0': {'XI1': 74}, 'FJ1': {'XW0': 62}, 'HQ0': {'QF1': 44}, 'HQ1': {'ZZ0': 54, 'QH0': 56}, 'JM0': {'KR1': 78}, 'JM1': {'ZK0': 66}, 'KR0': {'MG0': 4, 'MX1': 58, 'BQ1': 62}, 'KR1': {'JM0': 78}, 'LV0': {'NU1': 64}, 'LV1': {'MX0': 76}, 'MF0': {'VL1': 60}, 'MF1': {'NU0': 52}, 'MG0': {'KR0': 4, 'MX1': 56, 'BQ1': 60}, 'MG1': {'RH0': 58}, 'MX0': {'LV1': 76}, 'MX1': {'BQ1': 6, 'MG0': 56, 'KR0': 58}, 'NK0': {'QH1': 52}, 'NK1': {'ZB0': 70}, 'NU0': {'MF1': 52}, 'NU1': {'LV0': 64}, 'QF0': {'EK1': 74}, 'QF1': {'HQ0': 44}, 'QH0': {'ZZ0': 4, 'HQ1': 56}, 'QH1': {'NK0': 52}, 'QX0': {'CA1': 66}, 'QX1': {'EK0': 50}, 'RH0': {'MG1': 58}, 'RH1': {'VO0': 46}, 'SX0': {'ZB1': 56}, 'SX1': {'ZN0': 64}, 'VL0': {'AA0': 4, 'ZK1': 58}, 'VL1': {'MF0': 60}, 'VO0': {'RH1': 46}, 'VO1': {'DV0': 44}, 'XI0': {'DV1': 54}, 'XI1': {'FJ0': 74}, 'XW0': {'FJ1': 62}, 'XW1': {'CA0': 56}, 'ZB0': {'NK1': 70}, 'ZB1': {'SX0': 56}, 'ZK0': {'JM1': 66}, 'ZK1': {'AA0': 56, 'VL0': 58}, 'ZN0': {'SX1': 64}, 'ZN1': {'BI0': 50}, 'ZZ0': {'QH0': 4, 'HQ1': 54}}
# ans (7162, 'ZZ0', 0, 'AA0  ZK1 ZK0 JM1 JM0 KR1 KR0 BQ1 BQ0 BI1 BI0 ZN1 ZN0 SX1 SX0 ZB1 ZB0 NK1 NK0 QH1 QH0 HQ1 HQ0 QF1 QF0 EK1 EK0 QX1 QX0 CA1 CA0 XW1 XW0 FJ1 FJ0 XI1 XI0 DV1 DV0 VO1 VO0 RH1 RH0 MG1 MG0 KR0 KR1 JM0 JM1 ZK0 ZK1 VL0 VL1 MF0 MF1 NU0 NU1 LV0 LV1 MX0 MX1 BQ1 BQ0 BI1 BI0 ZN1 ZN0 SX1 SX0 ZB1 ZB0 NK1 NK0 QH1 QH0 HQ1 HQ0 QF1 QF0 EK1 EK0 QX1 QX0 CA1 CA0 XW1 XW0 FJ1 FJ0 XI1 XI0 DV1 DV0 VO1 VO0 RH1 RH0 MG1 MG0 KR0 KR1 JM0 JM1 ZK0 ZK1 VL0 VL1 MF0 MF1 NU0 NU1 LV0 LV1 MX0 MX1 BQ1 BQ0 BI1 BI0 ZN1 ZN0 SX1 SX0 ZB1 ZB0 NK1 NK0 QH1 QH0 HQ1 HQ0 QF1 QF0 EK1 EK0 QX1 QX0 CA1 CA0 XW1 XW0 FJ1 FJ0 XI1 XI0 DV1 DV0 VO1 VO0 RH1 RH0 MG1 MG0 KR0 KR1 JM0 JM1 ZK0 ZK1 VL0 VL1 MF0 MF1 NU0 NU1 LV0 LV1 MX0 MX1 KR0 KR1 JM0 JM1 ZK0 ZK1 VL0 VL1 MF0 MF1 NU0 NU1 LV0 LV1 MX0 MX1 KR0 KR1 JM0 JM1 ZK0 ZK1 VL0 VL1 MF0 MF1 NU0 NU1 LV0 LV1 MX0 MX1 KR0 KR1 JM0 JM1 ZK0 ZK1 VL0 VL1 MF0 MF1 NU0 NU1 LV0 LV1 MX0 MX1 MG0 MG1 RH0 RH1 VO0 VO1 DV0 DV1 XI0 XI1 FJ0 FJ1 XW0 XW1 CA0 CA1 QX0 QX1 EK0 EK1 QF0 QF1 HQ0 HQ1 ZZ0')
# p[i] AA0 p[i+1] ZK1 dist 56 steps 57 level 1
# p[i] ZK0 p[i+1] JM1 dist 66 steps 124 level 2
# p[i] JM0 p[i+1] KR1 dist 78 steps 203 level 3
# p[i] KR0 p[i+1] BQ1 dist 62 steps 266 level 4
# p[i] BQ0 p[i+1] BI1 dist 64 steps 331 level 5
# p[i] BI0 p[i+1] ZN1 dist 50 steps 382 level 6
# p[i] ZN0 p[i+1] SX1 dist 64 steps 447 level 7
# p[i] SX0 p[i+1] ZB1 dist 56 steps 504 level 8
# p[i] ZB0 p[i+1] NK1 dist 70 steps 575 level 9
# p[i] NK0 p[i+1] QH1 dist 52 steps 628 level 10
# p[i] QH0 p[i+1] HQ1 dist 56 steps 685 level 11
# p[i] HQ0 p[i+1] QF1 dist 44 steps 730 level 12
# p[i] QF0 p[i+1] EK1 dist 74 steps 805 level 13
# p[i] EK0 p[i+1] QX1 dist 50 steps 856 level 14
# p[i] QX0 p[i+1] CA1 dist 66 steps 923 level 15
# p[i] CA0 p[i+1] XW1 dist 56 steps 980 level 16
# p[i] XW0 p[i+1] FJ1 dist 62 steps 1043 level 17
# p[i] FJ0 p[i+1] XI1 dist 74 steps 1118 level 18
# p[i] XI0 p[i+1] DV1 dist 54 steps 1173 level 19
# p[i] DV0 p[i+1] VO1 dist 44 steps 1218 level 20
# p[i] VO0 p[i+1] RH1 dist 46 steps 1265 level 21
# p[i] RH0 p[i+1] MG1 dist 58 steps 1324 level 22
# p[i] MG0 p[i+1] KR0 dist 4 steps 1329 level 21
# p[i] KR1 p[i+1] JM0 dist 78 steps 1408 level 20
# p[i] JM1 p[i+1] ZK0 dist 66 steps 1475 level 19
# p[i] ZK1 p[i+1] VL0 dist 58 steps 1534 level 18
# p[i] VL1 p[i+1] MF0 dist 60 steps 1595 level 17
# p[i] MF1 p[i+1] NU0 dist 52 steps 1648 level 16
# p[i] NU1 p[i+1] LV0 dist 64 steps 1713 level 15
# p[i] LV1 p[i+1] MX0 dist 76 steps 1790 level 14
# p[i] MX1 p[i+1] BQ1 dist 6 steps 1797 level 15
# p[i] BQ0 p[i+1] BI1 dist 64 steps 1862 level 16
# p[i] BI0 p[i+1] ZN1 dist 50 steps 1913 level 17
# p[i] ZN0 p[i+1] SX1 dist 64 steps 1978 level 18
# p[i] SX0 p[i+1] ZB1 dist 56 steps 2035 level 19
# p[i] ZB0 p[i+1] NK1 dist 70 steps 2106 level 20
# p[i] NK0 p[i+1] QH1 dist 52 steps 2159 level 21
# p[i] QH0 p[i+1] HQ1 dist 56 steps 2216 level 22
# p[i] HQ0 p[i+1] QF1 dist 44 steps 2261 level 23
# p[i] QF0 p[i+1] EK1 dist 74 steps 2336 level 24
# p[i] EK0 p[i+1] QX1 dist 50 steps 2387 level 25
# p[i] QX0 p[i+1] CA1 dist 66 steps 2454 level 26
# p[i] CA0 p[i+1] XW1 dist 56 steps 2511 level 27
# p[i] XW0 p[i+1] FJ1 dist 62 steps 2574 level 28
# p[i] FJ0 p[i+1] XI1 dist 74 steps 2649 level 29
# p[i] XI0 p[i+1] DV1 dist 54 steps 2704 level 30
# p[i] DV0 p[i+1] VO1 dist 44 steps 2749 level 31
# p[i] VO0 p[i+1] RH1 dist 46 steps 2796 level 32
# p[i] RH0 p[i+1] MG1 dist 58 steps 2855 level 33
# p[i] MG0 p[i+1] KR0 dist 4 steps 2860 level 32
# p[i] KR1 p[i+1] JM0 dist 78 steps 2939 level 31
# p[i] JM1 p[i+1] ZK0 dist 66 steps 3006 level 30
# p[i] ZK1 p[i+1] VL0 dist 58 steps 3065 level 29
# p[i] VL1 p[i+1] MF0 dist 60 steps 3126 level 28
# p[i] MF1 p[i+1] NU0 dist 52 steps 3179 level 27
# p[i] NU1 p[i+1] LV0 dist 64 steps 3244 level 26
# p[i] LV1 p[i+1] MX0 dist 76 steps 3321 level 25
# p[i] MX1 p[i+1] BQ1 dist 6 steps 3328 level 26
# p[i] BQ0 p[i+1] BI1 dist 64 steps 3393 level 27
# p[i] BI0 p[i+1] ZN1 dist 50 steps 3444 level 28
# p[i] ZN0 p[i+1] SX1 dist 64 steps 3509 level 29
# p[i] SX0 p[i+1] ZB1 dist 56 steps 3566 level 30
# p[i] ZB0 p[i+1] NK1 dist 70 steps 3637 level 31
# p[i] NK0 p[i+1] QH1 dist 52 steps 3690 level 32
# p[i] QH0 p[i+1] HQ1 dist 56 steps 3747 level 33
# p[i] HQ0 p[i+1] QF1 dist 44 steps 3792 level 34
# p[i] QF0 p[i+1] EK1 dist 74 steps 3867 level 35
# p[i] EK0 p[i+1] QX1 dist 50 steps 3918 level 36
# p[i] QX0 p[i+1] CA1 dist 66 steps 3985 level 37
# p[i] CA0 p[i+1] XW1 dist 56 steps 4042 level 38
# p[i] XW0 p[i+1] FJ1 dist 62 steps 4105 level 39
# p[i] FJ0 p[i+1] XI1 dist 74 steps 4180 level 40
# p[i] XI0 p[i+1] DV1 dist 54 steps 4235 level 41
# p[i] DV0 p[i+1] VO1 dist 44 steps 4280 level 42
# p[i] VO0 p[i+1] RH1 dist 46 steps 4327 level 43
# p[i] RH0 p[i+1] MG1 dist 58 steps 4386 level 44
# p[i] MG0 p[i+1] KR0 dist 4 steps 4391 level 43
# p[i] KR1 p[i+1] JM0 dist 78 steps 4470 level 42
# p[i] JM1 p[i+1] ZK0 dist 66 steps 4537 level 41
# p[i] ZK1 p[i+1] VL0 dist 58 steps 4596 level 40
# p[i] VL1 p[i+1] MF0 dist 60 steps 4657 level 39
# p[i] MF1 p[i+1] NU0 dist 52 steps 4710 level 38
# p[i] NU1 p[i+1] LV0 dist 64 steps 4775 level 37
# p[i] LV1 p[i+1] MX0 dist 76 steps 4852 level 36
# p[i] MX1 p[i+1] KR0 dist 58 steps 4911 level 35
# p[i] KR1 p[i+1] JM0 dist 78 steps 4990 level 34
# p[i] JM1 p[i+1] ZK0 dist 66 steps 5057 level 33
# p[i] ZK1 p[i+1] VL0 dist 58 steps 5116 level 32
# p[i] VL1 p[i+1] MF0 dist 60 steps 5177 level 31
# p[i] MF1 p[i+1] NU0 dist 52 steps 5230 level 30
# p[i] NU1 p[i+1] LV0 dist 64 steps 5295 level 29
# p[i] LV1 p[i+1] MX0 dist 76 steps 5372 level 28
# p[i] MX1 p[i+1] KR0 dist 58 steps 5431 level 27
# p[i] KR1 p[i+1] JM0 dist 78 steps 5510 level 26
# p[i] JM1 p[i+1] ZK0 dist 66 steps 5577 level 25
# p[i] ZK1 p[i+1] VL0 dist 58 steps 5636 level 24
# p[i] VL1 p[i+1] MF0 dist 60 steps 5697 level 23
# p[i] MF1 p[i+1] NU0 dist 52 steps 5750 level 22
# p[i] NU1 p[i+1] LV0 dist 64 steps 5815 level 21
# p[i] LV1 p[i+1] MX0 dist 76 steps 5892 level 20
# p[i] MX1 p[i+1] KR0 dist 58 steps 5951 level 19
# p[i] KR1 p[i+1] JM0 dist 78 steps 6030 level 18
# p[i] JM1 p[i+1] ZK0 dist 66 steps 6097 level 17
# p[i] ZK1 p[i+1] VL0 dist 58 steps 6156 level 16
# p[i] VL1 p[i+1] MF0 dist 60 steps 6217 level 15
# p[i] MF1 p[i+1] NU0 dist 52 steps 6270 level 14
# p[i] NU1 p[i+1] LV0 dist 64 steps 6335 level 13
# p[i] LV1 p[i+1] MX0 dist 76 steps 6412 level 12
# p[i] MX1 p[i+1] MG0 dist 56 steps 6469 level 11
# p[i] MG1 p[i+1] RH0 dist 58 steps 6528 level 10
# p[i] RH1 p[i+1] VO0 dist 46 steps 6575 level 9
# p[i] VO1 p[i+1] DV0 dist 44 steps 6620 level 8
# p[i] DV1 p[i+1] XI0 dist 54 steps 6675 level 7
# p[i] XI1 p[i+1] FJ0 dist 74 steps 6750 level 6
# p[i] FJ1 p[i+1] XW0 dist 62 steps 6813 level 5
# p[i] XW1 p[i+1] CA0 dist 56 steps 6870 level 4
# p[i] CA1 p[i+1] QX0 dist 66 steps 6937 level 3
# p[i] QX1 p[i+1] EK0 dist 50 steps 6988 level 2
# p[i] EK1 p[i+1] QF0 dist 74 steps 7063 level 1
# p[i] QF1 p[i+1] HQ0 dist 44 steps 7108 level 0
# p[i] HQ1 p[i+1] ZZ0 dist 54 steps 7163 level 0