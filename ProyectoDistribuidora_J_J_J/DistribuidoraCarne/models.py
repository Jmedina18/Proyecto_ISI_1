from django.db import models
from DistribuidoraCarne.validaciones import validar_nombre,validar_telefono,validar_correo,validar_date_time,validar_descripcion,validar_estado,validar_direccion
from DistribuidoraCarne.validaciones import validar_rtn,validar_fecha_nacimiento
from DistribuidoraCarne.validaciones import validar_date_time, validar_salario, validar_salario_base, validar_id, validar_stock_actual,validar_Cantidad
from DistribuidoraCarne.validaciones import validar_Total_Cotizacion,validar_numero_tarjeta,validar_fecha_vencimiento,validar_cvv,validar_valor_impuesto,validar_nombre_titular

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50, default='Identidad')
    def __str__(self):
        return self.nombre
    

    
class TipoCargo(models.Model):
    nombre = models.CharField(max_length=50, validators=[validar_nombre])
    descripcion = models.CharField(max_length=200, validators=[validar_descripcion])
    salario_base = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_salario_base])
    descripcion_actualizacion = models.CharField(max_length=255, validators=[validar_descripcion])
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateField(auto_now=True)    
    def __str__(self):
        return self.nombre
    
class Sucursal(models.Model):
    nombre_surcusal = models.CharField(max_length=65, validators=[validar_nombre])
    ciudad = models.CharField(max_length=65, validators=[validar_nombre])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    telefono = models.CharField(max_length=50, validators=[validar_telefono])
    rtn = models.CharField(max_length=14, validators=[validar_rtn])
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateField(auto_now=True)


    def __str__(self):
        return self.nombre_surcusal
    
    class Meta:
        verbose_name = 'Surcusal'
        verbose_name_plural = 'Surcusales'  
    
class Clientes(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE,default=1)
    id_cliente = models.CharField(max_length=14)  # Campo para el número de identificación
    nombre_cliente = models.CharField(max_length=65,validators=[validar_nombre])
    telefono = models.CharField(max_length=20, validators=[validar_telefono])
    rtn = models.CharField(max_length=14, validators=[validar_rtn])
    correo = models.CharField(max_length=50, validators=[validar_correo])
    direccion = models.CharField(max_length=150, validators=[validar_direccion])
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
        def __str__(self):
            return self.nombre_cliente
    
class Empleados(models.Model):
    id_empleado = models.CharField(max_length=15, validators= [validar_id])# Campo para el número de identificación
    nombre_empleado = models.CharField(max_length=65 ,validators=[validar_nombre])
    fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])
    salario = models.DecimalField(max_digits=10, decimal_places=2,validators=[validar_salario])
    email = models.CharField(max_length=50, validators=[validar_correo])
    telefono = models.CharField(max_length=50, validators=[validar_telefono])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    tipo_cargo = models.ForeignKey(TipoCargo, on_delete=models.CASCADE,default=1)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE,default=1)
    surcusal = models.ForeignKey(Sucursal, on_delete=models.CASCADE,default=1)


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre_empleado    
  
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=65, validators=[validar_nombre])
    stock_actual = models.CharField(max_length=4, validators=[validar_stock_actual])
    estado  = models.BooleanField(null=True, validators=[validar_estado])

    def __str__(self):
        return self.nombre_categoria        

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=65, validators=[validar_nombre])
    telefono = models.CharField(max_length=8, validators=[validar_telefono])
    correo = models.CharField(max_length=65, null=True,validators=[validar_correo])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    rtn = models.CharField(max_length=14,validators=[validar_rtn])
    nombre_proveedor = models.CharField(max_length=65, validators=[validar_nombre])
    celular_contacto = models.CharField(max_length=8,validators=[validar_telefono])
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateField(auto_now=True)
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre_proveedor

class Impuesto(models.Model):
    nombre_impuesto = models.CharField(max_length=20,validators=[validar_nombre])
    descripcion_impuesto = models.CharField(max_length=50,validators=[validar_descripcion])
    valor_impuesto = models.DecimalField(max_digits=5, decimal_places=2,default=00.00, validators=[validar_valor_impuesto])

    def __str__(self):
        return f"{self.tipo_impuesto} - {self.nombre_impuesto}"

    class Meta:
        db_table = 'impuesto'


class Parametros_impuestos(models.Model):
    id_impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE,default=1)
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateField(auto_now=True)
    def __str__(self):
        return self.impuesto
        
class Producto(models.Model):
    nombre_producto = models.CharField(help_text='Nombre del producto',max_length=50, validators=[validar_nombre])
    descripcion = models.CharField(max_length=255,validators=[validar_descripcion])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2,default=150, validators=[validar_salario])
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2,default=200, validators=[validar_salario])
    stock = models.PositiveIntegerField(validators=[validar_stock_actual])
    id_impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE,default=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,default=1)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,default=1)
    fecha_agregado = models.DateField(auto_now_add=True, validators=[validar_date_time])
    fecha_modificado = models.DateField(auto_now=True, validators=[validar_date_time])
    estado = models.BooleanField(validators=[validar_estado])

    def __str__(self):
        return self.nombre_producto
   
   
class Inventario(models.Model):
    surcusal = models.ForeignKey(Sucursal, on_delete=models.CASCADE,default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField(validators=[validar_date_time])
    cantidad = models.PositiveIntegerField(validators=[validar_Cantidad]) 
    nivel_minimo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_maximo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.surcusal}"
    

class Devoluciones(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE,default=1)
    cantidad = models.IntegerField(validators=[validar_Cantidad])
    descripcion = models.CharField(max_length=255,validators=[validar_descripcion])
    fecha_devolucion = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Devolucion'
        verbose_name_plural = 'Devoluciones'  

    def _str_(self):
        return self.descripcion

class Cotizacion(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_cotizacion = models.DateField(auto_now_add=True)
    total_cotizacion = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_Total_Cotizacion])
   

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'  
    

    def _str_(self):
        return self.id_cliente

  
class MetodoPago(models.Model):
    DEBITO = 'debito'
    CREDITO = 'credito'

    TIPO_METODO_CHOICES = [
        (DEBITO, 'Débito'),
        (CREDITO, 'Crédito'),
    ]

    id_metodo_pago = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    tipo_metodo_pago = models.CharField(max_length=50, choices=TIPO_METODO_CHOICES, validators=[validar_descripcion])
    numero_tarjeta = models.CharField(max_length=25, validators=[validar_numero_tarjeta])
    fecha_vencimiento = models.DateField(validators=[validar_fecha_vencimiento])
    cvv = models.CharField(max_length=4, validators=[validar_cvv])
    nombre_titular = models.CharField(max_length=60, validators=[validar_nombre_titular])

    def __str__(self):
        return f"{self.get_tipo_metodo_pago_display()}"

    class Meta:
        db_table = 'metodo_pago'

        
class ComprasEnc(models.Model):
    fecha_compra=models.DateField(null=True,blank=True)
    observacion=models.TextField(blank=True,null=True)
    no_factura=models.CharField(max_length=100)
    fecha_factura=models.DateField()
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        if self.sub_total == None  or self.descuento == None:
            self.sub_total = 0
            self.descuento = 0
            
        self.total = self.sub_total - self.descuento
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name="Encabezado Compra"

class ComprasDet(models.Model):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio_prv=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_prv))
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDet, self).save()
    
    class Mega:
        verbose_name_plural = "Detalles Compras"
        verbose_name="Detalle Compra"

class FacturaEnc(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.sub_total - self.descuento
        super(FacturaEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name="Encabezado Factura"

    

class FacturaDet(models.Model):
    factura = models.ForeignKey(FacturaEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio))
        self.total = self.sub_total - float(self.descuento)
        super(FacturaDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name="Detalle Factura"
        
#hacer models despacho... 


#hacer modelds precioo historico,FK  ID PRODUCTO, ID SURCUSAL
