class Setting:
    def __init__(self):
        self.config = {
            'right_pressed': False,
            'left_pressed': False,
            'self.img_path': 'images/alien.bmp'
        }

    def get(self, key):
        return self.config[key]
    
    def set(self, key, value):
        self.config[key] = value