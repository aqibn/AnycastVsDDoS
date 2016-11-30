#le==letter Nu==number
function download {

Le=$1
Nu=$2
Et=$3
St=$4
Hr=$5

wget -O "$Le"root$5 "https://atlas.ripe.net/api/v2/measurements/$Nu/results?start="$St"&stop="$Et"&format=json" 
}

#for i in `seq 1 7`;
# do
let b="1448841600"
# let b="$a - 86399"
let a="1449003600-7200"
let c=$b
let k=0
#follow is the timezone-free version
#let x=`date +%s`
#let a=""$x"/86400 * 86400"
#let b="$a - 86399"
# download A 10309 $a $b 
# download B 10310 $a $b 
# download C 10311 $a $b 
# download D 10312 $a $b 
# download E 10313 $a $b 
# download F 10304 $a $b 
# download G 10314 $a $b 
# download H 10315 $a $b 
for i in {1448841600..1448996400..7200}
do 
  echo "Dowload $k times"
  echo "time $i times"
  ((k++))
  let d=$i+7200
  # download I 10305 $d $i $k
	download K 10301 $d $i $k
	download D 10312 $d $i $k 


done
# download J 10316 $a $b 
# download K 10301 $a $b 
# download L 10308 $a $b 
# download M 10306 $a $b 
# done
