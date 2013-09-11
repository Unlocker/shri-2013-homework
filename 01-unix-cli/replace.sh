#!/bin/bash

#
# Решение ДЗ №1 ШРИ 2013 года
# Автор: Максимов Сергей
#

# Скрипт принимает единственный параметр:
# - директория, в которой производить поиск
# директория по умолчанию та, в которой лежит скрипт

DIR="$1" 
[ "$DIR" == "" ] && DIR="."
PATTERN="\(<title>\)КИТ\(<\/title>\)"

for file in `find $DIR -name '*.html'`
do
  if grep -q $PATTERN "$file"; then
    echo $file
    sed -i 's/\(<title>\)КИТ\(<\/title>\)/\1ШРИ\2/g' "$file"
  fi
done