#!/bin/bash

# Путь к файлу токена
TOKEN_DUMP="/tmp/xauth.dump"
REMOTE_USER="wowa"
REMOTE_HOME="/home/$REMOTE_USER"
REMOTE_AUTH="$REMOTE_HOME/.Xauthority"

# Проверка DISPLAY
if [ -z "$DISPLAY" ]; then
    export DISPLAY=:0
    echo "DISPLAY не был задан, установлено :0"
fi

# На машине с GUI — извлекаем токен
echo "Извлечение токена из X-сессии..."
xauth extract - "$DISPLAY" > "$TOKEN_DUMP"

# На удалённой машине — копируем и применяем
echo "Копирование токена в SSH-сессию..."
scp "$TOKEN_DUMP" "$REMOTE_USER@localhost:$TOKEN_DUMP"

echo "Мердж токена в ~/.Xauthority..."
ssh "$REMOTE_USER@localhost" "touch $REMOTE_AUTH && xauth merge $TOKEN_DUMP && export DISPLAY=:0 && export XAUTHORITY=$REMOTE_AUTH"

echo "Готово. Теперь можно запускать графику из SSH."
