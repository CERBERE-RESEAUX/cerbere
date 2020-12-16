import json
import nmap

class Model:

    def __init__(self):
        self.nmScan = nmap.PortScanner()
        self.e1 = '127.0.0.1'
        self.e2 = '20-30'
        self.res = None

    # def calculate(self):
    #     x, y = np.meshgrid(np.linspace(-5, 5, self.xpoint), np.linspace(-5, 5, self.ypoint))
    #     z = np.cos(x ** 2 * y ** 3)
    #     self.res = {"x": x, "y": y, "z": z}

    def show_entry_fields(self):
        json_res = self.nmScan.scan(self.e1, self.e2) 
        return json.dumps((json_res), indent=4)
