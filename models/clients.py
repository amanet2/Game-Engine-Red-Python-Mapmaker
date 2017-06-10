class Map:
    def __init__(self, source):
        self.source = source
        self.scenes = []
        self.obj_refs={}
        self.obj_codes={}
        self.scene_size = 3000
        self.cell_size = 100
class Scene:
    def __init__(self,name,bg_path,bg_sx,bg_sy):
        self.name = name
        self.background = Background(bg_path,bg_sx,bg_sy)
        self.objects = []
        self.entities = []
class Background:
    def __init__(self,path,sx,sy):
        self.path = path
        self.size_x = sx
        self.size_y = sy
class Object:
    def __init__(self,path,spx,spy,sx,sy,cl):
        self.path = path
        self.size_x = sx
        self.size_y = sy
        self.spawn_x = spx
        self.spawn_y = spy
        self.does_clip = cl
class Entity(Object):
    def __init__(self,path,spx,spy,sx,sy,ap,ar,cl):
        super().__init__(path,spx,spy,sx,sy,cl)
        self.animation_path = ap
        self.animation_rate = ar
