# Prototipo de experiencia

Abre `index.html`: es una demostración autónoma sin backend ni llamadas de red para ejecutar tareas.

- `build.py`: HTML/CSS/JS base.
- `beautifului_adapt.py`: patrones de interacción adaptados de BeautifulUI.
- `fonts/`: Noto Sans y avisos de licencia.
- `third_party/beautifului/`: licencia, procedencia y README de referencia; no incluye el proyecto React completo.

Regeneración multiplataforma:

```sh
python3 prototypes/estela/build.py
```

Los archivos fuente usan rutas relativas a su directorio. No requieren las rutas `/workspace` del entorno original.
