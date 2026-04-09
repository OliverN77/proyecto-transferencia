# 📋 Gestion-Info

Un sistema de gestión de usuarios basado en consola que demuestra **operaciones CRUD**, **arquitectura limpia** y **persistencia en JSON** con Python. Perfecto para aprender buenas prácticas en gestión de datos y patrones de diseño de software.

---

## 🎯 Características

- ✅ **Crear Usuarios** — Registrar nuevos usuarios con IDs auto-incrementados y validación
- 📖 **Listar Registros** — Ver todos los usuarios ordenados alfabéticamente por nombre
- 🔍 **Buscar Usuario** — Encontrar usuarios por nombre (búsqueda sin distinción de mayúsculas)
- ✏️ **Actualizar Usuarios** — Modificar detalles del usuario (nombre, email, edad, estado)
- 🗑️ **Eliminar Usuarios** — Eliminar usuarios del sistema
- 💾 **Persistencia de Datos** — Guardar y cargar datos de usuarios desde JSON con manejo de errores
- 📊 **Reportes con Pandas** — Generar reportes filtrados y agrupados con análisis de datos
- 📥 **Exportar a CSV** — Exportar registros a archivos CSV con filtrado y ordenamiento avanzado
- 🎓 **Arquitectura Limpia** — Separación de responsabilidades con módulos dedicados para servicio, validación y capas de datos

---

## 📦 Inicio Rápido

### Requisitos Previos
- **Python 3.10** o superior
- **Dependencias externas** listadas en `requirements.txt`

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/yourusername/gestion-info.git
cd gestion-info
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

Este comando instalará:
- **pandas** — para análisis de datos y exportación a CSV
- **colorama** — para estilos de color en consola
- **openpyxl** — soporte para reportes en Excel

3. **Ejecutar la aplicación**
```bash
python src/main.py
```

### Uso Básico

Una vez que se inicializa la aplicación, verás un menú interactivo:

```
========================================
Menú de Gestión de Usuarios
========================================
1. Crear usuario
2. Listar registros
3. Buscar registros
4. Actualizar usuario
5. Eliminar usuario
6. Guardar datos
7. Generar Reporte
8. Exportar a CSV
9. Salir

Seleccione una opción: 
```

**Ejemplo de flujo de trabajo:**
1. Selecciona la opción **1** para registrar un nuevo usuario
2. Ingresa nombre, email, edad y estado
3. Ver usuarios con la opción **2**
4. Generar reportes con la opción **7** (con filtros y agrupación disponibles)
5. Exportar datos a CSV con la opción **8** (con opciones de filtrado avanzado)
6. Guardar cambios a JSON con la opción **6** antes de salir

---

## 📊 Funcionalidades Avanzadas

### Reportes (Opción 7)
- **Reporte General** — Visualiza todos los usuarios con estadísticas
- **Agrupado por Estado** — Agrupa usuarios por estado (activo/inactivo)
- **Agrupado por Edad** — Agrupa usuarios por edad
- **Solo Activos** — Filtra y muestra solo usuarios activos

### Exportación a CSV (Opción 8)
- **Exportación Completa** — Exporta todos los registros a `reporte_completo.csv`
- **Usuarios Activos** — Exporta solo activos a `usuarios_activos.csv`
- **Mayores de 18** — Exporta mayores de 18 años a `usuarios_mayores_18.csv`
- **Personalizado** — Elige nombre, filtros, y columna para ordenar

**Los archivos se guardan en la carpeta `data/`**

---

## 🏗️ Arquitectura del Proyecto

### Estructura de Directorios

```
gestion-info/
├─ README.md                    # Este archivo - documentación del proyecto
├─ requirements.txt             # Dependencias del proyecto (pandas, colorama, openpyxl)
├─ .gitignore                   # Reglas de ignorar archivos para Git
├─ data/
│  └─ registros.json           # Archivo JSON con registros persistentes de usuarios
└─ src/
   ├─ main.py                  # Punto de entrada - orquesta el bucle del menú
   ├─ menu.py                  # Interfaz de usuario - lógica del menú en consola
   ├─ service.py               # Lógica empresarial - implementa operaciones CRUD
   ├─ file.py                  # Capa de datos - maneja persistencia en JSON
   ├─ validate.py              # Lógica de validación y funciones auxiliares
   └─ integration.py            # Integraciones con librerías externas (Pandas, reportes)
```

### Responsabilidades de Módulos

| Módulo | Propósito | Funciones Clave |
|--------|-----------|---|
| **main.py** | Punto de entrada y orquestación del menú | Control del flujo de la aplicación |
| **menu.py** | Interfaz de usuario en consola | Mostrar menús y recopilar entrada del usuario |
| **service.py** | Lógica empresarial CRUD | `registrar_usuario()`, `listar_usuarios()`, `buscar_usuario()`, `actualizar_usuario()`, `eliminar_usuario()` |
| **file.py** | Capa de persistencia de datos | Operaciones de lectura/escritura en JSON con manejo de errores |
| **validate.py** | Validación de entrada y auxiliares | Validación de email, rangos de edad, validación de estado |
| **integration.py** | Integraciones futuras | Marcador de posición para Faker, Pandas, APIs externas |

---

## 📝 Estilo de Código y Convenciones

Este proyecto sigue **PEP 8** con énfasis en **nomenclatura snake_case**:

### Convenciones de Nombres

```python
# ✅ Variables y funciones: snake_case
nombre_usuario = "Oliver Nieto"
def registrar_usuario(nombre, email, edad, estado):
    pass

# ✅ Constantes: UPPER_SNAKE_CASE
EDAD_MAXIMA = 99
EDAD_MINIMA = 1
RUTA_ARCHIVO_JSON = "data/registros.json"

# ✅ Clases: PascalCase
class ServicioUsuario:
    pass

# ❌ Evitar camelCase
nombreUsuario = "Oliver"  # NO nombreUsuario
```

### Nomenclatura de Archivos

- Todos los archivos Python usan **snake_case**: `main.py`, `service.py`, `file.py` (NO Main.py o ServiceFile.py)
- Los archivos de datos siguen la convención: `registros.json`

---

## 📊 Modelo de Datos

### Estructura de Registros de Usuario (Dinámica)

Los usuarios se almacenan en `data/registros.json` en un formato JSON flexible y escalable. El archivo crece dinámicamente a medida que se registran nuevos usuarios, con IDs auto-incrementados:

```json
{
  "usuarios": [
    {
      "id": 1,
      "nombre": "Juan Pérez",
      "email": "juan@example.com",
      "edad": 28,
      "estado": "activo"
    },
    {
      "id": 2,
      "nombre": "María García",
      "email": "maria@example.com",
      "edad": 35,
      "estado": "inactivo"
    },
    {
      "id": 3,
      "nombre": "Carlos López",
      "email": "carlos@example.com",
      "edad": 42,
      "estado": "activo"
    }
  ]
}
```

**Características dinámicas:**
- ✨ Los IDs se generan automáticamente (1, 2, 3, ...)
- ✨ El archivo JSON crece con cada nuevo usuario registrado
- ✨ Los cambios se guardan solo al usar la opción "Guardar cambios"
- ✨ Soporta caracteres internacionales (UTF-8)

### Reglas de Validación de Campos

| Campo | Tipo | Validación | Ejemplo |
|-------|------|-----------|---------|
| **id** | Entero | Auto-incrementado, único | `1`, `2`, `3` |
| **nombre** | Cadena | Requerido | `"Oliver Nieto"` |
| **email** | Cadena | Debe contener `@` y `.` | `"oliver@example.com"` |
| **edad** | Entero | Rango: 1-99 | `25` |
| **estado** | Cadena | `"activo"` o `"inactivo"` | `"activo"` |

---

## 💻 Detalles Técnicos

### Dependencias Externas (requirements.txt)

Este proyecto utiliza las siguientes librerías externas:

```
pandas>=2.0.0                   # Análisis de datos y manipulación de DataFrames
colorama>=0.4.6                 # Estilos de color y formato en consola
openpyxl>=3.1.0                 # Soporte para reportes en formato Excel
```

**Instalación de dependencias:**
```bash
pip install -r requirements.txt
```

Este comando instala automáticamente todas las versiones requeridas:

| Librería | Versión | Propósito |
|----------|---------|----------|
| **pandas** | ≥2.0.0 | Análisis de datos, generación de reportes, exportación a CSV y Excel |
| **colorama** | ≥0.4.6 | Colores y estilos en la salida de consola para mejor presentación |
| **openpyxl** | ≥3.1.0 | Creación y manipulación de archivos Excel (.xlsx) |

### Persistencia de Datos
- **Formato**: JSON (legible por humanos, fácil de inspeccionar y depurar)
- **Ubicación**: `data/registros.json`
- **Codificación**: UTF-8 para soporte de caracteres internacionales
- **Manejo de Errores**: Recuperación elegante si el archivo está corrupto o falta

### Gestión de Memoria
1. La aplicación carga todos los usuarios desde JSON en memoria al inicio
2. Todas las operaciones CRUD trabajan con datos en memoria (operaciones rápidas)
3. Opción explícita de "Guardar cambios" persiste datos a archivo JSON
4. Previene pérdida accidental de datos mediante paso de guardado intencional

---

## 🚀 Mejoras Futuras

El módulo `src/integration.py` está reservado para extender funcionalidad:

- **Integración Faker** — Generar datos de prueba realistas automáticamente
- **Exportación Pandas** — Exportar registros de usuarios a CSV/Excel para análisis
- **API REST** — Agregar Flask/FastAPI para exponer operaciones vía HTTP
- **Base de Datos** — Migrar de JSON a SQLite/PostgreSQL para escalabilidad
- **Autenticación** — Agregar inicio de sesión de usuario y control de acceso basado en roles

---

## 📚 Resultados de Aprendizaje

Este proyecto demuestra:

- ✓ **Operaciones CRUD** — Flujo completo de gestión de datos
- ✓ **Arquitectura Limpia** — Separación de preocupaciones (UI, lógica empresarial, persistencia)
- ✓ **Persistencia JSON** — Trabajo con datos estructurados y E/S de archivos
- ✓ **Validación de Entrada** — Aseguramiento de integridad de datos
- ✓ **Convención Snake_case** — Estándares profesionales de nomenclatura en Python
- ✓ **Programación Funcional** — Uso de `lambda`, `filter()` y comprensiones de listas
- ✓ **Manejo de Errores** — Recuperación elegante de entrada inválida y errores de archivos

---

## 📄 Licencia

Licencia MIT — Siéntete libre de usar este proyecto con fines de aprendizaje y personales.

---

## 👤 Créditos

**Estudiante:** Oliver Nieto  
**Ficha:** 3406211  
**Tipo de Proyecto:** Proyecto de transferencia
**Creado:** 2026

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo agregar más campos a los registros de usuario?**  
R: ¡Sí! Actualiza las reglas de validación en `src/validate.py` y modifica las indicaciones del menú en `src/menu.py`.

**P: ¿Qué pasa si el archivo JSON se corrompe?**  
R: El módulo `src/file.py` incluye manejo de errores. Te alertará y creará una copia de seguridad.

**P: ¿Cómo reinicio todos los datos?**  
R: Elimina `data/registros.json` y reinicia la aplicación—creará un archivo nuevo.

**P: ¿Puedo ejecutar esto en Windows/Mac/Linux?**  
R: ¡Sí! Python y JSON son multiplataforma. Funciona en todos los sistemas operativos.