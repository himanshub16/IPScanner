nmcli dev show | grep GENERAL.DEVICE -i > gen_dev
cut -d ':' -f 2 gen_dev > out1
cat out1 | tr -d ' ' > gen_dev

nmcli dev show | grep GENERAL.TYPE -i > gen_type
cut -d ':' -f 2 gen_type > out2
cat out2 | tr -d ' ' > gen_type


echo "Device Type"
echo "-------------"
paste gen_dev gen_type -d ' : '
rm out1 out2 gen_dev gen_type
