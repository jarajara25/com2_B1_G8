import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
    def __init__(self):  
        gr.sync_block.__init__(
            self,
            name='e_Dif',   
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.acum_anterior = 0
        
    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y = output_items[0]  # Señal de salida
        N = len(x)

        # Diferenciación acumulada: y[n] = x[n] - acum_anterior
        for i in range(N):
            y[i] = x[i] - self.acum_anterior  # Restamos el valor acumulado anterior
            self.acum_anterior = x[i]  # Actualizamos el acumulado con el valor actual
        
        return len(y)
    
