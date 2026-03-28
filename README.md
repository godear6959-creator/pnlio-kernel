# PNLIO Node

Nodo PNLIO - Sistema de servidor con capacidades de IA y shell remoto.

## Características

- Servidor socket en puerto 5000
- Autenticación por hash SHA256
- Comandos remotos vía socket
- Sistema de aprendizaje de comandos
- Loop de limpieza automática cada 20 segundos
- Menú interactivo CLI

## Instalación

```bash
chmod +x install.sh
./install.sh
```

O manualmente:

```bash
sudo apt update
sudo apt install -y python3 python3-pip netcat
chmod +x pnlio_node.py
```

## Uso

### Ejecutar el nodo:
```bash
python3 pnlio_node.py
```

### Comandos disponibles vía socket (puerto 5000):
- `info` - Muestra información del sistema
- `top` - Muestra estadísticas de comandos más usados
- `ia <texto>` - Procesa texto con IA (invierte el string)
- `<comando_shell>` - Ejecuta cualquier comando shell
- `exit` - Cierra conexión

### Menú interactivo:
1. Info - Información del sistema
2. CMD - Ejecutar comando shell
3. IA - Procesar texto
4. Stats - Estadísticas
5. Salir

## Password

Default: `g24` (hash SHA256)

## Autor

Gonzalo Mauricio de la Rivera Arellano

---

![PNLIO Motto](motto.png)
