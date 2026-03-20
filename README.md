# fra2mo_navigation

Questo pacchetto ROS 2 fornisce due launch file per la navigazione:
- `slam.launch.py`: per la creazione della mappa dell'ambiente tramite SLAM Toolbox.
- `amcl.launch.py`: per la localizzazione sulla mappa creata tramite AMCL e Nav2.

## Utilizzo

1. **Creazione della mappa (SLAM):**
   ```bash
   ros2 launch fra2mo_navigation slam.launch.py
   ```
   Salva la mappa con:
   ```bash
   ros2 run nav2_map_server map_saver_cli -f <nome_mappa>
   ```

2. **Localizzazione (AMCL):**
   Modifica il percorso della mappa nel file di configurazione di Nav2, poi lancia:
   ```bash
   ros2 launch fra2mo_navigation amcl.launch.py
   ```

## Note
- Il pacchetto è indipendente da `fra2mo_description`.
- Personalizza i percorsi dei file `.rviz` nei launch file secondo le tue esigenze.
