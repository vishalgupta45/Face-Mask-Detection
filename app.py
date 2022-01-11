from views.AuthView import AuthView 
from views.DetectionView import DetectionView

class MyApp:
    
    def run(self):
        av = AuthView()
        av.transfer_control = self.detection
        av.load()
        

    def detection(self):
        dv = DetectionView()
        dv.load()

ma = MyApp()
ma.run()
    