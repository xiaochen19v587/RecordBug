#! /bin/bash
gnome-terminal  --window -e 'bash -c "source '$1' '$2';exec bash"'