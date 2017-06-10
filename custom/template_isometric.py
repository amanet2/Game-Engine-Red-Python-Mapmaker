from models.clients import Map,Scene,Object,Entity
from utils.scene_utils import SceneUtils

'''
EDIT THE OBJECT REFERENCE DICT AND THE CODE DICT AT THE TOP
THEN FILL IN TEMPLATES BELOW.
HIGHLY RECCOMENDED THAT YOU MAKE USE OF THAT `INSERT` KEY
AND FIND/REPLACE WITH REGULAR EXPRESSIONS
'''

class MapDoc():
    new_map = Map('custom_isometric')
    new_map.scene_size = 3000
    new_map.cell_size = 100
    scene_utils = SceneUtils(new_map)


    new_map.obj_defs ={
        'scenery_grass':'objects/scenery/sceneryGrassTile.png',
        'scenery_grass_lr':'objects/scenery/sceneryGrassTileLR.png',
        'scenery_grass_ul':'objects/scenery/sceneryGrassTileUL.png',
        'scenery_block':'objects/scenery/sceneryBlock.png',
        'scenery_tree':'objects/scenery/sceneryBlockTree.png',
        'big_red':'animations/bigredrotate/bigRed090.png',
        'enemy':'animations/bigredrotate_evil/bigRed090_evil.png',
        'next_scene_portal':'animations/portal_green/portal_green0.png',
        'prev_scene_portal':'animations/portal_blue/portal_blue0.png',
        'big_red_animation_pack':'animations/bigredrotate',
        'enemy_animation_pack':'animations/bigredrotate_evil',
        'next_scene_portal_animation_pack':'animations/portal_green',
        'prev_scene_portal_animation_pack':'animations/portal_blue'
    }

    new_map.obj_codes = {
        '0':'scenery_block',
        '1':'scenery_tree',
        '*':'scenery_grass',
        'v':'scenery_grass_lr',
        '^':'scenery_grass_ul',
        'e':('enemy',('enemy_animation_pack',0)),
        'p':('big_red',('big_red_animation_pack',0)),
    }

    # =====

    scene0 = Scene('test-scene1','dungeonbackground.jpg',new_map.scene_size,new_map.scene_size)

    scene_grid = '''
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,v,*,*,*,*,*,*,*,*,*,*,^,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,v,*,p,*,*,*,*,*,*,*,*,^,v,*,*,*,*,*,*,*,*,^,-,
-,-,-,-,-,-,v,*,*,*,*,*,*,*,1,*,*,^,v,*,*,*,*,1,*,*,*,^,-,-,
-,-,-,-,-,v,*,*,*,*,*,1,*,*,*,*,^,v,*,1,*,*,*,*,*,*,^,-,-,-,
-,-,-,-,v,*,*,*,*,1,*,*,*,*,*,^,v,*,*,*,*,*,*,*,*,^,-,-,-,-,
-,-,-,v,*,*,*,*,*,*,*,*,*,*,^,v,*,*,1,*,*,*,*,*,^,-,-,-,-,-,
-,-,v,*,*,*,*,*,*,1,*,*,*,^,v,*,*,*,*,*,1,*,*,^,-,-,-,-,-,-,
-,v,*,*,*,*,*,*,*,*,*,*,^,v,*,*,*,*,*,*,*,*,^,-,-,-,-,-,-,-,
v,*,*,*,*,*,*,*,*,*,*,^,v,*,*,*,*,*,*,*,*,^,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,v,*,*,*,*,*,*,*,*,^,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,e,-,-,-,-,-,e,-,-,-,-,-,e,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
'''

    scene_utils.things_setup_from_grid(scene0,scene_grid)

    # =====

    new_map.scenes.append(scene0)
