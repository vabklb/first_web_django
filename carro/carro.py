class Carro(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro']={}
        #else:
        self.carro = carro
        
    def add(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id]={
                'producto_id':producto.id,
                'nombre':producto.nombre,
                'precio': str(producto.precio),
                'cantidad': 1,
                'imagen': producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] += 1
                    value['precio'] = float(value['precio']) + producto.precio
                    break
        self.guardar_carro()
    
    def dell(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def dell_unidad(self, producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] -= 1
                    value['precio'] = float(value['precio']) - producto.precio
                    if value['cantidad'] < 1:
                        self.dell(producto)
                        
                    break
        self.guardar_carro()

    def clean(self):
        self.session['carro']={}
        self.session.modified = True
        
        
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
                    
            
        
