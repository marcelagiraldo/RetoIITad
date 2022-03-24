import io
from singlell import SingleLL
class ReadData:
    def __init__(self) :
        self.archivo = str("Archivo_Reto.txt")
        self.list_node = SingleLL()
        self.iniciar_programa()

    def iniciar_programa(self):
        while True:
            try:
                decision = int(input(">>>>>>>>>>>>>¿Qué desea realizar?<<<<<<<<<<<<<<<<<\n"+
                            "1:Leer archivo existente\n2:Editar archivo\n3:Sobreescribir en el archivo\n       >>>"))
                if decision == 1:
                    self.show_file_content()
                    self.converter_text_in_node(self.archivo)
                elif decision == 2:
                    self.write_in_file()
                elif decision == 3:
                    self.replace_file()
                eleccion = input("\n>>>>>>>>>>>>>>>>¿QUÉ DESEA CONTINUAR HACIENDO<<<<<<<<<<<<<<<<<<?\n"+
                                    "a.Insertar un nuevo nodo\n"+
                                    "b.Eliminar un nodo\n"+
                                    "c.Consultar por el valor de un nodo especificado\n"+
                                    "d.Editar el valor de un nodo existente en la lista\n"+
                                    "e. Invertir el contenido de la lista\n"+
                                    "f. Vaciar la lista\n"+
                                    "g. Salir del sistema\n >>>")
                if eleccion == "a":
                    x = input("    1.Al inicio\n    2.Al final\n    3.En una posición especifica\n")
                elif eleccion == "b":
                    x = input("    1.Al inicio\n    2.Al final\n    3.En una posición especifica\n")
                break
            except ValueError:
                print(">>>>>>>>>>>>>>>EROR<<<<<<<<<<<<<<<")
    '''Leer archivo por lineas'''
    def show_file_content(self):
        with io.open("Archivo_Reto.txt","r",encoding='utf-8') as data_file:
            file_line = data_file.readline()
            while(file_line != ""):
                print(file_line, end="")
                file_line = data_file.readline()
        data_file.close()  
    '''Escribir en el archivo'''
    def write_in_file(self):
        line_write = input("Ingrese el nuevo texto\n  >>>")
        with io.open("Archivo_Reto.txt","a", encoding="utf-8") as data_file:
            data_file.write('\n' + line_write)
        data_file.close()
        self.show_file_content()
    '''Sobreescribir en el archivo'''
    def replace_file(self):
        line_write = input("Ingrese el nuevo contenido\n    >>>")
        with io.open("Archivo_Reto.txt","w",encoding="utf-8") as data_file:
            data_file.write(line_write)
        data_file.close()
        self.show_file_content()
    
    def converter_text_in_node(self,archivo):
        with io.open(archivo,'r+',encoding='utf-8') as data_file:
            for line in data_file.readlines():
                new_node=SingleLL.Node(line)
                self.list_node.append_node(new_node.value)
        data_file.close()
    
    
    
    
        
    