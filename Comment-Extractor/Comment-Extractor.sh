#/bin/bash

rm comments
for i in $(cat $1)
do
        curl -s $i | grep -o -P "(<!--(.*?)-->)|(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)|(^'.*$)|(^#.*$)" > t
        if [ -s t ]
        then
                echo $i >> comments
                echo "" >> comments
                cat t >> comments
                echo "" >> comments
        fi
done
