
for i in {0..27};
    do
        echo "running $i"
        opencv_createsamples -img purell_new/$i.jpg -bg bg.txt -info info/info$i.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 200
    done
