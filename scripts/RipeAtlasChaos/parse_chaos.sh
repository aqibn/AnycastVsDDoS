#le==letter Nu==number
function parse {

Le=$1
Nu=$2
# Day=$2

python parse_chaos.py "$Le"root$Nu "$Le"rootparsed$Nu 
}

# for i in `seq 1 7`
# do 
# 	for j in {A..M}
# 	do
# 	parse $j $i
# 	done
# done
for i in {1..5}
do

	parse A $i
	parse B $i
	parse C $i
	parse D $i
	parse E $i
	parse F $i
	parse G $i
	parse H $i
	parse I $i
	parse J $i
	parse K $i
	parse L $i
	parse M $i

	# parse K $i
	# parse D $i

done

