#!/bin/bash
rm parameters.txt

sed '/?/!d' $1 >stripped

input="stripped"

while IFS= read -r line
do
  echo "$line" | cut -d '?' -f 2 >> parameters.txt
done < "$input"

sed -i 's/^/\&/' parameters.txt

cat parameters.txt | grep -oP '(?<=&).*?(?=\=)' > parameters
sed -i 's/&//g' parameters

awk '!seen[$0]++' parameters > parameters.txt

echo 'Saved all parameter names to parameters.txt'

rm parameters
rm stripped
