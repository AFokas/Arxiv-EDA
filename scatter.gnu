set terminal pngcairo size 1000,700 font ',18'
set ylabel "Number of Subjects" font ", 18"
set xlabel "Number of Articles" font ", 18"
filename="author_count_df.txt"
f(x)=a*x+b
filename="author_count_df.txt"
fit f(x) filename  using 2:1 via b,a
set yrange[0:8]
set key font "Helvetica,25"
set ytic 2
set xrange[0:100]
set xtic 25
set border linewidth 2
set title "Correlation between total number of articles published \n and number of subjects published in for 40187 Authors \n (R = 0.639)" font ", 20"
set output "scatter.png";plot filename using 2:1 notitle points 1 lt rgb "black",f(x)  with line linewidth 2 lc "black" notitle
