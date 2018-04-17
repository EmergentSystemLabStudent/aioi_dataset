#!/bin/zsh
rm -f script.hcopy

for var in `ls -1 *.wav`
do
        var2=`echo $var|sed -e "s/.wav/.mfc/g"`
        echo $var $var2 >> script.hcopy
done

HCopy -C config.hcopy -S script.hcopy

for var in `ls -1 *.mfc`
do
        var2=`echo $var|sed -e "s/.mfc/.txt/g"`
        HList -r $var > $var2
done
