# Decisiones en Python

En programación, **tomar decisiones** permite que el código ejecute
diferentes instrucciones dependiendo de ciertas condiciones. En Python,
las estructuras más comunes para controlar el flujo de decisiones son
`if`, `elif`, `else` y `match`.

------------------------------------------------------------------------

## 1. `if`

La estructura `if` se utiliza para ejecutar un bloque de código **solo
si** una condición es verdadera.

### Sintaxis básica:

``` python
if condicion:
    # Código a ejecutar si la condición es verdadera
```

### Ejemplo:

``` python
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
```

------------------------------------------------------------------------

## 2. `if` con `else`

Cuando necesitamos una **alternativa** si la condición no se cumple,
usamos `else`.

### Ejemplo:

``` python
edad = 16
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

------------------------------------------------------------------------

## 3. `if`, `elif`, `else`

`elif` (abreviación de "else if") se utiliza cuando hay **múltiples
condiciones** que queremos evaluar en orden.

### Ejemplo:

``` python
nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

------------------------------------------------------------------------

## 4. `match` (Python 3.10+)

La estructura `match` permite manejar varias condiciones de una manera
más **limpia y legible**, similar a `switch` en otros lenguajes.

### Sintaxis básica:

``` python
match variable:
    case valor1:
        # Código
    case valor2:
        # Código
    case _:
        # Caso por defecto
```

### Ejemplo:

``` python
dia = "lunes"

match dia:
    case "lunes":
        print("Inicio de semana")
    case "viernes":
        print("¡Por fin viernes!")
    case _:
        print("Es un día cualquiera")
```

------------------------------------------------------------------------

## 5. Buenas prácticas al usar decisiones

-   Usar **indentación correcta** para evitar errores.\
-   Mantener las condiciones simples y legibles.\
-   Priorizar `match` cuando hay muchas opciones y se busca claridad.\
-   Comenzar con `if` y `else` si eres principiante para comprender la
    lógica básica.

------------------------------------------------------------------------

## 6. Ejemplo completo

``` python
temperatura = 25

if temperatura > 30:
    print("Hace mucho calor.")
elif temperatura >= 20:
    print("El clima es agradable.")
else:
    print("Hace frío.")
```

``` python
clima = "nublado"

match clima:
    case "soleado":
        print("Lleva gafas de sol.")
    case "lluvioso":
        print("Lleva paraguas.")
    case _:
        print("Prepárate para cualquier clima.")
```
