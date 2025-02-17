import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
    def __init__(self):  
        gr.sync_block.__init__(
            self,
            name='e_Diff',   
            in_sig=[np.float32],
            out_sig=[np.float32]
        )  # Cierre correctamente el paréntesis aquí
        self.acum_anterior = 0

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y0 = output_items[0]
        N = len(x)
        
        diff = np.cumsum(x) - self.acum_anterior
        self.acum_anterior = diff[N-1]
        
        y0[:] = diff
        
        return len(output_items[0])

