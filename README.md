# pyQT

Создание полноэкранного графического окна на PyQt5 без рамки, с анимацией шариков, запускаемого из SSH-сессии на удалённой машине с X-сервером.

Особенности:
Полноэкранное окно без рамки и курсора
Анимация шариков с отскоком от границ
Работает из SSH после перезапуска системы
Низкая нагрузка на CPU по сравнению с OpenCV

1. Установка системных зависимостей (на машине с GUI)

```
sudo apt update
sudo apt install python3-tk python3-pyqt5 xauth libxcb-xinerama0 libxkbcommon-x11-0 libxcb1 libx11-xcb1 libxrender1 libxi6 libxcomposite1 libxcursor1 libxrandr2 libxfixes3 libxext6
```

2. Создание виртуального окружения

```
python3 -m venv pyqtenv
source pyqtenv/bin/activate
pip install pyqt5
```

3. Доступ к X-серверу после перезапуска (На машине с GUI):

```
xauth extract - $DISPLAY > /tmp/xauth.dump
```

4. Доступ к X-серверу после перезапуска (В SSH-сессии):

```
touch ~/.Xauthority
xauth merge /tmp/xauth.dump
export DISPLAY=:0
export XAUTHORITY=/home/wowa/.Xauthority
```

5. Запуск

```
source pyqtenv/bin/activate
python balls.py
```
