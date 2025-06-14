from tkinter import *
from tkinter import messagebox

class SistemaFacturacionSupermercado:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Busqueda De Productos")
        self.root.geometry("900x600")

        self.productos = {
           "Leche Colanta 1L": 2500,
            "Pan Bimbo Integral": 1500,
            "Huevos Roa 12 unidades": 3000,
            "Arroz Diana 1kg": 2000,
            "Azúcar Incauca 1kg": 1000,
            "Café Juan Valdez 500g": 3500,
            "Queso Alpina 250g": 2800,
            "Jabón Dove 4 unidades": 1800,
            "Aceite Primor 900ml": 4000,
            "Harina Doble Cero 500g": 2200,
            "Mantequilla Alquería 200g": 2600,
            "Pasta La Muñeca 500g": 2400,
            "Galletas Noel Maizena 400g": 1800,
            "Yogur Alpina Natural 1L": 2100,
            "Atún Van Camp's 170g": 3200,
            "Maíz Amarillo La Esperanza 1kg": 1900,
            "Cereal Kellogg's Corn Flakes 300g": 2700,
            "Vinagre Blanco La Esmeralda 500ml": 2300,
            "Salsa de Tomate Heinz 350g": 2000,
            "Tomate Chonto 1kg": 1500,
            # Productos de ferretería
            "Martillo Stanley 16oz": 15000,
            "Taladro Bosch 500W": 85000,
            "Destornillador Phillips Truper": 5000,
            "Llave Ajustable Bahco 10 pulgadas": 20000,
            "Cinta Métrica Stanley 3m": 8000,
            "Pegamento Resistol 100g": 3500,
            "Cerradura Yale para puerta principal": 45000,
            "Clavos de Acero 2 pulgadas (1kg)": 12000,
            "Sierra Eléctrica Black+Decker": 105000,
            "Pintura Vinilo Satinado Blanco Galón": 35000,
            # Productos de tecnología
            "Laptop HP Pavilion 15.6''": 2000000,
            "Smartphone Samsung Galaxy S21": 3000000,
            "Tablet Apple iPad 10.2''": 1500000,
            "Monitor LG UltraWide 34''": 2500000,
            "Impresora Epson EcoTank L3150": 800000,
            "Auriculares Sony WH-1000XM4": 1200000,
            "Router TP-Link Archer AX1800": 400000,
            "Teclado Logitech K480": 100000,
            "Mouse Inalámbrico Microsoft": 80000,
            "Cámara Canon EOS Rebel T7": 1500000,
            # Puedes agregar más productos aquí...
        }

        self.carrito = {}
        self.total = 0.0

        self.color_fondo = "#f2f2f2"
        self.color_boton = "#4CAF50"
        self.color_boton_hover = "#45a049"
        self.color_texto = "#333"

        self.frame_buscar = Frame(root, bg=self.color_fondo)
        self.frame_buscar.pack(pady=20)

        self.lbl_bienvenida = Label(self.frame_buscar, text="Bienvenido al Sistema de busqueda de productos", font=("Arial", 24), bg=self.color_fondo, fg=self.color_texto)
        self.lbl_bienvenida.pack(pady=10)

        self.entry_buscar = Entry(self.frame_buscar, width=50, font=("Arial", 14))
        self.entry_buscar.pack(side=LEFT, padx=10)

        self.btn_buscar = Button(self.frame_buscar, text="Buscar", command=self.buscar_producto, bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        self.btn_buscar.pack(side=LEFT, padx=10)

        self.frame_productos = Frame(root, bg=self.color_fondo)
        self.frame_productos.pack(pady=20, padx=10, fill=BOTH, expand=True)

        self.lbl_productos = Label(self.frame_productos, text="Productos", font=("Arial", 18, "bold"), bg=self.color_fondo, fg=self.color_texto)
        self.lbl_productos.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.scrollbar_productos = Scrollbar(self.frame_productos)
        self.scrollbar_productos.grid(row=1, column=1, sticky="ns")

        self.listbox_productos = Listbox(self.frame_productos, width=60, height=20, font=("Arial", 12), yscrollcommand=self.scrollbar_productos.set)
        self.listbox_productos.grid(row=1, column=0, padx=10, sticky="nsew")
        self.scrollbar_productos.config(command=self.listbox_productos.yview)

        self.frame_total = Frame(root, bg=self.color_fondo)
        self.frame_total.pack(pady=20)

        self.lbl_total = Label(self.frame_total, text="Total: $0.00", font=("Arial", 18), bg=self.color_fondo, fg=self.color_texto)
        self.lbl_total.pack(padx=10)

        self.btn_agregar = Button(self.frame_total, text="Agregar al Carrito", command=self.agregar_al_carrito, bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        self.btn_agregar.pack(side=LEFT, padx=10)

        self.btn_finalizar = Button(self.frame_total, text="Finalizar Compra", command=self.finalizar_compra, bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        self.btn_finalizar.pack(side=RIGHT, padx=10)

        self.frame_carrito = Frame(root, bg=self.color_marco)
        self.frame_carrito.pack(pady=20, padx=10, fill=BOTH, expand=True)

        self.lbl_carrito = Label(self.frame_carrito, text="Carrito de Compras", font=("Arial", 18, "bold"), bg=self.color_marco, fg=self.color_texto)
        self.lbl_carrito.pack(pady=10)

        self.texto_carrito = Text(self.frame_carrito, width=60, height=10, font=("Arial", 12))
        self.texto_carrito.pack(pady=10)

        self.lbl_total_compra = Label(self.frame_carrito, text="Total de la Compra: $0.00", font=("Arial", 14), bg=self.color_marco, fg=self.color_texto)
        self.lbl_total_compra.pack(pady=10)

        self.btn_agregar_nuevo = Button(self.frame_carrito, text="Agregar Nuevo Producto", command=self.agregar_nuevo_producto, bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        self.btn_agregar_nuevo.pack(pady=10)

   
        self.actualizar_lista_productos()

    def actualizar_lista_productos(self):
        self.listbox_productos.delete(0, END)
        for producto, precio in self.productos.items():
            self.listbox_productos.insert(END, f"{producto} - ${precio:.2f}")

    def buscar_producto(self):
        self.listbox_productos.delete(0, END)
        texto_busqueda = self.entry_buscar.get().lower()
        for producto, precio in self.productos.items():
            if texto_busqueda in producto.lower():
                self.listbox_productos.insert(END, f"{producto} - ${precio:.2f}")

    def agregar_al_carrito(self):
        seleccion = self.listbox_productos.curselection()
        print("Se ha seleccionado:", seleccion)
        if seleccion:
            producto_seleccionado = self.listbox_productos.get(seleccion)
            print("Producto seleccionado:", producto_seleccionado)
            producto, precio = producto_seleccionado.split(" - ")
            precio = float(precio.replace("$", ""))
            if producto in self.carrito:
                self.carrito[producto] += precio
            else:
                self.carrito[producto] = precio
            print("Carrito actualizado:", self.carrito)
            self.actualizar_carrito()

    def actualizar_carrito(self):
        self.texto_carrito.delete(1.0, END)
        self.total = sum(self.carrito.values())
        for producto, precio in self.carrito.items():
            self.texto_carrito.insert(END, f"{producto} - ${precio:.2f}\n")
        self.lbl_total_compra.config(text=f"Total de la Compra: ${self.total:.2f}")
        self.lbl_total.config(text=f"Total: ${self.total:.2f}")

    def finalizar_compra(self):
        messagebox.showinfo("Compra Finalizada", "¡Gracias por su compra!")
        self.carrito = {}
        self.total = 0.0
        self.texto_carrito.delete(1.0, END)
        self.lbl_total_compra.config(text="Total de la Compra: $0.00")
        self.lbl_total.config(text="Total: $0.00")

    def agregar_nuevo_producto(self):
        ventana_agregar = Toplevel(self.root)
        ventana_agregar.title("Agregar Nuevo Producto")

        frame_agregar = Frame(ventana_agregar, bg=self.color_fondo)
        frame_agregar.pack(padx=20, pady=10)

        lbl_nombre = Label(frame_agregar, text="Nombre del Producto:", font=("Arial", 14), bg=self.color_fondo, fg=self.color_texto)
        lbl_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        entry_nombre = Entry(frame_agregar, width=30, font=("Arial", 12))
        entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        lbl_precio = Label(frame_agregar, text="Precio:", font=("Arial", 14), bg=self.color_fondo, fg=self.color_texto)
        lbl_precio.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        entry_precio = Entry(frame_agregar, width=15, font=("Arial", 12))
        entry_precio.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        btn_agregar = Button(frame_agregar, text="Agregar", command=lambda: self.agregar_producto_nuevo(entry_nombre.get(), entry_precio.get(), ventana_agregar), bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        btn_agregar.grid(row=2, columnspan=2, pady=20)

    def agregar_producto_nuevo(self, nombre, precio, ventana):
        try:
            precio = float(precio)
            if nombre and precio > 0:
                self.productos[nombre] = precio
                self.actualizar_lista_productos()
                messagebox.showinfo("Producto Agregado", f"Se ha agregado '{nombre}' correctamente.")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Ingrese un nombre de producto válido y un precio mayor que cero.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un precio válido (número).")

if __name__ == "__main__":
    root = Tk()
    app = SistemaFacturacionSupermercado(root)
    root.mainloop()

