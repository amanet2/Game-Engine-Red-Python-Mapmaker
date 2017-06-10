from models.clients import Map,Scene,Object,Entity

class SceneUtils:
    def __init__(self,m:Map):
        self.map = m

    def append_static_obj_to_scene(self, s:Scene,oref:str,sx:int,sy:int,solid:int):
        s.objects.append(Object(oref,sx,sy,self.map.cell_size,self.map.cell_size,solid))

    def append_entity_to_scene(self, s:Scene,oref:str,animref:str,sx:int,sy:int,animrate:str,solid:int):
        s.entities.append(Entity(oref,sx,sy,self.map.cell_size,self.map.cell_size,animref,animrate,solid))

    def get_ref_for_obj_code(self, code: str) -> str:
        try:
            toret = self.map.obj_defs[self.map.obj_codes[code]]
            # print(toret)
            return toret
        except:
            return ''

    def get_ref_for_entity_code(self, code: str) -> str:
        try:
            toret = self.map.obj_defs[self.map.obj_codes[code][0]]
            # print(toret)
            return toret
        except:
            return ''

    def get_anim_ref_for_entity_code(self, code: str) -> str:
        try:
            # print(code)
            toret = self.map.obj_defs[self.map.obj_codes[code][1][0]]
            # print(toret)
            return toret
        except:
            return ''

    def get_anim_rate_for_entity_code(self, code: str) -> int:
        try:
            toret = self.map.obj_codes[code][1][1]
            # print(toret)
            return toret
        except:
            return ''

    def things_setup_from_grid(self, scene: Scene, grid: str):
        scene_size = scene.background.size_x
        grid_rows = grid.count('\n')-1


        grid = grid.rstrip()
        grid = grid.replace(',','')
        grid = grid.replace('\n','')


        self.map.cell_size = int(scene_size/grid_rows)
        for i in range(0,grid_rows):
            for j in range(0,grid_rows):
                cell_x = int(self.map.cell_size*j)
                cell_y = int(self.map.cell_size*i)

                obj_code = grid[i*grid_rows+j]
                obj_ref = self.get_ref_for_obj_code(obj_code)
                ent_ref = self.get_ref_for_entity_code(obj_code)

                if obj_ref != '':
                    sol = 1
                    if obj_code != '0':
                        sol = 0
                    if obj_code == '1' and 'isometric' in self.map.source:
                        self.append_static_obj_to_scene(scene,self.get_ref_for_obj_code('*'),cell_x,cell_y,0)
                    self.append_static_obj_to_scene(scene,obj_ref,cell_x,cell_y,sol)

                if ent_ref != '':
                    anim_rate = self.get_anim_rate_for_entity_code(obj_code)
                    anim_ref = self.get_anim_ref_for_entity_code(obj_code)
                    sol = 1
                    if anim_rate > 0:
                        sol = 0
                    if 'custom_1' not in self.map.source:
                        self.append_static_obj_to_scene(scene,self.get_ref_for_obj_code('*'),cell_x,cell_y,0)
                    self.append_entity_to_scene(scene,ent_ref,anim_ref,cell_x,cell_y,anim_rate,sol)
